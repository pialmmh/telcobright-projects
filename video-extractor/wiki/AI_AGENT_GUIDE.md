# AI Agent Guide — Using This Wiki to Build Software

This wiki is a structured snapshot of software products extracted from tutorial videos. It is designed to be consumed by an AI coding agent that will reproduce or clone the described software.

## How to read this wiki

1. **Start at [`index.md`](index.md)** — it lists every product and links to that product's pages.
2. **For any product, read the pages in this order**:
   1. `<product>-modules.md` — module/navigation overview
   2. `<product>-data-entities.md` — entity schemas (use these for DB design)
   3. Per-module pages — UX, fields, workflows
   4. Any `<product>-vs-<other>.md` — pattern comparisons
3. **Also read** the matching `<product>/knowledge_graph.json` — it is the machine-readable mirror of the wiki and is authoritative when there's a conflict (the wiki is rendered prose; the JSON is the source schema).

## Authority order (when sources disagree)

1. `<product>/knowledge_graph.json` — authoritative for entities, fields, modules, screen names.
2. Wiki markdown — authoritative for narrative, workflows, UX descriptions, comparisons.
3. `<product>/screenshots/*.jpg` — visual confirmation only. **May be absent.**

## About screenshots

Each product has a `screenshots/` directory holding one representative image per significant scene from the source video. Wiki pages reference this directory via relative paths (e.g. `../<product>/screenshots/frame_0079.jpg`).

**The screenshot directory may be missing** (pruned to save space, or not synced in this checkout). Before relying on any frame:

```bash
ls <product>/screenshots/frame_NNNN.jpg
```

If the file is absent, **do not invent visual details**. Work from the wiki text + JSON only, and surface gaps explicitly rather than guessing.

A separate `frames/` directory may also exist alongside `screenshots/` — that's the raw 1 fps capture and is **not** part of the wiki contract. Ignore it; reference only `screenshots/`.

## What to build from this wiki

- **DB schema** → `<product>-data-entities.md` + the `data_entities` array in `knowledge_graph.json`. Fields, types, and relationships are listed.
- **API surface** → derive CRUD endpoints per entity unless module pages specify a different shape.
- **UI screens** → one page per module describes layout, components, fields. Match the navigation tree in `<product>-modules.md`.
- **Workflows** → state machines and step sequences are in module pages, usually as tables or numbered lists.
- **Cross-module features** → listed in `cross_module_features` (JSON) and the modules page (markdown).

## What NOT to assume

- Don't assume a feature exists if it isn't in the wiki/JSON — the source video may not have shown it. Mark such features as "out of scope of the source" rather than inventing them.
- Don't reproduce video-specific demo data (sample names, phone numbers, addresses) as fixed values — treat them as illustrative.
- Don't assume tech stack from the wiki alone. The wiki captures *what the product does*, not *how it was built*. Pick the implementation stack based on the user's separate instructions.

## Asking for clarification

If a wiki page is ambiguous, contradicts the JSON, or lacks information needed to implement a feature: surface the question to the user. Do not guess. The wiki is a frozen snapshot; only the user can resolve gaps.
