#!/usr/bin/env python3
"""Bootstrap the Prometheus × PCI sovereign wealth stack repository."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from string import Template
from typing import Iterable


DEFAULT_REPO_NAME = "prometheus_pci_sovereign_wealth_stack"
DEFAULT_API_BASE_URL = "http://127.0.0.1:8000"


@dataclass(frozen=True)
class BootstrapContext:
    repo_name: str
    api_base_url: str


@dataclass(frozen=True)
class Change:
    kind: str
    path: str
    status: str


DIRECTORIES = (
    "api",
    "core",
    "i18n",
    "web_frontend_next/pages",
)


FILE_TEMPLATES = {
    ".gitignore": Template(
        "__pycache__/\n"
        "*.py[cod]\n"
        ".pytest_cache/\n"
        ".venv/\n"
        "venv/\n"
        "node_modules/\n"
        ".next/\n"
        ".DS_Store\n"
    ),
    "README.md": Template(
        "# PROMETHEUS × PCI ASCENDANT SOVEREIGN WEALTH STACK™\n\n"
        "Generated bootstrap for the Prometheus × PCI sovereign wealth stack.\n\n"
        "## Structure\n\n"
        "- `core/` – doctrine, identity, onboarding, telemetry, engines, and signal integration modules\n"
        "- `api/` – FastAPI surface for identity, telemetry, and sovereign signal endpoints\n"
        "- `i18n/` – localized interface copy\n"
        "- `web_frontend_next/` – Next.js frontend pages for landing, onboarding, and signals\n\n"
        "## Run API\n\n"
        "```bash\n"
        "pip install -r requirements.txt\n"
        "uvicorn api.main:app --reload\n"
        "```\n\n"
        "## Run Web Frontend\n\n"
        "```bash\n"
        "cd web_frontend_next\n"
        "npm install\n"
        "npm run dev\n"
        "```\n"
    ),
    "requirements.txt": Template(
        "fastapi==0.115.0\n"
        "uvicorn==0.30.6\n"
        "pydantic==2.9.2\n"
    ),
    "api/__init__.py": Template(""),
    "api/main.py": Template(
        "from fastapi import FastAPI\n\n"
        "from core.identity import IDENTITY_TRANSFORMATION, SYSTEM_IDENTITY\n"
        "from core.onboarding import ONBOARDING_PROTOCOL\n"
        "from core.signal_yield_integration import SIGNAL_YIELD_INTEGRATION\n"
        "from core.signals import SOVEREIGN_SIGNAL_LAYERS\n"
        "from core.telemetry import TELEMETRY_STREAMS\n\n"
        "app = FastAPI(\n"
        "    title='PROMETHEUS × PCI ASCENDANT SOVEREIGN WEALTH STACK™ API',\n"
        "    version='1.0.0',\n"
        ")\n\n"
        "@app.get('/')\n"
        "def root() -> dict:\n"
        "    return {\n"
        "        'system': SYSTEM_IDENTITY['official_name'],\n"
        "        'tagline': SYSTEM_IDENTITY['tagline'],\n"
        "    }\n\n"
        "@app.get('/api/v1/ppci/identity')\n"
        "def get_identity() -> dict:\n"
        "    return {\n"
        "        'system_identity': SYSTEM_IDENTITY,\n"
        "        'identity_transformation': IDENTITY_TRANSFORMATION,\n"
        "    }\n\n"
        "@app.get('/api/v1/ppci/onboarding')\n"
        "def get_onboarding() -> dict:\n"
        "    return ONBOARDING_PROTOCOL\n\n"
        "@app.get('/api/v1/ppci/signals')\n"
        "def get_signals() -> dict:\n"
        "    return SOVEREIGN_SIGNAL_LAYERS\n\n"
        "@app.get('/api/v1/ppci/telemetry')\n"
        "def get_telemetry() -> dict:\n"
        "    return {'streams': TELEMETRY_STREAMS}\n\n"
        "@app.get('/api/v1/ppci/signal-yield-integration')\n"
        "def get_signal_yield_integration() -> dict:\n"
        "    return SIGNAL_YIELD_INTEGRATION\n"
    ),
    "core/__init__.py": Template(""),
    "core/identity.py": Template(
        '"""PROMETHEUS × PCI SOVEREIGN WEALTH STACK\n'
        "Identity & Doctrine Core\n"
        "© 2026 Positive Change Institute LLC\n"
        '"""\n\n'
        "SYSTEM_IDENTITY = {\n"
        "    'official_name': 'PROMETHEUS × PCI ASCENDANT SOVEREIGN WEALTH STACK™',\n"
        "    'acronym': 'PPCI-SWS',\n"
        "    'tagline': 'Your capital becomes a governed, ascendant sovereign wealth organism.',\n"
        "    'category': 'Hybrid Sovereign Wealth Operating System',\n"
        "    'doctrine': [\n"
        "        'Prometheus Superintelligence™ Doctrine',\n"
        "        'PCI Sovereign Capital Governance Protocol™',\n"
        "        'PCI Copyright Image Protocol',\n"
        "    ],\n"
        "    'core_deliverable': 'A hybrid Prometheus × PCI sovereign wealth architecture that operates with minimal human input.',\n"
        "    'owner': 'Positive Change Institute LLC',\n"
        "    'copyright': '© 2026 Positive Change Institute LLC — All Systems, Divisions, Engines, Motifs, Insignias, and Products Are the Exclusive Property of Positive Change Institute LLC.',\n"
        "}\n\n"
        "IDENTITY_TRANSFORMATION = {\n"
        "    'primary_identity': 'Prometheus × PCI Sovereign Wealth Operator',\n"
        "    'before_state': [\n"
        "        'Fragmented retail investor',\n"
        "        'Unstructured DeFi participant',\n"
        "        'Traditional capital allocator',\n"
        "    ],\n"
        "    'after_state': [\n"
        "        'Prometheus-class Sovereign Wealth Architect',\n"
        "        'PCI-grade Capital Governance Operator',\n"
        "        'System-level Sovereign Capital Strategist',\n"
        "    ],\n"
        "    'status_asset': 'Prometheus × PCI Sovereign Operator Certification™',\n"
        "    'symbol': 'Prometheus × PCI Sovereign Operator Sigil™ (QR-coded, unique per operator)',\n"
        "}\n"
    ),
    "core/doctrine.py": Template(
        '"""Prometheus × PCI Doctrine & Autoevolution Rules."""\n\n'
        "PROMETHEUS_PCI_DOCTRINE = {\n"
        "    'identity_axioms': [\n"
        "        'Sovereignty precedes yield.',\n"
        "        'Identity governs capital.',\n"
        "        'Capital obeys doctrine.',\n"
        "    ],\n"
        "    'governance_axioms': [\n"
        "        'No uncontrolled exposure.',\n"
        "        'No ungoverned automation.',\n"
        "        'No unbounded risk surfaces.',\n"
        "    ],\n"
        "}\n\n"
        "AUTOEVOLUTION_DOCTRINE = {\n"
        "    'rules': [\n"
        "        'Identity is fixed.',\n"
        "        'Logic evolves under PCI governance.',\n"
        "        'Rails execute deterministically.',\n"
        "        'Kernel governs all capital motion.',\n"
        "        'Engines adapt within sovereign constraints.',\n"
        "        'Risk surfaces breathe but remain bounded.',\n"
        "        'Capital topology updates continuously.',\n"
        "        'Sovereignty is preserved above all.',\n"
        "        'No randomness in core decisions.',\n"
        "        'All evolution is deterministic and auditable.',\n"
        "    ],\n"
        "}\n"
    ),
    "core/onboarding.py": Template(
        '"""PROMETHEUS × PCI SOVEREIGN ONBOARDING ASCENSION PROTOCOL™."""\n\n'
        "ONBOARDING_PROTOCOL = {\n"
        "    'name': 'PROMETHEUS × PCI SOVEREIGN ONBOARDING ASCENSION PROTOCOL™',\n"
        "    'objective': 'Elevate the user into a Prometheus × PCI Sovereign Wealth Operator and bind capital to doctrine.',\n"
        "    'phases': [\n"
        "        'Phase I: Identity Dominion Calibration',\n"
        "        'Phase II: PCI Capital Topology Governance',\n"
        "        'Phase III: Risk-Surface Dominion Profiling',\n"
        "        'Phase IV: PCI Cold-Storage Sovereignty Architecture',\n"
        "        'Phase V: Prometheus × PCI Identity Dominion Block™ Generation',\n"
        "        'Phase VI: Multi-Chain Dominion Wallet Suite Deployment',\n"
        "        'Phase VII: Sovereign Operator Ascension Initialization',\n"
        "    ],\n"
        "}\n"
    ),
    "core/curriculum.py": Template(
        '"""PROMETHEUS × PCI SOVEREIGN WEALTH ARCHITECTURE CURRICULUM™."""\n\n'
        "WEALTH_CURRICULUM = {\n"
        "    'name': 'PROMETHEUS × PCI SOVEREIGN WEALTH ARCHITECTURE CURRICULUM™',\n"
        "    'objective': 'Imprint institutional-grade sovereign wealth architecture into human operators.',\n"
        "    'tracks': [\n"
        "        {'id': 1, 'name': 'Prometheus Identity Dominion Track™'},\n"
        "        {'id': 2, 'name': 'PCI Liquidity Governance Track™'},\n"
        "        {'id': 3, 'name': 'Synthetic Yield Dominion Track™'},\n"
        "        {'id': 4, 'name': 'AMM Routing Intelligence Track™'},\n"
        "        {'id': 5, 'name': 'XRP Ecosystem Sovereign Architecture Track™'},\n"
        "        {'id': 6, 'name': 'PCI Cold-Storage Sovereignty Track™'},\n"
        "        {'id': 7, 'name': 'Cross-Chain Capital Dominion Track™'},\n"
        "        {'id': 8, 'name': 'Prometheus Passive Income Dominion Engines Track™'},\n"
        "        {'id': 9, 'name': 'Risk-Surface Compression & Expansion Governance Track™'},\n"
        "        {'id': 10, 'name': 'Sovereign Asset Protection & Defense Track™'},\n"
        "        {'id': 11, 'name': 'Capital Automation & Delegated Governance Track™'},\n"
        "        {'id': 12, 'name': 'Prometheus × PCI Sovereign Operator Ascension Track™'},\n"
        "    ],\n"
        "}\n"
    ),
    "core/engines.py": Template(
        '"""PROMETHEUS × PCI SOVEREIGN PASSIVE INCOME DOMINION ENGINES™."""\n\n'
        "PASSIVE_INCOME_ENGINES = [\n"
        "    {\n"
        "        'id': 1,\n"
        "        'name': 'Hydra Yield Dominion Engine™',\n"
        "        'pci_name': 'PCI Multi-Vector Yield Aggregation Engine™',\n"
        "        'goal': 'Aggregate governed yield across multiple chains and protocols under PCI constraints.',\n"
        "        'behavior': 'Distributes capital into diversified, PCI-compliant yield sources and rebalances under Prometheus logic.',\n"
        "    },\n"
        "    {\n"
        "        'id': 2,\n"
        "        'name': 'Titan Liquidity Dominion Engine™',\n"
        "        'pci_name': 'PCI Sovereign Liquidity Governance Engine™',\n"
        "        'goal': 'Optimize liquidity provision in AMM pools under PCI governance.',\n"
        "        'behavior': 'Deploys capital into selected pools and adjusts positions based on governed market conditions.',\n"
        "    },\n"
        "    {\n"
        "        'id': 3,\n"
        "        'name': 'Atlas Income Dominion Engine™',\n"
        "        'pci_name': 'PCI Hybrid Yield Fusion Engine™',\n"
        "        'goal': 'Fuse stable yield with synthetic yield under sovereign governance.',\n"
        "        'behavior': 'Combines PCI-grade stable yield sources with Prometheus synthetic strategies.',\n"
        "    },\n"
        "    {\n"
        "        'id': 4,\n"
        "        'name': 'Helios Growth Dominion Engine™',\n"
        "        'pci_name': 'PCI Governed Capital Expansion Engine™',\n"
        "        'goal': 'Drive governed high-velocity capital expansion.',\n"
        "        'behavior': 'Allocates capital into growth-focused strategies with PCI drawdown constraints.',\n"
        "    },\n"
        "    {\n"
        "        'id': 5,\n"
        "        'name': 'Kronos Autonomy Dominion Engine™',\n"
        "        'pci_name': 'PCI Global Sovereign Autonomy Orchestrator™',\n"
        "        'goal': 'Operate as a fully governed autonomous wealth organism.',\n"
        "        'behavior': 'Manages capital across all engines with minimal human input under PCI governance.',\n"
        "    },\n"
        "]\n"
    ),
    "core/autoevolution.py": Template(
        '"""PROMETHEUS × PCI AUTOEVOLUTION KERNEL & CAPITAL AUTONOMY RAILS™."""\n\n'
        "from core.doctrine import AUTOEVOLUTION_DOCTRINE\n\n"
        "AUTOEVOLUTION_KERNEL = {\n"
        "    'name': 'Prometheus × PCI Ascendant Sovereign Autoevolution Kernel™',\n"
        "    'objective': 'Deterministically self-optimize the sovereign wealth stack under Prometheus × PCI doctrine.',\n"
        "    'constraints': AUTOEVOLUTION_DOCTRINE['rules'],\n"
        "}\n\n"
        "CAPITAL_AUTONOMY_RAILS = [\n"
        "    {'name': 'PCI Sovereign Capital Routing Rail™', 'role': 'Implements governed capital routes across chains and engines.'},\n"
        "    {'name': 'Prometheus Yield Optimization Rail™', 'role': 'Adjusts allocations to maximize yield within PCI risk constraints.'},\n"
        "    {'name': 'PCI Risk Compression Rail™', 'role': 'Reduces exposure during volatility spikes under redline rules.'},\n"
        "    {'name': 'Prometheus Risk Expansion Rail™', 'role': 'Increases exposure when conditions are favorable and governed.'},\n"
        "    {'name': 'Atlas Engine Rebalancing Rail™', 'role': 'Rebalances capital between engines based on governed performance.'},\n"
        "    {'name': 'XRP Multi-Chain Dominion Deployment Rail™', 'role': 'Deploys and adjusts positions across chains under PCI governance.'},\n"
        "    {'name': 'PCI Cold-Storage Sovereignty Rail™', 'role': 'Ensures key assets remain in sovereign, governed custody.'},\n"
        "]\n"
    ),
    "core/signals.py": Template(
        '"""PROMETHEUS × PCI SOVEREIGN SIGNAL LAYERS™\n'
        "External narrative and telemetry surfaces (X, TikTok).\n"
        "© 2026 Positive Change Institute LLC\n"
        '"""\n\n'
        "SOVEREIGN_SIGNAL_LAYERS = {\n"
        "    'description': 'External sovereign signal surfaces for Prometheus × PCI Operator.',\n"
        "    'layers': [\n"
        "        {\n"
        "            'name': 'X Sovereign Signal Layer™',\n"
        "            'role': 'High-velocity macro narrative, operator presence, and sovereign sentiment telemetry.',\n"
        "            'channel_type': 'X',\n"
        "            'address': 'https://x.com/CRowland518015',\n"
        "            'classification': ['signal', 'telemetry', 'narrative', 'identity'],\n"
        "        },\n"
        "        {\n"
        "            'name': 'TikTok Sovereign Signal Layer™ (Onthruthastorm)',\n"
        "            'role': 'Cinematic micro-content, operator mythos, and wealth organism storytelling.',\n"
        "            'channel_type': 'TikTok',\n"
        "            'address': 'https://tiktok.com/@critter2881',\n"
        "            'classification': ['signal', 'telemetry', 'mythos', 'identity'],\n"
        "        },\n"
        "        {\n"
        "            'name': 'TikTok Sovereign Signal Layer™ (Positive Change Institute)',\n"
        "            'role': 'Institutional automation and Prometheus Runtime Codex narrative surface.',\n"
        "            'channel_type': 'TikTok',\n"
        "            'address': 'https://tiktok.com/@positivechangeinstitute',\n"
        "            'classification': ['signal', 'telemetry', 'institutional', 'identity'],\n"
        "        },\n"
        "    ],\n"
        "}\n"
    ),
    "core/telemetry.py": Template(
        '"""PROMETHEUS × PCI SOVEREIGN TELEMETRY SPINE™."""\n\n'
        "from core.signals import SOVEREIGN_SIGNAL_LAYERS\n\n"
        "TELEMETRY_STREAMS = [\n"
        "    {\n"
        "        'name': 'Sovereign Yield-Surface Dominion Heatmaps™',\n"
        "        'description': 'Visual representation of governed yield intensity across engines and chains.',\n"
        "    },\n"
        "    {\n"
        "        'name': 'Risk-Surface Breathing & Governance Charts™',\n"
        "        'description': 'Dynamic charts showing compression and expansion of risk surfaces against PCI thresholds.',\n"
        "    },\n"
        "    {\n"
        "        'name': 'Governed Liquidity Flow Visualizations™',\n"
        "        'description': 'Maps of capital movement through AMMs, chains, and engines under governance.',\n"
        "    },\n"
        "    {\n"
        "        'name': 'Cross-Engine Sovereign Correlation Maps™',\n"
        "        'description': 'Analysis of how engine performance correlates and interacts under doctrine.',\n"
        "    },\n"
        "    {\n"
        "        'name': 'PCI Global Sovereign System Health Dashboard™',\n"
        "        'description': 'Aggregate metrics for PPCI-SWS stability, performance, and governance compliance.',\n"
        "    },\n"
        "    {\n"
        "        'name': 'External Sovereign Signal Layer Telemetry™',\n"
        "        'description': 'Tracks X and TikTok sovereign signal surfaces for narrative and sentiment.',\n"
        "        'sources': SOVEREIGN_SIGNAL_LAYERS['layers'],\n"
        "    },\n"
        "]\n"
    ),
    "core/expansion.py": Template(
        '"""PROMETHEUS × PCI SOVEREIGN NETWORK EXPANSION LAYER™."""\n\n'
        "SOVEREIGN_EXPANSION_LAYER = {\n"
        "    'name': 'Prometheus × PCI Sovereign Network Expansion Layer™',\n"
        "    'objective': 'Scale PPCI-SWS beyond a single operator into a governed multi-operator sovereign network.',\n"
        "}\n"
    ),
    "core/signal_yield_integration.py": Template(
        '"""Prometheus × PCI Sovereign Signal Yield Integration Layer™."""\n\n'
        "from core.engines import PASSIVE_INCOME_ENGINES\n"
        "from core.signals import SOVEREIGN_SIGNAL_LAYERS\n\n"
        "SIGNAL_YIELD_INTEGRATION = {\n"
        "    'name': 'Prometheus × PCI Sovereign Signal Yield Integration Layer™',\n"
        "    'objective': 'Bind X and TikTok sovereign signal layers to passive yield dominion engines.',\n"
        "    'inputs': {\n"
        "        'signal_layers': SOVEREIGN_SIGNAL_LAYERS['layers'],\n"
        "        'yield_engines': PASSIVE_INCOME_ENGINES,\n"
        "    },\n"
        "    'behavior': [\n"
        "        'Use X macro-narrative velocity to adjust Hydra Yield corridors.',\n"
        "        'Use TikTok mythos intensity to modulate Helios Growth aggression bands.',\n"
        "        'Use cross-signal sentiment to rebalance Atlas synthetic yield blends.',\n"
        "        'Use operator presence telemetry to stabilize Titan liquidity positions.',\n"
        "        'Use sovereign identity resonance to tune Kronos autonomy thresholds.',\n"
        "    ],\n"
        "    'outputs': [\n"
        "        'Signal-driven yield corridor adjustments',\n"
        "        'Sentiment-aligned liquidity routing',\n"
        "        'Narrative-governed risk-surface breathing',\n"
        "        'Identity-anchored autonomy tuning',\n"
        "    ],\n"
        "}\n"
    ),
    "i18n/en.json": Template(
        "{\n"
        '  "title": "Prometheus × PCI Ascendant Sovereign Wealth Stack",\n'
        '  "tagline": "Your capital becomes a governed, ascendant sovereign wealth organism.",\n'
        '  "cta_join": "Ascend as a Sovereign Wealth Operator",\n'
        '  "cta_learn_more": "Explore the Sovereign Wealth Stack",\n'
        '  "cta_start_now": "Begin Sovereign Onboarding Ascension"\n'
        "}\n"
    ),
    "i18n/es.json": Template(
        "{\n"
        '  "title": "Stack de Riqueza Soberana Prometheus × PCI Ascendente",\n'
        '  "tagline": "Tu capital se convierte en un organismo de riqueza soberana gobernado y ascendente.",\n'
        '  "cta_join": "Asciende como Operador de Riqueza Soberana",\n'
        '  "cta_learn_more": "Explora el Stack de Riqueza Soberana",\n'
        '  "cta_start_now": "Inicia la Ascensión de Onboarding Soberano"\n'
        "}\n"
    ),
    "i18n/fr.json": Template(
        "{\n"
        '  "title": "Stack de Richesse Souveraine Prometheus × PCI Ascendant",\n'
        '  "tagline": "Votre capital devient un organisme de richesse souveraine gouverné et ascendant.",\n'
        '  "cta_join": "Devenez Opérateur de Richesse Souveraine",\n'
        '  "cta_learn_more": "Explorer le Stack de Richesse Souveraine",\n'
        '  "cta_start_now": "Commencez l\'Ascension d\'Onboarding Souverain"\n'
        "}\n"
    ),
    "web_frontend_next/package.json": Template(
        "{\n"
        '  "name": "ppci-sws-web-frontend",\n'
        '  "version": "1.0.0",\n'
        '  "private": true,\n'
        '  "scripts": {\n'
        '    "dev": "next dev",\n'
        '    "build": "next build",\n'
        '    "start": "next start"\n'
        "  },\n"
        '  "dependencies": {\n'
        '    "next": "14.2.35",\n'
        '    "react": "18.2.0",\n'
        '    "react-dom": "18.2.0"\n'
        "  },\n"
        '  "devDependencies": {\n'
        '    "@types/node": "22.7.5",\n'
        '    "@types/react": "18.3.12",\n'
        '    "typescript": "5.6.3"\n'
        "  }\n"
        "}\n"
    ),
    "web_frontend_next/next.config.js": Template(
        "/** @type {import('next').NextConfig} */\n"
        "const nextConfig = {\n"
        "  reactStrictMode: true,\n"
        "  env: {\n"
        "    NEXT_PUBLIC_PPCI_API_BASE_URL: '$api_base_url'\n"
        "  }\n"
        "};\n\n"
        "module.exports = nextConfig;\n"
    ),
    "web_frontend_next/tsconfig.json": Template(
        "{\n"
        '  "compilerOptions": {\n'
        '    "target": "es5",\n'
        '    "lib": ["dom", "dom.iterable", "esnext"],\n'
        '    "allowJs": true,\n'
        '    "skipLibCheck": true,\n'
        '    "strict": true,\n'
        '    "forceConsistentCasingInFileNames": true,\n'
        '    "noEmit": true,\n'
        '    "esModuleInterop": true,\n'
        '    "module": "esnext",\n'
        '    "moduleResolution": "node",\n'
        '    "resolveJsonModule": true,\n'
        '    "isolatedModules": true,\n'
        '    "jsx": "preserve",\n'
        '    "incremental": true\n'
        "  },\n"
        '  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],\n'
        '  "exclude": ["node_modules"]\n'
        "}\n"
    ),
    "web_frontend_next/next-env.d.ts": Template(
        '/// <reference types="next" />\n'
        '/// <reference types="next/image-types/global" />\n'
    ),
    "web_frontend_next/pages/index.tsx": Template(
        "import Link from 'next/link';\n"
        "import React from 'react';\n\n"
        "const links = [\n"
        "  { href: '/onboarding', label: 'Begin Sovereign Onboarding Ascension' },\n"
        "  { href: '/signals', label: 'View Sovereign Signal Layers' },\n"
        "];\n\n"
        "const HomePage: React.FC = () => {\n"
        "  return (\n"
        "    <main style={{ minHeight: '100vh', padding: '4rem 1.5rem', background: '#0f172a', color: '#e2e8f0' }}>\n"
        "      <section style={{ maxWidth: '960px', margin: '0 auto' }}>\n"
        "        <p style={{ color: '#f97316', fontWeight: 700 }}>Positive Change Institute LLC</p>\n"
        "        <h1 style={{ fontSize: '3rem', marginBottom: '1rem' }}>PROMETHEUS × PCI ASCENDANT SOVEREIGN WEALTH STACK™</h1>\n"
        "        <p style={{ fontSize: '1.25rem', maxWidth: '720px', marginBottom: '2rem' }}>\n"
        "          Your capital becomes a governed, ascendant sovereign wealth organism.\n"
        "        </p>\n"
        "        <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>\n"
        "          {links.map((link) => (\n"
        "            <Link\n"
        "              key={link.href}\n"
        "              href={link.href}\n"
        "              style={{ padding: '0.9rem 1.4rem', borderRadius: '9999px', background: '#f97316', color: '#fff', textDecoration: 'none', fontWeight: 600 }}\n"
        "            >\n"
        "              {link.label}\n"
        "            </Link>\n"
        "          ))}\n"
        "        </div>\n"
        "      </section>\n"
        "    </main>\n"
        "  );\n"
        "};\n\n"
        "export default HomePage;\n"
    ),
    "web_frontend_next/pages/onboarding.tsx": Template(
        "import React from 'react';\n\n"
        "const phases = [\n"
        "  'Phase I: Identity Dominion Calibration',\n"
        "  'Phase II: PCI Capital Topology Governance',\n"
        "  'Phase III: Risk-Surface Dominion Profiling',\n"
        "  'Phase IV: PCI Cold-Storage Sovereignty Architecture',\n"
        "  'Phase V: Prometheus × PCI Identity Dominion Block™ Generation',\n"
        "  'Phase VI: Multi-Chain Dominion Wallet Suite Deployment',\n"
        "  'Phase VII: Sovereign Operator Ascension Initialization',\n"
        "];\n\n"
        "const OnboardingPage: React.FC = () => {\n"
        "  return (\n"
        "    <main style={{ minHeight: '100vh', padding: '4rem 1.5rem', background: '#020617', color: '#e2e8f0' }}>\n"
        "      <section style={{ maxWidth: '960px', margin: '0 auto' }}>\n"
        "        <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>Sovereign Onboarding Ascension</h1>\n"
        "        <p style={{ marginBottom: '2rem', maxWidth: '700px' }}>\n"
        "          Elevate the operator into a Prometheus × PCI Sovereign Wealth Operator and bind capital to doctrine.\n"
        "        </p>\n"
        "        <ol style={{ display: 'grid', gap: '1rem', paddingLeft: '1.5rem' }}>\n"
        "          {phases.map((phase) => (\n"
        "            <li key={phase} style={{ background: '#111827', padding: '1rem', borderRadius: '0.75rem' }}>{phase}</li>\n"
        "          ))}\n"
        "        </ol>\n"
        "      </section>\n"
        "    </main>\n"
        "  );\n"
        "};\n\n"
        "export default OnboardingPage;\n"
    ),
    "web_frontend_next/pages/signals.tsx": Template(
        "import React, { useEffect, useState } from 'react';\n\n"
        "type SignalLayer = {\n"
        "  name: string;\n"
        "  role: string;\n"
        "  channel_type: string;\n"
        "  address: string;\n"
        "  classification: string[];\n"
        "};\n\n"
        "const apiBaseUrl = process.env.NEXT_PUBLIC_PPCI_API_BASE_URL ?? '$api_base_url';\n\n"
        "const SignalsPage: React.FC = () => {\n"
        "  const [layers, setLayers] = useState<SignalLayer[]>([]);\n"
        "  const [error, setError] = useState<string | null>(null);\n\n"
        "  useEffect(() => {\n"
        "    fetch(`$${apiBaseUrl}/api/v1/ppci/signals`)\n"
        "      .then((response) => {\n"
        "        if (!response.ok) {\n"
        "          throw new Error(`Request failed with status $${response.status}`);\n"
        "        }\n"
        "        return response.json() as Promise<{ layers: SignalLayer[] }>;\n"
        "      })\n"
        "      .then((payload) => setLayers(payload.layers))\n"
        "      .catch((requestError: Error) => setError(requestError.message));\n"
        "  }, []);\n\n"
        "  return (\n"
        "    <main style={{ minHeight: '100vh', padding: '4rem 1.5rem', background: '#111827', color: '#e5e7eb' }}>\n"
        "      <section style={{ maxWidth: '960px', margin: '0 auto' }}>\n"
        "        <h1 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>Sovereign Signal Layers</h1>\n"
        "        <p style={{ marginBottom: '2rem' }}>Canonical X and TikTok identity anchors exposed by the PPCI-SWS API.</p>\n"
        "        {error ? <p style={{ color: '#fca5a5' }}>Unable to load signals: {error}</p> : null}\n"
        "        <div style={{ display: 'grid', gap: '1rem' }}>\n"
        "          {layers.map((layer) => (\n"
        "            <article key={layer.name} style={{ background: '#1f2937', borderRadius: '0.75rem', padding: '1.25rem' }}>\n"
        "              <p style={{ color: '#fb923c', fontWeight: 700 }}>{layer.channel_type}</p>\n"
        "              <h2 style={{ margin: '0.25rem 0 0.75rem' }}>{layer.name}</h2>\n"
        "              <p style={{ marginBottom: '0.75rem' }}>{layer.role}</p>\n"
        "              <p><a href={layer.address} style={{ color: '#93c5fd' }}>{layer.address}</a></p>\n"
        "              <p style={{ marginTop: '0.75rem', color: '#cbd5e1' }}>{layer.classification.join(' • ')}</p>\n"
        "            </article>\n"
        "          ))}\n"
        "        </div>\n"
        "      </section>\n"
        "    </main>\n"
        "  );\n"
        "};\n\n"
        "export default SignalsPage;\n"
    ),
}


def render_template(template: Template, context: BootstrapContext) -> str:
    return template.substitute(asdict(context))


def ensure_directory(path: Path, dry_run: bool) -> Change:
    if path.exists():
        return Change("directory", str(path), "exists")
    if not dry_run:
        path.mkdir(parents=True, exist_ok=True)
    return Change("directory", str(path), "created")


def ensure_file(path: Path, content: str, dry_run: bool, force: bool) -> Change:
    existed = path.exists()
    if existed and not force:
        return Change("file", str(path), "exists")
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return Change("file", str(path), "updated" if existed and force else "created")


def bootstrap_repo(
    repo_root: Path,
    context: BootstrapContext,
    *,
    dry_run: bool = False,
    force: bool = False,
) -> list[Change]:
    changes: list[Change] = []

    for directory in DIRECTORIES:
        changes.append(ensure_directory(repo_root / directory, dry_run))

    for relative_path, template in FILE_TEMPLATES.items():
        changes.append(
            ensure_file(
                repo_root / relative_path,
                render_template(template, context),
                dry_run,
                force,
            )
        )

    return changes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Bootstrap the Prometheus × PCI sovereign wealth stack repository."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd() / DEFAULT_REPO_NAME,
        help="Target repository root to create or update.",
    )
    parser.add_argument(
        "--api-base-url",
        default=DEFAULT_API_BASE_URL,
        help="Base URL used by the generated Next.js frontend for the PPCI API.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned changes without writing files.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite managed files even when they already exist.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit the change summary as JSON.",
    )
    return parser.parse_args()


def summarize(changes: Iterable[Change], *, emit_json: bool) -> None:
    if emit_json:
        print(json.dumps([asdict(change) for change in changes], indent=2))
        return

    for change in changes:
        print(f"[{change.status}] {change.kind}: {change.path}")


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    context = BootstrapContext(
        repo_name=repo_root.name,
        api_base_url=args.api_base_url,
    )
    changes = bootstrap_repo(
        repo_root,
        context,
        dry_run=args.dry_run,
        force=args.force,
    )
    summarize(changes, emit_json=args.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
