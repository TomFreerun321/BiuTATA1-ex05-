"""
============================================================
  Global-Tech Infrastructure — PowerScale Deployment Scheduler
  Production-grade wrapper: Polling + Cron scheduling
  Demonstrates POC → Production upgrade (L08 requirement)
============================================================

WHAT THIS ADDS BEYOND THE BASIC KICKOFF:
  - Polling: checks every interval if a new deployment request exists
  - Scheduler (cron-style): runs the crew on a recurring schedule
  - Robustness: error handling, retry logic, run logging
  - Initiative beyond minimum requirement (הגדלת ראש)
============================================================
"""

import os
import time
import json
import logging
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ── Logging setup ────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("scheduler_log.txt"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger("GTI-Scheduler")

# ── Configuration ────────────────────────────────────────────
POLL_INTERVAL_SECONDS = 30        # check every 30 seconds for new requests
MAX_RETRIES = 3                   # retry failed runs up to 3 times
REQUEST_FILE = "deployment_request.json"   # polling target
OUTPUT_DIR = Path(__file__).parent


def check_for_new_request() -> dict | None:
    """
    POLLING: Check if a new deployment request file has arrived.
    In production this would poll a database, API endpoint, or message queue.
    Here we poll for a local JSON file as a demonstration.
    """
    request_path = OUTPUT_DIR / REQUEST_FILE
    if request_path.exists():
        log.info(f"New deployment request detected: {request_path}")
        with open(request_path) as f:
            data = json.load(f)
        # Remove the file so we don't process it again (mark as consumed)
        request_path.unlink()
        return data
    return None


def run_crew(request: dict, attempt: int = 1) -> bool:
    """
    Run the full 4-agent CrewAI crew for the given request.
    Returns True on success, False on failure.
    """
    from crewai import Agent, Task, Crew, Process, LLM

    client = request.get("client", "FinancePlus Corp")
    log.info(f"[Attempt {attempt}/{MAX_RETRIES}] Starting crew for client: {client}")

    try:
        # Import crew definition from main.py
        from main import (
            storage_architect,
            network_engineer,
            security_officer,
            deployment_manager,
            task_architecture,
            task_networking,
            task_security,
            task_deployment_report,
        )

        crew = Crew(
            agents=[storage_architect, network_engineer, security_officer, deployment_manager],
            tasks=[task_architecture, task_networking, task_security, task_deployment_report],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff(inputs=request)

        # Save timestamped output
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_file = OUTPUT_DIR / f"report_{timestamp}_{client.replace(' ', '_')}.json"

        raw = result.raw.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[-1]
        if raw.endswith("```"):
            raw = raw.rsplit("```", 1)[0]
        raw = raw.strip()

        try:
            parsed = json.loads(raw)
            with open(out_file, "w") as f:
                json.dump(parsed, f, indent=2)
            log.info(f"Report saved: {out_file}")
        except json.JSONDecodeError:
            with open(out_file.with_suffix(".txt"), "w") as f:
                f.write(result.raw)
            log.warning(f"Raw output saved (JSON parse failed): {out_file}")

        return True

    except Exception as e:
        log.error(f"Crew run failed (attempt {attempt}): {e}")
        return False


def run_with_retry(request: dict) -> bool:
    """
    ROBUSTNESS: Retry failed crew runs up to MAX_RETRIES times.
    """
    for attempt in range(1, MAX_RETRIES + 1):
        success = run_crew(request, attempt=attempt)
        if success:
            return True
        if attempt < MAX_RETRIES:
            wait = attempt * 10
            log.info(f"Retrying in {wait} seconds...")
            time.sleep(wait)
    log.error("All retry attempts exhausted. Skipping this request.")
    return False


def polling_loop():
    """
    POLLING MODE: Continuously poll for new deployment requests.
    Runs indefinitely — suitable for a background service / daemon.
    Stop with Ctrl+C.
    """
    log.info("=" * 60)
    log.info("  Global-Tech Infrastructure — Polling Mode ACTIVE")
    log.info(f"  Checking every {POLL_INTERVAL_SECONDS}s for new requests")
    log.info(f"  Drop a '{REQUEST_FILE}' file to trigger a run")
    log.info("  Press Ctrl+C to stop")
    log.info("=" * 60)

    while True:
        try:
            request = check_for_new_request()
            if request:
                log.info(f"Processing request: {request}")
                run_with_retry(request)
            else:
                log.debug(f"No request found. Next check in {POLL_INTERVAL_SECONDS}s...")
            time.sleep(POLL_INTERVAL_SECONDS)

        except KeyboardInterrupt:
            log.info("Polling stopped by user. Global-Tech Infrastructure standing down.")
            break


def scheduled_run():
    """
    SCHEDULER MODE: Run the crew once on a fixed schedule (cron-style).
    In production, this would be called by cron / Task Scheduler / Airflow.

    Linux/macOS cron example (runs every day at 06:00):
        0 6 * * * /usr/bin/python3 /path/to/M5\ Complete/scheduler.py --scheduled

    Windows Task Scheduler:
        Action: python3 scheduler.py --scheduled
        Trigger: Daily at 06:00
    """
    log.info("=" * 60)
    log.info("  Global-Tech Infrastructure — Scheduled Run")
    log.info(f"  Triggered at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info("=" * 60)

    default_request = {
        "client": "FinancePlus Corp",
        "deployment": "Dell PowerScale All-Flash Cluster",
        "org": "Global-Tech Infrastructure",
    }

    success = run_with_retry(default_request)
    status = "SUCCESS" if success else "FAILED"
    log.info(f"Scheduled run completed: {status}")


# ── Example: create a sample request file for polling demo ───
def create_sample_request():
    """Drop a sample request file to trigger the polling loop."""
    sample = {
        "client": "FinancePlus Corp",
        "deployment": "Dell PowerScale All-Flash Cluster",
        "org": "Global-Tech Infrastructure",
    }
    with open(OUTPUT_DIR / REQUEST_FILE, "w") as f:
        json.dump(sample, f, indent=2)
    print(f"Sample request file created: {REQUEST_FILE}")
    print("The polling loop will pick it up on the next check interval.")


# ── Entry point ───────────────────────────────────────────────
if __name__ == "__main__":
    import sys

    mode = sys.argv[1] if len(sys.argv) > 1 else "--poll"

    if mode == "--poll":
        polling_loop()
    elif mode == "--scheduled":
        scheduled_run()
    elif mode == "--sample":
        create_sample_request()
    else:
        print("Usage:")
        print("  python3 scheduler.py --poll        # Start polling loop")
        print("  python3 scheduler.py --scheduled   # Single scheduled run (for cron)")
        print("  python3 scheduler.py --sample      # Create a sample request file")
