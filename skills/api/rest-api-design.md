# REST API Design
## Problem Framing
Codex must transform product requirements into a coherent REST API specification that balances usability, security, and maintainability.

## Steps
1. Clarify functional scope, data domains, and non-functional requirements with stakeholders or documentation.
2. Model resources, relationships, and versioning strategy; draft route table with CRUD operations where applicable.
3. Define request/response schemas with validation rules, error formats, and pagination strategy.
4. Review authentication, authorization, and rate limiting implications; prepare follow-up questions for unknowns.
5. Summarize the API proposal and provide next steps for implementation or feedback.

## Inputs and Outputs
- Inputs: product requirements, data model references, compliance constraints.
- Outputs: structured API design doc including endpoints, schemas, auth strategy, and open questions.

## Acceptance Checklist
- [ ] Proposed routes cover all documented user journeys and edge cases.
- [ ] Schemas align with data constraints and include validation details.
- [ ] Security considerations note auth, rate limits, and sensitive fields.
- [ ] Summary lists follow-up actions and testing strategy.

## Safety Notes
- Protect PII and secrets when drafting example payloads.
- Label any speculative endpoints to prevent accidental deployment without review.
