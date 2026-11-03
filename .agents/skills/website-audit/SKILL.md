---
name: website-audit
description: Perform a read-only baseline audit of an existing website for technical SEO, on-page SEO, content, performance, accessibility and GEO/AEO readiness without modifying the website.
---

# Website Audit

## Safety

This skill is read-only. Do not edit website files, CMS content, DNS, hosting, analytics, robots, sitemap or production settings during the audit.

## Audit dimensions

### Crawl and indexation
- HTTP status and redirect chains.
- Robots.txt directives and sitemap references.
- XML sitemap validity, canonical host and indexable URL coverage.
- Meta robots and X-Robots-Tag.
- Canonical tags and duplicate URL patterns.
- Orphan pages, crawl depth and internal links where crawl data permits.
- Soft 404s, 404s, 5xx, redirect loops and broken links.
- JavaScript rendering and indexable content visibility.

### On-page and content
- Unique, descriptive titles and meta descriptions.
- One clear primary page topic; heading hierarchy.
- Search intent and content usefulness.
- Duplicate/thin/near-duplicate content.
- Image alt attributes (distinguish decorative images).
- Descriptive URLs, breadcrumbs and internal anchors.
- E-E-A-T-related evidence: authorship, sourcing, first-hand experience, business identity and contact details. Do not treat E-E-A-T as a direct numeric Google ranking factor.
- Content freshness where dates and change history are verifiable.

### Structured data
- Existing JSON-LD, Microdata or RDFa.
- Syntax and schema type suitability.
- Required/recommended properties and consistency with visible content.
- Rich-result eligibility limitations. Valid schema does not guarantee rich results.

### Performance and experience
- Core Web Vitals field data when available: LCP, INP, CLS.
- Lab data separately labelled (e.g. Lighthouse/PageSpeed).
- Mobile usability and responsive behavior.
- Accessibility smoke checks and semantic structure.
- Third-party scripts and asset weight where measurable.

### GEO/AEO readiness
- Clear entity/business identity.
- Consistent organization/product facts.
- Answerable questions and concise factual explanations.
- Evidence, citations, authorship and source transparency.
- Machine-readable structured data.
- Crawl access for relevant search/AI user agents, without recommending blanket access changes without a reason.
- Current AI/search answer visibility only when directly tested and documented.

## Output

For each issue record:
- ID and category
- URL(s)
- Severity (Critical/High/Medium/Low/Informational)
- Observed evidence and timestamp
- Why it matters
- Recommended remediation
- Whether it changes visible text/UI
- Validation method
- Confidence and limitations

Produce `website-audit.md` and a URL inventory. Do not change the site.
