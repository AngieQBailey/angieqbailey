# AQB Case Study Design System Reference

This file contains the complete CSS, HTML boilerplate, and component patterns for all three page types in the case study system. Load this file when building any case study deliverable.

## Table of Contents

1. [Design Tokens (CSS Variables)](#design-tokens)
2. [Case Study Page Boilerplate](#case-study-page)
3. [Branded Artifact Page Boilerplate](#branded-artifact-page)
4. [Blank Template Boilerplate](#blank-template)
5. [Component Library](#component-library)
6. [Responsive Breakpoints](#responsive-breakpoints)
7. [JavaScript Patterns](#javascript-patterns)

---

## Design Tokens

### Dark Variant (Case Study + Branded Artifact Pages)

```css
:root {
    --nuit:     #121A28;      /* Parisian Night — background */
    --cacao:    #2D1B14;      /* Bitter Cacao — spine, structural elements */
    --quetzal:  #00685E;      /* Quetzal Green — borders, grid lines, structural accents */
    --quetzal-bright: #00A896; /* Quetzal Bright — ALL green text on dark backgrounds */
    --ecru:     #F5F5DC;      /* Ecru Wool — primary text */
    --rosso:    #C41E3A;      /* Valentino Rosso — surgical accent only */
    --ecru-dim: rgba(245, 245, 220, 0.6);   /* Body text */
    --ecru-ghost: rgba(245, 245, 220, 0.08); /* Borders only — NOT for card backgrounds */
    --quetzal-line: rgba(0, 104, 94, 0.1);  /* Blueprint grid */
    --spine-left: 22%;        /* Structural spine position */
}
```

**Card/panel backgrounds:** Use `rgba(245, 245, 220, 0.14)` directly — not `var(--ecru-ghost)` which is 0.08 opacity and too faint. This applies to `.approach-item`, `.artifact-card`, `.outcome-stat` and any panel that needs visual separation from the dark background.

**Green text rule:** Use `var(--quetzal-bright)` for `color:` properties (section labels, card tags, metric labels, nav marks, footer). Keep `var(--quetzal)` for `border:` and structural line properties.

**Yellow flag color:** Yellow constraint flags and severity badges use `#D4A017` (a warm gold) for both `color` and `border`. This is the one UI color in the system that does not map to a CSS variable, because the Analytical Palette has no yellow. Do NOT use `var(--quetzal)` or `var(--quetzal-bright)` for yellow flags. That makes them render green.

### Light Variant (Blank Templates)

```css
:root {
    --nuit: #121A28;
    --cacao: #2D1B14;
    --quetzal: #00685E;
    --ecru: #F5F5DC;
    --rosso: #C41E3A;
    --text: #1a1a1a;          /* Primary text (dark on light) */
    --text-dim: #555;         /* Secondary text */
    --border: #d4d0c8;        /* Table borders */
    --border-light: #e8e4dc;  /* Light borders */
    --hover-bg: rgba(0, 104, 94, 0.04); /* Row hover */
}
```

### Global Resets (Both Variants)

```css
*, *::before, *::after {
    margin: 0; padding: 0; box-sizing: border-box;
    font-style: normal !important;    /* No italics enforcement */
    border-radius: 0 !important;      /* No rounded corners enforcement */
}

::selection {
    background: var(--rosso);
    color: var(--ecru);
}
```

### Font Import (All Pages)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Imbue:opsz,wght@10..100,400;10..100,700;10..100,900&family=IBM+Plex+Mono:wght@400;700&family=IBM+Plex+Sans:wght@300;400;500;700&display=swap" rel="stylesheet">
```

---

## Case Study Page

### Full HTML Structure

```html
<!DOCTYPE html>
<html lang="en" style="background-color:#121A28;">
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-S0MXDDKP4E"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-S0MXDDKP4E');
    </script>
    <meta charset="UTF-8">
    <meta name="color-scheme" content="dark">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Case Study: {Title} — {One-line forensic summary}">
    <meta name="author" content="Angie Bailey">
    <meta name="theme-color" content="#121A28">
    <meta property="og:title" content="{Title} // Angie Bailey">
    <meta property="og:description" content="{Lede text}">
    <meta property="og:type" content="article">
    <title>{Title} // Angie Bailey</title>
    {font imports}
    <style>
        {all CSS — see below}
    </style>
</head>
<body style="background-color: #121A28;">
    <div class="blueprint-overlay" aria-hidden="true"></div>
    <div class="spine" aria-hidden="true"></div>
    <nav class="nav-bar" role="navigation" aria-label="Primary">
        <a href="/" class="nav-mark" style="text-decoration: none;">AB</a>
        <ul class="nav-links">
            <li><a href="/#warehouse">Warehouse</a></li>
            <li><a href="/#investigation">Investigation</a></li>
            <li><a href="/#verdict">Verdict</a></li>
            <li><a href="/#signal">Signal</a></li>
        </ul>
    </nav>
    <main>
        <!-- HEADER -->
        <section class="case-header section-content">
            <span class="case-meta">Case Study // {Category}</span>
            <span class="case-tag">{Cross-Functional Tag}</span>
            <h1>{Title Line 1}<br>{Line 2}<br><span class="accent-word">{Accent Word}</span></h1>
            <div class="case-lede">
                <p>{Lede paragraph with <strong>key tension bolded</strong>}</p>
            </div>
        </section>

        <!-- THE EVIDENCE — goes right after the header, above the fold -->
        <section class="case-section section-content reveal">
            <span class="section-label">The Evidence</span>
            <h2>Frameworks<br>&amp; Artifacts</h2>
            <div class="case-body"><p>{Intro}</p></div>
            <div class="artifact-grid">
                <a href="assets/{slug}.html" class="artifact-card" target="_blank" rel="noopener noreferrer">
                    <div class="artifact-type">{Type}</div>
                    <div class="artifact-name">{Name}<br>{Line 2}</div>
                    <div class="artifact-desc">{Description}</div>
                    <div class="artifact-action">View {Type} &rarr;</div>
                </a>
                <!-- more cards -->
            </div>
        </section>

        <!-- THE SITUATION -->
        <section class="case-section section-content reveal">
            <span class="section-label">The Situation</span>
            <h2>{Diagnostic Headline}<br>{Line 2}</h2>
            <div class="case-body">
                <p>{Body paragraphs...}</p>
                <!-- Optional failure loop -->
                <div class="failure-loop">
                    <div class="loop-step"><span class="loop-arrow">&rarr;</span> {Step}</div>
                    <!-- more steps -->
                </div>
            </div>
        </section>

        <!-- PRESSURE POINTS -->
        <section class="case-section section-content reveal">
            <span class="section-label">Pressure Points Surfaced</span>
            <h2>What the<br>Diagnostic Found</h2>
            <div class="case-body"><p>{Intro}</p></div>
            <div class="constraint-list">
                <div class="constraint-item">
                    <span class="constraint-flag red">Red</span>
                    <div>
                        <div class="constraint-label">{Finding Title}</div>
                        <div class="constraint-detail">{Finding Detail}</div>
                    </div>
                </div>
                <!-- more items with .red or .yellow flags -->
            </div>
        </section>

        <!-- THE APPROACH -->
        <section class="case-section section-content reveal">
            <span class="section-label">The Approach</span>
            <h2>{Approach Headline}<br>{Line 2}</h2>
            <div class="case-body"><p>{Philosophy}</p></div>
            <div class="approach-grid">
                <div class="approach-item">
                    <div class="approach-day">Day 01</div>
                    <div class="approach-title">{Title}<br>{Line 2}</div>
                    <div class="approach-desc">{Description}</div>
                </div>
                <!-- Day 02, Day 03, Principle -->
            </div>
        </section>

        <!-- THE OUTCOME -->
        <section class="case-section section-content reveal">
            <span class="section-label">The Outcome</span>
            <h2>What the<br>{Event} Produced</h2>
            <div class="outcome-grid">
                <div class="outcome-stat">
                    <div class="outcome-number">{N}</div>
                    <div class="outcome-label">{What it means}<br>{Line 2}</div>
                </div>
                <div class="outcome-stat">
                    <div class="outcome-number highlight">{Key Number}</div>
                    <div class="outcome-label">{Highlighted metric}</div>
                </div>
                <!-- more stats -->
            </div>
            <div class="case-body" style="margin-top: 2rem;">
                <p>{Closing summary with <strong>bold conclusion</strong>}</p>
            </div>
            <a href="/" class="back-link">Back to The Warehouse</a>
        </section>
    </main>
    <footer>
        <div class="footer-content">
            <span>&copy; {year} Angie Bailey</span>
        </div>
    </footer>
    <script>
        /* IntersectionObserver for .reveal — see JavaScript Patterns section */
    </script>
</body>
</html>
```

### Case Study Page CSS (Complete)

```css
/* === Base === */
html { scroll-behavior: smooth; scroll-padding-top: 2rem; }
body {
    background-color: var(--nuit); color: var(--ecru);
    font-family: 'IBM Plex Sans', sans-serif; font-weight: 400;
    line-height: 1.6; -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale; overflow-x: hidden;
}

/* === Architectural Elements === */
.blueprint-overlay {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    pointer-events: none; z-index: 1000;
    background-image:
        linear-gradient(to right, var(--quetzal-line) 1px, transparent 1px),
        linear-gradient(to bottom, var(--quetzal-line) 1px, transparent 1px);
    background-size: 40px 40px;
    animation: grid-fade 2s ease 0.5s both;
}

.spine {
    position: fixed; left: calc(var(--spine-left) - 40px);
    top: 0; width: 4px; height: 100%;
    background-color: var(--cacao); z-index: 500;
    animation: spine-draw 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

/* === Navigation === */
.nav-bar {
    position: fixed; top: 0; left: 0; width: 100%; z-index: 900;
    padding: 1.5rem 2rem 1.5rem var(--spine-left);
    display: flex; justify-content: space-between; align-items: center;
    background: linear-gradient(to bottom, var(--nuit) 60%, transparent);
}
.nav-mark {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase;
    color: var(--quetzal-bright); text-decoration: none;
}
.nav-links { display: flex; gap: 2rem; list-style: none; padding-right: 2rem; }
.nav-links a {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    font-weight: 400; color: var(--ecru-dim); text-decoration: none;
    text-transform: uppercase; letter-spacing: 0.1em;
    transition: color 0.2s ease; position: relative;
}
.nav-links a::after {
    content: ''; position: absolute; bottom: -4px; left: 0;
    width: 0; height: 2px; background: var(--rosso);
    transition: width 0.3s ease;
}
.nav-links a:hover { color: var(--ecru); }
.nav-links a:hover::after { width: 100%; }

/* === Content Layout === */
main { position: relative; z-index: 10; }
.section-content {
    padding-left: var(--spine-left); padding-right: 4rem; max-width: 1200px;
}

/* === Case Header === */
.case-header {
    min-height: 70vh; display: flex; flex-direction: column;
    justify-content: center; padding-top: 8rem; padding-bottom: 4rem;
}
.case-meta {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.8rem;
    color: var(--quetzal); letter-spacing: 0.1em; margin-bottom: 2rem;
    display: block; animation: fade-up 0.8s ease 0.4s both;
}
.case-tag {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    font-weight: 700; color: var(--rosso); text-transform: uppercase;
    letter-spacing: 0.2em; margin-bottom: 1.5rem; display: block;
    animation: fade-up 0.8s ease 0.5s both;
}
.case-header h1 {
    font-family: 'Imbue', serif; font-size: clamp(2.5rem, 7vw, 6rem);
    font-weight: 900; line-height: 0.9; color: var(--ecru);
    text-transform: uppercase; letter-spacing: -0.02em;
    margin-bottom: 2.5rem; max-width: 700px;
    animation: fade-up 0.8s ease 0.6s both;
}
.case-header h1 .accent-word { color: var(--rosso); }
.case-lede {
    border-left: 5px solid var(--rosso); padding-left: 2rem;
    max-width: 600px; animation: fade-up 0.8s ease 0.8s both;
}
.case-lede p {
    font-size: 1.15rem; font-weight: 300; line-height: 1.7; color: var(--ecru-dim);
}
.case-lede strong { color: var(--ecru); font-weight: 500; }

/* === Case Sections === */
.case-section {
    padding-top: 2.5rem; padding-bottom: 2.5rem;
    border-top: 1px solid var(--ecru-ghost);
}
.section-label {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    font-weight: 700; color: var(--quetzal-bright); letter-spacing: 0.2em;
    text-transform: uppercase; margin-bottom: 0.5rem; display: block;
}
h2 {
    font-family: 'Imbue', serif; font-size: clamp(1.8rem, 4vw, 3rem);
    font-weight: 900; color: var(--ecru); text-transform: uppercase;
    line-height: 0.95; letter-spacing: -0.01em; margin-bottom: 2.5rem;
}
.case-body p {
    font-size: 1.05rem; font-weight: 300; line-height: 1.8;
    color: var(--ecru-dim); margin-bottom: 1.5rem; max-width: 650px;
}
.case-body p strong { color: var(--ecru); font-weight: 500; }

/* === Constraint List === */
.constraint-list { margin: 2rem 0; max-width: 650px; }
.constraint-item {
    padding: 1.25rem 0; border-bottom: 1px solid var(--ecru-ghost);
    display: grid; grid-template-columns: auto 1fr; gap: 1.25rem; align-items: start;
}
.constraint-item:first-child { border-top: 1px solid var(--ecru-ghost); }
.constraint-flag {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    font-weight: 700; letter-spacing: 0.1em; padding: 0.2rem 0.5rem;
    text-transform: uppercase; min-width: 50px; text-align: center;
}
.constraint-flag.red { color: var(--rosso); border: 1px solid var(--rosso); }
.constraint-flag.yellow { color: #D4A017; border: 1px solid #D4A017; }
.constraint-label { font-size: 0.95rem; font-weight: 400; color: var(--ecru); line-height: 1.4; }
.constraint-detail { font-size: 0.85rem; font-weight: 300; color: var(--ecru-dim); margin-top: 0.25rem; }

/* === Failure Loop === */
.failure-loop {
    border-left: 3px solid var(--cacao); padding-left: 1.5rem;
    margin: 2rem 0; max-width: 400px;
}
.failure-loop .loop-step {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    color: var(--ecru-dim); padding: 0.4rem 0; display: flex;
    align-items: center; gap: 0.75rem;
}
.failure-loop .loop-arrow { color: var(--rosso); font-weight: 700; }

/* === Approach Grid === */
.approach-grid {
    display: grid; grid-template-columns: 1fr 1fr; gap: 2px;
    margin: 2.5rem 0; max-width: 750px;
}
.approach-item { background: rgba(245, 245, 220, 0.14); padding: 2rem 1.75rem; }
.approach-day {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    font-weight: 700; color: var(--rosso); text-transform: uppercase;
    letter-spacing: 0.2em; margin-bottom: 0.75rem;
}
.approach-title {
    font-family: 'Imbue', serif; font-size: 1.3rem; font-weight: 700;
    color: var(--ecru); text-transform: uppercase; line-height: 1.1;
    margin-bottom: 0.75rem;
}
.approach-desc {
    font-size: 0.85rem; font-weight: 300; color: var(--ecru-dim); line-height: 1.5;
}

/* === Artifact Grid === */
.artifact-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2px; margin: 2.5rem 0;
}
.artifact-card {
    background: rgba(245, 245, 220, 0.14); padding: 2rem 1.75rem;
    position: relative; transition: background 0.3s ease;
    text-decoration: none; display: block;
}
.artifact-card::before {
    content: ''; position: absolute; top: 0; left: 0;
    width: 0; height: 3px; background: var(--rosso);
    transition: width 0.4s ease;
}
.artifact-card:hover { background: rgba(245, 245, 220, 0.18); }
.artifact-card:hover::before { width: 100%; }
.artifact-type {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    font-weight: 700; color: var(--quetzal-bright); text-transform: uppercase;
    letter-spacing: 0.2em; margin-bottom: 0.75rem;
}
.artifact-name {
    font-family: 'Imbue', serif; font-size: 1.15rem; font-weight: 700;
    color: var(--ecru); text-transform: uppercase; line-height: 1.15;
    margin-bottom: 0.75rem;
}
.artifact-desc {
    font-size: 0.85rem; font-weight: 300; color: var(--ecru-dim);
    line-height: 1.5; margin-bottom: 1rem;
}
.artifact-action {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    color: var(--rosso); text-transform: uppercase; letter-spacing: 0.15em;
}

/* === Outcome Grid === */
.outcome-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2px; margin: 2.5rem 0; max-width: 750px;
}
.outcome-stat { background: rgba(245, 245, 220, 0.14); padding: 2rem 1.75rem; }
.outcome-number {
    font-family: 'Imbue', serif; font-size: 2.5rem; font-weight: 900;
    color: var(--ecru); line-height: 1; margin-bottom: 0.5rem;
}
.outcome-number.highlight { color: var(--rosso); }
.outcome-label {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    color: var(--quetzal-bright); text-transform: uppercase; letter-spacing: 0.1em;
    line-height: 1.4;
}

/* === Back Link === */
.back-link {
    display: inline-flex; align-items: center; gap: 0.75rem;
    font-family: 'IBM Plex Mono', monospace; font-size: 0.8rem;
    color: var(--ecru-dim); text-decoration: none; text-transform: uppercase;
    letter-spacing: 0.1em; transition: color 0.2s ease; margin-top: 3rem;
}
.back-link::before {
    content: ''; display: block; width: 24px; height: 2px;
    background: var(--quetzal); transition: width 0.3s ease, background 0.3s ease;
}
.back-link:hover { color: var(--ecru); }
.back-link:hover::before { width: 40px; background: var(--rosso); }

/* === Footer === */
footer {
    padding: 2rem 2rem 2rem var(--spine-left);
    border-top: 1px solid var(--ecru-ghost);
}
.footer-content {
    display: flex; justify-content: space-between; align-items: center;
    max-width: 1200px;
}
.footer-content span {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    color: var(--ecru-dim); letter-spacing: 0.05em;
}

/* === Animations === */
@keyframes spine-draw { from { height: 0; } to { height: 100%; } }
@keyframes fade-up { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
@keyframes grid-fade { from { opacity: 0; } to { opacity: 1; } }
.reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.6s ease, transform 0.6s ease; }
.reveal.visible { opacity: 1; transform: translateY(0); }
```

---

## Branded Artifact Page

Uses the same dark-variant design system as the case study page. The key addition is the `.doc-content` layout and the download button.

### Additional CSS (on top of case study base)

```css
/* Document content area */
.doc-content {
    padding-left: var(--spine-left); padding-right: 4rem; max-width: 1200px;
}

/* Download button */
.download-btn {
    display: inline-block; font-family: 'IBM Plex Mono', monospace;
    font-size: 0.85rem; font-weight: 700; letter-spacing: 0.15em;
    text-transform: uppercase; color: var(--nuit); background: var(--ecru);
    text-decoration: none; padding: 0.75rem 2rem;
    transition: background 0.2s, color 0.2s;
}
.download-btn:hover { background: var(--rosso); color: var(--ecru); }

/* Branded tables */
.branded-table { width: 100%; border-collapse: collapse; margin: 2rem 0; }
.branded-table th {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    font-weight: 700; color: var(--quetzal-bright); text-transform: uppercase;
    letter-spacing: 0.1em; text-align: left; padding: 0.75rem 1rem;
    border-bottom: 2px solid var(--cacao);
}
.branded-table td {
    font-size: 0.85rem; font-weight: 300; color: var(--ecru-dim);
    padding: 1rem; border-bottom: 1px solid var(--ecru-ghost);
    vertical-align: top; line-height: 1.5;
}
.branded-table tr:hover td { background: var(--ecru-ghost); }

/* Flag badges */
.flag {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    font-weight: 700; letter-spacing: 0.1em; padding: 0.15rem 0.4rem;
    text-transform: uppercase; display: inline-block;
}
.flag.red { color: var(--rosso); border: 1px solid var(--rosso); }
.flag.yellow { color: #D4A017; border: 1px solid #D4A017; }
.flag.green { color: var(--ecru-dim); border: 1px solid rgba(245, 245, 220, 0.3); }

/* Stat rows */
.stat-row {
    display: flex; gap: 2px; margin: 2rem 0;
}
.stat-box {
    background: rgba(245, 245, 220, 0.14); padding: 1.5rem; flex: 1; text-align: center;
}
.stat-box .stat-num {
    font-family: 'Imbue', serif; font-size: 2rem; font-weight: 900; color: var(--ecru);
}
.stat-box .stat-label {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    color: var(--quetzal-bright); text-transform: uppercase; letter-spacing: 0.1em;
}

/* Callout/principle boxes */
.core-principle {
    border-left: 4px solid var(--rosso); padding: 2rem;
    background: rgba(245, 245, 220, 0.14); margin: 2.5rem 0; max-width: 650px;
}
```

### Artifact Page Navigation Pattern

The nav links back to the case study AND the main site:

```html
<nav class="nav-bar" role="navigation">
    <a href="../{case-slug}.html" class="nav-mark" style="text-decoration: none;">
        &larr; {Case Name}
    </a>
    <ul class="nav-links">
        <li><a href="/">Main Site</a></li>
    </ul>
</nav>
```

---

## Blank Template

### Full CSS for Light-Variant Templates

```css
:root {
    --nuit: #121A28; --cacao: #2D1B14; --quetzal: #00685E;
    --ecru: #F5F5DC; --rosso: #C41E3A;
    --text: #1a1a1a; --text-dim: #555; --border: #d4d0c8;
    --border-light: #e8e4dc; --hover-bg: rgba(0, 104, 94, 0.04);
}

*, *::before, *::after {
    margin: 0; padding: 0; box-sizing: border-box;
    font-style: normal !important; border-radius: 0 !important;
}
::selection { background: var(--rosso); color: var(--ecru); }

body {
    background-color: var(--ecru); color: var(--text);
    font-family: 'IBM Plex Sans', sans-serif; font-weight: 400;
    line-height: 1.6; -webkit-font-smoothing: antialiased;
    padding: 4rem 3rem; max-width: 1000px;
}

/* Header */
.template-header {
    margin-bottom: 3rem; padding-bottom: 2rem;
    border-bottom: 2px solid var(--cacao);
}
.template-type {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.65rem;
    font-weight: 700; color: var(--rosso); text-transform: uppercase;
    letter-spacing: 0.2em; margin-bottom: 1rem;
}
h1 {
    font-family: 'Imbue', serif; font-size: 2.5rem; font-weight: 900;
    line-height: 0.9; text-transform: uppercase; margin-bottom: 0.75rem;
    color: var(--nuit);
}
h1 .accent { color: var(--rosso); }
.subtitle {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem;
    color: var(--quetzal); letter-spacing: 0.05em; margin-bottom: 1.5rem;
}
.instructions {
    font-size: 0.95rem; font-weight: 300; color: var(--text-dim);
    line-height: 1.7; max-width: 600px;
}
.instructions strong { color: var(--text); font-weight: 500; }

/* Print Button */
.print-btn {
    display: inline-block; font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem; font-weight: 700; letter-spacing: 0.15em;
    text-transform: uppercase; color: var(--ecru); background: var(--nuit);
    border: none; padding: 0.75rem 2rem; cursor: pointer; margin-top: 1rem;
    transition: background 0.2s;
}
.print-btn:hover { background: var(--quetzal); }

/* Sections */
.section { margin-top: 3rem; }
.section-label {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.7rem;
    font-weight: 700; color: var(--quetzal); letter-spacing: 0.2em;
    text-transform: uppercase; margin-bottom: 1rem;
}
h2 {
    font-family: 'Imbue', serif; font-size: 1.8rem; font-weight: 900;
    text-transform: uppercase; line-height: 0.95; margin-bottom: 1.5rem;
    color: var(--nuit);
}

/* Tables */
table { width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.85rem; }
th {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.65rem;
    font-weight: 700; color: var(--quetzal); text-transform: uppercase;
    letter-spacing: 0.1em; text-align: left; padding: 0.75rem 1rem;
    border-bottom: 2px solid var(--cacao);
}
td {
    padding: 1.5rem 1rem; border-bottom: 1px solid var(--border);
    color: var(--text-dim); font-weight: 300; vertical-align: top;
}
tr:hover td { background: var(--hover-bg); }

/* Flags */
.flag-key { margin: 2rem 0; font-size: 0.85rem; color: var(--text-dim); }
.flag {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.6rem;
    font-weight: 700; letter-spacing: 0.1em; padding: 0.15rem 0.4rem;
    text-transform: uppercase; display: inline-block; margin-right: 1rem;
}
.flag.red { color: var(--rosso); border: 1px solid var(--rosso); }
.flag.yellow { color: #D4A017; border: 1px solid #D4A017; }
.flag.green { color: var(--text-dim); border: 1px solid var(--border); }

/* Day Cards (for methodology templates) */
.day-card {
    background: rgba(0, 104, 94, 0.06); padding: 2rem; margin-bottom: 2px;
}
.day-num {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.65rem;
    font-weight: 700; color: var(--rosso); text-transform: uppercase;
    letter-spacing: 0.2em; margin-bottom: 0.5rem;
}
.day-label {
    font-family: 'Imbue', serif; font-size: 1.3rem; font-weight: 900;
    color: var(--nuit); text-transform: uppercase; line-height: 1.1;
    margin-bottom: 1rem;
}
.field { margin-bottom: 1.5rem; }
.field-label {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.6rem;
    font-weight: 700; color: var(--quetzal); text-transform: uppercase;
    letter-spacing: 0.15em; margin-bottom: 0.5rem;
}
.field-area {
    border-bottom: 1px solid var(--border); padding: 0.75rem 0;
    min-height: 2.5rem; color: var(--text-dim); font-weight: 300;
    font-size: 0.9rem;
}
.mantra-area {
    border-left: 3px solid var(--cacao); padding: 1rem; margin: 1rem 0;
}
.mantra-area .field-area { min-height: 4rem; }

/* Category key (for register templates) */
.category-key { margin: 2rem 0; max-width: 600px; }
.cat-item {
    padding: 0.75rem 1rem; background: rgba(0, 104, 94, 0.06);
    margin-bottom: 2px; display: flex; gap: 1rem; align-items: baseline;
}
.cat-name {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.65rem;
    font-weight: 700; color: var(--quetzal); text-transform: uppercase;
    letter-spacing: 0.1em; min-width: 100px;
}
.cat-desc {
    font-size: 0.8rem; font-weight: 300; color: var(--text-dim); line-height: 1.5;
}

/* Resolution key (for friction map templates) */
.resolution-key {
    margin: 2rem 0; padding: 1.5rem;
    background: rgba(0, 104, 94, 0.06); max-width: 600px;
}
.resolution-key p {
    font-size: 0.85rem; font-weight: 300; color: var(--text-dim);
    line-height: 1.6; margin-bottom: 0.5rem;
}
.resolution-key strong { color: var(--text); font-weight: 500; }

/* Attribution */
.attribution {
    font-family: 'IBM Plex Mono', monospace; font-size: 0.7rem;
    color: var(--text-dim); letter-spacing: 0.05em; margin-top: 4rem;
    padding-top: 1.5rem; border-top: 1px solid var(--border);
}

/* === Print Styles === */

/* For TABLE-BASED templates (frameworks, registers, maps): */
@page { size: landscape; margin: 0.5in; }
@media print {
    body { background: white; padding: 1rem; max-width: none; }
    .print-btn { display: none; }
    table { font-size: 0.75rem; }
    td { min-height: 60px; padding: 1rem 0.75rem; }
    th { font-size: 0.6rem; }
}

/* For NON-TABLE templates (methodologies, day-card layouts):
   OMIT the @page { size: landscape; } rule. Keep portrait. */
@media print {
    body { background: white; padding: 2rem; }
    .day-card { border: 1px solid #ddd; }
    .print-btn { display: none; }
}
```

**Important:** Table-based templates get `@page { size: landscape; }`. Non-table templates (day-card layouts like facilitation mindsets) stay portrait — omit the `@page` rule entirely.

---

## Responsive Breakpoints

Both dark-variant pages use these breakpoints:

```css
@media (max-width: 900px) {
    :root { --spine-left: 5%; }
    .spine { left: 12px; width: 3px; }
    .section-content, .doc-content { padding-left: 2rem; padding-right: 2rem; }
    .nav-bar { padding-left: 2rem; }
    .approach-grid { grid-template-columns: 1fr; }
    .artifact-grid { grid-template-columns: 1fr; }
    .outcome-grid { grid-template-columns: 1fr 1fr; }
    .nav-links { gap: 1.25rem; padding-right: 1rem; }
    footer { padding-left: 2rem; }
}

@media (max-width: 500px) {
    .nav-mark { display: none; }
    .nav-bar { justify-content: flex-end; }
    .nav-links a { font-size: 0.75rem; }
    .blueprint-overlay { background-size: 24px 24px; }
    .outcome-grid { grid-template-columns: 1fr; }
}
```

---

## JavaScript Patterns

### Scroll Reveal (IntersectionObserver)

Used on both case study pages and branded artifact pages:

```javascript
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

Apply `.reveal` class to every `<section>` except the header section. The observer adds `.visible` when the element enters the viewport, triggering the CSS transition from `opacity: 0; transform: translateY(30px)` to `opacity: 1; transform: translateY(0)`.
