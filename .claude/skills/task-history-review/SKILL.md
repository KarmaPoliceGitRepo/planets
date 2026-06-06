---
name: task-history-review
description: Review and summarize the recent work/tasks done in this repository — by inspecting git commits, reflog, branches, recently modified files, and GitHub PRs/issues. Use when the user asks "what have I worked on", "list the tasks from the last N hours/days", "what changed recently", "summarize recent activity", or wants a recap of recent task history for this repo.
---

# Task History Review

Produce an honest, evidence-based recap of recent work in this repository. There is **no persistent chat transcript** across Claude Code sessions — each session is fresh — so this skill reconstructs activity from durable artifacts (git + GitHub), and is clear about that limitation.

## What to gather

Run these (adjust the time window to the user's request — default to what they ask, e.g. "2 hours", "today", "this week"):

1. **Current time** for an accurate window: `date`
2. **Commits in the window** (all branches):
   `git log --all --since="<window>" --pretty=format:"%h | %ci | %an | %s"`
3. **Recent commits regardless of window** (fallback context, last ~20):
   `git log --all --pretty=format:"%h | %ci | %an | %s" -20`
4. **Branches**: `git branch -a`
5. **Reflog** (captures checkouts/resets/rebases not visible in log):
   `git reflog -30`
6. **Recently modified files** (work-in-progress not yet committed):
   `find . -type f -not -path './.git/*' -mmin -<minutes>` — substitute a real number of minutes for `<minutes>` (e.g. `-mmin -120` for the last 2 hours).
7. **Uncommitted changes**: `git status --short` and `git diff --stat`
8. **GitHub activity** via the GitHub MCP tools (load with ToolSearch if needed):
   - `mcp__github__list_pull_requests` (state: all, sort: updated)
   - `mcp__github__list_issues` (orderBy: UPDATED_AT)
   - `mcp__github__list_commits` (filter by `since` and/or `author`)

   Scope these to the repository in the session's allowed list. If the user
   wants a specific author, pass their username/email.

## How to report

- Lead with the **headline**: how many tasks/changes fall in the requested window, or plainly state "no activity in the last N hours" if so.
- Group findings by source (commits, PRs, issues, WIP files) and within each, list newest-first with timestamps so the user can map them to a timeline.
- For each commit/PR/issue, give the short SHA/number, time, and a one-line description of what it did.
- **Be honest about gaps.** If there's no record, say so directly and explain why (fresh container, no cross-session memory). Do not fabricate a task list. Point the user to their Claude Code app/web session list for the actual prompt history, since that is the only place raw request history lives.
- Offer to dig deeper (full diff of a specific commit, contents of a PR, etc.) rather than dumping everything.

## Caveats

- This reflects *artifacts*, not *requests*: a task the user asked about but that produced no commit/PR/file change won't show up here.
- In an ephemeral remote container, only pushed/committed work and remote GitHub state survive; local-only uncommitted work from a prior session is gone.
