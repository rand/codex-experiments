# Prompt Discovery
## Problem Framing
Codex benefits from gathering existing prompts, templates, and style guides to maintain continuity when generating new automations or documentation.

## Steps
1. Search the repository for `*.md`, `*.prompt`, and agent configuration files referencing instructions.
2. Extract canonical phrases, guardrails, and tone guidance into a working note.
3. Validate findings with `_INDEX` or manifest files to ensure coverage of required contexts.
4. Present a consolidated prompt pack and identify gaps or conflicting instructions.

## Inputs and Outputs
- Inputs: repository documentation, naming conventions, team style guides.
- Outputs: curated prompt snippets grouped by use case, list of missing or ambiguous guidance.

## Acceptance Checklist
- [ ] Search covers both top-level docs and nested skill directories.
- [ ] Notes cite file paths for each extracted prompt.
- [ ] Gaps include recommended follow-up tasks or owners.
- [ ] Deliverable is ready to be supplied to Codex as contextual grounding.

## Safety Notes
- Exclude sensitive or redacted passages from prompt libraries.
- Respect license restrictions when referencing external prompts or datasets.
