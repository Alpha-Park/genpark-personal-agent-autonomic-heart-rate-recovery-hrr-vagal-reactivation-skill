# genpark-personal-agent-autonomic-heart-rate-recovery-hrr-vagal-reactivation-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

Post-exercise 1-minute Heart Rate Recovery (HRR1, bpm) parasympathetic vagal reactivation & cardiac autonomic mortality index.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `evaluate_heart_rate_recovery_vagal_tone`
- **Category**: `personal_agent`

### Method Documentation
Evaluate parasympathetic cardiac autonomic reactivation using 1-minute and 2-minute post-exercise Heart Rate Recovery (HRR1 & HRR2, bpm).
A blunted HRR1 (< 12 bpm upright, or < 18 bpm supine) reflects impaired vagal tone reactivation and serves as a powerful independent predictor of all-cause mortality.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "evaluate_heart_rate_recovery_vagal_tone",
    "arguments": {
    "peak_exercise_hr_bpm": 172,
    "hr_at_1min_recovery_bpm": 146,
    "hr_at_2min_recovery_bpm": 128,
    "protocol": "UPRIGHT_TREADMILL"
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
