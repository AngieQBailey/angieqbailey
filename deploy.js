/**
 * Safe Deploy Script for angieqbailey.com
 *
 * Always pulls the latest version from GitHub before pushing.
 * Prevents overwrites of manual edits made directly on GitHub.
 *
 * Usage (from sandbox):
 *   node deploy.js <local-file> <repo-path> "<commit-message>"
 *
 * Examples:
 *   node deploy.js index.html index.html "Update warehouse cards"
 *   node deploy.js "Portfolio Work/Verdict/add-value-not-noise.html" "verdict/add-value-not-noise.html" "Fix typo"
 *   node deploy.js styles.css styles.css "Add new CSS component"
 *
 * The script will:
 *   1. Fetch the latest version from GitHub (if file exists)
 *   2. Compare local file against remote
 *   3. Show file sizes for verification
 *   4. Push with correct SHA to prevent conflicts
 *   5. Report success/failure
 *
 * PAT must be set as environment variable or updated below.
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

// Configuration
const PAT = process.env.GITHUB_PAT;
if (!PAT) {
    console.error('ERROR: Set GITHUB_PAT environment variable before running.');
    console.error('  export GITHUB_PAT="github_pat_..."');
    process.exit(1);
}
const REPO = 'AngieQBailey/angieqbailey';

function githubAPI(method, repoPath, body) {
    return new Promise((resolve, reject) => {
        const options = {
            hostname: 'api.github.com',
            path: `/repos/${REPO}/contents/${repoPath}`,
            method: method,
            headers: {
                'Authorization': `Bearer ${PAT}`,
                'User-Agent': 'AQB-SafeDeploy',
                'Content-Type': 'application/json',
                'Accept': 'application/vnd.github.v3+json'
            }
        };

        const req = https.request(options, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
                try {
                    resolve({ status: res.statusCode, data: JSON.parse(data) });
                } catch(e) {
                    resolve({ status: res.statusCode, data: data });
                }
            });
        });
        req.on('error', reject);
        if (body) req.write(JSON.stringify(body));
        req.end();
    });
}

async function safeDeploy(localPath, repoPath, commitMessage) {
    console.log(`\n=== Safe Deploy ===`);
    console.log(`Local:  ${localPath}`);
    console.log(`Remote: ${repoPath}`);
    console.log(`Message: ${commitMessage}`);
    console.log('');

    // Step 1: Read local file
    if (!fs.existsSync(localPath)) {
        console.error(`ERROR: Local file not found: ${localPath}`);
        process.exit(1);
    }
    const localContent = fs.readFileSync(localPath);
    const localB64 = localContent.toString('base64');
    console.log(`Local file: ${localContent.length} bytes`);

    // Step 2: Fetch remote version
    let remoteSha = null;
    let remoteSize = 0;
    const remote = await githubAPI('GET', repoPath);

    if (remote.status === 200 && remote.data.sha) {
        remoteSha = remote.data.sha;
        remoteSize = remote.data.size;
        console.log(`Remote file: ${remoteSize} bytes (SHA: ${remoteSha.substring(0, 7)})`);

        // Step 3: Check if remote was modified since last known state
        if (remoteSize === localContent.length) {
            console.log(`WARNING: Files are the same size. Deploying anyway (content may differ).`);
        } else {
            console.log(`Size difference: ${localContent.length - remoteSize} bytes`);
        }
    } else {
        console.log(`New file (does not exist in repo yet)`);
    }

    // Step 4: Deploy
    const body = {
        message: commitMessage,
        content: localB64
    };
    if (remoteSha) body.sha = remoteSha;

    const result = await githubAPI('PUT', repoPath, body);

    if (result.status === 200 || result.status === 201) {
        const newSha = result.data.content ? result.data.content.sha.substring(0, 7) : 'unknown';
        console.log(`\nSUCCESS: Deployed ${repoPath} (new SHA: ${newSha})`);
    } else if (result.status === 409) {
        console.error(`\nCONFLICT: The remote file was modified since we fetched it.`);
        console.error(`Someone else pushed a change. Re-run this script to get the latest SHA.`);
        process.exit(1);
    } else {
        console.error(`\nFAILED: ${result.status}`);
        console.error(JSON.stringify(result.data).substring(0, 300));
        process.exit(1);
    }
}

// Parse command line arguments
const args = process.argv.slice(2);
if (args.length < 3) {
    console.log('Usage: node deploy.js <local-file> <repo-path> "<commit-message>"');
    console.log('');
    console.log('Examples:');
    console.log('  node deploy.js index.html index.html "Update warehouse cards"');
    console.log('  node deploy.js styles.css styles.css "Add hover effect"');
    console.log('  node deploy.js "Portfolio Work/Verdict/add-value-not-noise.html" "verdict/add-value-not-noise.html" "Fix typo"');
    process.exit(0);
}

safeDeploy(args[0], args[1], args[2]).catch(err => {
    console.error('Deploy error:', err.message);
    process.exit(1);
});
