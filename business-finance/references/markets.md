# markets

Load for prices, market data, portfolio math and trading logic.

## data

| field | rule |
| --- | --- |
| price | with currency, timestamp and source |
| volume | with the aggregation window |
| corporate action | split and dividend adjusted, or flagged raw |
| timezone | utc stored, exchange local for display |

A price without a timestamp is unusable: store UTC, the exchange-local session date and the adjusted flag. A series mixing adjusted and raw closes is wrong.

Ingest checks that catch real breaks:

- Monotonic timestamps per symbol; a bar earlier than its predecessor means a late correction, not a new bar.
- Gap detection against the exchange calendar. A missing session is a data hole; a missing weekend is correct.
- Return outlier over 20 sigma for a large cap is a bad print, not a move. Cross-check a second source before storing.
- Split detection: a one-day drop near 2:1, 3:1 or 10:1 with volume spike is a split the feed failed to adjust.
- Duplicate (symbol, timestamp) rows collapse to one; keep the later arrival and log the overwrite.
- Currency of the quote is not the currency of the listing. Store both.

## returns

```
simple:  r = p1 / p0 - 1
log:     r = ln(p1 / p0)
annual:  (1 + r)^(252 / n) - 1     # trading days
```

State which convention a number uses. Mixing simple and log returns breaks aggregation.

- Simple returns aggregate across assets: portfolio return is the weighted sum.
- Log returns aggregate across time: the sum of daily logs is the period log return.
- Convert before aggregating: `log(1 + r)` to sum, `exp(sum) - 1` to report.
- Volatility annualizes with `sqrt(252)` for daily, `sqrt(52)` for weekly, `sqrt(12)` for monthly. Annualizing by `252` a figure computed on calendar days is a 5% error.
- A return over a period containing a cash flow is not a return; it is a return plus a flow.

## performance

```
twr = prod(1 + r_t) - 1                 # time weighted, per sub-period, flow at period start
mwr = irr(cashflows)                    # money weighted, solves npv = 0
sharpe = mean(r - rf) / stdev(r) * sqrt(252)
sortino = mean(r - rf) / downside_dev * sqrt(252)
max_dd = min over t of (equity_t / peak_t - 1)
```

- Time weighted answers "how did the strategy do"; money weighted answers "how did this investor do". A large contribution before a drawdown makes them diverge, and reporting the wrong one is a misrepresentation.
- Sub-period boundaries fall on every external cash flow, not on month ends.
- Sharpe on daily data with a risk-free rate quoted annually: convert the rate to daily first, or the ratio is off by the compounding.
- Downside deviation uses only returns below the target, with the full count in the denominator.
- Max drawdown is computed on the equity curve, peak to trough, over the whole series. The worst single day is a different number and usually flattering.

## portfolio

- Position value = quantity x price, in one currency, with the fx rate dated.
- Cost basis method stated: fifo, lifo, average.
- Realized and unrealized kept separate.
- Book fees as an expense line in the broker's currency, not as a reduced fill price; the tax lot depends on the gross.
- Corporate actions adjust quantity and basis, not just price: a 2:1 split doubles shares and halves basis; a spin-off allocates basis by relative fair value on the ex date.
- Short positions carry negative quantity and a borrow cost line; a negative position value without a borrow accrual is a missing cost.
- Reconcile to the broker statement every period. The difference is either a missing fee, a missing action or a timing cut-off, and it is never zero by accident.

## backtest traps

| trap | symptom | guard |
| --- | --- | --- |
| lookahead | impossible returns | shift signals by one bar |
| survivorship | only winners in the set | include delisted symbols |
| overfitting | great in sample | out-of-sample window, walk forward |
| costs ignored | thin edge | spread, fee, slippage per trade |
| illiquid fills | fills at mid | size against volume |
| point-in-time data | restated fundamentals | use as-reported values with the publication date |
| rebalance drift | weights wander | rebalance on a stated schedule and log the turnover |
| borrow and short | impossible short returns | charge borrow, exclude hard-to-borrow names |

A backtest without costs and slippage is a curve fit: charge commission, half the spread and 1-2 ticks per side; a strategy that dies at 10bps was never there.

Walk-forward is the minimum honest test: fit on window 1, trade window 2, roll, and report the concatenated out-of-sample result. A single 70/30 split with parameters tuned on the 70 is in-sample with extra steps.

## risk

- Max drawdown over the whole series, not the worst day.
- Exposure per symbol and per sector, before and after a trade.
- Correlation cluster: three positions in one factor is one position.
- Position limits in both notional and risk terms: 5% of equity and 0.5% of equity at the stop are different constraints and both bind.
- Concentration check on the largest single loss, not the average: one position that can lose 30% of equity fails regardless of the mean.
- Leverage stated gross and net; a market-neutral book can still be 4x gross and gap on a spread.

## execution

- Order types named: market, limit, stop, stop-limit. A stop becomes a market order in a gap; say so when the risk number assumes the stop price.
- Slippage measured per fill against the arrival mid, stored with the order id.
- Partial fills are the normal case; the position is the sum of fills, not the intended size.
- A cancel-replace is two messages, not one; a rejected replace leaves the original live.

## review

- Every number has a source and a timestamp.
- Every derived metric names its convention.
- Simulated results are labeled simulated, never presented as performance.
- A performance figure states the period, the currency, the cost assumption and whether it is net of fees.
