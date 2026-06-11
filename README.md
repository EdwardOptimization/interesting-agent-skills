# Interesting Agent Skills

Personal incubator for unusual, useful, or experimental agent skills.

This repository is intentionally broader than project-specific skill packs. Use
it for skills that are worth keeping, testing, and possibly publishing later,
but that do not belong to a single product or research repo.

## Current Skills

| Skill | Purpose | Status |
| --- | --- | --- |
| `爽.skill` | Immediate-gratification mode for fast, reversible, honest quick wins. | draft |
| `戒断.skill` | Agent impulse-control mode for delaying over-searching, over-refactoring, over-polishing, and repeated tool loops. | draft |

## Repository Layout

```text
interesting-agent-skills/
├── README.md
├── CONTRIBUTING.md
├── skills/
│   ├── 爽.skill/
│   │   ├── SKILL.md
│   │   └── evals/evals.json
│   └── 戒断.skill/
│       ├── SKILL.md
│       └── evals/evals.json
└── scripts/
    └── validate_skills.py
```

## Skill Standard

Each skill directory should contain:

- `SKILL.md` with YAML frontmatter including `name` and `description`.
- A focused trigger description that is neither too broad nor too passive.
- Operational instructions short enough for an agent to follow under pressure.
- Optional `evals/evals.json` with realistic prompts and expected behavior.

Prefer skills that change agent behavior in a repeatable way. Avoid storing raw
private logs, credentials, proprietary data, or one-off chat transcripts here.

## Validate

```bash
python3 scripts/validate_skills.py
```

## Install Locally

Copy the desired skill into an agent's local skills directory:

```bash
cp -R skills/爽.skill ~/.agents/skills/
cp -R skills/戒断.skill ~/.agents/skills/
```

Restart or reload the agent session if the runtime does not hot-load new skills.
