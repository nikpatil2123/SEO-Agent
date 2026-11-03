---
name: implementation
description: Implement only approved SEO, GEO and AEO changes in an existing website repository while preserving UI, UX, styling, layout, components and functionality.
---

# Approved Website Implementation

## Preconditions

Do not run this skill until:
- A versioned implementation plan has explicit approval.
- Each visible content change has separate page-specific approval.
- Each UI/design change has separate explicit approval.
- Repository and deployment access are authorized.
- A clean baseline and rollback path exist.

## Default protected scope

Treat the following as protected unless explicitly approved:
- CSS, SCSS, stylesheets, design tokens and Tailwind classes.
- Layouts, templates, components and visual primitives.
- Navigation, headers, footers, menus, forms and buttons.
- Responsive breakpoints, spacing, typography, colors and animations.
- Existing visible text/content.
- Application logic, API behavior, authentication, payments and conversion flows.
- Analytics, consent management, privacy and security configuration.

## Potentially allowed changes

Only if listed in the approved plan:
- Metadata in framework-native metadata files.
- Canonical/robots metadata.
- Sitemap and robots configuration.
- JSON-LD that matches verified visible content.
- Non-visual semantic/accessibility corrections that do not alter behavior or appearance.
- Alt text changes after checking whether the image is informative or decorative.
- Approved visible copy changes.
- Approved UI changes (only exact scope).

## Procedure

1. Inspect repository and identify framework/CMS.
2. Record current branch, commit, working tree and affected routes.
3. Create a dedicated branch.
4. Create backup/restore point appropriate to the system.
5. Map each approved plan item to files and URLs.
6. Implement the smallest possible diff.
7. Avoid unrelated refactoring, dependency upgrades or formatting churn.
8. For every changed file, record reason, approval ID and affected URL.
9. Run relevant tests after each coherent change.
10. Review the diff against protected-file rules.
11. Stop if implementation requires an unapproved protected change.

## Do not

- Push directly to the default branch.
- Deploy to production.
- change DNS, hosting, secrets, database data or environment configuration unless explicitly authorized in a separate change request.
- install paid tools or incur costs without permission.
- bypass a failed test to report success.
- change visible content based on plan-level approval alone.

## Output

Provide a change log with file paths, URL mapping, approval reference, tests and any deferred items.
