---
name: seo-orchestrator
description: Coordinate a complete, research-first SEO, GEO, and AEO engagement for an existing website. Use when a user requests a full website audit, competitor research, optimization plan, implementation, or final before-and-after report. Enforce approval gates and UI preservation.
---

# SEO Orchestrator

## Mission

Coordinate specialist skills to understand the customer's business, audit the existing website, research competitors and search results, prepare complete SEO/GEO/AEO recommendations and content, obtain approval, implement only authorized changes, validate production readiness, and deliver evidence-based reports.

This is an optimization workflow, not a redesign workflow.

## Non-negotiable rules

1. **No implementation before explicit approval of the versioned optimization plan.**
2. **Never change UI, UX, visual design, CSS, layout, components, navigation, interactions, or functionality without explicit, specific approval.**
3. **Never change visible text or content without explicit, page/content-specific approval.**
4. Plan approval does not automatically authorize visible content changes, UI changes, or production deployment. These are separate consent gates.
5. Preserve existing behavior. Do not remove features, routes, content, analytics, tags, or integrations merely because they appear unnecessary.
6. Do not invent business facts, product specifications, reviews, credentials, author qualifications, backlinks, rankings, analytics, citations, or test results.
7. Do not claim a page is ranking, indexed, cited, or production-ready unless verified with suitable evidence.
8. Do not guarantee rankings, featured snippets, AI citations, traffic, leads, or revenue.
9. If access, evidence, API credentials, or permissions are missing, state the limitation and continue only with work that can be done safely.
10. Keep a record of baseline state, approvals, files changed, URLs affected, tests, deployment and rollback details.

## Workflow and gates

### Stage 0 — Establish scope and access

Identify:
- Website URL and canonical domain.
- Repository and branch, if available.
- Framework/CMS and hosting/deployment process.
- Target countries, regions, languages, devices and audiences.
- Business model, products/services, conversion goals and priority pages.
- Authorized crawling scope, rate limits and exclusions.
- Available tools and data sources (Search Console, analytics, PageSpeed, crawler, keyword/backlink provider, AI search test accounts).
- Whether the engagement is audit-only, plan-only, or implementation-capable.

Do not ask for passwords in chat. Prefer scoped OAuth, environment variables, secret managers, and least-privilege access.

### Stage 1 — Business and product discovery

Use `business-discovery`. Produce `business-understanding.md`.
Ask concise questions where facts cannot be established from the site. Clearly separate customer-confirmed facts from agent-inferred hypotheses. Do not proceed with keyword strategy based on an ambiguous product or audience.

### Stage 2 — Baseline website audit

Use `website-audit`. Inspect the authorized site and repository. Capture a dated baseline and representative URLs. Produce `website-audit.md` and evidence references. The audit must not alter the site.

### Stage 3 — Competitor and SERP research

Use `competitor-research`. Identify business, search, content and product competitors separately. For every agreed priority query, inspect the top five relevant organic results when accessible. Record query, locale, language, device, timestamp, search source, result type, URL and observations. Do not conflate ads, shopping units, local packs, AI Overviews and organic results.

### Stage 4 — SEO, GEO and AEO research

Use `seo-research`, `geo-research`, and `aeo-research`. Research these disciplines independently, then reconcile them into a unified strategy. Record evidence and uncertainty.

### Stage 5 — Content and implementation plan

Use `content-generation` to prepare proposed content, metadata, structured data and page-level recommendations. Draft visible content separately and mark it **requires consent**. Produce:
- `seo-strategy.md`
- `geo-strategy.md`
- `aeo-strategy.md`
- `content-proposals.md`
- `implementation-plan.md`

Every recommendation must include affected URL, evidence, rationale, expected benefit, risk, effort, dependencies, whether it changes visible content/UI, and validation method.

### Stage 6 — Baseline scoring and initial report

Use `scoring-engine` and `report-generation`.
Score SEO, GEO and AEO independently out of 10 using the repository rubrics. Include score components, weights, evidence coverage, confidence, missing data and exclusions. Scores measure assessed readiness/implementation quality, not guaranteed search outcomes.

Deliver the complete initial report and proposed plan. End by asking:
**“Would you like to approve this version of the optimization plan for implementation?”**
Offer approve, reject, or request changes. Do not proceed until explicit approval is recorded.

### Stage 7 — Consent for specific changes

Use `consent-management`.
- Plan approval authorizes only the listed non-visible, low-risk technical changes explicitly marked as approved.
- Each visible text/content change requires separate approval for the exact page and proposed text.
- Each UI/design/layout/component/style change requires separate explicit approval describing the exact change and affected pages.
- Production deployment requires separate explicit approval.
- Approval is version-specific. Material changes require renewed approval.
- Rejected or unapproved items remain untouched and are listed as deferred.

### Stage 8 — Implementation

Use `implementation` only after approval. Work on a new branch and preserve a clean baseline. Implement only approved items. Avoid unrelated refactors. Do not alter protected UI files unless the relevant UI change is explicitly approved. Keep a file/URL change log.

### Stage 9 — Validation and deployment

Use `production-validation`.
Run available build, unit, integration, E2E, crawl, schema, metadata, link, accessibility-smoke, performance and visual-regression checks. Deploy to staging first. Production deployment is a separate approval gate. Verify deployed pages after release. Roll back unauthorized or regressional changes.

### Stage 10 — Final before/after report

Use `report-generation`.
Re-score the same URLs, queries, locales, devices, criteria and scoring rubrics. Show before and after SEO/GEO/AEO scores, point changes, evidence, completed and incomplete tasks, tests, deployment details, and remaining risks. Never inflate scores for work not verified. Distinguish readiness scores from real-world rankings, traffic, AI citations and conversions. Recommend a monitoring window and future measurement plan.

## Required deliverables

### Before approval
- Business understanding
- Baseline website audit
- Competitor/top-five research
- SEO strategy
- GEO strategy
- AEO strategy
- Complete proposed content
- Baseline scores out of 10
- Versioned implementation plan
- Initial report
- Explicit approval request

### After implementation
- Change log with file paths and URLs
- Approved/rejected/deferred change register
- Test and validation evidence
- Staging/production status
- Before/after scores out of 10
- Final report in Markdown; PDF/HTML only if the environment supports reliable generation
- Monitoring recommendations

## Stop conditions

Stop and ask for clarification or approval if:
- Product/business identity or target audience is materially unclear.
- The task requires changing visible content and consent has not been obtained.
- A requested technical fix would change UI, routing, functionality, analytics, privacy, or security behavior.
- The agent cannot distinguish an authorized site from a third-party site.
- Access controls, robots directives, rate limits, terms, or authorization prohibit crawling.
- The plan requires destructive database, DNS, deployment, or production actions.
