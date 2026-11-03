---
name: production-validation
description: Validate approved SEO, GEO and AEO implementation through automated tests, crawling, schema checks, visual regression and post-deployment verification.
---

# Production Validation

## Gates

1. Local validation.
2. Staging deployment and validation.
3. Separate explicit production deployment approval.
4. Production deployment.
5. Post-deployment verification.

## Checks

### Build and application
- Framework build succeeds.
- Unit/integration/E2E tests pass where available.
- No new console errors or server errors.
- Critical routes and conversion journeys remain functional.
- Existing API, authentication, forms and integrations remain functional.

### SEO
- Status codes and redirect chains.
- Canonical URL correctness.
- Robots directives and sitemap.
- Title/meta description and heading presence.
- Internal links and broken links.
- Indexability and rendered content.
- Hreflang correctness where applicable.
- JSON-LD syntax and page-content consistency.

### GEO/AEO
- Entity facts are consistent and supported.
- Proposed answers are visible, accurate and useful.
- Citations/references resolve and support claims.
- Structured data is valid and truthful.
- AI visibility tests are repeated only through documented sources and methods.

### UI preservation
- Capture baseline and after screenshots for representative routes/viewports.
- Run visual regression comparison if tooling is available.
- Compare DOM/component changes and CSS diffs.
- Verify layout, typography, colors, spacing, navigation and interactions.
- Any unexpected visual or functional regression blocks release.
- If visual testing is unavailable, disclose the limitation; do not claim visual equivalence.

### Performance and accessibility
- Compare field data only with comparable field data.
- Compare lab data only under comparable test conditions.
- Check LCP, INP, CLS where measurable.
- Run accessibility smoke tests for affected pages.

## Failure handling

- Do not suppress failures.
- Fix only within approved scope.
- If a fix requires unapproved visible/UI changes, pause and request consent.
- Roll back unauthorized or harmful changes.
- Record failed checks, root cause, owner/action and release decision.

## Production status

Use precise labels:
- Not started
- In progress
- Passed in local
- Passed in staging
- Production approved
- Deployed
- Post-deployment verified
- Failed / rolled back

A successful local build is not proof of production readiness.
