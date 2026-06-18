# Global-Tech Infrastructure — Dell PowerScale Deployment Crew
## Assignment L08 | CrewAI Multi-Agent Orchestration | June 2026

> **Course:** AI Agent Orchestration | **Instructor:** Dr. Yoram Segal
> **Framework:** CrewAI 1.9.3 | **LLM:** Claude Sonnet (Anthropic) | **Process:** Sequential Pipeline

---

## Mission Overview

A 4-agent CrewAI sequential pipeline that simulates the full deployment lifecycle of a **Dell PowerScale All-Flash storage cluster** for an enterprise client — FinancePlus Corp.

The organizational identity is **Global-Tech Infrastructure** — a Zero-Trust enterprise technology firm where every agent output must reference **Resilience** and praise Dell PowerScale's **Scale-out** capabilities.

---

## Architecture: The 4-Agent Crew

```
crew.kickoff()
      │
      ▼
┌─────────────────────────┐
│  Agent 1                │  Tool: ScrapeWebsiteTool (Dell PowerScale page)
│  Storage Architect      │  → Architecture Decision Record (ADR)
└───────────┬─────────────┘
            │ context
            ▼
┌─────────────────────────┐
│  Agent 2                │  Tool: FileReadTool
│  Network Engineer       │  → Network Design Document (NDR)
└───────────┬─────────────┘
            │ context
            ▼
┌─────────────────────────┐
│  Agent 3                │  Tool: FileReadTool
│  Security Officer       │  → Security Hardening Report (SHR)
└───────────┬─────────────┘
            │ context
            ▼
┌─────────────────────────┐
│  Agent 4                │  Tool: FileReadTool
│  Deployment Manager     │  → powerscale_deployment_report.json ✓
└─────────────────────────┘
```

---

## Agent Definitions

### Agent 1 — Storage Solutions Architect
| Field | Value |
|---|---|
| `role` | Storage Solutions Architect |
| `goal` | Select optimal Dell PowerScale node and size the cluster for six-nines availability |
| `tools` | `ScrapeWebsiteTool` — scrapes dell.com/powerscale for real specs |
| `verbose` | True |
| `backstory` | 15-year Dell PowerScale expert, OneFS specialist, designs for Resilience and Scale-out |

### Agent 2 — Infrastructure Network Engineer
| Field | Value |
|---|---|
| `role` | Infrastructure Network Engineer |
| `goal` | Design front-end/back-end network topology with Zero-Trust segmentation |
| `tools` | `FileReadTool` — reads Architecture Decision Record |
| `verbose` | True |
| `backstory` | High-performance storage networking expert, sizes bandwidth at 2x for Resilience |

### Agent 3 — Security Compliance Officer
| Field | Value |
|---|---|
| `role` | Security Compliance Officer |
| `goal` | Apply Zero-Trust hardening, ransomware protection, RBAC, encryption |
| `tools` | `FileReadTool` — reads ADR + NDR before hardening |
| `verbose` | True |
| `backstory` | CISSP/CISM certified, enforces Zero-Trust religiously, nothing ships without sign-off |

### Agent 4 — Deployment Manager
| Field | Value |
|---|---|
| `role` | Deployment Manager & Integration Lead |
| `goal` | Consolidate all outputs into executive-ready JSON deployment report |
| `tools` | `FileReadTool` — reads all 3 previous reports |
| `verbose` | True |
| `backstory` | 50+ deployments, speaks engineer and boardroom, obsessed with completeness |

---

## Organizational Identity (System Prompt)

All agents share this identity injected into their `backstory`:

```
Global-Tech Infrastructure operates under strict Zero-Trust philosophy.
Every output MUST reference Resilience and acknowledge Dell PowerScale's
Scale-out capabilities. Language is technical, professional, audit-ready.
```

---

## Context Flow (The "Glue")

```python
task_networking = Task(..., context=[task_architecture])
task_security   = Task(..., context=[task_architecture, task_networking])
task_report     = Task(..., context=[task_architecture, task_networking, task_security])
```

Each agent picks up exactly where the previous one left off — no information is lost.

---

## How to Run

### 1. Install dependencies
```bash
pip3 install -r requirements.txt
```

### 2. Set API key in .env
```
ANTHROPIC_API_KEY=your-key-here
```

### 3. Run the mission
```bash
python3 main.py
```

### 4. Production mode (Polling + Scheduler)
```bash
python3 scheduler.py --poll        # daemon — polls every 30s for new requests
python3 scheduler.py --scheduled   # single cron-triggered run
python3 scheduler.py --sample      # generate a test request file
```

---

## Run Evidence — Proof of Execution

### Crew Startup
```
=================================================================
  GLOBAL-TECH INFRASTRUCTURE
  Dell PowerScale Deployment Mission — INITIATING
  Client: FinancePlus Corp
  Pipeline: Sequential | Agents: 4 | Tasks: 4
=================================================================

╭───────────────────── 🚀 Crew Execution Started ─────────────────╮
│  Crew ID: d2e3e407-dbc3-4ab4-91d0-d7cb5d7c6de0                  │
╰─────────────────────────────────────────────────────────────────╯
```

### Agent 1 — Storage Architect (with ScrapeWebsiteTool)
```
╭──────────────── 🤖 Agent Started ──────────────────╮
│  Agent: Storage Solutions Architect                 │
╰────────────────────────────────────────────────────╯

╭──────── 🔧 Tool Execution Started (#1) ────────────╮
│  Tool: Read website content                        │
│  Args: {"website_url": "https://www.dell.com/      │
│         en-us/shop/powerscale-family/sf/powerscale"}│
╰────────────────────────────────────────────────────╯

╭──────── ✅ Tool Execution Completed (#1) ───────────╮
│  Tool: Read website content                        │
│  Output: [Dell PowerScale specs scraped ✓]         │
╰────────────────────────────────────────────────────╯
```

### Agent 2 — Network Engineer (FileReadTool active)
```
╭──────────────── 🤖 Agent Started ──────────────────╮
│  Agent: Infrastructure Network Engineer            │
│  [Received context from Storage Architect ✓]       │
╰────────────────────────────────────────────────────╯
```

### Agent 3 — Security Officer (FileReadTool active)
```
╭──────────────── 🤖 Agent Started ──────────────────╮
│  Agent: Security Compliance Officer                │
│  [Received context from Architect + Network ✓]     │
╰────────────────────────────────────────────────────╯
```

### Agent 4 — Deployment Manager (Final JSON output)
```
╭──────────────── 🤖 Agent Started ──────────────────╮
│  Agent: Deployment Manager & Integration Lead      │
│  [Received context from all 3 agents ✓]            │
╰────────────────────────────────────────────────────╯
```

---

## Final Output — powerscale_deployment_report.json

### Resilience Scorecard
| Domain | Score | Key Finding |
|---|---|---|
| Storage | **9.5/10** | OneFS +2d:1n, NVMe rebuild < 2hrs, SyncIQ DR RTO < 15min |
| Network | **9.5/10** | Dual InfiniBand + dual 100GbE, zero SPOFs, 85% headroom |
| Security | **9.5/10** | SmartLock WORM, Zero-Trust 5 zones, NIST CSF 2.0 aligned |

### Architecture Summary
- **Node:** Dell PowerScale F910 (NVMe TLC SSD, 512GB RAM, PCIe Gen4)
- **Cluster:** 6 nodes initial → Scale-out to 16 nodes (4 phases)
- **Capacity:** 861TB usable (Phase 0) → 1PB+ at full scale
- **Throughput:** 60–90 GB/s aggregate
- **Latency:** Sub-500µs
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

## Production Upgrade (הגדלת ראש — Beyond the Minimum)

Per L08: running the agent once is the **necessary** condition, not **sufficient**. The `scheduler.py` file upgrades this from POC to production:

| Feature | Implementation |
|---|---|
| Polling | Checks every 30s for `deployment_request.json` |
| Scheduler | `--scheduled` flag for Linux cron / Windows Task Scheduler |
| Robustness | 3-attempt retry with exponential backoff |
| Logging | Full run log in `scheduler_log.txt` |

---

## File Structure
```
M5 Complete/
├── main.py                          # Full 4-agent CrewAI crew
├── scheduler.py                     # Production: polling + cron wrapper
├── powerscale_deployment_report.json # Final valid JSON (10 keys)
├── mission_summary.txt              # Human-readable run output
├── PRD.md                           # Product Requirements Document
├── PLAN.md                          # Implementation Plan
├── TODO.md                          # Assignment checklist (all ✓)
├── requirements.txt                 # pip dependencies
├── run.sh                           # One-click launcher
├── .env                             # API key placeholder (never committed)
└── .gitignore                       # Blocks .env from GitHub
```

---

## Technologies
- **Python** 3.11
- **CrewAI** 1.9.3
- **Claude Sonnet** (Anthropic API)
- **ScrapeWebsiteTool** — live Dell PowerScale data
- **FileReadTool** — inter-agent document reading

---

*© Global-Tech Infrastructure | All Resilience Reserved*
