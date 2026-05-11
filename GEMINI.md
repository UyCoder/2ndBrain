# LLM Wiki Schema: Competitor Analysis

This document defines the structure, conventions, and workflows for maintaining this competitor analysis knowledge base.

## 1. Core Architecture
- **/raw**: Immutable source documents (clippings, PDFs, meeting notes, etc.).
- **/wiki**: Persistent, interlinked markdown pages maintained by the LLM.
- **/wiki/index.md**: Content-oriented catalog of all wiki pages.
- **/wiki/log.md**: Chronological record of ingests and queries.

## 2. Wiki Structure
Organize pages into the following categories:
- **Competitors**: Dedicated pages for each company (e.g., `competitor-acme.md`).
- **Products**: Features, pricing, and comparisons of specific offerings.
- **Market Trends**: Broad industry shifts and macro-trends.
- **Concepts**: Specific technologies, business models, or strategies.
- **Syntheses**: Deep dives and cross-competitor analyses.

## 3. Maintenance Workflows

### Ingest Workflow
When a new source is added to `/raw`:
1. **Read & Extract**: Identify key facts, claims, and data points.
2. **Update Competitor/Product Pages**: Integrate new info into existing pages. Flag contradictions.
3. **Update Index**: Ensure the new/updated pages are reflected in `index.md`.
4. **Log Action**: Append a entry to `log.md` with the format `## [YYYY-MM-DD] ingest | Description`.

### Query Workflow
When a question is asked:
1. **Consult Index**: Use `index.md` to find relevant pages.
2. **Synthesize**: Read relevant pages and raw sources if necessary to answer.
3. **Compound**: If the answer is substantial, offer to save it as a new Synthesis page in the wiki.

### Lint Workflow
Periodically check for:
- Dead links or orphan pages.
- Stale data or unaddressed contradictions.
- Missing cross-references between related competitors/products.

## 4. Writing Style
- Use clear, professional, and objective language.
- Use internal wikilinks: `[[page-name]]`.
- Include citations to raw sources (e.g., `[Source: raw/article.md]`).
- Use YAML frontmatter for metadata (e.g., `tags`, `last_updated`, `competitor`).


## 5. Promt for wiki generation
 I added a webpage via clipper. Ingest every article extremely thoroughly. build relationships automatically. add one wiki for one file average. the wiki you generated should be contains more info as possible. and language should be in Uyghur language. also try to make more link to other wiki between wiki page. the clipping pages that you already generated wiki page from must be moved to the raw folder, so that you will not analyze it each time later.

## 6. Prompt for Article translation
Translate all the clippings from [Aisixiang Chinese] articles to Uyghur language inside clippings folder and put the translation in the translationArtcles folder . don't remove any clippings after translation.