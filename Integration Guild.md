# 🔌 Integration Guide

Proof‑of‑Contribution Protocol Core
Version: 0.1.0  
Status: Draft (Alpha)

---

## 🎯 Purpose

This guide explains how to integrate with the Proof‑of‑Contribution Protocol Core, including:

- How to submit contribution events  
- How to run validation  
- How to compute deterministic scores  
- How to generate and verify contribution proofs  
- How to extend the protocol with custom validators or scoring rules  

This document is intended for developers building apps, bots, services, or Solana programs that rely on contribution verification.

---

1. Integration Overview

Integrating with the protocol involves four steps:

1. Create a Contribution Event  
2. Submit it to the Validation Pipeline  
3. Compute a Deterministic Score  
4. Generate or Verify a Contribution Proof

The protocol is designed to be:

- Stateless  
- Deterministic  
- Easy to embed in any environment  
- Extendable through modular validators  

---

2. Creating a Contribution Event

A contribution event is a structured JSON object.

Example Event

`json
{
  "id": "evt_12345",
  "timestamp": 1738000000,
  "actor": "Fh29...abc",
  "type": "code_commit",
  "payload": {
    "repo": "GitDigital/Proof-of-Contribution-Protocol-Core",
    "commit_hash": "abc123"
  },
  "metadata": {
    "source": "github_webhook"
  }
}
`

Required fields

| Field       | Description |
|-------------|-------------|
| id        | Unique event identifier |
| timestamp | Unix timestamp |
| actor     | Public key or identifier |
| type      | Contribution type |
| payload   | Type‑specific data |
| metadata  | Optional contextual data |

---

3. Submitting an Event to the Validation Pipeline

The validation pipeline ensures the event is:

- Well‑formed  
- Authentic  
- Non‑replayed  
- Type‑valid  
- Payload‑valid  

Validation Call (Pseudocode)

`ts
const result = validateEvent(event);
`

Validation Output

`json
{
  "eventid": "evt12345",
  "valid": true,
  "errors": [],
  "validator": "core",
  "version": "0.1.0"
}
`

If valid = false, the event must not proceed to scoring.

---

4. Computing a Deterministic Score

Once validated, the event is passed to the scoring engine.

Scoring Call (Pseudocode)

`ts
const score = scoreEvent(event);
`

Example Output

`json
{
  "eventid": "evt12345",
  "score": 5,
  "rulesapplied": ["codecommit_base"],
  "version": "0.1.0"
}
`

Scoring rules are defined in /spec/scoring-rules.md (to be added).

---

5. Generating a Contribution Proof

A contribution proof is the final output of the protocol.

Proof Call (Pseudocode)

`ts
const proof = generateProof(event, validation, score);
`

Example Proof

`json
{
  "eventid": "evt12345",
  "score": 5,
  "validated": true,
  "signature": null,
  "version": "0.1.0"
}
`

Optional: Signing Proofs

Integrators may sign proofs using:

- Wallet keys  
- Service keys  
- Program‑derived addresses (PDAs)  

This enables:

- Governance  
- Rewards  
- Cross‑platform verification  

---

6. Verifying a Contribution Proof

Verification ensures:

- The proof is well‑formed  
- The score is correct  
- The validation state is correct  
- The signature (if present) is valid  

Verification Call (Pseudocode)

`ts
const verified = verifyProof(proof);
`

---

7. Extending the Protocol

The protocol is modular. Integrators can add:

Custom Validators

Examples:

- GitHub‑specific validators  
- Discord activity validators  
- Governance participation validators  

Custom Scoring Rules

Examples:

- Weighted scoring  
- Domain‑specific scoring  
- Time‑decay scoring  

Custom Proof Formats

Examples:

- Signed Solana transactions  
- On‑chain attestations  
- Zero‑knowledge proofs (future extension)  

---

8. Integration Patterns

Pattern A: Off‑Chain Integration

Best for:

- Bots  
- Web services  
- Automation pipelines  

Flow:

1. Receive event  
2. Validate  
3. Score  
4. Generate proof  
5. Store or forward proof  

---

Pattern B: Hybrid On‑Chain Integration

Best for:

- Solana programs  
- On‑chain governance  
- Reward distribution  

Flow:

1. Validate off‑chain  
2. Score off‑chain  
3. Submit proof on‑chain  
4. Program verifies proof  

---

Pattern C: Fully On‑Chain (Future)

Planned for:

- ZK‑based proofs  
- Stateless validation  
- On‑chain scoring  

---

9. Error Handling

Integrators must handle:

- Invalid events  
- Missing fields  
- Unsupported types  
- Validation failures  
- Scoring rule mismatches  
- Version mismatches  

Errors must be deterministic and reproducible.

---

10. Best Practices

- Use unique event IDs  
- Validate timestamps  
- Avoid storing PII  
- Keep payloads minimal  
- Version your validators  
- Version your scoring rules  
- Log validation and scoring results  
- Use signatures for high‑trust systems  

---

11. Example Implementations

Reference implementations will be provided in:

- /examples/javascript  
- /examples/rust  
- /examples/python  

---

12. Status

This integration guide is in Alpha and will evolve as the protocol matures.
