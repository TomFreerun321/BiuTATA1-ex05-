# PRD — Product Requirements Document
## Global-Tech Infrastructure | Dell PowerScale Deployment Crew

---

## 1. Overview
A multi-agent AI system built with CrewAI that simulates the full deployment lifecycle of a Dell PowerScale All-Flash storage cluster for an enterprise client (FinancePlus Corp).

## 2. Business Problem
Enterprise storage deployments require coordinated expertise across architecture, networking, security, and project management. This system automates that coordination using a sequential AI agent pipeline.

## 3. Users
- Course assignment submission (Dr. Yoram Segal, June 2026)
- Enterprise IT managers evaluating AI orchestration for infrastructure planning

## 4. Functional Requirements

| # | Requirement | Priority |
|---|---|---|
| FR-01 | 4 specialized AI agents with distinct roles | Must Have |
| FR-02 | Sequential pipeline (no token waste) | Must Have |
| FR-03 | Shared organizational identity across all agents | Must Have |
| FR-04 | Context passing between tasks | Must Have |
| FR-05 | verbose=True on all agents | Must Have |
| FR-06 | Tools assigned to each agent | Must Have |
| FR-07 | Single kickoff command | Must Have |
| FR-08 | Valid JSON final report | Must Have |
| FR-09 | Polling + Scheduler (production upgrade) | Should Have |

## 5. Non-Functional Requirements
- Language: Python 3.11+
- Framework: CrewAI 1.9.3
- LLM: Claude Sonnet (Anthropic)
- Process: Sequential (not hierarchical — avoids token overhead)
- Output: Valid JSON + human-readable summary

## 6. Organizational Identity
**Name:** Global-Tech Infrastructure
**Culture:** Zero-Trust security philosophy
**Language:** Technical, professional, formal
**Mandatory terms:** "Resilience" and "Scale-out" must appear in every agent output

## 7. Agent Specifications

### Agent 1 — Storage Solutions Architect
- **Tool:** ScrapeWebsiteTool (Dell PowerScale product page)
- **Goal:** Select optimal node (F910/F710) and size the cluster

### Agent 2 — Infrastructure Network Engineer
- **Tool:** FileReadTool
- **Goal:** Design back-end/front-end network topology with Zero-Trust segmentation

### Agent 3 — Security Compliance Officer
- **Tool:** FileReadTool
- **Goal:** Apply hardening, ransomware protection, RBAC, encryption policies

### Agent 4 — Deployment Manager
- **Tool:** FileReadTool
- **Goal:** Produce final JSON deployment report ready for executive sign-off

## 8. Success Criteria
- All 4 agents complete their tasks without error
- Context flows correctly between all 4 tasks
- Final JSON is valid and contains all 10 required keys
- "Resilience" and "Scale-out" appear in every agent output
- Run completes from a single `python3 main.py` command
