import { z } from "zod";
import fs from "fs/promises";
import path from "path";

const UniversalProposalSchema = z.object({
  signal_type: z.literal("governance_proposal"),
  proposal_id: z.string(),
  proposed_by: z.string(),
  timestamp: z.string(),
  version_target: z.string(),
  title: z.string(),
  description: z.string(),
  justification: z.string(),
  affected_modules: z.array(z.string()),
  proposed_mutations: z.object({
    field: z.string(),
    action: z.enum(["add", "update", "remove"]),
    new_value: z.any(),
  }),
  dependencies: z.array(z.string()).optional(),
  proposal_type: z.enum(["upgrade", "policy", "emergency", "meta"]),
  urgency_level: z.enum(["low", "medium", "high", "critical"]),
  test_vector: z.string().optional(),
  compliance_check: z.boolean(),
  signature: z.string().optional(),
});

async function main() {
  const data = await fs.readFile(
    path.join(process.cwd(), "examples", "valid-proposal.json"),
    "utf-8"
  );
  const jsonData = JSON.parse(data);
  const parsed = UniversalProposalSchema.parse(jsonData);
  console.log("✅ Proposal object is valid:", parsed.proposal_id);
}

main().catch((err) => {
  console.error("❌ Validation failed:\n", err.errors ?? err);
  process.exit(1);
});