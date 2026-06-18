# TODO — Assignment Checklist
## Global-Tech Infrastructure | Dell PowerScale Deployment Crew

---

## Assignment Requirements

### Core Requirements
- [x] Choose a personal Use Case (mission)
- [x] Sequential process (Pipe) — not too complex
- [x] Build at least 4 chained agents on CrewAI
- [x] Define `role` for each agent
- [x] Define `goal` for each agent
- [x] Define `tools` for each agent
- [x] Define organizational identity (backstory / System Prompt)
- [x] Shared language across all agents (Zero-Trust, Resilience, Scale-out)
- [x] `verbose=True` on all agents
- [x] Run with one terminal and one manager (`crew.kickoff()`)
- [x] "Think big" — managerial output (BOM, scorecard, phases, risk register)

### Context Flow
- [x] Task 2 receives context from Task 1
- [x] Task 3 receives context from Tasks 1 + 2
- [x] Task 4 receives context from Tasks 1 + 2 + 3

### Output
- [x] Valid JSON final report (10 keys)
- [x] `sign_off: APPROVED FOR PROCUREMENT`
- [x] Resilience scorecard
- [x] Hardware BOM
- [x] Implementation phases

### Production Upgrade (הגדלת ראש)
- [x] Polling mechanism (`scheduler.py --poll`)
- [x] Scheduler/Cron mode (`scheduler.py --scheduled`)
- [x] Retry logic (3 attempts on failure)
- [x] Run logging (`scheduler_log.txt`)

### GitHub Submission
- [x] `README.md` — detailed report with run evidence
- [x] `PRD.md` — Product Requirements Document
- [x] `PLAN.md` — Implementation Plan
- [x] `TODO.md` — this checklist
- [x] `main.py` — full CrewAI crew
- [x] `scheduler.py` — production polling + cron wrapper
- [x] `powerscale_deployment_report.json` — valid JSON output
- [x] `mission_summary.txt` — human-readable run output
- [x] `requirements.txt` — dependencies
- [x] `.gitignore` — API key never pushed to GitHub
- [x] `.env` — placeholder only (no real key in repo)

---

## Security Checklist
- [x] API key removed from `.env` before GitHub push
- [x] `.gitignore` blocks `.env` from being committed
- [x] No hardcoded secrets anywhere in codebase
- [ ] Regenerate Anthropic API key (Commander's action — pending)
