# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-personal-agent-autonomic-heart-rate-recovery-hrr-vagal-reactivation-skill
Category: personal_agent
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def evaluate_heart_rate_recovery_vagal_tone(peak_exercise_hr_bpm, hr_at_1min_recovery_bpm, hr_at_2min_recovery_bpm=None, protocol="UPRIGHT_TREADMILL"):
    if peak_exercise_hr_bpm <= hr_at_1min_recovery_bpm:
        raise ValueError("Peak HR must be greater than recovery HR")
        
    hrr1_drop = peak_exercise_hr_bpm - hr_at_1min_recovery_bpm
    hrr2_drop = (peak_exercise_hr_bpm - hr_at_2min_recovery_bpm) if hr_at_2min_recovery_bpm else None
    
    # Established clinical cutoffs for HRR1 (Cole CR et al., NEJM):
    # Upright active cool-down: Abnormal < 12 bpm
    # Passive supine rest: Abnormal < 18 bpm
    cutoff = 12 if "UPRIGHT" in protocol.upper() else 18
    
    if hrr1_drop >= 25:
        tier = "EXCELLENT_VAGAL_REACTIVATION"
        mortality_hazard = "MINIMAL"
    elif hrr1_drop >= cutoff:
        tier = "NORMAL_PARASYMPATHETIC_RECOVERY"
        mortality_hazard = "STANDARD_POPULATION"
    else:
        tier = "BLUNTED_HEART_RATE_RECOVERY"
        mortality_hazard = "SIGNIFICANTLY_ELEVATED_MORTALITY_HAZARD"
        
    return {
        "peak_exercise_hr_bpm": peak_exercise_hr_bpm,
        "hr_at_1min_recovery_bpm": hr_at_1min_recovery_bpm,
        "hrr_1min_drop_bpm": hrr1_drop,
        "hrr_2min_drop_bpm": hrr2_drop,
        "autonomic_reactivation_tier": tier,
        "cardiovascular_mortality_hazard": mortality_hazard,
        "vagal_reactivation_impaired": hrr1_drop < cutoff,
        "guidance": "Blunted vagal rebound correlates with sympathetic overactivation and cardiac dysautonomia; prioritize parasympathetic recovery exercises." if hrr1_drop < cutoff else "Healthy autonomic vagal reactivation."
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "evaluate_heart_rate_recovery_vagal_tone",
                        "description": """Evaluate parasympathetic cardiac autonomic reactivation using 1-minute and 2-minute post-exercise Heart Rate Recovery (HRR1 & HRR2, bpm).
A blunted HRR1 (< 12 bpm upright, or < 18 bpm supine) reflects impaired vagal tone reactivation and serves as a powerful independent predictor of all-cause mortality.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = evaluate_heart_rate_recovery_vagal_tone(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'peak_exercise_hr_bpm': 172, 'hr_at_1min_recovery_bpm': 146, 'hr_at_2min_recovery_bpm': 128, 'protocol': 'UPRIGHT_TREADMILL'}
        out = evaluate_heart_rate_recovery_vagal_tone(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
