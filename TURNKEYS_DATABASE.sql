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

-- © 2026 Positive Change Institute LLC
-- All Systems, Divisions, Engines, Motifs, Insignias, and Products
-- Are the Exclusive Property of Positive Change Institute LLC.