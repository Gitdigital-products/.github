# 📚 API Reference

Proof‑of‑Contribution Protocol Core
Version: 0.1.0  
Status: Draft (Alpha)

---

## 🎯 Purpose

This API Reference defines the public interfaces, data structures, and deterministic behaviors of the Proof‑of‑Contribution Protocol Core.  
### It is designed for developers integrating the protocol into:

- Applications  
- Bots  
- Automation pipelines  
- Solana programs  
- Governance systems  
- Reward engines  

#### This reference covers:

- Event schema  
- Validation API  
- Scoring API  
- Proof generation API  
- Proof verification API  
- Error formats  
- Versioning rules  

---

1. Contribution Event Schema

A Contribution Event is the core input to the protocol.

##### Schema

`json
{
  "id": "string",
  "timestamp": "unix_timestamp",
  "actor": "publickeyor_identifier",
  "type": "string",
  "payload": {},
  "metadata": {}
}
`

##### Field Definitions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | Unique event identifier |
| timestamp | number | Yes | Unix timestamp |
| actor | string | Yes | Public key or identifier |
| type | string | Yes | Contribution type |
| payload | object | Yes | Type‑specific data |
| metadata | object | No | Optional contextual data |

---

2. Validation API

The Validation API ensures that events are:

- Well‑formed  
- Authentic  
- Non‑replayed  
- Type‑valid  
- Payload‑valid  

Function: validateEvent(event)

Input

A valid Contribution Event.

Output

`json
{
  "event_id": "string",
  "valid": true,
  "errors": [],
  "validator": "core",
  "version": "0.1.0"
}
`

#### Error Output

`json
{
  "event_id": "string",
  "valid": false,
  "errors": ["missing_field: payload.repo"],
  "validator": "core",
  "version": "0.1.0"
}
`

---

3. Scoring API

The Scoring API applies deterministic scoring rules.

Function: scoreEvent(event)

Input

A validated Contribution Event.

Output

`json
{
  "event_id": "string",
  "score": 0,
  "rulesapplied": ["rulename"],
  "version": "0.1.0"
}
`

#### Scoring Rules

Defined in:

`
/spec/scoring-rules.md
`

Rules must be:

- Deterministic  
- Pure functions  
- Versioned  

---

4. Contribution Proof API

The Proof API assembles the final proof object.

Function: generateProof(event, validation, score)

Output

`json
{
  "event_id": "string",
  "score": 0,
  "validated": true,
  "signature": null,
  "version": "0.1.0"
}
`

Optional: Signed Proofs

Integrators may sign proofs using:

- Wallet keys  
- Service keys  
- PDAs  

Signature format is integrator‑defined.

---

5. Proof Verification API

Function: verifyProof(proof)

Output

`json
{
  "valid": true,
  "errors": [],
  "version": "0.1.0"
}
`

#### Error Output

`json
{
  "valid": false,
  "errors": ["invalid_signature"],
  "version": "0.1.0"
}
`

---

6. Error Format

All errors follow a consistent structure.

Error Object

`json
{
  "code": "string",
  "message": "string",
  "field": "optional"
}
`

##### Common Error Codes

| Code | Meaning |
|------|---------|
| missing_field | Required field missing |
| invalid_type | Unsupported contribution type |
| invalid_payload | Payload failed validation |
| timestamp_invalid | Timestamp outside allowed range |
| replay_detected | Event already processed |
| scoring_error | Scoring rule failure |
| signature_invalid | Invalid signature |
| version_mismatch | Protocol version mismatch |

---

7. Versioning Rules

The API follows semantic versioning:

- MAJOR — breaking changes  
- MINOR — new features  
- PATCH — fixes  

All API responses include a version field.

---

8. Determinism Requirements

All API functions must:

- Produce identical output for identical input  
- Avoid randomness  
- Avoid external API calls  
- Avoid floating‑point drift  
- Avoid environment‑dependent behavior  

---

9. Example End‑to‑End Flow

10. Validate

`ts
const validation = validateEvent(event);
`

2. Score

`ts
const score = scoreEvent(event);
`

3. Generate Proof

`ts
const proof = generateProof(event, validation, score);
`

4. Verify Proof

`ts
const verified = verifyProof(proof);
`

---

10. Status

This API Reference is in Alpha and will evolve as the protocol matures.
