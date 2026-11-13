# Interesting Agent Skills

An incubator for unusual, useful, and behavior-shaping agent skills.

This repository collects small skill packages that change how an agent works:
how it starts, stops, verifies, explores, resists loops, or turns a fuzzy idea
into a usable artifact. It is intentionally broader than project-specific skill
packs and is meant for skills that are worth testing before they are published
or promoted elsewhere.

See [docs/readme-intros.md](docs/readme-intros.md) for alternate README intro
styles.

## Current Skills

| Skill | Purpose | Status |
| --- | --- | --- |
| `quick-hit` | Immediate-gratification mode for fast, reversible, honest quick wins. | draft |
| `agent-sobriety` | Agent impulse-control mode for delaying over-searching, over-refactoring, over-polishing, and repeated tool loops. | draft |
| [`linux-system-migration`](skills/linux-system-migration/SKILL.md) | Linux-to-Linux host migration with inventory reconciliation, workflow acceptance, cutover, and source retirement gates. | draft |

## Repository Layout

```text
interesting-agent-skills/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── docs/
│   └── readme-intros.md
├── skills/
│   ├── quick-hit/
│   │   ├── SKILL.md
│   │   └── evals/evals.json
│   ├── agent-sobriety/
│   │   ├── SKILL.md
│   │   └── evals/evals.json
│   └── linux-system-migration/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/reconciliation.md
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

Install a selected skill with the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add EdwardOptimization/interesting-agent-skills --skill linux-system-migration
```

For reproducible installs, use a reviewed full commit instead of a moving branch:

```bash
npx skills add EdwardOptimization/interesting-agent-skills@FULL_COMMIT_SHA --skill linux-system-migration
```

Replace `FULL_COMMIT_SHA` with an existing full commit hash from this repository.
Each skill is a normal directory; selecting one does not require installing the
others. Draft skills have passed structural checks but are not yet established
as reliable by behavioral evaluation. Files under `evals/` are evaluation prompts,
not records of completed evaluations.

Copy the desired skill into your agent runtime's local skills directory.
For runtimes that use `~/.agents/skills`, run:

```bash
cp -R skills/quick-hit ~/.agents/skills/
cp -R skills/agent-sobriety ~/.agents/skills/
cp -R skills/linux-system-migration ~/.agents/skills/
```

For Codex, Claude Code, Copilot, or other `SKILL.md`-compatible runtimes, copy
the skill directory into that runtime's configured skills directory. Restart or
reload the agent session if the runtime does not hot-load new skills.

## License

MIT. See [LICENSE](LICENSE).
