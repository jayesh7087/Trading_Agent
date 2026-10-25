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

---

## 3. Mathematical Translation Matrix (Pine Script to Python)

Aapki script ke exact logic ko Python agent me convert karne ka roadmap:

| Pine Script Component | Script Implementation | Python Engine Equivalent |
| :--- | :--- | :--- |
| **PDH / PDL Fetch** | `request.security(..., "D", high[1])` | Daily resampled DataFrame se previous candle ka `High` & `Low`. |
| **Pivot Detection** | `ta.pivothigh(high, 5, 5)` | Scipy / Pandas rolling window: `High[i]` is maximum of `i-5` to `i+5`. |
| **Displacement Check** | `abs(close - open) > sma(body, 20) * mult` | Rolling 20 SMA of candle bodies multiplied by `1.2` (Oil) or `1.3` (Gold). |
| **FVG Detection** | Bull: `low > high[2]`, Bear: `high < low[2]` | Shifted series indexing: `df['low'] > df['high'].shift(2)`. |
| **Sweep Entry Price**| Bull: `(low[2] + high) / 2.0` | Exact 50% midpoint of the 3-candle Fair Value Gap. |
| **Breaker Entry Price**| Oil: `brk_mid`, Gold: `close` | Midpoint calculation for Oil; Market Close for Gold. |
| **Exit Resolution** | TP (+2.5R), SL (-1R), 30-bar time stop | Per-bar price traversal check: `high >= tp`, `low <= sl`, `bar_count >= 30`. |

---

## 4. Capital Management, Brokerage & Dynamic Lot Sizing

Real-world accuracy ke liye paper trading me real broker costs include kiye gaye hain:

### Financial Rules
* **Initial Capital:** ₹10,000 (Base Level).
* **Starting Position:** 1 Single Lot (MCX Mini/Micro or equivalent CFDs).
* **Flat Brokerage:** ₹25 per executed order (Entry + Exit = ₹50 round turn per trade).
* **Dynamic Sizing Scale-up Formula:**
  $$\text{Lot Size} = \max\left(1, \left\lfloor \frac{\text{Current Wallet Balance}}{\text{Base Capital (₹10,000)}} \right\rfloor\right)$$
  * *Example:* 
    * ₹10,000 to ₹19,999 -> 1 Lot (Brokerage: ₹25/order)
    * ₹20,000 to ₹29,999 -> 2 Lots (Brokerage: ₹50/order)
    * ₹50,000+ -> 5 Lots (Brokerage: ₹125/order)
    * ₹1,00,000+ -> 10 Lots (Brokerage: ₹250/order)
* **Capital Protection Rule:** Agar capital draw down hokar ₹10,000 ke niche jata hai, lot size wapas 1 standard minimum par freeze ho jayega.

---

## 5. AI Loss-Auditing Engine (Post-Mortem Logger)

Ye system ka sabse intelligent component hai. Jab bhi koi trade **SL HIT (-1R)** ya **TIME STOP** par close hoga, agent chupchap band nahi hoga; wo niche diye gaye parameters ko check karke **Failure Cause** log karega:

### Root Cause Categories (Failure Taxonomy)
1. **`SESSION_LEAK`:** Gold trade London/NY peak session ke bahar trigger hua ya low volume period me tha.
2. **`DISPLACEMENT_EXHAUSTION`:** Breakout candle ka volume/size average se 3x se zyada tha (exhaustion candle, institutional continuation nahi).
3. **`COUNTER_TREND_TRAP`:** Trade HTF (Higher Timeframe 1-Hour/4-Hour) trend ke opposite tha.
4. **`TIME_STOP_CHOP`:** Market low-volatility zone me freeze ho gaya aur 30 bars tak target/SL touch nahi hua.
5. **`HIGH_IMPACT_NEWS_SLIP`:** US Core CPI, PPI, ya FOMC press conference ke 15 minute ke window me SL hit hua.

### Logged Database Structure (`trades_audit.db`)
```sql
CREATE TABLE trade_audit (
    trade_id TEXT PRIMARY KEY,
    timestamp TEXT,
    instrument TEXT,
    agent_name TEXT,
    setup_type TEXT,
    entry_price REAL,
    exit_price REAL,
    pnl_net REAL,
    brokerage_deducted REAL,
    result TEXT, -- 'TARGET_HIT', 'SL_HIT', 'TIME_STOP'
    loss_root_cause TEXT, -- Auto-detected failure reason
    bars_held INTEGER,
    capital_after_trade REAL
);
Overall Project Readiness: [ 20% ] ▓▓░░░░░░░░░░░░░░░░░░

---

Ise save karne ke baad bata, fir **Phase 2** ke pehle do items—**Telegram Bot Token** aur **Free Data Stream setup** par kaam shuru karte hain!
