# PLAN — Global-Tech Infrastructure: PowerScale Deployment Crew

## Implementation Strategy

The system is implemented as a **sequential CrewAI pipeline** where each agent's output becomes the input context for the next. This mirrors a real-world enterprise deployment workflow: architect → network engineer → security officer → deployment manager.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                  CrewAI Sequential Pipeline                  │
│                                                             │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   │
│  │   Storage    │──▶│   Network    │──▶│   Security   │   │
│  │  Architect   │   │  Engineer    │   │   Officer    │   │
│  │  (Agent 1)   │   │  (Agent 2)   │   │  (Agent 3)   │   │
│  └──────────────┘   └──────────────┘   └──────────────┘   │
│         │                  │                  │             │
│         └──────────────────┴──────────────────┘             │
│                             │                               │
│                    ┌──────────────────┐                     │
│                    │   Deployment     │                     │
│                    │    Manager       │                     │
│                    │   (Agent 4)      │                     │
│                    └──────────────────┘                     │
│                             │                               │
│              ┌──────────────┴──────────────┐                │
│              ▼                             ▼                │
│  powerscale_deployment_report.json   mission_summary.txt    │
└─────────────────────────────────────────────────────────────┘
```

---

## Phase 1 — Environment Setup

**Goal:** Establish Python environment and dependencies

- [ ] Create project directory
- [ ] Install CrewAI 1.9.3+ and crewai-tools
- [ ] Install python-dotenv
- [ ] Configure `.env` with `ANTHROPIC_API_KEY`
- [ ] Create `.gitignore` to exclude `.env` and output artifacts

**Key file:** `requirements.txt`
```
crewai==1.9.3
crewai-tools
python-dotenv
```

---

## Phase 2 — LLM & Tools Configuration

**Goal:** Wire the LLM and per-agent tools

- [ ] Initialize `LLM` object with `anthropic/claude-sonnet-4-6` model
- [ ] Create `ScrapeWebsiteTool` pointing to Dell PowerScale product page (for Agent 1)
- [ ] Create `FileReadTool` for agents 2, 3, 4 to read previous outputs

**Design decision:** Use Anthropic Claude (not OpenAI) as the underlying LLM — better long-context handling for chained agent contexts.

---

## Phase 3 — Organizational Identity

**Goal:** Establish shared persona across all agents

- Define `ORG_IDENTITY` string injected into every agent's `backstory`
- Principles: Zero-Trust, Resilience, Scale-out excellence, audit-ready documentation
- This ensures output coherence across all 4 agents

---

## Phase 4 — Agent Definitions

**Goal:** Define all 4 agents with role, goal, and backstory

| Agent | Role | Primary Tool |
|-------|------|-------------|
| `storage_architect` | Storage Solutions Architect | `dell_scraper` (web scraper) |
| `network_engineer` | Infrastructure Network Engineer | `file_reader` |
| `security_officer` | Security Compliance Officer | `file_reader` |
| `deployment_manager` | Deployment Manager & Integration Lead | `file_reader` |

Each agent:
- `verbose=True` for full pipeline observability
- `allow_delegation=False` — strict sequential handoff

---

## Phase 5 — Task Definitions

**Goal:** Define 4 tasks with precise prompts and expected outputs

### Task 1 — Architecture Decision Record
- **Inputs:** FinancePlus Corp requirements (capacity, performance, availability, budget)
- **Outputs:** ADR — node model selection, cluster size math, OneFS protection level, Scale-out path
- **Agent:** `storage_architect`

### Task 2 — Network Design Document
- **Context:** Task 1 output
- **Outputs:** Back-end InfiniBand topology, front-end 100GbE bonding, Zero-Trust VLAN segmentation, bandwidth/SPOF analysis
- **Agent:** `network_engineer`

### Task 3 — Security Hardening Report
- **Context:** Tasks 1 + 2
- **Outputs:** SmartLock WORM config, Data Poisoning defense, RBAC roles, encryption policy, NIST CSF mapping, residual risk register
- **Agent:** `security_officer`

### Task 4 — Final JSON Deployment Report
- **Context:** Tasks 1 + 2 + 3
- **Outputs:** Single valid JSON object with 10 required top-level keys
- **Critical constraint:** Raw JSON only — no markdown fences
- **Agent:** `deployment_manager`

---

## Phase 6 — Crew Assembly & Kickoff

**Goal:** Assemble and execute the pipeline

```python
crew = Crew(
    agents=[storage_architect, network_engineer, security_officer, deployment_manager],
    tasks=[task_architecture, task_networking, task_security, task_deployment_report],
    process=Process.sequential,
    verbose=True,
)
result = crew.kickoff(inputs={...})
```

---

## Phase 7 — Output Processing

**Goal:** Save validated JSON and human-readable summary

- Strip markdown fences if LLM wraps JSON in ` ```json ` blocks
- Validate with `json.loads()`
- Save to `powerscale_deployment_report.json` (pretty-printed, indent=2)
- Save raw to `mission_summary.txt`

---

## Phase 8 — Production Scheduler (Bonus)

**Goal:** Demonstrate POC → Production upgrade

File: `scheduler.py`

| Mode | Command | Behavior |
|------|---------|----------|
| Polling | `python3 scheduler.py --poll` | Checks every 30s for `deployment_request.json` |
| Scheduled | `python3 scheduler.py --scheduled` | Single cron-triggered run |
| Sample | `python3 scheduler.py --sample` | Creates a sample request file |

Additional features:
- Retry logic (up to 3 attempts with backoff)
- File-based logging to `scheduler_log.txt`
- Timestamped output reports per run

---

## Risk Register

| Risk | Likelihood | Mitigation |
|------|-----------|-----------|
| LLM adds markdown fences around JSON | High | Strip logic in output processing |
| JSON truncated due to token limit | Medium | Set `max_tokens=4096`, keep field values concise |
| API key not set | Low | `.env` validation, clear error message |
| CrewAI version incompatibility | Low | Pin `crewai==1.9.3` in requirements.txt |
