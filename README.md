# 🧭 Navigation

## 🏛️ Core
- [[Home]]
- [[Ecosystem Overview]]
- [[Governance Model]]
- [[Tax-First Architecture]]
- [[Contributor Authority]]

## ⚙️ Automation
- [[Workflow Engine]]
- [[KYC Validator]]
- [[API Gateway]]

## 💳 Lending
- [[Credit Authority]]
- [[Loaner Ledger]]
- [[Legal Agreements]]

## 📚 Documentation
- [[Documentation Wizard]]
- [[Templates]]
- [[Badge Catalog]]


# 🏷️ Badge Catalog

## 🏷️ Badges
![Badges](https://img.shields.io/badge/Badges-Catalog-ff9800)
![Branding](https://img.shields.io/badge/Branding-Consistent-673ab7)

---

## 📘 Summary
The Badge Catalog defines all official GitDigital badges for:
- Governance  
- Automation  
- Lending  
- Documentation  
- Security  
- Ecosystem  

---

## 🧱 Categories

### **1. Governance**
Governance, Authority, Compliance.

### **2. Automation**
Workflow Engine, KYC, API Gateway.

### **3. Lending**
Credit Authority, Loaner Ledger.

### **4. Documentation**
Docs, Templates, Wizard.

---

## 🔗 Related Pages
- [[Templates]]
- [[Documentation Wizard]]


# 🧩 Templates Library

## 🏷️ Badges
![Templates](https://img.shields.io/badge/Templates-Library-8bc34a)
![Docs](https://img.shields.io/badge/Docs-Standardized-2196f3)

---

## 📘 Summary
A complete library of reusable templates for:
- Agreements  
- Ledgers  
- READMEs  
- Workflows  
- Contributor onboarding  

---

## 🧱 Template Types

### **1. Agreements**
Founder loans, contributor contracts.

### **2. Documentation**
README, wiki, governance docs.

### **3. Automation**
Workflow forms, metadata blocks.

---

## 🔗 Related Pages
- [[Documentation Wizard]]
- [[Badge Catalog]]


# 🪄 Documentation Wizard

## 🏷️ Badges
![Docs](https://img.shields.io/badge/Docs-Wizard%20Powered-9c27b0)
![Templates](https://img.shields.io/badge/Templates-Automated-8bc34a)
![Standards](https://img.shields.io/badge/Standards-Consistent-2196f3)

---

## 📘 Summary
The Documentation Wizard automates:
- README generation  
- Agreement templates  
- Ledger entries  
- Contributor onboarding docs  

---

## 🧱 Features

### **1. Template Library**
Reusable, standardized modules.

### **2. Metadata Enforcement**
Ensures consistent structure.

### **3. Badge Integration**
Automatic badge walls.

---

## 🔗 Related Pages
- [[Templates]]
- [[Badge Catalog]]


# 📜 Legal Agreements

## 🏷️ Badges
![Agreements](https://img.shields.io/badge/Agreements-Legal%20Binding-795548)
![Identity](https://img.shields.io/badge/Identity-Verified-3f51b5)
![Compliance](https://img.shields.io/badge/Compliance-Enforced-0a7)

---

## 📘 Summary
All agreements in GitDigital are:
- Legally binding  
- Identity‑verified  
- Signature‑required  
- Immutable  

---

## 🧱 Agreement Types

### **1. Founder Loan Agreements**
Dual‑signature, KYC‑verified.

### **2. Contributor Agreements**
Role‑based, authority‑scoped.

### **3. Operational Agreements**
Workflow‑generated.

---

## 🔗 Related Pages
- [[KYC Validator]]
- [[Loaner Ledger]]



# 🧱 GitDigital Badge Wall

## 🚀 Milestones
🧱 Architecture Complete  
📘 Spec v1.0  
🛡️ Compliance Ready  
🚀 Devnet Live  
🌐 Mainnet Candidate  

## 🌀 Tiers
🌱 Concept  
🔧 Prototype  
🟦 Devnet  
🧪 Audit Prep  
🟩 Mainnet  
🌀 Ecosystem Ready  

## 🔱 Solana Signals
🔱 Solana Aligned  
🟣 Grant Candidate  
🟪 Grant Awarded  
🔗 Ecosystem Integration  
🛡️ Security Ready  

## 💼 Sponsors
💼 Sponsor Ready  
📊 DD Ready  
🏢 Enterprise Ready  
🟦 Open Source  

## 🏛️ Governance & Compliance
🏛️ Governance Published  
🔐 Security Policy  
📂 Audit Packet  
📝 Reviewer Ready  
🧬 Compliance dNFT


<!-- Security Badges -->
![Security Foundational](https://img.shields.io/badge/security-foundational-blue)

<!-- Activity Badges -->
![Last Commit](https://img.shields.io/badge/commit-current-brightgreen)

<!-- Technology Badges -->
![License](https://img.shields.io/badge/license-MIT-yellow)


<!-- Security Badges -->
![Security Foundational](https://img.shields.io/badge/security-foundational-blue)
![Security Scanning](https://img.shields.io/badge/security-scanning-inactive-red)

<!-- Activity Badges -->
![Last Commit](https://img.shields.io/badge/commit-recent-yellow)
![Release Status](https://img.shields.io/badge/releases-none-red)

<!-- Technology Badges -->
![License](https://img.shields.io/badge/license-MIT-yellow)

<!-- Quality Badges -->
![Documentation](https://img.shields.io/badge/docs-minimal-orange)

<!-- Community Badges -->
![Governance](https://img.shields.io/badge/governance-partial-orange)



**Core Badge Verification Workflow** (`.github/workflows/badge-verification.yml`):
```yaml
name: Badge Verification

on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight UTC
  push:
    paths:
      - '.github/workflows/**'
      - 'package.json'
      - 'requirements.txt'
  workflow_dispatch:

jobs:
  badge-verification:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      
      - name: Collect Repository Metrics
        run: |
          node scripts/collect-metrics.js
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Generate Badge Status
        run: |
          node scripts/compute-badges.js
      
      - name: Upload Badge Status
        uses: actions/upload-artifact@v4
        with:
          name: badge-status
          path: badge-status.json
```



<!-- Security Badges -->
![Security Foundational](https://img.shields.io/badge/security-foundational-blue)

<!-- Activity Badges -->
![Last Commit](https://img.shields.io/badge/commit-current-brightgreen)

<!-- Technology Badges -->
![License](https://img.shields.io/badge/license-MIT-yellow)




<!-- Security Badges -->
![Security Foundational](https://img.shields.io/badge/security-foundational-blue)
![Security Scanning](https://img.shields.io/badge/security-scanning-active-green)
![Dependency Status](https://img.shields.io/badge/deps-up--to--date-brightgreen)

<!-- Activity Badges -->
![Last Commit](https://img.shields.io/badge/commit-recent-yellow)
![Issues Health](https://img.shields.io/badge/issues-healthy-brightgreen)
![PR Velocity](https://img.shields.io/badge/PR-velocity-fast-brightgreen)

<!-- Maturity Badges -->
![CI Status](https://img.shields.io/badge/CI-passing-brightgreen)
![Versioning](https://img.shields.io/badge/versioning-semver-blue)
![Test Coverage](https://img.shields.io/badge/coverage-comprehensive-brightgreen)

<!-- Technology Badges -->
![Containerized](https://img.shields.io/badge/containerized-Docker-blue)
![CI Platform](https://img.shields.io/badge/CI-GitHub_Actions-blue)

<!-- Quality Badges -->
![Linting](https://img.shields.io/badge/linting-passing-brightgreen)
![Documentation](https://img.shields.io/badge/docs-complete-brightgreen)
![Code Owners](https://img.shields.io/badge/codeowners-defined-blue)

<!-- Community Badges -->
![License](https://img.shields.io/badge/license-MIT-yellow)



# Solana KYC Compliance SDK

### Purpose
A compliance layer designed to bridge institutional KYC/AML processes with Solana’s token infrastructure.

### Key Features
- **On-chain Whitelist Registry:** Secure, transparent, and auditable list of verified addresses.
- **SDK Integration:** Simple TypeScript client for wallet-level verification and token gating.
- **Regulatory Alignment:** Eases the adoption of compliant Real-World Asset issuance.

### Quick Start
```bash
# Clone the repo
git clone https://github.com/Gitdigital-products/solana-kyc-compliance-sdk.git
cd solana-kyc-compliance-sdk

# Build the Rust program
cd programs/compliance_registry
cargo build-bpf

# Build the SDK
cd ../../sdk/typescript
npm install && npm run build
Open-source SDK for enforcing KYC/AML compliance directly at the token level on Solana using Token Extensions (Transfer Hook &amp; Permanent Delegate). Includes a Rust on-chain program, TypeScript SDK, and Compliance Registry for institutional-grade Real-World Asset (RWA) issuance.
