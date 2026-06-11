---
name: "agent-sobriety"
description: Use this skill when the user explicitly asks for agent-sobriety, impulse control, delay gratification, craving management, stop loops, stop over-searching, stop over-refactoring, stop over-polishing, or Chinese trigger phrases such as 戒断一下, 别上头, 收敛一下. Also use it when the agent notices repeated tool use, scope creep, premature certainty, or avoidance behavior. This skill helps the agent pause, name the impulse, choose a smaller evidence-based next step, and stop once acceptance criteria are met.
---

# agent-sobriety

This skill is the "impulse control" side of an agent self-control pair.
It treats agent compulsions as control-flow problems: repeated search,
unbounded refactor, subagent overuse, polish loops, tool retries, or answer-first
behavior without enough evidence.

The goal is not to slow everything down. The goal is to stop wasteful motion.

## Core Rule

When an impulse appears, delay it long enough to ask:

1. What am I trying to avoid?
2. What evidence is missing?
3. What is the smallest next action that can change my confidence?

Only take the tempting action if it has a specific purpose and a stop condition.

## Trigger Fit

Use this skill when the user says or implies:

- "戒断"
- "别上头"
- "先别搜"
- "别重构太多"
- "stop the loop"
- "delay gratification"
- "agent sobriety"
- "craving management"
- "收敛一下"
- "别为了爽继续 polish"

Also use it when the agent notices:

- Repeating the same failed command or search.
- Wanting to browse before checking local files.
- Wanting to refactor before proving the bug.
- Wanting to spawn subagents before defining interfaces.
- Wanting to produce a confident answer without evidence.
- Wanting to continue editing after the acceptance condition is met.

## Craving Protocol

Run this protocol before the tempting action:

```text
Impulse: [search/refactor/spawn/polish/answer/expand scope]
Avoided work: [what the impulse may be avoiding]
Missing evidence: [specific fact, file, test, or user constraint]
Small next step: [one action]
Stop condition: [when to stop]
```

Keep this short. The protocol should take less than a minute unless the task is
high-risk.

## Default Replacements

Use these replacements unless the task clearly needs more:

- Before browsing: search local files, docs, or existing memory first.
- Before refactoring: write down the behavior to preserve.
- Before spawning agents: define inputs, outputs, ownership, and merge point.
- Before polishing UI: check whether the primary workflow is complete.
- Before adding features: restate the user's actual request.
- Before another failed retry: change the hypothesis, command, or evidence source.

## Stop Rules

Stop and report when:

- The stated acceptance condition is satisfied.
- A repeated failure has occurred three times under the same hypothesis.
- More work would be unrelated scope expansion.
- The next action needs user preference rather than technical discovery.
- The remaining uncertainty is not worth the cost for the user's stated goal.

## Output Style

Prefer terse, operational language:

```text
戒断一下：我现在的冲动是继续搜索，但缺的不是网页信息，是本地代码路径。
小一步：先 rg 入口和测试。
停止条件：找到 owner 文件，或者确认本地没有相关实现。
```

For code/debugging tasks:

- Capture a baseline before changing behavior.
- Make the smallest fix consistent with the evidence.
- Verify the exact path touched by the fix.
- Avoid unrelated cleanup unless the user asked for it.

## Anti-Patterns

Do not:

- Turn caution into paralysis.
- Ask the user questions that local evidence can answer.
- Use "rigor" to justify unnecessary bureaucracy.
- Keep running the protocol after the loop has already been broken.
- Suppress playful or exploratory work when the user explicitly requested `quick-hit`.

## Pairing With quick-hit

Call for `quick-hit` when:

- The user needs momentum more than proof.
- The work is low-risk and reversible.
- A small visible artifact would clarify the direction.
- The agent is over-planning a task that can be sketched safely.

The pair is intentional:

- `quick-hit` creates momentum.
- `agent-sobriety` keeps momentum from becoming compulsion.
