# afi-governance — Agent Instructions ⚠️ HIGH RISK

**afi-governance** contains on-chain governance contracts and Epoch Pulse coordination logic for AFI Protocol. This repo defines how protocol governance decisions are made and executed on-chain.

**⚠️ WARNING**: This repo contains governance smart contracts. Changes can have systemic impact on protocol governance. All contract modifications require explicit human approval and security audit.

**Global Authority**: All agents operating in AFI Protocol repos must follow `afi-config/codex/governance/droids/AFI_DROID_CHARTER.v0.1.md`. If this AGENTS.md conflicts with the Charter, **the Charter wins**.

---

## Build & Test

```bash
# Install dependencies
npm install

# Build TypeScript
npm run build

# Type check
npm run typecheck

# Run tests (placeholder - no tests yet)
npm test
```

**Expected outcomes**: TypeScript compiles without errors. Add tests before deploying any governance logic.

---

## Run Locally / Dev Workflow

This repo has no dev server. Typical workflow:

1. Edit governance contracts or coordination logic
2. Write comprehensive tests FIRST
3. Run `npm run build && npm run typecheck`
4. Get explicit human approval before deploying

**Do not deploy governance changes without security review.**

---

## Architecture Overview

**Purpose**: Define on-chain governance mechanics, Epoch Pulse coordination, and protocol parameter updates.

**Key directories**:
- `contracts/` — Governance smart contracts (if Solidity)
- `src/` — TypeScript governance coordination logic
- `proposals/` — Governance proposal schemas and templates
- `pulse/` — Epoch Pulse design and coordination

**Consumed by**: afi-token, afi-reactor, on-chain governance processes.

---

## Security

- **⚠️ Governance changes are systemic**: Incorrect governance logic can lock funds, break protocol, or enable attacks.
- **All contract changes require audit**: Do not modify governance contracts without explicit human approval and security review.
- **Test coverage is mandatory**: All governance logic must have comprehensive tests.
- **No secrets in code**: Use environment variables for private keys and API keys.
- **Proposal validation**: All governance proposals must follow schema contracts.

---

## Git Workflows

- **Base branch**: `main` or `migration/multi-repo-reorg`
- **Branch naming**: `feat/`, `fix/`, `security/`
- **Commit messages**: Conventional commits (e.g., `feat(governance): add epoch transition proposal schema`)
- **Before committing**: Run `npm run build && npm run typecheck && npm test`
- **⚠️ Never force-push**: Governance changes must be traceable

---

## Conventions & Patterns

- **Language**: TypeScript (ESM), Solidity (if contracts)
- **Proposal schemas**: JSON Schema, validated against afi-config schemas
- **Epoch Pulse**: Follow design in `pulse/design.md`
- **Tests**: Comprehensive coverage for all governance paths

---

## Scope & Boundaries for Agents

**Allowed** (with extreme caution):
- Add governance proposal schemas when explicitly requested
- Improve documentation on governance processes
- Add tests for existing governance logic
- Update Epoch Pulse coordination logic with clear spec and tests

**Forbidden**:
- Modify governance contracts without explicit human approval and security audit
- Change governance parameters (quorum, voting periods, etc.) without spec
- Deploy governance changes to mainnet
- Add governance logic without comprehensive tests
- Change proposal validation logic without understanding impact

**When unsure**: **Do not proceed**. Ask for explicit spec, security review, and human approval. Governance changes are irreversible on-chain.

---

**Last Updated**: 2025-11-26  
**Maintainers**: AFI Governance Team  
**Charter**: `afi-config/codex/governance/droids/AFI_DROID_CHARTER.v0.1.md`

