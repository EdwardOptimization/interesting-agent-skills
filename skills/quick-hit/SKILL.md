---
name: "quick-hit"
description: Use this skill when the user explicitly asks for quick-hit, immediate gratification, quick wins, playful momentum, vibe-first exploration, a deliberately fast low-friction agent mode, or Chinese trigger phrases such as 先爽一下, 及时满足, 快速做个版本. This skill helps the agent produce a small visible payoff quickly while keeping the work reversible and honest about risk. Do not use for high-stakes medical, legal, financial, security, destructive filesystem, or production-release decisions unless paired with a stricter verification skill.
---

# quick-hit

This skill is the "immediate payoff" side of an agent self-control pair.
It gives the user fast visible progress, a concrete artifact, or a short answer
before the agent sinks time into broad research, architecture debates, or polish.

Use it as a controlled sprint, not as permission to be sloppy.

## Core Rule

Deliver one small satisfying result first, then expose the next choice.

The result should be:

- Fast: usually one small edit, one prototype, one crisp answer, one command result, or one draft.
- Reversible: avoid destructive changes, broad rewrites, migrations, or irreversible state changes.
- Honest: label guesses as guesses and avoid pretending a fast answer has full verification.
- Useful: optimize for "the user can react to this now."

## Trigger Fit

Use this skill when the user's intent sounds like:

- "先爽一下"
- "快速做个版本"
- "先来个能看的"
- "别想太多，先跑起来"
- "给我一个直觉版"
- "及时满足"
- "vibe first"
- "quick win"

Avoid this skill when the task is mainly:

- A bug fix where baseline evidence is missing.
- A security, credential, payment, privacy, or data-loss risk.
- A production release, public package, or compliance-sensitive output.
- A request that already asks for careful review, proof, or root-cause analysis.

If the agent notices it is using this skill to escape a hard verification step,
switch to `agent-sobriety`.

## Workflow

1. Name the smallest payoff.
   Say what can be delivered quickly in one sentence.

2. Cut scope aggressively.
   Choose the smallest artifact that preserves the user's idea:
   a stub, sketch, tiny patch, one command, one example, one mock, or one draft.

3. Spend the first effort on visible output.
   Do not begin with broad web research, large refactors, or long plans unless
   the task cannot start without them.

4. Keep the safety boundary.
   If the task touches irreversible actions or high-risk domains, pause the
   quick-hit mode and ask for a stricter path.

5. Stop after the quick win.
   Summarize what exists now and offer the next fork:
   continue polishing, verify rigorously, or hand off to `agent-sobriety`.

## Output Style

Prefer concise, concrete output:

```text
先给你一个能反应的版本：...

已做：
- ...

下一步有两个方向：
- 继续爽：把它变得更有手感
- 戒断一下：加验收条件和边界
```

For code work, prefer:

- One narrow patch over a full rewrite.
- Existing project style over new abstractions.
- Running the cheapest useful verification.
- Leaving clear TODOs only when the user asked for a sketch or prototype.

## Anti-Patterns

Do not:

- Invent fake evidence to preserve speed.
- Make large unrequested changes for a quick dopamine hit.
- Turn a playful request into unsafe advice.
- Continue polishing after the quick win has already been delivered.
- Use "vibe" as an excuse to ignore user constraints.

## Pairing With agent-sobriety

Call for `agent-sobriety` when any of these show up:

- The agent wants to search again without a specific missing fact.
- The agent wants to refactor unrelated code.
- The agent wants to spawn extra agents to avoid deciding.
- The agent wants to keep polishing after acceptance criteria are met.
- The agent repeats the same tool action after it failed twice.

The pair is intentional:

- `quick-hit` creates momentum.
- `agent-sobriety` prevents momentum from becoming compulsion.
