---
name: prompt-master
description: Prompt engineering helper — craft, critique, refine, and iterate on prompts for LLMs (Claude and others). Use when the user asks to write a prompt, improve an existing prompt, evaluate why a prompt underperforms, generate few-shot examples, design a system prompt, or compare prompt strategies. Invoked via /prompt-master.
---

# prompt-master — prompt engineering helper

`prompt-master` helps you write prompts that reliably get the output you want from an LLM. It covers system prompts, user-turn prompts, few-shot examples, chain-of-thought setups, and iterative refinement.

## Workflow

When invoked, follow this sequence:

### 1. Understand the goal

Ask (or infer from context):
- **Task** — What should the model produce? (classify, summarize, generate code, answer questions, …)
- **Model** — Which LLM? Defaults to Claude if unspecified.
- **Input format** — What does the user/system pass in at runtime?
- **Output format** — Exact format expected (JSON, markdown, plain prose, …)
- **Failure mode** — What does a bad output look like? What has already been tried?

If the user pastes an existing prompt, go straight to critique mode (step 3).

### 2. Draft the prompt

Apply these principles in order:

**Clarity first**
- State the task in the opening sentence. Don't bury it.
- One task per prompt; if there are sub-tasks, sequence them explicitly.
- Use imperative voice: "Summarize the article in three bullet points."

**Persona and role (for system prompts)**
- Define the model's role when it changes output quality.
- Example: `You are an expert podcast editor who specialises in pacing and narrative flow.`
- Keep the persona to one sentence; don't over-specify irrelevant traits.

**Context injection**
- Put variable runtime content in clearly delimited blocks using XML-like tags:

```
You are a helpful assistant.

Transcript:
[TRANSCRIPT]
{{TRANSCRIPT}}
[/TRANSCRIPT]

Task: Identify the three most engaging moments in the transcript above.
```

- Label each distinct input part so the model can reference it unambiguously.

**Output specification**
- Describe the expected format explicitly.
- For JSON: supply a schema or a single short example object.
- Specify length: "Answer in 2–3 sentences", "Return a list of up to 10 items."
- When you need only structured output: end with `Respond ONLY with valid JSON. No prose before or after.`

**Reasoning (chain-of-thought)**
- For complex tasks prepend: "Think step by step before giving your final answer."
- For Claude: prefix the assistant turn with `Let me think through this:` to prime CoT.
- Avoid CoT for simple classification tasks — it wastes tokens and can confuse the output format.

**Constraints and guardrails**
- List what the model must NOT do: "Do not add information not present in the source text."
- For length limits: "Stay under 150 words." / "Respond in exactly 5 bullet points."

### 3. Critique an existing prompt

When the user shares a prompt that isn't working, evaluate it against these failure modes:

| Failure mode | Symptom | Fix |
|---|---|---|
| Ambiguous task | Model hedges or asks clarifying questions | Restate the task with a concrete verb and expected output |
| Overloaded prompt | Output mixes tasks or skips steps | Split into separate prompts or number the steps |
| Missing output spec | Inconsistent format across runs | Add an explicit format description or example |
| No context delimiters | Model confuses instructions with content | Wrap variable content in labelled tags |
| Prompt too long | Model ignores later instructions | Move the most critical instruction to the top AND bottom |
| Over-specified persona | Refusals or off-tone responses | Simplify persona to the core expertise needed |

### 4. Generate few-shot examples

When the task has a non-obvious output style, provide 2–3 input/output pairs before the real input:

```
Task: Rewrite the sentence to be warmer and more conversational.

Example 1
Input: The meeting has been rescheduled to Thursday.
Output: Hey — just a heads up, we moved the meeting to Thursday!

Example 2
Input: Please submit your report by end of day.
Output: Could you get the report in by end of day? That'd be great.

Now rewrite this:
Input: Your subscription will expire in 7 days.
Output:
```

Rules for good few-shot examples:
- Cover edge cases, not just the easy case.
- Keep examples as short as possible while still showing the pattern.
- Use the same delimiters in examples as in the real prompt.

### 5. Iterate

After drafting, suggest one concrete test the user should run:
- Give one sample input and predict the expected output.
- Flag one part of the prompt most likely to cause variance.
- Propose the single highest-leverage edit if a first run fails.

## Quick templates

### System prompt skeleton (Claude)
```
You are [ROLE] who [CORE EXPERTISE].

When given [INPUT TYPE], you will [TASK] and return [OUTPUT FORMAT].

Rules:
- [CONSTRAINT 1]
- [CONSTRAINT 2]
```

### Classification prompt
```
Classify the following text into exactly one of these categories: [CAT_A | CAT_B | CAT_C].

Text:
"""
{{TEXT}}
"""

Reply with only the category name. Nothing else.
```

### Summarisation prompt
```
Summarise the following [DOCUMENT TYPE] in [N] bullet points.
Each bullet must be one sentence and start with a strong verb.

[DOCUMENT TYPE]:
"""
{{CONTENT}}
"""
```

### JSON extraction prompt
```
Extract the requested fields from the text below and return them as JSON.

Schema:
{
  "field_one": "string",
  "field_two": "number | null"
}

Text:
"""
{{TEXT}}
"""

Return ONLY valid JSON matching the schema above. No markdown fences. No explanation.
```

## Claude-specific tips

- **Prefill the assistant turn** to lock in format: end the human turn, then open the assistant turn with `{` or a markdown fence to force the model to start there.
- **Use XML tags** (not markdown headers) for multi-part inputs — Claude is trained to parse them reliably.
- **Avoid sycophancy bait**: don't say "This is the most important task" or "You must get this perfect" — it increases hallucination.
- **Temperature**: set to 0 for deterministic extraction/classification; 0.5–1.0 for creative or varied outputs.
- See the `claude-api` skill for up-to-date model IDs, context limits, and pricing before recommending a specific model.

## After producing a prompt

1. Show the finished prompt in a fenced code block so the user can copy it directly.
2. Note any runtime variables (e.g. `{{TRANSCRIPT}}`) so the user knows what to substitute.
3. Suggest the next iteration: what to change if the output is too long / too short / wrong format.
