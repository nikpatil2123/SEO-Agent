---
name: scoring-engine
description: Calculate transparent, evidence-based SEO, GEO and AEO readiness scores out of 10 using fixed weighted rubrics and comparable before/after assessments.
---

# Scoring Engine

## General rules

- Score SEO, GEO and AEO independently from 0.0 to 10.0.
- Use the same rubric, URLs, queries, locale, device, evidence sources and observation method for baseline and post-implementation scoring wherever possible.
- Each criterion is scored 0–5, then normalized by its weight.
- A criterion with no evidence is **Not assessed**, not automatically zero. Re-normalize only if the report clearly discloses coverage; also show evidence coverage.
- A missing capability may be scored zero only when it was actually checked and found absent.
- Show criterion-level evidence, confidence and limitations.
- Do not equate readiness score with Google ranking, organic traffic, AI citations or conversions.
- Never manipulate weights after seeing results.

## Formula

For assessed criteria:
`Score / 10 = 10 × sum(weight_i × criterion_score_i / 5) / sum(assessed_weight_i)`

Weights sum to 100 within each discipline. Report assessed-weight coverage separately.

## SEO rubric (weights)

| Criterion | Weight |
|---|---:|
| Crawlability and indexation controls | 15 |
| Technical foundations: status, redirects, canonicals, sitemap, robots | 15 |
| On-page metadata and semantic structure | 10 |
| Search intent and content usefulness/coverage | 15 |
| Internal linking and information architecture | 10 |
| Mobile experience and Core Web Vitals evidence | 10 |
| Structured data accuracy/eligibility | 5 |
| Authority/trust evidence and link profile observations | 10 |
| Measurement readiness (Search Console/analytics/conversions) | 10 |

## GEO rubric (weights)

| Criterion | Weight |
|---|---:|
| Business/entity clarity and consistency | 15 |
| Factual completeness and product/service specificity | 15 |
| Original expertise, evidence and source transparency | 15 |
| Topical coverage and useful entity relationships | 10 |
| Citation-ready claims and references | 15 |
| Technical accessibility and stable canonical content | 10 |
| Third-party corroboration/brand presence (evidence-based) | 10 |
| Measured AI answer mentions/citations across documented tests | 10 |

If AI platform testing is unavailable, mark it Not assessed and disclose the reduced coverage. Do not infer citations from content quality.

## AEO rubric (weights)

| Criterion | Weight |
|---|---:|
| Real question/query research | 15 |
| Directness and accuracy of answers | 20 |
| Answer structure and extractability | 15 |
| Coverage of relevant questions and intent | 15 |
| Supporting evidence, freshness and attribution | 10 |
| Semantic structure and appropriate schema | 10 |
| Readability and accessible rendering | 5 |
| Measured answer/featured-snippet visibility | 10 |

If live answer-result testing is unavailable, mark it Not assessed.

## Criterion scale

- 0: Checked and absent/broken.
- 1: Severe deficiencies; little usable implementation.
- 2: Partial implementation with material gaps.
- 3: Adequate baseline; notable improvements remain.
- 4: Strong implementation with minor gaps.
- 5: Fully implemented for the assessed scope, validated and supported by evidence.

## Before/after reporting

Show:
- Baseline score
- Post-implementation score
- Point change (after minus before)
- Assessed weight coverage
- Criterion-level score changes
- Evidence references
- Unchanged/unassessed criteria
- Scope differences that prevent direct comparison

Do not label a score "Google score" or "AI score". Use "assessed SEO readiness", "assessed GEO readiness", and "assessed AEO readiness".
