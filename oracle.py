import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def fmt(x): return str(jsnum(x))
def r2(x): return math.floor(x + 0.5) / 100

def weight_plan(bodyKg):
    if not (bodyKg > 0):
        return {"error": "weight must be positive"}
    return {"target": jsnum(r2(bodyKg * 10)), "lo": jsnum(r2(bodyKg * 7)),
            "hi": jsnum(r2(bodyKg * 12)), "nearest": math.floor(bodyKg / 10 + 0.5)}

def share_plan(kgA, kgB):
    if not (kgA > 0) or not (kgB > 0):
        return {"error": "both sleepers must be positive"}
    target = math.floor((kgA + kgB) * 0.75 + 0.5) / 10
    diff = kgA - kgB if kgA >= kgB else kgB - kgA
    return {"target": jsnum(target), "diff": diff, "verdict": "singles" if diff > 30 else "shared"}

def wash_plan(blanketKg, washerKg):
    if not (blanketKg > 0) or not (washerKg > 0):
        return {"error": "blanket and washer must be positive"}
    spare = math.floor((washerKg - blanketKg) / washerKg * 100 + 0.5)
    verdict = "laundromat" if spare < 0 else ("tight" if spare < 20 else "easy")
    return {"spare": spare, "verdict": verdict}

def render_weight(r, bodyKg):
    return ("At " + fmt(bodyKg) + " kg of sleeper the labeled 10% rule says about " + fmt(r["target"])
            + " kg, inside a band of " + fmt(r["lo"]) + " to " + fmt(r["hi"]) + " kg - the nearest catalog size is "
            + fmt(r["nearest"]) + " kg.")

def render_share(r, kgA, kgB):
    tail = "one shared blanket serves" if r["verdict"] == "shared" else "two singles sleep better"
    return ("At " + fmt(kgA) + " kg and " + fmt(kgB) + " kg the shared labeled rule says about " + fmt(r["target"])
            + " kg, and with " + fmt(r["diff"]) + " kg between the sleepers " + tail + ".")

def render_wash(r, blanketKg, washerKg):
    tail = ("an easy home wash" if r["verdict"] == "easy"
            else ("a tight home wash, no room for the duvet cover" if r["verdict"] == "tight" else "the laundromat's big machine"))
    return ("A blanket of " + fmt(blanketKg) + " kg in a washer rated " + fmt(washerKg) + " kg leaves "
            + fmt(r["spare"]) + "% of the drum free - " + tail + ".")

cases = []
for a in [(70,), (55,), (90,), (0,)]:
    r = weight_plan(*a)
    cases.append({"fn": "weightPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_weight(r, *a)})
for a in [(70, 55), (90, 50), (80, 75), (0, 55)]:
    r = share_plan(*a)
    cases.append({"fn": "sharePlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_share(r, *a)})
for a in [(7, 8), (5, 10), (12, 8), (0, 8)]:
    r = wash_plan(*a)
    cases.append({"fn": "washPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_wash(r, *a)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
