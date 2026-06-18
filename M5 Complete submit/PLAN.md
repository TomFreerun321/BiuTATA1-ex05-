# PLAN — Implementation Plan
## Global-Tech Infrastructure | Dell PowerScale Deployment Crew

---

## Phase 1 — Design & Architecture
**Owner:** Storage Solutions Architect Agent
**Tool:** ScrapeWebsiteTool → Dell PowerScale product page

Steps:
1. Scrape Dell PowerScale F-series specifications
2. Evaluate F910 vs F710 vs F210 against client requirements
3. Select optimal node model with justification
4. Calculate cluster size (node count, raw vs usable capacity)
5. Define OneFS protection level (+2d:1n minimum)
6. Document Scale-out expansion path to 1PB
7. Output: Architecture Decision Record (ADR)

---

## Phase 2 — Network Design
**Owner:** Infrastructure Network Engineer Agent
**Tool:** FileReadTool → reads ADR from Phase 1
**Context:** Receives Phase 1 output automatically via `context=[task_architecture]`

Steps:
1. Read Architecture Decision Record
2. Design back-end cluster interconnect (InfiniBand / 100GbE RoCE)
3. Design front-end client connectivity (dual-port NIC, LACP bonding)
4. Define Zero-Trust VLAN segmentation (client / management / back-end)
5. Calculate bandwidth headroom for Scale-out
6. Identify and mitigate all SPOFs
7. Output: Network Design Document (NDR)

---

## Phase 3 — Security Hardening
**Owner:** Security Compliance Officer Agent
**Tool:** FileReadTool → reads ADR + NDR
**Context:** Receives Phases 1+2 outputs via `context=[task_architecture, task_networking]`

Steps:
1. Apply SmartLock WORM ransomware protection
2. Define Data Poisoning defense controls
3. Configure Zero-Trust RBAC (4 roles: Admin, DataOwner, Auditor, ReadOnly)
4. Specify encryption (DARE at-rest + TLS 1.3 in-transit)
5. Map controls to NIST CSF 2.0
6. Produce Residual Risk Register
7. Output: Security Hardening Report (SHR)

---

## Phase 4 — Final Report
**Owner:** Deployment Manager Agent
**Tool:** FileReadTool → reads all previous outputs
**Context:** Receives all 3 previous outputs via `context=[task_architecture, task_networking, task_security]`

Steps:
1. Consolidate ADR + NDR + SHR
2. Build Hardware BOM
3. Write Executive Summary
4. Produce Implementation Phases timeline
5. Generate Resilience Scorecard (1-10 per domain)
6. Add Strategic Recommendations
7. Sign-off: APPROVED FOR PROCUREMENT
8. Output: `powerscale_deployment_report.json` (valid JSON, 10 keys)

---

## Production Upgrade (scheduler.py)
Beyond the basic one-shot `kickoff()`, a production wrapper adds:
- **Polling loop**: checks every 30s for `deployment_request.json`
- **Cron scheduler**: `--scheduled` mode for Task Scheduler / cron
- **Retry logic**: up to 3 attempts on failure
- **Run logging**: `scheduler_log.txt`

```
python3 scheduler.py --poll       # daemon mode
python3 scheduler.py --scheduled  # cron-triggered single run
python3 scheduler.py --sample     # generate test request
```
