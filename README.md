# 📘 PROJECT BLUEPRINT: DUAL-COMMODITY AUTONOMOUS AI AGENT SYSTEM
**Document Version:** `v1.0.0-PROD-BLUEPRINT`  
**Base Strategy Engine:** `stratagy_v1.2.9_Mechanical SMC: Main Chart Overlay`  
**Primary Assets:** Gold (`XAU/USD` & `MCX GOLD`) | Crude Oil (`WTI/USOIL` & `MCX CRUDE OIL`)  
**Host Architecture:** 100% Free Cloud Infrastructure (Zero-Laptop Running Dependency)  

---

## 1. Executive Summary & Objective

Is project ka motive TradingView ke free-plan limitations (alert drop, webhook paywall, restricted backtesting) ko bypass karke ek aisa **autonomous Python-based dual-agent framework** banana hai jo:
1. 24/5 global aur Indian MCX sessions ko autonomously monitor kare.
2. Setup 1 (PDH/PDL Sweep + FVG) aur Setup 2 (Displacement Breaker Tap) ko bina human error ke execute kare.
3. Telegram par rich live alerts fire kare (Entry, SL, TP, Risk:Reward).
4. ₹10,000 starting virtual capital ke sath real-world brokerage/slippage deduct karke dynamic compounding paper-trade kare.
5. **AI Loss Auditing Engine:** Har loss trade ka post-mortem kare ki setup kyun fail hua (session timing, news spike, displacement failure, ya adverse trend).

---

## 2. Core Architecture & Two-Agent Separation

Dono commodities ka behavior aur volatility alag hai, isliye system do independent agents me divide rahega:


