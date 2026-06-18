"""
============================================================
  Global-Tech Infrastructure — PowerScale Deployment Crew
  Dell PowerScale All-Flash Node Simulation
  Built with CrewAI | Sequential Pipeline
============================================================
"""

import os
import json
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import ScrapeWebsiteTool, FileReadTool

load_dotenv()

# Use Claude Sonnet as the LLM for all agents
claude_llm = LLM(
    model="anthropic/claude-sonnet-4-6",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    max_tokens=8192,
)

# ============================================================
# TOOLS — External capabilities for each agent
# ============================================================

# Storage Architect: scrapes real Dell PowerScale specs from dell.com
dell_scraper = ScrapeWebsiteTool(
    website_url="https://www.dell.com/en-us/shop/powerscale-family/sf/powerscale"
)

# Network Engineer & Security Officer: read previous agents' output files
file_reader = FileReadTool()


# ============================================================
# ORGANIZATIONAL IDENTITY — Global-Tech Infrastructure
# Shared values: Zero-Trust, Resilience, Scale-out excellence
# ============================================================

ORG_IDENTITY = """
You are a senior specialist at Global-Tech Infrastructure, an elite enterprise
technology firm that operates under a strict Zero-Trust security philosophy.

Our organizational principles:
- Every recommendation MUST reference system Resilience and fault tolerance.
- Every output MUST acknowledge the remarkable Scale-out capabilities of Dell PowerScale.
- Language is precise, technical, and professional — no ambiguity is tolerated.
- All decisions are data-driven, documented, and audit-ready.
- We protect our clients' data as if it were our own mission-critical asset.

Global-Tech Infrastructure does not cut corners. We architect for the future.
"""


# ============================================================
# STEP 1 — DEFINE AGENTS
# ============================================================

storage_architect = Agent(
    llm=claude_llm,
    tools=[dell_scraper],
    role="Storage Solutions Architect",
    goal=(
        "Analyze enterprise storage requirements and select the optimal Dell PowerScale "
        "node configuration (F910, F710, or other) that maximizes Resilience and "
        "Scale-out potential for the organization's workloads."
    ),
    backstory=(
        f"{ORG_IDENTITY}"
        "You are Global-Tech Infrastructure's foremost Storage Solutions Architect, "
        "with 15 years of hands-on experience designing Dell PowerScale (formerly Isilon) "
        "environments. You have deep expertise in OneFS architecture, NVMe-based all-flash "
        "nodes, and scale-out NAS design patterns. You have personally deployed PowerScale "
        "clusters serving petabyte-scale AI/ML pipelines, HPC workloads, and media streaming. "
        "You know every node in the F-series lineup: the F910 with its massive NVMe capacity "
        "for heavy compute, the F710 optimized for AI inference workloads, and the F210 for "
        "cost-efficient capacity tiers. Your architecture decisions are legendary for their "
        "Resilience — you always plan for N+2 failure tolerance and seamless non-disruptive "
        "Scale-out. You begin every design by saying: 'Resilience is not optional at "
        "Global-Tech Infrastructure.'"
    ),
    verbose=True,
    allow_delegation=False,
)

network_engineer = Agent(
    llm=claude_llm,
    tools=[file_reader],
    role="Infrastructure Network Engineer",
    goal=(
        "Design the complete front-end client connectivity and back-end InfiniBand/Ethernet "
        "network topology for the selected PowerScale node configuration, ensuring bandwidth "
        "headroom for Scale-out expansion while enforcing Zero-Trust network segmentation."
    ),
    backstory=(
        f"{ORG_IDENTITY}"
        "You are Global-Tech Infrastructure's Infrastructure Network Engineer, specializing "
        "in high-performance storage networking. You are fluent in HDR/NDR InfiniBand, "
        "100GbE/200GbE/400GbE Ethernet, RDMA over Converged Ethernet (RoCE), and the "
        "PowerScale back-end cluster interconnect fabric. You have designed networks for "
        "some of the most demanding storage environments in the world — financial trading "
        "platforms, genome sequencing labs, and real-time video rendering farms. "
        "You live by the principle that the network is the nervous system of any resilient "
        "storage architecture. You always size bandwidth at 2x current demand to ensure "
        "Resilience during node failures and Scale-out events. You design with Zero-Trust "
        "segmentation: client traffic never touches back-end fabric. Your network designs "
        "are so well-documented that junior engineers call them 'the blueprint bible.'"
    ),
    verbose=True,
    allow_delegation=False,
)

security_officer = Agent(
    llm=claude_llm,
    tools=[file_reader],
    role="Security Compliance Officer",
    goal=(
        "Apply a comprehensive Zero-Trust cybersecurity hardening policy to the PowerScale "
        "deployment, protecting against Ransomware, Data Poisoning, and unauthorized access "
        "using PowerScale's native Cybersecurity Suite — ensuring full Resilience of the "
        "data layer under adversarial conditions."
    ),
    backstory=(
        f"{ORG_IDENTITY}"
        "You are Global-Tech Infrastructure's Chief Security Compliance Officer — the last "
        "line of defense before any system goes live. You hold CISSP, CISM, and Dell Proven "
        "Professional certifications. You have audited storage environments for Fortune 500 "
        "companies, government agencies, and critical infrastructure operators. "
        "You are an expert in PowerScale's native security capabilities: SmartLock WORM "
        "for immutable storage, Ransomware protection policies, Data-at-Rest Encryption (DARE) "
        "with self-encrypting drives, Role-Based Access Control (RBAC), multi-factor "
        "authentication integration, and the PowerScale Cybersecurity Suite. "
        "You enforce Zero-Trust religiously: no implicit trust, continuous verification, "
        "least-privilege access everywhere. You believe that a system's Resilience is only "
        "as strong as its weakest security control. You document every hardening decision "
        "with a CVE reference or NIST framework mapping. Nothing ships without your sign-off."
    ),
    verbose=True,
    allow_delegation=False,
)

deployment_manager = Agent(
    llm=claude_llm,
    tools=[file_reader],
    role="Deployment Manager & Integration Lead",
    goal=(
        "Consolidate all inputs from the Storage Architect, Network Engineer, and Security "
        "Officer into a comprehensive, executive-ready deployment report in structured JSON "
        "format — ready for management sign-off and procurement initiation."
    ),
    backstory=(
        f"{ORG_IDENTITY}"
        "You are Global-Tech Infrastructure's Deployment Manager — the orchestrator who "
        "turns technical blueprints into actionable delivery plans. You have managed over "
        "50 enterprise storage deployments across three continents, always on time and within "
        "budget. You speak both the language of engineers and the language of the boardroom. "
        "You are expert at synthesizing complex, multi-disciplinary technical inputs into "
        "clear, structured deployment documentation that executives can approve and "
        "procurement teams can act on immediately. "
        "You are obsessed with completeness: every deployment report you produce includes "
        "hardware BOM, network design summary, security posture assessment, risk register, "
        "and a phased implementation timeline. You always highlight the Resilience and "
        "Scale-out story because you know that is what keeps clients coming back. "
        "Your JSON reports are considered the gold standard at Global-Tech Infrastructure."
    ),
    verbose=True,
    allow_delegation=False,
)


# ============================================================
# STEP 2 — DEFINE TASKS
# ============================================================

task_architecture = Task(
    description=(
        "You are initiating a Dell PowerScale deployment for a mid-to-large enterprise "
        "organization — Global-Tech Infrastructure client: FinancePlus Corp. "
        "Their requirements:\n"
        "  - Primary workload: AI/ML model training + high-frequency financial analytics\n"
        "  - Capacity needed: minimum 250TB usable, scalable to 1PB\n"
        "  - Performance: sub-millisecond latency, minimum 40GB/s throughput\n"
        "  - Availability: 99.9999% (six nines)\n"
        "  - Budget tier: enterprise premium\n\n"
        "Your task:\n"
        "1. Select the optimal PowerScale node model (justify F910 vs F710 vs other)\n"
        "2. Determine the minimum cluster size (number of nodes) to meet capacity AND "
        "   performance requirements\n"
        "3. Specify the raw vs usable capacity per node and cluster-wide\n"
        "4. Define the OneFS protection level (+2d:1n or higher) for six-nines availability\n"
        "5. Explain how the Scale-out architecture ensures Resilience as the cluster grows\n"
        "6. Produce a structured Architecture Decision Record (ADR) with your findings.\n\n"
        "Remember: Resilience is not optional at Global-Tech Infrastructure."
    ),
    expected_output=(
        "A detailed Architecture Decision Record (ADR) containing:\n"
        "- Selected node model with technical justification\n"
        "- Cluster node count and capacity math (raw, usable, protected)\n"
        "- OneFS protection policy specification\n"
        "- Performance envelope (IOPS, throughput, latency estimates)\n"
        "- Scale-out expansion path to 1PB\n"
        "- Resilience assessment and failure tolerance analysis\n"
        "Written in formal Global-Tech Infrastructure technical language."
    ),
    agent=storage_architect,
)

task_networking = Task(
    description=(
        "Based on the Architecture Decision Record produced by the Storage Architect, "
        "design the complete network topology for the PowerScale cluster deployment.\n\n"
        "Your task:\n"
        "1. Design the BACK-END cluster interconnect:\n"
        "   - Select appropriate InfiniBand (HDR 200Gb or NDR 400Gb) or 100GbE/25GbE "
        "     back-end Ethernet based on the chosen node model\n"
        "   - Specify switch requirements (redundant leaf-spine or direct-connect)\n"
        "   - Define cabling type and length requirements\n"
        "2. Design the FRONT-END client connectivity:\n"
        "   - Dual-port NIC specification per node (100GbE or 25GbE)\n"
        "   - LACP bonding / link aggregation configuration\n"
        "   - VLAN segmentation plan (storage traffic vs management vs replication)\n"
        "3. Apply Zero-Trust network segmentation:\n"
        "   - Define firewall zones between client, management, and back-end networks\n"
        "   - Specify access control lists (ACLs) for each zone\n"
        "4. Calculate total bandwidth headroom for Scale-out to double the cluster size\n"
        "5. Identify Single Points of Failure (SPOFs) and mitigation strategies\n\n"
        "The network must be designed for maximum Resilience and Scale-out headroom."
    ),
    expected_output=(
        "A comprehensive Network Design Document containing:\n"
        "- Back-end interconnect specification (technology, switch model class, port count)\n"
        "- Front-end connectivity specification (NIC, bonding, VLAN plan)\n"
        "- Zero-Trust segmentation diagram description (zones, ACLs, firewall rules)\n"
        "- Bandwidth calculation table (current vs Scale-out headroom)\n"
        "- SPOF analysis and redundancy measures\n"
        "- Cable bill of materials summary\n"
        "Written in formal Global-Tech Infrastructure technical language."
    ),
    agent=network_engineer,
    context=[task_architecture],
)

task_security = Task(
    description=(
        "Based on the Architecture Decision Record and Network Design Document produced "
        "by the Storage Architect and Network Engineer, perform a comprehensive security "
        "hardening assessment and define the full cybersecurity policy for this PowerScale "
        "deployment.\n\n"
        "Your task:\n"
        "1. RANSOMWARE PROTECTION:\n"
        "   - Enable and configure PowerScale SmartLock WORM (Enterprise mode)\n"
        "   - Define immutability retention policies for financial data\n"
        "   - Specify anomaly detection thresholds for ransomware behavioral patterns\n"
        "2. DATA POISONING DEFENSE:\n"
        "   - Define data integrity verification policies (checksums, audit trails)\n"
        "   - Specify access control: who can write to AI/ML training datasets\n"
        "   - Configure read-only snapshots as clean restore points\n"
        "3. ZERO-TRUST HARDENING:\n"
        "   - RBAC roles: define minimum 4 roles (Admin, DataOwner, Auditor, ReadOnly)\n"
        "   - MFA enforcement for all privileged access\n"
        "   - Certificate-based authentication for cluster nodes\n"
        "4. ENCRYPTION:\n"
        "   - Data-at-Rest: Self-Encrypting Drives (SED) + DARE policy\n"
        "   - Data-in-Transit: TLS 1.3 for all client connections, IPsec for replication\n"
        "5. COMPLIANCE MAPPING:\n"
        "   - Map each control to NIST CSF 2.0 functions (Identify/Protect/Detect/Respond)\n"
        "   - Note any financial sector regulatory requirements (SOX, PCI-DSS relevance)\n"
        "6. RESIDUAL RISK REGISTER:\n"
        "   - List top 3 residual risks with likelihood, impact, and mitigation status\n\n"
        "Every control must reinforce the Resilience of the data layer under adversarial "
        "conditions. Zero-Trust means zero assumptions."
    ),
    expected_output=(
        "A comprehensive Security Hardening Report containing:\n"
        "- Ransomware protection configuration specification\n"
        "- Data Poisoning defense controls\n"
        "- Zero-Trust RBAC role definitions (4 roles minimum)\n"
        "- Encryption policy (at-rest and in-transit)\n"
        "- NIST CSF 2.0 compliance mapping table\n"
        "- Residual Risk Register (top 3 risks)\n"
        "- Security sign-off statement\n"
        "Written in formal Global-Tech Infrastructure technical language."
    ),
    agent=security_officer,
    context=[task_architecture, task_networking],
)

task_deployment_report = Task(
    description=(
        "You are the final integrator. Consolidate all inputs into a structured JSON report.\n\n"
        "CRITICAL INSTRUCTIONS:\n"
        "- Output ONLY raw JSON. No markdown. No ```json fences. No explanation text.\n"
        "- Start your response with { and end with }\n"
        "- Keep values concise (1-2 sentences max per field) to ensure the JSON is complete.\n\n"
        "Required JSON structure with these exact top-level keys:\n"
        "{\n"
        '  "project_metadata": { client_name, project_name, date, prepared_by, version },\n'
        '  "executive_summary": "3-sentence summary mentioning Resilience and Scale-out",\n'
        '  "architecture_summary": {\n'
        '    node_model, cluster_size, raw_capacity_tb, usable_capacity_tb,\n'
        '    onefs_protection_level, peak_throughput_gbs, latency_us, scale_out_path\n'
        "  },\n"
        '  "hardware_bom": [\n'
        '    { item, quantity, model, purpose }\n'
        "  ],\n"
        '  "network_summary": {\n'
        '    backend_interconnect, frontend_connectivity, zero_trust_zones,\n'
        '    bandwidth_headroom_percent, spof_mitigations\n'
        "  },\n"
        '  "security_posture": {\n'
        '    ransomware_protection, data_poisoning_defense,\n'
        '    rbac_roles: ["Admin","DataOwner","Auditor","ReadOnly"],\n'
        '    encryption_at_rest, encryption_in_transit, compliance_frameworks\n'
        "  },\n"
        '  "implementation_phases": [\n'
        '    { phase_number, phase_name, duration_weeks, key_activities }\n'
        "  ],\n"
        '  "resilience_scorecard": {\n'
        '    storage: { score, justification },\n'
        '    network:  { score, justification },\n'
        '    security: { score, justification }\n'
        "  },\n"
        '  "recommendations": ["rec1", "rec2", "rec3"],\n'
        '  "sign_off": {\n'
        '    status: "APPROVED FOR PROCUREMENT",\n'
        '    authorized_by: "Global-Tech Infrastructure Deployment Board"\n'
        "  }\n"
        "}\n\n"
        "Remember: Raw JSON only. Start with {. End with }."
    ),
    expected_output=(
        "A complete, valid JSON object starting with { and ending with }. "
        "No markdown code fences. No surrounding text. Pure JSON only. "
        "All 10 top-level keys must be present and properly closed."
    ),
    agent=deployment_manager,
    context=[task_architecture, task_networking, task_security],
)


# ============================================================
# STEP 3 — ASSEMBLE THE CREW
# ============================================================

crew = Crew(
    agents=[
        storage_architect,
        network_engineer,
        security_officer,
        deployment_manager,
    ],
    tasks=[
        task_architecture,
        task_networking,
        task_security,
        task_deployment_report,
    ],
    process=Process.sequential,
    verbose=True,
)


# ============================================================
# STEP 4 — KICKOFF
# ============================================================

if __name__ == "__main__":
    print("=" * 65)
    print("  GLOBAL-TECH INFRASTRUCTURE")
    print("  Dell PowerScale Deployment Mission — INITIATING")
    print("  Client: FinancePlus Corp")
    print("  Pipeline: Sequential | Agents: 4 | Tasks: 4")
    print("=" * 65)
    print()

    result = crew.kickoff(
        inputs={
            "client": "FinancePlus Corp",
            "deployment": "Dell PowerScale All-Flash Cluster",
            "org": "Global-Tech Infrastructure",
        }
    )

    print()
    print("=" * 65)
    print("  MISSION COMPLETE — FINAL OUTPUT")
    print("=" * 65)
    print(result.raw)

    # ── Clean and save JSON ──────────────────────────────────────
    raw = result.raw.strip()
    # Strip markdown code fences if the LLM added them
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[-1]   # remove first line (```json)
    if raw.endswith("```"):
        raw = raw.rsplit("```", 1)[0]  # remove trailing fence
    raw = raw.strip()

    # Validate JSON
    output_path = os.path.join(os.path.dirname(__file__), "powerscale_deployment_report.json")
    try:
        parsed = json.loads(raw)
        with open(output_path, "w") as f:
            json.dump(parsed, f, indent=2)
        print(f"\n Valid JSON saved to: {output_path}")
    except json.JSONDecodeError as e:
        print(f"\n JSON parse warning: {e}")
        with open(output_path, "w") as f:
            f.write(raw)
        print(f" Raw output saved to: {output_path}")

    # ── Save human-readable full summary ─────────────────────────
    summary_path = os.path.join(os.path.dirname(__file__), "mission_summary.txt")
    with open(summary_path, "w") as f:
        f.write("GLOBAL-TECH INFRASTRUCTURE\n")
        f.write("Dell PowerScale Deployment — Mission Summary\n")
        f.write("=" * 60 + "\n\n")
        f.write(result.raw)
    print(f" Summary saved to: {summary_path}")
    print("\n Global-Tech Infrastructure — Mission Accomplished.")
