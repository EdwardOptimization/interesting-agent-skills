# Contributing

This is a personal incubation repo. Keep additions small, reviewable, and safe.

## Add A Skill

1. Create `skills/<skill-name>/SKILL.md`.
2. Add a concise frontmatter `name` and `description`.
3. Add `evals/evals.json` when the skill has testable behavior.
4. Run `python3 scripts/validate_skills.py`.
5. Update `README.md` with the skill and status.

## Acceptance Criteria

A skill should be kept here only if it satisfies at least one of:

- It captures a recurring agent behavior pattern.
- It improves safety, verification, taste, or delivery quality.
- It is a useful experiment that can be evaluated with prompts.
- It is entertaining but still operationally bounded.

Do not add skills that hide risky behavior behind cute names, encourage
credential leakage, bypass user consent, or publish private project material.
