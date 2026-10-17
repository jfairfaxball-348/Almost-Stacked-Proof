module

public import AlmostStacked.Main

/-!
# The solution

Comparator compares the declarations named in `comparator.json`, as they are in this module,
with their counterparts in `Challenge.lean`. They are declared and proved in
`AlmostStacked/Main.lean` (and `clearable_stackable` in `AlmostStacked/Basic.lean`), with the
definitions in `AlmostStacked/Defs.lean`. The finite facts about `G9` are kernel evaluations
(`decide +kernel`) of the verified layer checker `AlmostStacked/Checker.lean` on the
certificate data in `AlmostStacked/Data/`; no `native_decide` is used.
-/
