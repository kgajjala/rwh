#!/usr/bin/env python3
"""Total-return index series for the deep-dive line charts (kg-investment-analysis v7).

Usage:
  python3 -I prices.py OUT.json TICKER[,TICKER...] --start YYYY-MM-DD [--end YYYY-MM-DD]
                       [--interval 1mo|1wk|1d] [--weekly] [--names PEP=PepsiCo,KO=Coca-Cola]

Pulls daily Yahoo Finance chart data (dividend-adjusted closes) up to --end, resamples to month-ends
(--interval 1mo, the last trading day of each month) or Fridays (--interval 1wk or --weekly),
rebases every series to 100 on the first common date,
and writes {"dates": [...], "order": [...], "names": {...}, "series": {T: [...]},
"cagr": {T: x}, "total": {T: x}}. --weekly samples daily data on Fridays (plus the last day).
It also prints the latest close per ticker, for the Step 0 cross-check (not a substitute
for verifying the price on the quote page).
"""
import json, sys, datetime, urllib.request, argparse

def fetch(t, p1, p2, interval):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1={p1}&period2={p2}&interval={interval}&events=div"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    j = json.load(urllib.request.urlopen(req, timeout=30))["chart"]["result"][0]
    ts = j["timestamp"]; adj = j["indicators"]["adjclose"][0]["adjclose"]; cl = j["indicators"]["quote"][0]["close"]
    rows = [(datetime.datetime.utcfromtimestamp(a).date(), b, c) for a, b, c in zip(ts, adj, cl) if b]
    return rows, j["meta"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("tickers"); ap.add_argument("--start", required=True)
    ap.add_argument("--end"); ap.add_argument("--interval", default="1mo"); ap.add_argument("--weekly", action="store_true")
    ap.add_argument("--names", default="")
    a = ap.parse_args()
    d0 = datetime.datetime.fromisoformat(a.start).replace(tzinfo=datetime.timezone.utc)
    d1 = datetime.datetime.fromisoformat(a.end).replace(tzinfo=datetime.timezone.utc) if a.end else datetime.datetime.now(datetime.timezone.utc)
    p1, p2 = int(d0.timestamp()), int(d1.timestamp()) + 86400
    names = dict(x.split("=", 1) for x in a.names.split(",") if "=" in x)
    tick = a.tickers.split(","); data = {}
    end_date = d1.date()
    for t in tick:
        # Always fetch DAILY bars and resample: Yahoo's monthly/weekly bars ignore period2 and close at the
        # latest price, which would leak post-report prices into a report pinned to an earlier date.
        rows, meta = fetch(t, p1, p2, "1d")
        rows = [r for r in rows if r[0] <= end_date]
        if a.interval == "1mo":
            key = lambda d: d.strftime("%Y-%m")
        else:
            key = lambda d: d.isoformat()
        dd = {}
        for d, adj, cl in rows: dd[key(d)] = adj          # monthly: the last trading day of each month wins
        data[t] = dd
        print(f"{t}: last close {rows[-1][2]:.2f} on {rows[-1][0]}  (meta price {meta.get('regularMarketPrice')})")
    dates = sorted(set.intersection(*[set(v) for v in data.values()]))
    if a.weekly or a.interval == "1wk":
        keep = [d for i, d in enumerate(dates) if i == 0 or i == len(dates) - 1 or datetime.date.fromisoformat(d).weekday() == 4]
        dates = keep
    series = {t: [round(data[t][d] / data[t][dates[0]] * 100, 1) for d in dates] for t in tick}
    first = datetime.date.fromisoformat(dates[0] + ("-01" if len(dates[0]) == 7 else ""))
    last = datetime.date.fromisoformat(dates[-1] + ("-01" if len(dates[-1]) == 7 else ""))
    yrs = max((last - first).days / 365.25, 1e-9)
    out = {"dates": dates, "order": tick, "names": {t: names.get(t, t) for t in tick}, "series": series,
           "total": {t: series[t][-1] / 100 - 1 for t in tick},
           "cagr": {t: (series[t][-1] / 100) ** (1 / yrs) - 1 for t in tick}}
    json.dump(out, open(a.out, "w"), separators=(",", ":"))
    for t in tick: print(f"  {t}: total {out['total'][t]:+.1%}, {out['cagr'][t]:+.1%}/yr over {yrs:.1f} yrs")

if __name__ == "__main__":
    main()
