(function (root) {
  "use strict";
  function jsfmt(x) { return String(x); }

  function weightPlan(bodyKg) {
    if (!(bodyKg > 0)) return { error: "weight must be positive" };
    var target = Math.round(bodyKg * 10) / 100;
    var lo = Math.round(bodyKg * 7) / 100;
    var hi = Math.round(bodyKg * 12) / 100;
    var nearest = Math.round(bodyKg / 10);
    return { target: target, lo: lo, hi: hi, nearest: nearest };
  }

  function sharePlan(kgA, kgB) {
    if (!(kgA > 0) || !(kgB > 0)) return { error: "both sleepers must be positive" };
    var target = Math.round((kgA + kgB) * 0.75) / 10;
    var diff = kgA >= kgB ? kgA - kgB : kgB - kgA;
    var verdict = diff > 30 ? "singles" : "shared";
    return { target: target, diff: diff, verdict: verdict };
  }

  function washPlan(blanketKg, washerKg) {
    if (!(blanketKg > 0) || !(washerKg > 0)) return { error: "blanket and washer must be positive" };
    var spare = Math.round((washerKg - blanketKg) / washerKg * 100);
    var verdict = spare < 0 ? "laundromat" : (spare < 20 ? "tight" : "easy");
    return { spare: spare, verdict: verdict };
  }

  function renderWeight(r, bodyKg) {
    return "At " + bodyKg + " kg of sleeper the labeled 10% rule says about " + r.target + " kg, inside a band of " + r.lo + " to " + r.hi + " kg - the nearest catalog size is " + r.nearest + " kg.";
  }

  function renderShare(r, kgA, kgB) {
    var tail = r.verdict === "shared" ? "one shared blanket serves" : "two singles sleep better";
    return "At " + kgA + " kg and " + kgB + " kg the shared labeled rule says about " + r.target + " kg, and with " + r.diff + " kg between the sleepers " + tail + ".";
  }

  function renderWash(r, blanketKg, washerKg) {
    var tail = r.verdict === "easy" ? "an easy home wash" : (r.verdict === "tight" ? "a tight home wash, no room for the duvet cover" : "the laundromat's big machine");
    return "A blanket of " + blanketKg + " kg in a washer rated " + washerKg + " kg leaves " + r.spare + "% of the drum free - " + tail + ".";
  }

  var api = { weightPlan: weightPlan, sharePlan: sharePlan, washPlan: washPlan, renderWeight: renderWeight, renderShare: renderShare, renderWash: renderWash };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.BlanketMath = api;
})(this);
