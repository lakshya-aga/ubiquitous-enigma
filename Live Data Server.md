
# Plan

## 1. Process shape (monolithic gateway)

One Python asyncio process with four subsystems running as supervised tasks:

- **StreamManager** — owns all outbound WS connections to streaming sources, auto-reconnect w/ backoff
- **PollManager** — APScheduler-style loop, one job per polled source, staggered
- **DataRepository** — in-memory latest-value store + ring buffer per channel (last N ticks), optional Redis mirror for persistence/replay
- **SubscriberServer** — WS server strategies connect to, handles `subscribe`/`unsubscribe` messages per channel

Each source is a self-contained module implementing either a `StreamSource` or `PollSource` protocol. Adding a new source = one file + registry entry.

## 2. Sources (initial set)

**Streaming:**

- Prices — Binance (crypto) and/or Alpaca/Polygon (equities) — pick one to start
- News — Finnhub WS or Benzinga

**Polled:**

- GDELT 2.0 GKG (15-min cadence)
- FRED macro series (daily; list of series IDs in config)
- Economic calendar — TradingEconomics or FMP (hourly)
- Optional: COT reports (weekly), CoinGecko global metrics

## 3. Internal schema

All messages normalized to a Pydantic envelope: `{source, channel, symbol, ts_event, ts_ingest, payload}`. Channels are hierarchical: `prices.binance.BTCUSDT`, `news.finnhub`, `macro.fred.DGS10`, `geopolitics.gdelt.gkg`. Strategies subscribe by glob (`prices.binance.*`).

## 4. Transport to strategies

Outbound WS with JSON. Message types: `subscribe`, `unsubscribe`, `snapshot` (last value on subscribe), `update`. No auth for v1 (localhost), token-based later.

## 5. Config

Single `config.yaml` — API keys via env vars, source enable/disable flags, poll intervals, FRED series list, subscriber port.

## 6. Observability

Structured JSON logs + per-source health metrics (last_msg_ts, reconnect_count, error_count) exposed on a `/health` HTTP endpoint.

## 7. Skill documentation (auto-generated)

A `generate_skill.py` script introspects the source registry + Pydantic schemas and emits `SKILL.md` containing:

- Connection instructions (host, port, protocol)
- Every channel, its schema, cadence, example payload
- Subscribe/unsubscribe message format
- Example strategy snippet

Regenerated on every source addition so the agent skill never drifts.

## 8. Layout

```
gateway/  main.py                 # entrypoint, task supervisor  config.py               # yaml + env loader  schema.py               # Pydantic envelope + per-source payloads  repository.py           # latest + ring buffer + fanout  subscriber_server.py    # outbound WS  stream_manager.py  poll_manager.py  sources/    base.py               # StreamSource / PollSource protocols    prices_binance.py    news_finnhub.py    gdelt.py    fred.py    econ_calendar.py  tools/    generate_skill.pyconfig.yamlSKILL.md                  # generatedpyproject.toml
```

## 9. Build order

1. Skeleton + config + schema + repository + subscriber server (testable with a fake source)
2. One streaming source (Binance — no API key)
3. One polled source (FRED — free key)
4. `generate_skill.py`
5. Remaining sources
6. Health endpoint + logging polish