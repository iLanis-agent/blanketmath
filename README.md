# Blanket math

The weighted blanket weight a sleeper actually needs, whether two sleepers share one, and if it fits the washer - labeled rules of thumb with exact arithmetic, not medical advice.

Live site: https://ilanis-agent.github.io/blanketmath/

## The three tools

- **Weight plan** - `weightPlan(bodyKg)`: the labeled 10% target, its 7-12% band and the nearest catalog size.
- **Share plan** - `sharePlan(kgA, kgB)`: shared target at the labeled 7.5% rule and a share-versus-singles call.
- **Wash plan** - `washPlan(blanketKg, washerKg)`: drum spare percent and an easy/tight/laundromat verdict.

## Labeled norms (rules of thumb, not medical advice)

- Single: about 10% of body weight, band 7-12%. Shared: 7.5% of combined, and over 30 kg between sleepers argues for two singles. Weighted blankets are not for infants; children or anyone who cannot push the blanket off alone need a clinician's or caregiver's call.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (12 cases, 60 checks)

Regenerate the oracle expectations: `python3 oracle.py`
