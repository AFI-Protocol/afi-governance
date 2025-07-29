# Governance Schemas

This directory contains standardized schemas used for AFI governance proposals and related agent scoring logic.

## Included Files

- **UniversalProposalSignal.schema.json**  
  Canonical schema for proposal-as-signal logic. Enables agent scoring, metadata enrichment, and DAO integration.  
  Contains full annotations, including strategy tags, confidence signals, and timestamp metadata.

## Usage

These schemas are used by governance validators to assess the quality and characteristics of proposals submitted to the AFI DAO. They are referenced by proposal validators and scored using standardized insight fields defined in the schema.

## Compatibility

- ✅ AOS Codex
- ✅ Agent Validator Scoring
- ✅ Proposal Replay & Insight Review
