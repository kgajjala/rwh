#!/usr/bin/env python3
"""Annual series from the SEC XBRL company-facts API (kg-investment-analysis v7).

Usage:
  python3 -I xbrl.py CIK OUT.json "Your Name your@email" [TAG,TAG!,...]

CIK may be unpadded. A trailing "!" marks an instant (balance-sheet) tag. Without a tag
list it pulls the default set the five-year table needs. Values come from annual frames
(CYyyyy for flows, CYyyyyQ4I for instants, falling back to Q3I for fiscal years ending in
late September). Fiscal-year labels follow the SEC frame, so check them against the 10-K
for companies whose fiscal year does not end in December.
Output: {"tag": {"year": value_in_billions_or_raw}}; also prints a compact table.
"""
import json, sys, urllib.request

DEFAULT = ("Revenues,RevenueFromContractWithCustomerExcludingAssessedTax,OperatingIncomeLoss,NetIncomeLoss,"
           "NetCashProvidedByUsedInOperatingActivities,PaymentsToAcquirePropertyPlantAndEquipment,"
           "PaymentsToAcquireProductiveAssets,ShareBasedCompensation,PaymentsOfDividends,PaymentsOfDividendsCommonStock,"
           "PaymentsForRepurchaseOfCommonStock,PaymentsToAcquireBusinessesNetOfCashAcquired,"
           "DepreciationDepletionAndAmortization,DepreciationAndAmortization,InterestExpense,IncomeTaxExpenseBenefit,"
           "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest,"
           "WeightedAverageNumberOfDilutedSharesOutstanding,EarningsPerShareDiluted,"
           "StockholdersEquity!,LongTermDebtNoncurrent!,LongTermDebtCurrent!,DebtCurrent!,"
           "CashAndCashEquivalentsAtCarryingValue!,ShortTermInvestments!,OperatingLeaseLiability!,"
           "PropertyPlantAndEquipmentNet!,Assets!,Goodwill!")

def main():
    cik = sys.argv[1].zfill(10); out = sys.argv[2]; ua = sys.argv[3]
    tags = (sys.argv[4] if len(sys.argv) > 4 else DEFAULT).split(",")
    req = urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json", headers={"User-Agent": ua})
    facts = json.load(urllib.request.urlopen(req, timeout=60))
    g = facts["facts"].get("us-gaap", {})
    res = {}
    for t in tags:
        inst = t.endswith("!"); t = t.rstrip("!")
        if t not in g: continue
        vals = {}
        for unit, arr in g[t]["units"].items():
            for x in arr:
                fr = x.get("frame", "")
                if not fr.startswith("CY"): continue
                if inst:
                    if fr.endswith("Q4I"): vals[int(fr[2:6])] = x["val"]
                    elif fr.endswith("Q3I"): vals.setdefault(int(fr[2:6]), x["val"])
                elif len(fr) == 6: vals[int(fr[2:])] = x["val"]
        if vals:
            res[t + ("!" if inst else "")] = {y: (round(v / 1e9, 3) if abs(v) > 1e5 else v) for y, v in sorted(vals.items())}
    json.dump({"entity": facts.get("entityName"), "cik": cik, "series": res}, open(out, "w"), indent=1)
    print(facts.get("entityName"))
    for t, v in res.items():
        last = {y: v[y] for y in list(v)[-6:]}
        print(f"  {t:58s} {last}")

if __name__ == "__main__":
    main()
