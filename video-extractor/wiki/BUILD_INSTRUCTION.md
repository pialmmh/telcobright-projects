# Building Software from a Video-Extracted Wiki

You are being asked to build a working clone of a software product whose specification was extracted from a tutorial video. The specification lives in a Karpathy-style wiki at:

```
/home/mustafa/telcobright-projects/video-extractor/wiki/
```

with companion machine-readable JSON and screenshots at:

```
/home/mustafa/telcobright-projects/video-extractor/<product>/knowledge_graph.json
/home/mustafa/telcobright-projects/video-extractor/<product>/screenshots/
```

## Step 0 — Read the agent guide first

Open `wiki/AI_AGENT_GUIDE.md` before anything else. It defines the read order, the authority hierarchy (JSON > wiki > screenshots), and the rules for handling missing artifacts. Do not skip it.

## Step 1 — LOOK AT THE SCREENSHOTS. THIS IS NOT OPTIONAL.

The wiki text is dense but compressed; it cannot reproduce every visual nuance. The screenshots in `<product>/screenshots/` are the highest-fidelity record of what the software looks like and how its UI is laid out. **Open every screenshot in the product's `screenshots/` directory using the `Read` tool before you write a single line of code.**

Why this matters:

- Field labels, button labels, dropdown contents, icon affordances, modal layouts, column orders, badge colours, status pills, tab arrangements, table row densities, pagination styles — these are visible in the screenshots and frequently *not* fully spelled out in the markdown.
- Spatial relationships (left panel vs right panel, sticky headers, action bars at top vs bottom, inline vs modal editing) determine the React/HTML structure you write. Markdown tables flatten this; screenshots preserve it.
- Empty-state and loading-state hints, microcopy, and helper text often appear only in the image.
- The wiki's job is to *index* and *summarise* what the screenshots show. If you build only from the prose, you will produce a UI that is structurally wrong even if the data model is correct.

Concrete rule:

> Before implementing any screen, you MUST `Read` every screenshot referenced for that screen (look up `representative_frames` in `knowledge_graph.json`, or scan `screenshots/` and match by section). If a screenshot is missing from the directory, say so explicitly in your plan and surface it to the user — do not silently fall back to text-only.

## Step 2 — Confirm the screenshot directory exists

```bash
ls /home/mustafa/telcobright-projects/video-extractor/<product>/screenshots/ | wc -l
```

If empty or missing, **stop and ask the user**. The screenshots are part of the contract — if they were pruned from this checkout, the user needs to know before you proceed text-only.

## Step 3 — Build plan, then code

After reading the wiki + JSON + every screenshot:

1. Write a short build plan: modules in build order, the entities each module needs, the screens each module owns, and which screenshots informed each screen.
2. Wait for user approval.
3. Then code.

## Authority order when sources disagree

1. `<product>/knowledge_graph.json` — authoritative for entities, fields, modules, screen names.
2. Wiki markdown — authoritative for narrative, workflows, comparisons.
3. `<product>/screenshots/*.jpg` — authoritative for visual layout, exact labels, spatial structure.

When the JSON says "field X exists" and a screenshot shows it labelled differently — trust the screenshot for the label, the JSON for the existence.

## What NOT to do

- Don't invent features that aren't in the wiki, JSON, *and* visible in at least one screenshot. If it's only in one source and looks ambiguous, ask.
- Don't substitute "modern best practice" for what the screenshots show. If the demo product uses a 1990s-style table with no sort indicators, build that — don't upgrade it unprompted.
- Don't skip reading screenshots because the markdown "looked complete." It never is.
- Don't reproduce demo data (sample names, phone numbers, addresses) as fixtures unless the user asks — those are illustrative.
- Don't pick a tech stack from the wiki. The wiki captures *what the product does*, not *how it was built*. Use the stack the user specifies.

## When to ask the user

- A screenshot is missing for a screen you need to build.
- The JSON, wiki, and screenshots disagree in a non-trivial way.
- A workflow has a branch that the video clearly didn't cover.
- The user-facing tech stack / runtime / DB choice was not specified.

## Quick checklist before you write code

- [ ] Read `wiki/AI_AGENT_GUIDE.md`
- [ ] Read `wiki/index.md` and the product's pages in order
- [ ] Read `<product>/knowledge_graph.json`
- [ ] **Read every JPG in `<product>/screenshots/` using the `Read` tool**
- [ ] Confirmed screenshots directory is non-empty (else stopped and asked)
- [ ] Wrote a build plan and got user approval
- [ ] Confirmed tech stack with user
