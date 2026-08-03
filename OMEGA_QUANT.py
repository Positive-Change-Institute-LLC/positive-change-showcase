#!/usr/bin/env python3
"""
PCI / PROMETHEUS / OMEGA QUANT AUTHORITY
SOVEREIGN STACK – FULL RUNTIME (ALL-IN-ONE PYTHON FILE)
Author: Christopher S. Rowland Sr.
Positive Change Institute LLC

This file contains:
- Identity + Doctrine
- Whop Program Registry
- Prometheus Assessment Engine
- Scoring + Routing Logic
- FastAPI Runtime
- Uvicorn Entrypoint

Run: python omega_quant.py
Access: http://0.0.0.0:8000
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import json

# ============================================================
# 1. IDENTITY + DOCTRINE
# ============================================================

class Identity(BaseModel):
    founder: str
    company: str
    mission: str
    brands: dict

PCI_IDENTITY = Identity(
    founder="Christopher S. Rowland Sr.",
    company="Positive Change Institute LLC",
    mission="Build sovereign systems for credit, income, operations, and protection.",
    brands={
        "prometheus": "Prometheus Superintelligence™ – central orchestrator",
        "omega_quant": "Omega Quant Authority – sovereign financial architecture",
        "pci_sovereign": "PCI Sovereign Systems™ – multi-domain platform"
    },
)

DOCTRINE = {
    "pci_sovereign_standard": [
        "User sovereignty: user owns data, keys, and progression.",
        "Causality: every artifact must move a measurable metric.",
        "Precision: credit, income, ops, and protection are quantified.",
        "Golden Ratio: layout, narrative, and tiering follow φ ≈ 1.618."
    ],
    "prometheus_principles": [
        "Assess → Score → Route → Orchestrate.",
        "Every decision is deterministic and sovereign-aligned.",
        "Prometheus is the causal engine of PCI.",
        "Intelligence flows from data to doctrine to destiny."
    ],
    "omega_quant_principles": [
        "Credit architecture as a sovereign system.",
        "Income systems as scalable infrastructure.",
        "Operational stacks as resilience engines.",
        "Protection as legacy preservation.",
        "Quantified truth: every claim is measurable."
    ],
    "copyright": "© 2026 Positive Change Institute LLC — All Systems, Divisions, Engines, Motifs, Insignias, and Products Are the Exclusive Property of Positive Change Institute LLC."
}

# ============================================================
# 2. WHOP PROGRAM MODEL + REGISTRY
# ============================================================

class Program(BaseModel):
    name: str
    who: str
    what: str
    where: str
    why: str
    how: str
    outcome_metric: str
    whop_url: str
    price: str
    tier: int

PROGRAMS: List[Program] = [
    Program(
        name="Credit Architecture Foundations",
        who="Individual Sovereign",
        what="Credit Architecture",
        where="US Credit",
        why="Escape fragility",
        how="Guided workflows + templates",
        outcome_metric="Credit readiness score + limit potential",
        whop_url="https://whop.com/credit-architecture-foundations",
        price="$49",
        tier=1
    ),
    Program(
        name="Income Systems Engine",
        who="Founder/Operator",
        what="Income Systems",
        where="Hybrid",
        why="Scale safely",
        how="Playbooks + automations",
        outcome_metric="Income stability index",
        whop_url="https://whop.com/income-systems-engine",
        price="$149",
        tier=2
    ),
    Program(
        name="Sovereign Ops Stack",
        who="Founder/Operator",
        what="Operational Stack",
        where="Hybrid",
        why="Build resilience",
        how="Operational workflows + system templates",
        outcome_metric="Operational maturity score",
        whop_url="https://whop.com/sovereign-ops-stack",
        price="$299",
        tier=3
    ),
    Program(
        name="Omega Quant Elite",
        who="Enterprise/Family Office",
        what="Sovereign Protection",
        where="Global Crypto",
        why="Protect legacy",
        how="Labs + custom orchestration",
        outcome_metric="Sovereign protection index",
        whop_url="https://whop.com/omega-quant-elite",
        price="$997",
        tier=4
    ),
]

# ============================================================
# 3. PROMETHEUS ENGINE – USER STATE + SCORING + ROUTING
# ============================================================

class UserState(BaseModel):
    role: str              # individual | founder | enterprise
    region: str            # us | global | hybrid
    credit_level: Optional[int] = None
    income_stability: Optional[int] = None
    ops_maturity: Optional[int] = None
    protection_level: Optional[int] = None

class Score(BaseModel):
    readiness: int
    sovereignty: int
    overall: int

class Recommendation(BaseModel):
    score: Score
    recommended_programs: List[Program]
    narrative: str
    next_action: str

def compute_score(state: UserState) -> Score:
    base = 50
    credit = state.credit_level or base
    income = state.income_stability or base
    ops = state.ops_maturity or base
    protection = state.protection_level or base

    readiness = int((credit + income) / 2)
    sovereignty = int((ops + protection) / 2)
    overall = int((readiness + sovereignty) / 2)

    return Score(readiness=readiness, sovereignty=sovereignty, overall=overall)

def match_programs(state: UserState, score: Score) -> List[Program]:
    role_map = {
        "individual": "Individual Sovereign",
        "founder": "Founder/Operator",
        "enterprise": "Enterprise/Family Office",
    }
    region_map = {
        "us": "US Credit",
        "global": "Global Crypto",
        "hybrid": "Hybrid",
    }

    target_who = role_map.get(state.role.lower())
    target_where = region_map.get(state.region.lower())

    matches = [
        p for p in PROGRAMS
        if p.who == target_who or p.where == target_where
    ]

    if not matches:
        matches = PROGRAMS

    # Score-based routing
    if score.readiness < 50:
        return [p for p in matches if p.tier <= 2] or matches[:2]

    if score.sovereignty < 50:
        return [p for p in matches if "Ops" in p.name or "Income" in p.name] or matches

    if score.overall > 75:
        return [p for p in matches if p.tier >= 3] or matches[-2:]

    return matches

def build_narrative(score: Score, role: str) -> str:
    readiness_assessment = "strong" if score.readiness > 60 else "developing" if score.readiness > 40 else "foundational"
    sovereignty_assessment = "established" if score.sovereignty > 60 else "emerging" if score.sovereignty > 40 else "nascent"
    
    return (
        f"Your sovereign profile: readiness ({readiness_assessment}), sovereignty ({sovereignty_assessment}). "
        f"Prometheus maps credit, income, ops, and protection into a unified stack. "
        f"Recommended pathway increases your sovereign index and moves measurable metrics forward."
    )

# ============================================================
# 4. FASTAPI RUNTIME
# ============================================================

app = FastAPI(
    title="PCI / Prometheus Sovereign Stack Runtime",
    description="Full operational runtime for identity, doctrine, programs, assessment, scoring, and routing.",
    version="1.0.0",
)

@app.get("/")
def root():
    return {
        "service": "PCI / Prometheus Sovereign Stack Runtime",
        "status": "🜂 Online",
        "endpoints": {
            "identity": "/identity",
            "doctrine": "/doctrine",
            "programs": "/programs",
            "assess": "/assess (POST)",
            "route": "/route (POST)"
        },
        "founder": "Christopher S. Rowland Sr.",
        "company": "Positive Change Institute LLC",
        "copyright": "© 2026 Positive Change Institute LLC"
    }

@app.get("/identity", response_model=Identity)
def get_identity():
    return PCI_IDENTITY

@app.get("/doctrine")
def get_doctrine():
    return DOCTRINE

@app.get("/programs", response_model=List[Program])
def get_programs():
    return PROGRAMS

@app.post("/assess", response_model=Recommendation)
def assess(state: UserState):
    score = compute_score(state)
    programs = match_programs(state, score)
    narrative = build_narrative(score, state.role)
    next_action = f"Explore {programs[0].name}" if programs else "Contact support"
    return Recommendation(
        score=score,
        recommended_programs=programs,
        narrative=narrative,
        next_action=next_action
    )

@app.post("/route")
def route(state: UserState):
    score = compute_score(state)
    programs = match_programs(state, score)
    primary = programs[0] if programs else PROGRAMS[0]
    return {
        "assessment_complete": True,
        "score": score.dict(),
        "recommended_program": {
            "name": primary.name,
            "price": primary.price,
            "tier": primary.tier,
            "whop_url": primary.whop_url
        },
        "next_action": f"Visit {primary.whop_url}",
        "message": "Sovereign pathway activated. Your progression is now tracked."
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Prometheus Sovereign Stack",
        "uptime": "continuous",
        "doctrine_enforcement": "active",
        "program_registry": f"{len(PROGRAMS)} programs online"
    }

# ============================================================
# 5. UVICORN ENTRYPOINT
# ============================================================

if __name__ == "__main__":
    import uvicorn
    print("\n🜂 PCI / Prometheus Sovereign Stack Runtime")
    print("Author: Christopher S. Rowland Sr.")
    print("Company: Positive Change Institute LLC")
    print("\nStarting server at http://0.0.0.0:8000")
    print("Press CTRL+C to stop.\n")
    uvicorn.run(
        "omega_quant:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
