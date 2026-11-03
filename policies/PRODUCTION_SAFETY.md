# Production Safety Policy

1. Use least-privilege access. Do not request passwords in chat.
2. Never commit secrets, tokens, API keys, customer data or private reports.
3. Confirm authorization to access and crawl the target website.
4. Respect robots directives, rate limits, access controls and terms.
5. Do not run destructive commands or modify databases, DNS, hosting or infrastructure without separate authorization.
6. Create a clean Git branch and recoverable backup before changes.
7. Avoid unrelated refactoring and dependency upgrades.
8. Run local checks and staging tests before production.
9. Require separate production deployment approval.
10. Maintain a rollback plan and verify production after release.
11. Do not claim success until the relevant check has actually passed.
12. Keep customer data and reports private; do not publish them in a public repository.
