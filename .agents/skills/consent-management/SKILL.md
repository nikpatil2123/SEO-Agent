---
name: consent-management
description: Enforce explicit, scoped, versioned end-user consent for optimization plans, visible content edits, UI/design changes and production deployment.
---

# Consent Management

## Separate consent categories

1. **Plan approval:** authorizes only the explicitly listed implementation items in a specific plan version.
2. **Visible content approval:** authorizes exact proposed text/content for named URLs and sections.
3. **UI/design approval:** authorizes exact visual/layout/component/style changes for named pages and elements.
4. **Production deployment approval:** authorizes deployment of a specified tested release to production.

These approvals are independent. One does not imply another.

## Consent record

Record:
- Customer/project identifier (avoid unnecessary personal data)
- Plan version and hash/identifier
- Requested action and scope
- Exact URLs/files/components
- Proposed before/after content or design description
- Risks and expected effects
- Approver identity/role as available
- Decision: approved/rejected/changes requested
- Timestamp and channel
- Expiry or conditions, if specified

## Rules

- Silence is not consent.
- General statements such as "make it SEO-ready" are not consent for visible text or UI changes.
- Consent must be informed and specific.
- Approval of one page does not authorize the same change on every page.
- If proposed text changes after approval, request approval again.
- If the implementation materially differs from the approved plan, pause and re-approve.
- Rejected items must remain unchanged.
- Production deployment requires separate approval after staging validation.
- If the agent cannot reliably record the consent, it must not proceed.

## Required prompts

### Plan approval
"Do you approve implementation of plan [ID/version]? This approval covers only the listed changes. Visible content edits, UI/design changes and production deployment require separate approval."

### Visible content approval
"Do you approve replacing the current text on [URL/section] with the exact proposed text shown here? The layout and styling will remain unchanged."

### UI approval
"Do you approve this specific UI change on [URL/component]? Review the exact before/after description or preview. No other UI changes are authorized."

### Production approval
"Staging checks have completed. Do you approve deploying release [commit/release ID] to production?"

## If no consent

Continue read-only research, report the opportunity as pending approval, and do not modify the protected target.
