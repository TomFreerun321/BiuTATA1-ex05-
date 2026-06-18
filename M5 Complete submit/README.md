# BiuTATA1-ex05 — Global-Tech Infrastructure | Dell PowerScale Deployment Crew

> **Course:** AI Agent Orchestration (L08) | **Instructor:** Dr. Yoram Segal | **June 2026**
> **Framework:** CrewAI 1.9.3 | **LLM:** Claude Sonnet (Anthropic) | **Process:** Sequential Pipeline

---

## What Is This?

A **4-agent CrewAI sequential pipeline** that simulates the full enterprise deployment lifecycle of a **Dell PowerScale All-Flash storage cluster** for a fictional client — FinancePlus Corp.

The organizational identity is **Global-Tech Infrastructure** — a Zero-Trust enterprise technology firm where every agent output must reference **Resilience** and praise Dell PowerScale's **Scale-out** capabilities.

---

## The 4-Agent Pipeline

```
crew.kickoff()
      │
      ▼
┌─────────────────────────────────────────┐
│  Agent 1 — Storage Solutions Architect  │
│  Tool: ScrapeWebsiteTool (dell.com)     │
│  Output: Architecture Decision Record   │
└───────────────────┬─────────────────────┘
                    │ context
                    ▼
┌─────────────────────────────────────────┐
│  Agent 2 — Infrastructure Network Eng.  │
│  Tool: FileReadTool                     │
│  Output: Network Design Document        │
└───────────────────┬─────────────────────┘
                    │ context
                    ▼
┌─────────────────────────────────────────┐
│  Agent 3 — Security Compliance Officer  │
│  Tool: FileReadTool                     │
│  Output: Security Hardening Report      │
└───────────────────┬─────────────────────┘
                    │ context
                    ▼
┌─────────────────────────────────────────┐
│  Agent 4 — Deployment Manager           │
│  Tool: FileReadTool                     │
│  Output: powerscale_deployment_report.json │
└─────────────────────────────────────────┘
```

---

## Organizational Identity (System Prompt)

All 4 agents share this identity injected into their `backstory`:

```
Global-Tech Infrastructure operates under strict Zero-Trust philosophy.
Every output MUST reference Resilience and acknowledge Dell PowerScale's
remarkable Scale-out capabilities. Language is technical, professional,
and audit-ready at all times.
```

---

## Agent Definitions

| Agent | Role | Tool | Goal |
|---|---|---|---|
| 1 | Storage Solutions Architect | `ScrapeWebsiteTool` — scrapes dell.com | Select F910/F710 node, size the cluster |
| 2 | Infrastructure Network Engineer | `FileReadTool` | Design back-end/front-end topology, Zero-Trust segmentation |
| 3 | Security Compliance Officer | `FileReadTool` | Ransomware protection, RBAC, encryption, NIST CSF 2.0 |
| 4 | Deployment Manager | `FileReadTool` | Consolidate all outputs → valid JSON report |

---

## How to Run

```bash
# Install dependencies
pip3 install -r requirements.txt

# Add your Anthropic API key to .env
echo "ANTHROPIC_API_KEY=your-key-here" > .env

# Run the full 4-agent crew
python3 main.py

# Production mode: polling daemon
python3 scheduler.py --poll

# Production mode: single cron-triggered run
python3 scheduler.py --scheduled
```

---

## Run Evidence — Screenshots

### Pipeline Start
![Pipeline Start](M5%20Complete%20submit/GITHUB/screenshots/01_pipeline_start.png)

### Agent 1 — Storage Architect (ScrapeWebsiteTool active)
![Agent 1](M5%20Complete%20submit/GITHUB/screenshots/02_agent1_storage_architect.png)

### Agent 2 — Network Engineer
![Agent 2](M5%20Complete%20submit/GITHUB/screenshots/03_agent2_network_engineer.png)

### Agent 3 — Security Officer
![Agent 3](M5%20Complete%20submit/GITHUB/screenshots/04_agent3_security_officer.png)

### Agent 4 — Deployment Manager (JSON output)
![Agent 4](M5%20Complete%20submit/GITHUB/screenshots/05_agent4_json_output.png)

### Final JSON Output File
![JSON File](M5%20Complete%20submit/GITHUB/screenshots/06_json_output_file.png)

---

## Final Output — powerscale_deployment_report.json

### Resilience Scorecard
| Domain | Score | Justification |
|---|---|---|
| Storage | **9.5/10** | OneFS +2d:1n, NVMe rebuild < 2hrs, SyncIQ DR RTO < 15min |
| Network | **9.5/10** | Dual InfiniBand + dual 100GbE, zero SPOFs, 85% port headroom |
| Security | **9.5/10** | SmartLock WORM, Zero-Trust 5 zones, NIST CSF 2.0 aligned |

### Architecture Summary
- **Node:** Dell PowerScale F910 (NVMe TLC SSD, 512GB RAM, PCIe Gen4)
- **Cluster:** 6 nodes initial → Scale-out roadmap to 16 nodes (4 phases)
- **Capacity:** 861TB usable (Phase 0) → 1PB+ at full scale
- **Throughput:** 60–90 GB/s aggregate
- **Latency:** Sub-500µs end-to-end
- **Availability:** 99.9999% (Six Nines)

### Sign-Off
```json
{
  "sign_off": {
    "status": "APPROVED FOR PROCUREMENT",
    "authorized_by": "Global-Tech Infrastructure Deployment Board"
  }
}
```

---

## Production Upgrade — Beyond the Minimum (הגדלת ראש)

Per L08: running the agent once is the **necessary** condition, not **sufficient**.
`scheduler.py` upgrades this from POC to production:

| Feature | Implementation |
|---|---|
| **Polling** | Checks every 30s for `deployment_request.json` |
| **Scheduler** | `--scheduled` flag for Linux `cron` / Windows Task Scheduler |
| **Retry Logic** | 3 attempts with exponential backoff on failure |
| **Logging** | Full run log saved to `scheduler_log.txt` |

---

## File Structure

```
BiuTATA1-ex05/
└── M5 Complete submit/
    ├── main.py                            # Full 4-agent CrewAI crew
    ├── scheduler.py                       # Production polling + cron wrapper
    ├── powerscale_deployment_report.json  # Final valid JSON (10 keys, sign-off)
    ├── mission_summary.txt                # Human-readable run output
    ├── PRD.md                             # Product Requirements Document
    ├── PLAN.md                            # Implementation Plan
    ├── TODO.md                            # Assignment checklist (all ✓)
    ├── requirements.txt                   # pip dependencies
    ├── run.sh                             # One-click launcher
    ├── .env                               # API key placeholder (never committed)
    ├── .gitignore                         # Blocks .env from GitHub
    └── GITHUB/
        ├── PRD.md
        ├── PLAN.md
        ├── TODO.md
        ├── README.md
        └── screenshots/
            ├── 01_pipeline_start.png
            ├── 02_agent1_storage_architect.png
            ├── 03_agent2_network_engineer.png
            ├── 04_agent3_security_officer.png
            ├── 05_agent4_json_output.png
            └── 06_json_output_file.png
```

---

## Assignment Checklist

- [x] 4 agents minimum with `role`, `goal`, `backstory`, `tools`
- [x] Sequential process (Pipe) — `Process.sequential`
- [x] Organizational identity shared across all agents
- [x] "Resilience" + "Scale-out" in every agent output
- [x] `verbose=True` on all agents
- [x] Context flowing between all 4 tasks
- [x] Single `crew.kickoff()` — one terminal, one manager
- [x] Valid JSON final report (10 keys + sign-off)
- [x] PRD.md, PLAN.md, TODO.md markdown files
- [x] Screenshots proving execution
- [x] Production upgrade: Polling + Scheduler (`scheduler.py`)
- [x] No API keys in repository (`.gitignore` protects `.env`)

---

*© Global-Tech Infrastructure | All Resilience Reserved*
*Built with CrewAI + Claude Sonnet | L08 Assignment | June 2026*
