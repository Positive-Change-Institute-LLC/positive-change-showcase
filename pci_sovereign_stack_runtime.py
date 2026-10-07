"""Prototype assessment and program-routing API for the PCI sovereign stack."""

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field


class Identity(BaseModel):
    founder: str
    company: str
    mission: str
    brands: dict[str, str]


PCI_IDENTITY = Identity(
    founder="Christopher S. Rowland Sr.",
    company="Positive Change Institute LLC",
    mission="Build sovereign systems for credit, income, operations, and protection.",
    brands={
        "prometheus": "Prometheus Superintelligence – central orchestrator",
        "omega_quant": "Omega Quant Authority – sovereign financial architecture",
    },
)

DOCTRINE = {
    "pci_sovereign_standard": [
        "User sovereignty: user owns data, keys, and progression.",
        "Causality: every artifact must move a measurable metric.",
        "Precision: credit, income, ops, and protection are quantified.",
        "Golden Ratio: layout, narrative, and tiering follow φ ≈ 1.618.",
    ],
    "prometheus_principles": [
        "Assess → Score → Route → Orchestrate.",
        "Every decision is deterministic and sovereign-aligned.",
        "Prometheus is the causal engine of PCI.",
    ],
    "omega_quant_principles": [
        "Credit architecture as a sovereign system.",
        "Income systems as scalable infrastructure.",
        "Operational stacks as resilience engines.",
        "Protection as legacy preservation.",
    ],
}


class Program(BaseModel):
    name: str
    who: str
    what: str
    where: str
    why: str
    how: str
    outcome_metric: str
    whop_url: str


PROGRAMS = [
    Program(
        name="Credit Architecture Foundations",
        who="Individual Sovereign",
        what="Credit Architecture",
        where="US Credit",
        why="Escape fragility",
        how="Guided workflows + templates",
        outcome_metric="Credit readiness score + limit potential",
        whop_url="https://whop.com/credit-architecture-foundations",
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
    ),
]


class UserState(BaseModel):
    role: Literal["individual", "founder", "enterprise"]
    region: Literal["us", "global", "hybrid"]
    credit_level: int | None = Field(default=None, ge=0, le=100)
    income_stability: int | None = Field(default=None, ge=0, le=100)
    ops_maturity: int | None = Field(default=None, ge=0, le=100)
    protection_level: int | None = Field(default=None, ge=0, le=100)


class Score(BaseModel):
    readiness: int
    sovereignty: int


class Recommendation(BaseModel):
    score: Score
    recommended_programs: list[Program]
    narrative: str


def compute_score(state: UserState) -> Score:
    base = 50
    credit = state.credit_level if state.credit_level is not None else base
    income = state.income_stability if state.income_stability is not None else base
    ops = state.ops_maturity if state.ops_maturity is not None else base
    protection = state.protection_level if state.protection_level is not None else base

    return Score(
        readiness=int((credit + income) / 2),
        sovereignty=int((ops + protection) / 2),
    )


def match_programs(state: UserState, score: Score) -> list[Program]:
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
    target_who = role_map[state.role]
    target_where = region_map[state.region]
    matches = [
        program
        for program in PROGRAMS
        if program.who == target_who or program.where == target_where
    ]

    if score.readiness < 50:
        return [program for program in matches if "Foundations" in program.name] or matches
    if score.sovereignty > 70:
        return [program for program in matches if "Elite" in program.name] or matches
    return matches


def build_narrative(score: Score) -> str:
    return (
        f"Pain: readiness {score.readiness}, sovereignty {score.sovereignty}. "
        "Pattern: Prometheus maps credit, income, ops, and protection into a sovereign stack. "
        "Power: recommended programs increase your sovereign index."
    )


app = FastAPI(
    title="PCI / Prometheus Sovereign Stack Runtime",
    description=(
        "Prototype runtime for identity, doctrine, program registry, assessment, "
        "scoring, and deterministic program routing."
    ),
    version="1.0.0",
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "PCI / Prometheus Sovereign Stack Runtime Online",
        "identity": "/identity",
        "doctrine": "/doctrine",
        "programs": "/programs",
        "assess": "/assess",
        "route": "/route",
    }


@app.get("/identity", response_model=Identity)
def get_identity() -> Identity:
    return PCI_IDENTITY


@app.get("/doctrine")
def get_doctrine() -> dict[str, list[str]]:
    return DOCTRINE


@app.get("/programs", response_model=list[Program])
def get_programs() -> list[Program]:
    return PROGRAMS


@app.post("/assess", response_model=Recommendation)
def assess(state: UserState) -> Recommendation:
    score = compute_score(state)
    programs = match_programs(state, score)
    return Recommendation(
        score=score,
        recommended_programs=programs,
        narrative=build_narrative(score),
    )


@app.post("/route")
def route(state: UserState) -> dict[str, object]:
    score = compute_score(state)
    primary = match_programs(state, score)[0]
    return {
        "next": "/programs",
        "highlight": primary.name,
        "whop_url": primary.whop_url,
        "score": score.model_dump(),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("pci_sovereign_stack_runtime:app", host="127.0.0.1", port=8000)
