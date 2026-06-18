# TODO — Global-Tech Infrastructure: PowerScale Deployment Crew

## Status Legend
- [x] Done
- [ ] Pending / Future

---

## Core Pipeline

- [x] Set up Python virtual environment and install dependencies (`crewai==1.9.3`, `crewai-tools`, `python-dotenv`)
- [x] Configure `.env` with `ANTHROPIC_API_KEY`
- [x] Create `.gitignore` to exclude `.env` and sensitive output files
- [x] Define `ORG_IDENTITY` shared organizational persona string
- [x] Initialize Claude Sonnet LLM via `anthropic/claude-sonnet-4-6`
- [x] Create `ScrapeWebsiteTool` for Dell PowerScale product page
- [x] Create `FileReadTool` for inter-agent context sharing

## Agents

- [x] Define `storage_architect` agent (Storage Solutions Architect)
- [x] Define `network_engineer` agent (Infrastructure Network Engineer)
- [x] Define `security_officer` agent (Security Compliance Officer)
- [x] Define `deployment_manager` agent (Deployment Manager & Integration Lead)

## Tasks

- [x] Define `task_architecture` — Architecture Decision Record for FinancePlus Corp
- [x] Define `task_networking` — Network Design Document with Zero-Trust segmentation
- [x] Define `task_security` — Security Hardening Report with NIST CSF 2.0 mapping
- [x] Define `task_deployment_report` — Final structured JSON deployment report (raw JSON, no markdown)

## Crew Assembly

- [x] Assemble `Crew` with `Process.sequential`
- [x] Verify agent and task ordering matches expected pipeline flow
- [x] Set `verbose=True` on all agents for observability
- [x] Disable delegation (`allow_delegation=False`) for strict sequential handoff

## Output Processing

- [x] Implement markdown fence stripping (LLM may wrap JSON in ` ```json ` blocks)
- [x] Validate output with `json.loads()`
- [x] Save valid JSON to `powerscale_deployment_report.json`
- [x] Save human-readable summary to `mission_summary.txt`
- [x] Add fallback save for raw output on JSON parse failure

## Testing & Validation

- [x] Run full pipeline end-to-end with `python3 main.py`
- [x] Verify `powerscale_deployment_report.json` contains all 10 required top-level keys
- [x] Verify cluster capacity exceeds 250TB minimum requirement (actual: 557TB ✓)
- [x] Verify throughput exceeds 40GB/s minimum (actual: 144GB/s ✓)
- [x] Verify RBAC contains 4 roles: Admin, DataOwner, Auditor, ReadOnly ✓
- [x] Verify 5 implementation phases present ✓
- [x] Verify resilience scorecard covers storage, network, and security ✓

## Production Scheduler (Bonus — הגדלת ראש)

- [x] Create `scheduler.py` with polling loop (30-second interval)
- [x] Implement `--scheduled` mode for cron-triggered single run
- [x] Implement `--sample` mode to generate demo request file
- [x] Add retry logic with exponential backoff (up to 3 attempts)
- [x] Add file-based logging to `scheduler_log.txt`
- [x] Add timestamped output file naming per run

## Documentation

- [x] Write `README.md` at project root (setup + run instructions)
- [x] Create `GITHUB/PRD.md` — Product Requirements Document
- [x] Create `GITHUB/PLAN.md` — Implementation Plan
- [x] Create `GITHUB/TODO.md` — This file
- [x] Create `GITHUB/README.md` — Detailed assignment report with proof of execution

## Submission Checklist

- [x] All source files present: `main.py`, `scheduler.py`, `requirements.txt`, `run.sh`
- [x] Output artifacts present: `powerscale_deployment_report.json`, `mission_summary.txt`
- [x] `.env` excluded from repository (`.gitignore` in place)
- [x] GITHUB folder contains: `PRD.md`, `PLAN.md`, `TODO.md`, `README.md`
- [ ] Add screenshots of terminal execution to `GITHUB/screenshots/`
- [ ] Upload to GitHub repository

---

## Future Enhancements (Out of Scope for M5)

- [ ] Replace file polling with message queue (RabbitMQ / Redis Streams)
- [ ] Add Airflow DAG for production-grade scheduling
- [ ] Add email/Slack notification on report completion
- [ ] Support multi-client concurrent pipeline runs
- [ ] Add LangSmith or CrewAI Studio observability integration
