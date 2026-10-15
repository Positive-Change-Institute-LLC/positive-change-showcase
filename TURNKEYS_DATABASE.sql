-- ============================================================
-- PCI TURNKEY DATABASE — COMPLETE 120+ SEED DATA
-- Cloudflare D1 Database Schema + Insert Statements
-- Author: Christopher S. Rowland Sr.
-- Company: Positive Change Institute LLC
-- ============================================================

-- Create main turnkeys table
CREATE TABLE IF NOT EXISTS turnkeys (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  handle TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  description TEXT,
  category TEXT NOT NULL,
  price TEXT NOT NULL,
  is_premium INTEGER DEFAULT 0,
  vendor TEXT DEFAULT 'Positive Change Institute LLC',
  type TEXT DEFAULT 'Digital',
  status TEXT DEFAULT 'active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create categories table
CREATE TABLE IF NOT EXISTS categories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  description TEXT,
  product_count INTEGER DEFAULT 0
);

-- Create pricing tiers table
CREATE TABLE IF NOT EXISTS pricing_tiers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tier_name TEXT NOT NULL,
  tier_level INTEGER NOT NULL,
  min_price REAL,
  max_price REAL
);

-- Insert pricing tiers
INSERT INTO pricing_tiers (tier_name, tier_level, min_price, max_price) VALUES
('Free', 0, 0, 0),
('Starter', 1, 1, 100),
('Professional', 2, 101, 1000),
('Enterprise', 3, 1001, 10000),
('Premium', 4, 10001, 199999);

-- Insert categories
INSERT INTO categories (name, description) VALUES
('Crypto Trading', 'High-frequency and algorithmic trading systems for cryptocurrency'),
('DeFi Protocols', 'Decentralized finance protocols and liquidity systems'),
('Enterprise Blockchain', 'Enterprise-grade blockchain infrastructure and solutions'),
('AI/ML Systems', 'Artificial intelligence and machine learning trading systems'),
('NFT/Gaming', 'NFT marketplaces and blockchain gaming infrastructure'),
('Infrastructure', 'Blockchain infrastructure, APIs, and developer tools'),
('Services', 'Professional consulting and development services'),
('Education', 'Courses, certifications, and educational programs'),
('Bundles', 'Premium product bundles and packages'),
('Academy', 'PCI Counselor Academy certification programs');

-- ============================================================
-- CRYPTO TRADING SYSTEMS (20)
-- ============================================================

INSERT INTO turnkeys (handle, name, description, category, price, is_premium) VALUES
('prometheus-sovereign-intelligence', 'Prometheus Sovereign Intelligence', 'AI-powered crypto trading system with predictive analytics and autonomous execution', 'Crypto Trading', '$4,999', 1),
('quantum-hft-engine', 'Quantum HFT Engine', 'High-frequency trading algorithm with microsecond execution on major exchanges', 'Crypto Trading', '$7,999', 1),
('neural-arbitrage-system', 'Neural Arbitrage System', 'Cross-exchange arbitrage bot using neural network price prediction', 'Crypto Trading', '$3,499', 1),
('crypto-market-maker-pro', 'Crypto Market Maker Pro', 'Automated market making system for liquidity provision on DEXs and CEXs', 'Crypto Trading', '$5,999', 1),
('btc-eth-momentum-trader', 'BTC/ETH Momentum Trader', 'Trend-following algorithm optimized for Bitcoin and Ethereum', 'Crypto Trading', '$1,999', 0),
('grid-trading-bot-suite', 'Grid Trading Bot Suite', 'Multi-level grid trading bot for sideways markets', 'Crypto Trading', '$999', 0),
('scalping-algorithm-v4', 'Scalping Algorithm v4', 'High-frequency scalping bot for volatile altcoin pairs', 'Crypto Trading', '$2,999', 0),
('portfolio-rebalancer', 'Portfolio Rebalancer', 'Automated portfolio rebalancing across 50+ crypto assets', 'Crypto Trading', '$1,499', 0),
('options-trading-framework', 'Options Trading Framework', 'Crypto options trading with delta-neutral strategies', 'Crypto Trading', '$4,499', 1),
('futures-hedging-system', 'Futures Hedging System', 'Automated futures hedging for institutional portfolios', 'Crypto Trading', '$6,499', 1),
('twap-vwap-engine', 'TWAP/VWAP Execution Engine', 'Institutional-grade order execution with minimal slippage', 'Crypto Trading', '$3,999', 1),
('cross-chain-arbitrage', 'Cross-Chain Arbitrage', 'Arbitrage opportunities across Ethereum, Solana, BSC, and Polygon', 'Crypto Trading', '$5,499', 1),
('sentiment-trading-bot', 'Sentiment Trading Bot', 'Trades based on real-time social media and news sentiment analysis', 'Crypto Trading', '$2,499', 0),
('mean-reversion-system', 'Mean Reversion System', 'Statistical arbitrage using mean reversion strategies', 'Crypto Trading', '$1,999', 0),
('crypto-index-fund-builder', 'Crypto Index Fund Builder', 'Create and manage automated crypto index funds', 'Crypto Trading', '$3,499', 1),
('volatility-harvesting-bot', 'Volatility Harvesting Bot', 'Captures premium from volatility spikes across derivatives', 'Crypto Trading', '$4,999', 1),
('pair-trading-algorithm', 'Pair Trading Algorithm', 'Statistical pair trading between correlated crypto assets', 'Crypto Trading', '$2,999', 0),
('market-neutral-strategy', 'Market Neutral Strategy', 'Market-neutral crypto strategy with alpha generation', 'Crypto Trading', '$5,999', 1),
('algorithmic-otc-desk', 'Algorithmic OTC Desk', 'Over-the-counter trading algorithm for large block orders', 'Crypto Trading', '$8,999', 1),
('defi-yield-arbitrage', 'DeFi Yield Arbitrage', 'Cross-protocol yield arbitrage across lending platforms', 'Crypto Trading', '$3,999', 1);

-- ============================================================
-- DEFI PROTOCOLS (20)
-- ============================================================
INSERT INTO turnkeys (handle, name, description, category, price, is_premium) VALUES
('defi-protocol-builder', 'DeFi Protocol Builder', 'Complete DeFi protocol with liquidity pools, staking, and governance', 'DeFi Protocols', '$9,999', 1),
('lending-platform-v3', 'Lending Platform v3', 'Decentralized lending and borrowing platform with variable rates', 'DeFi Protocols', '$7,999', 1),
('automated-market-maker', 'Automated Market Maker', 'Custom AMM with concentrated liquidity and fee tiers', 'DeFi Protocols', '$6,499', 1),
('yield-aggregator-pro', 'Yield Aggregator Pro', 'Auto-compounding yield optimizer across 50+ DeFi protocols', 'DeFi Protocols', '$4,999', 1),
('staking-rewards-engine', 'Staking Rewards Engine', 'Multi-token staking platform with tiered reward structures', 'DeFi Protocols', '$3,499', 1),
('liquidity-manager', 'Liquidity Manager', 'Automated liquidity position management for Uniswap v3', 'DeFi Protocols', '$2,999', 0),
('governance-framework', 'Governance Framework', 'DAO governance system with proposal voting and treasury management', 'DeFi Protocols', '$5,999', 1),
('cross-chain-bridge', 'Cross-Chain Bridge', 'Trustless cross-chain token bridge with validator network', 'DeFi Protocols', '$8,999', 1),
('synthetic-asset-protocol', 'Synthetic Asset Protocol', 'Create and trade synthetic assets pegged to real-world assets', 'DeFi Protocols', '$7,499', 1),
('options-protocol', 'Options Protocol', 'Decentralized options trading with European and American styles', 'DeFi Protocols', '$6,999', 1),
('futures-dex', 'Futures DEX', 'Perpetual futures decentralized exchange with up to 100x leverage', 'DeFi Protocols', '$9,999', 1),
('prediction-market', 'Prediction Market', 'Decentralized prediction market for any future event', 'DeFi Protocols', '$3,999', 1),
('insurance-protocol', 'Insurance Protocol', 'Peer-to-peer insurance for smart contract and protocol risk', 'DeFi Protocols', '$5,499', 1),
('rebase-token-engine', 'Rebase Token Engine', 'Elastic supply token with algorithmic rebasing mechanisms', 'DeFi Protocols', '$2,499', 0),
('vesting-contract-factory', 'Vesting Contract Factory', 'Create custom vesting schedules for tokens and team allocations', 'DeFi Protocols', '$1,499', 0),
('multi-sig-treasury', 'Multi-Sig Treasury', 'Multi-signature treasury management for DAOs and protocols', 'DeFi Protocols', '$2,999', 0),
('flash-loan-arbitrage', 'Flash Loan Arbitrage', 'Flash loan arbitrage bot for DeFi opportunities', 'DeFi Protocols', '$4,499', 1),
('liquidation-bot', 'Liquidation Bot', 'Automated liquidation monitoring and execution for lending protocols', 'DeFi Protocols', '$3,999', 1),
('defi-dashboard', 'DeFi Dashboard', 'Real-time portfolio tracking across all DeFi positions', 'DeFi Protocols', '$1,999', 0),
('yield-curve-strategy', 'Yield Curve Strategy', 'Automated yield curve trading across DeFi maturities', 'DeFi Protocols', '$3,499', 1);

-- ============================================================
-- ENTERPRISE BLOCKCHAIN (15)
-- ============================================================
INSERT INTO turnkeys (handle, name, description, category, price, is_premium) VALUES
('enterprise-baas-platform', 'Enterprise BaaS Platform', 'Complete blockchain infrastructure for enterprise deployment', 'Enterprise Blockchain', '$19,999', 1),
('supply-chain-tracker', 'Supply Chain Tracker', 'End-to-end supply chain tracking with immutable audit trail', 'Enterprise Blockchain', '$14,999', 1),
('asset-tokenization-suite', 'Asset Tokenization Suite', 'Tokenize real-world assets with legal compliance framework', 'Enterprise Blockchain', '$12,999', 1),
('identity-management-system', 'Identity Management System', 'Decentralized identity with KYC/AML compliance', 'Enterprise Blockchain', '$9,999', 1),
('document-notarization', 'Document Notarization', 'Blockchain-based document timestamping and verification', 'Enterprise Blockchain', '$4,999', 1),
('private-blockchain-network', 'Private Blockchain Network', 'Deploy permissioned blockchain networks for enterprise consortia', 'Enterprise Blockchain', '$24,999', 1),
('smart-contract-audit-tool', 'Smart Contract Audit Tool', 'Automated smart contract vulnerability scanning and reporting', 'Enterprise Blockchain', '$6,999', 1),
('compliance-engine', 'Compliance Engine', 'Automated regulatory compliance monitoring and reporting', 'Enterprise Blockchain', '$8,999', 1),
('data-provenance-tracker', 'Data Provenance Tracker', 'Track data lineage and provenance across enterprise systems', 'Enterprise Blockchain', '$7,499', 1),
('tokenization-platform', 'Tokenization Platform', 'End-to-end platform for security token offerings (STOs)', 'Enterprise Blockchain', '$15,999', 1),
('blockchain-explorer', 'Blockchain Explorer', 'Custom blockchain explorer for private and public networks', 'Enterprise Blockchain', '$3,999', 1),
('wallet-infrastructure', 'Wallet Infrastructure', 'Enterprise-grade wallet with multi-sig and hardware support', 'Enterprise Blockchain', '$5,999', 1),
('payment-settlement', 'Payment Settlement', 'Blockchain-based payment settlement and reconciliation', 'Enterprise Blockchain', '$11,999', 1),
('trade-finance-platform', 'Trade Finance Platform', 'Blockchain trade finance with letter of credit automation', 'Enterprise Blockchain', '$16,999', 1),
('carbon-credit-marketplace', 'Carbon Credit Marketplace', 'Blockchain-based carbon credit trading and verification', 'Enterprise Blockchain', '$13,999', 1);

-- ============================================================
-- AI & MACHINE LEARNING (15)
-- ============================================================
INSERT INTO turnkeys (handle, name, description, category, price, is_premium) VALUES
('prometheus-ai-core', 'Prometheus AI Core', 'Core AI engine powering all Prometheus intelligence systems', 'AI/ML Systems', '$9,999', 1),
('neural-price-predictor', 'Neural Price Predictor', 'LSTM neural network for crypto price prediction', 'AI/ML Systems', '$3,499', 1),
('market-sentiment-ai', 'Market Sentiment AI', 'NLP-based market sentiment analysis from news and social media', 'AI/ML Systems', '$2,999', 0),
('anomaly-detection-system', 'Anomaly Detection System', 'Real-time anomaly detection for blockchain transactions', 'AI/ML Systems', '$4,999', 1),
('portfolio-optimizer', 'Portfolio Optimizer', 'AI-powered portfolio optimization using modern portfolio theory', 'AI/ML Systems', '$3,999', 1),
('risk-assessment-engine', 'Risk Assessment Engine', 'Machine learning risk scoring for DeFi protocols and tokens', 'AI/ML Systems', '$5,499', 1),
('pattern-recognition-bot', 'Pattern Recognition Bot', 'Chart pattern recognition using convolutional neural networks', 'AI/ML Systems', '$2,499', 0),
('natural-language-trading', 'Natural Language Trading', 'Execute trades via natural language commands processed by LLM', 'AI/ML Systems', '$4,499', 1),
('fraud-detection-ai', 'Fraud Detection AI', 'Blockchain fraud detection using graph neural networks', 'AI/ML Systems', '$6,999', 1),
('reinforcement-learning-trader', 'Reinforcement Learning Trader', 'RL-based trading agent that learns from market interaction', 'AI/ML Systems', '$7,999', 1),
('gas-price-predictor', 'Gas Price Predictor', 'AI model for predicting Ethereum gas prices and optimal timing', 'AI/ML Systems', '$1,999', 0),
('mev-bot-framework', 'MEV Bot Framework', 'Miner extractable value detection and capture strategies', 'AI/ML Systems', '$5,999', 1),
('on-chain-analytics-ai', 'On-Chain Analytics AI', 'AI-powered on-chain data analysis and wallet clustering', 'AI/ML Systems', '$3,499', 1),
('trading-signal-generator', 'Trading Signal Generator', 'Multi-model ensemble for generating trading signals', 'AI/ML Systems', '$4,999', 1),
('automated-research-agent', 'Automated Research Agent', 'AI agent that researches and summarizes crypto projects', 'AI/ML Systems', '$2,999', 0);

-- ============================================================
-- NFT & GAMING (15)
-- ============================================================
INSERT INTO turnkeys (handle, name, description, category, price, is_premium) VALUES
('nft-marketplace-pro', 'NFT Marketplace Pro', 'Full-featured NFT marketplace with auctions and royalties', 'NFT/Gaming', '$8,999', 1),
('gaming-loot-box-engine', 'Gaming Loot Box Engine', 'Blockchain-based loot box system with verifiable randomness', 'NFT/Gaming', '$4,999', 1),
('nft-fractionalizer', 'NFT Fractionalizer', 'Fractionalize NFTs into ERC-20 tokens for shared ownership', 'NFT/Gaming', '$3,499', 1),
('play-to-earn-framework', 'Play-to-Earn Framework', 'Complete P2E game backend with token rewards system', 'NFT/Gaming', '$12,999', 1),
('nft-lending-protocol', 'NFT Lending Protocol', 'Lend and borrow NFTs with floor price oracle', 'NFT/Gaming', '$5,999', 1),
('dynamic-nft-engine', 'Dynamic NFT Engine', 'Create NFTs that evolve based on on-chain conditions', 'NFT/Gaming', '$4,499', 1),
('gaming-inventory-system', 'Gaming Inventory System', 'Blockchain-based gaming inventory and item trading', 'NFT/Gaming', '$3,999', 1),
('nft-royalty-tracker', 'NFT Royalty Tracker', 'Automated royalty distribution for NFT creators', 'NFT/Gaming', '$2,499', 0),
('virtual-land-marketplace', 'Virtual Land Marketplace', 'Metaverse virtual land trading and development platform', 'NFT/Gaming', '$7,999', 1),
('nft-collection-generator', 'NFT Collection Generator', 'Generate entire NFT collections with metadata and rarity', 'NFT/Gaming', '$2,999', 0),
('gaming-tournament-engine', 'Gaming Tournament Engine', 'Blockchain tournament system with prize pools', 'NFT/Gaming', '$5,499', 1),
('nft-bridge', 'NFT Bridge', 'Cross-chain NFT bridge supporting major networks', 'NFT/Gaming', '$6,999', 1),
('gaming-dao-framework', 'Gaming DAO Framework', 'Player-owned gaming DAO with governance and treasury', 'NFT/Gaming', '$4,999', 1),
('nft-staking-platform', 'NFT Staking Platform', 'Stake NFTs for rewards and governance rights', 'NFT/Gaming', '$3,499', 1),
('metaverse-identity-system', 'Metaverse Identity System', 'Cross-platform metaverse identity and avatar system', 'NFT/Gaming', '$6,499', 1);

-- ============================================================
-- INFRASTRUCTURE & TOOLS (15)
-- ============================================================
INSERT INTO turnkeys (handle, name, description, category, price, is_premium) VALUES
('node-deployment-suite', 'Node Deployment Suite', 'Automated blockchain node deployment and management', 'Infrastructure', '$5,999', 1),
('indexer-framework', 'Indexer Framework', 'Custom blockchain indexer for fast data querying', 'Infrastructure', '$4,499', 1),
('oracle-network', 'Oracle Network', 'Decentralized oracle network for off-chain data', 'Infrastructure', '$7,999', 1),
('wallet-sdk', 'Wallet SDK', 'Multi-chain wallet software development kit', 'Infrastructure', '$3,499', 1),
('blockchain-api-gateway', 'Blockchain API Gateway', 'Unified API gateway for multiple blockchain networks', 'Infrastructure', '$4,999', 1),
('monitoring-stack', 'Monitoring Stack', 'Full monitoring and alerting for blockchain infrastructure', 'Infrastructure', '$2,999', 0),
('gas-station-network', 'Gas Station Network', 'Meta-transaction gas station for user-friendly dApps', 'Infrastructure', '$3,999', 1),
('key-management-system', 'Key Management System', 'Enterprise key management with HSM integration', 'Infrastructure', '$6,999', 1),
('blockchain-analytics-platform', 'Blockchain Analytics Platform', 'On-chain analytics and visualization platform', 'Infrastructure', '$5,499', 1),
('smart-contract-templates', 'Smart Contract Templates', 'Library of audited smart contract templates', 'Infrastructure', '$1,999', 0),
('testnet-faucet', 'Testnet Faucet', 'Automated testnet token faucet for development', 'Infrastructure', '$999', 0),
('ipfs-gateway', 'IPFS Gateway', 'Decentralized file storage gateway using IPFS', 'Infrastructure', '$2,499', 0),
('web3-auth-system', 'Web3 Auth System', 'Web3 authentication with wallet connect support', 'Infrastructure', '$3,499', 1),
('multi-chain-sdk', 'Multi-Chain SDK', 'Unified SDK for 20+ blockchain networks', 'Infrastructure', '$4,999', 1),
('blockchain-backup-system', 'Blockchain Backup System', 'Automated backup and recovery for blockchain data', 'Infrastructure', '$3,999', 1);

-- ============================================================
-- CONSULTING & SERVICES (10)
-- ============================================================
INSERT INTO turnkeys (handle, name, description, category, price, is_premium) VALUES
('smart-contract-development', 'Smart Contract Development', 'Custom smart contract development and deployment service', 'Services', '$9,999', 1),
('blockchain-consulting', 'Blockchain Consulting', 'Enterprise blockchain strategy and architecture consulting', 'Services', '$14,999', 1),
('tokenomics-design', 'Tokenomics Design', 'Custom tokenomics design with economic modeling', 'Services', '$7,999', 1),
('defi-strategy-package', 'DeFi Strategy Package', 'Complete DeFi strategy including protocol selection and yield optimization', 'Services', '$5,499', 1),
('security-audit-service', 'Security Audit Service', 'Comprehensive smart contract and protocol security audit', 'Services', '$8,999', 1),
('launchpad-package', 'Launchpad Package', 'Full token launch service including marketing and liquidity', 'Services', '$19,999', 1),
('trading-bot-setup', 'Trading Bot Setup', 'Custom trading bot development and deployment', 'Services', '$4,999', 1),
('dao-setup-service', 'DAO Setup Service', 'Complete DAO setup including legal framework and governance', 'Services', '$12,999', 1),
('nft-collection-launch', 'NFT Collection Launch', 'End-to-end NFT collection launch service', 'Services', '$6,999', 1),
('web3-integration', 'Web3 Integration', 'Integrate Web3 functionality into existing applications', 'Services', '$9,999', 1);

-- ============================================================
-- EDUCATION & RESEARCH (10)
-- ============================================================
INSERT INTO turnkeys (handle, name, description, category, price, is_premium) VALUES
('crypto-trading-course', 'Crypto Trading Course', 'Comprehensive crypto trading course with live strategies', 'Education', '$999', 0),
('defi-masterclass', 'DeFi Masterclass', 'Deep dive into DeFi protocols, strategies, and risk management', 'Education', '$1,499', 0),
('blockchain-developer-bootcamp', 'Blockchain Developer Bootcamp', 'Full blockchain developer curriculum with hands-on projects', 'Education', '$2,499', 0),
('smart-contract-course', 'Smart Contract Course', 'Solidity and smart contract development from beginner to advanced', 'Education', '$1,999', 0),
('nft-creation-workshop', 'NFT Creation Workshop', 'Learn to create, mint, and market NFT collections', 'Education', '$799', 0),
('trading-psychology-program', 'Trading Psychology Program', 'Mental frameworks and discipline for professional trading', 'Education', '$499', 0),
('research-reports-bundle', 'Research Reports Bundle', 'Monthly institutional-grade crypto research reports', 'Education', '$2,999', 0),
('algorithmic-trading-course', 'Algorithmic Trading Course', 'Build your own trading algorithms from scratch', 'Education', '$1,799', 0),
('defi-yield-strategies', 'DeFi Yield Strategies', 'Advanced yield farming and liquidity provision strategies', 'Education', '$1,299', 0),
('web3-fundamentals', 'Web3 Fundamentals', 'Introduction to Web3, blockchain, and decentralized applications', 'Education', '$399', 0);

-- ============================================================
-- BONUS: PREMIUM BUNDLES (5)
-- ============================================================
INSERT INTO turnkeys (handle, name, description, category, price, is_premium) VALUES
('enterprise-complete-bundle', 'Enterprise Complete Bundle', 'All enterprise products bundled at 40% discount', 'Bundles', '$99,999', 1),
('trading-pro-bundle', 'Trading Pro Bundle', 'All crypto trading systems bundled at 35% discount', 'Bundles', '$29,999', 1),
('defi-master-bundle', 'DeFi Master Bundle', 'All DeFi protocols bundled at 30% discount', 'Bundles', '$49,999', 1),
('ai-complete-bundle', 'AI Complete Bundle', 'All AI/ML products bundled at 25% discount', 'Bundles', '$39,999', 1),
('full-portfolio-access', 'Full Portfolio Access', 'Unlimited access to all 120+ turnkeys with lifetime updates', 'Bundles', '$199,999', 1);

-- ============================================================
-- PCI COUNSELOR ACADEMY (10)
-- ============================================================
INSERT INTO turnkeys (handle, name, description, category, price, is_premium) VALUES
('pci-counselor-academy-level-1', 'PCI Counselor Academy — Level 1', 'Foundational blockchain and crypto counseling certification', 'Academy', '$499', 0),
('pci-counselor-academy-level-2', 'PCI Counselor Academy — Level 2', 'Advanced DeFi and trading strategy counseling', 'Academy', '$999', 0),
('pci-counselor-academy-level-3', 'PCI Counselor Academy — Level 3', 'Enterprise blockchain consulting certification', 'Academy', '$1,999', 0),
('pci-counselor-academy-master', 'PCI Counselor Academy — Master', 'Master counselor certification with full toolkit access', 'Academy', '$4,999', 1),
('pci-counselor-academy-institutional', 'PCI Counselor Academy — Institutional', 'Institutional-grade counseling certification for firms', 'Academy', '$9,999', 1),
('pci-mentor-program', 'PCI Mentor Program', 'One-on-one mentorship with PCI senior counselors', 'Academy', '$2,499', 0),
('pci-community-access', 'PCI Community Access', 'Private community with weekly strategy calls and alpha', 'Academy', '$299', 0),
('pci-signal-service', 'PCI Signal Service', 'Daily trading signals from PCI algorithmic systems', 'Academy', '$199', 0),
('pci-portfolio-management', 'PCI Portfolio Management', 'Managed portfolio service with PCI strategies', 'Academy', '$5,999', 1),
('pci-white-label-program', 'PCI White-Label Program', 'White-label PCI products for your own brand', 'Academy', '$14,999', 1);

-- ============================================================
-- VERIFICATION QUERY
-- ============================================================
-- Run this to confirm all 135 turnkeys were inserted:
-- SELECT COUNT(*) as total_turnkeys FROM turnkeys;
-- SELECT category, COUNT(*) as count FROM turnkeys GROUP BY category ORDER BY count DESC;

-- © 2026 Positive Change Institute LLC
-- All Systems, Divisions, Engines, Motifs, Insignias, and Products
-- Are the Exclusive Property of Positive Change Institute LLC.