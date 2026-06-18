#!/bin/bash
# Global-Tech Infrastructure — Mission Launcher
echo "============================================"
echo "  GLOBAL-TECH INFRASTRUCTURE"
echo "  PowerScale Deployment Crew — LAUNCHING"
echo "============================================"

# Load .env if it exists
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Check for API key
if [ -z "$OPENAI_API_KEY" ] || [ "$OPENAI_API_KEY" = "your-openai-api-key-here" ]; then
    echo ""
    echo "ERROR: OPENAI_API_KEY not set in .env file"
    echo "Please add your key to .env and try again."
    exit 1
fi

echo "API key detected. Starting mission..."
echo ""
python3 main.py
