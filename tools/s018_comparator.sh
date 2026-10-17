#!/usr/bin/env bash
# S018 Milestone 2 (PLAN.md): Palomar-shaped Comparator run on formal/, unsandboxed (no bwrap on Windows).
# 1. Export Challenge and Solution with the toolchain's leanexport and Palomar's target order
#    (Quot builtins, theorem_names, permitted_axioms, primitiveTargets of Lake/CLI/Check.lean v4.35.0).
# 2. lake comparator --config <cfg> --challenge-from-export --solution-from-export --inadvisably-no-sandbox [--paranoid]
# usage: s018_comparator.sh <exportdir> <cfg.json> <logfile> [--paranoid]
# Exports are large and kept outside the repository; their sha256 go to the log.
set -u
EXP=$1; CFG=$2; LOG=$3; shift 3
cd "$(dirname "$0")/../formal"
mkdir -p "$EXP"
NAMES=$(python -I -c "import json,sys;c=json.load(open(sys.argv[1]));print(' '.join(c['theorem_names']))" comparator.json)
PRIM="Nat.add Nat.sub Nat.mul Nat.pow Nat.gcd Nat.div Nat.mod Nat.beq Nat.ble Nat.land Nat.lor Nat.xor Nat.shiftLeft Nat.shiftRight String.ofList Char.ofNat List eagerReduce Nat String String.mk Char optParam autoParam semiOutParam outParam"
TARGETS="Quot Quot.mk Quot.lift Quot.ind $NAMES propext Quot.sound Classical.choice $PRIM"
{
echo "utc_start $(date -u +%FT%TZ)"
echo "lean $(lean --version)"
echo "targets $TARGETS"
for m in Challenge Solution; do
  if [ ! -s "$EXP/$m.export" ]; then
    t0=$(date +%s)
    LEAN_ABORT_ON_PANIC=1 lake env leanexport $m -- $TARGETS > "$EXP/$m.export" 2> "$EXP/$m.export.err"
    echo "export $m rc=$? wall_s=$(( $(date +%s)-t0 )) bytes=$(stat -c %s "$EXP/$m.export")"
  fi
  echo "sha256 $(sha256sum "$EXP/$m.export" | cut -d' ' -f1) $m.export"
done
t0=$(date +%s)
LEAN_ABORT_ON_PANIC=1 lake comparator --config "$CFG" --challenge-from-export "$EXP/Challenge.export" \
  --solution-from-export "$EXP/Solution.export" --inadvisably-no-sandbox "$@" 2>&1
echo "comparator rc=$? wall_s=$(( $(date +%s)-t0 )) flags: $*"
echo "utc_end $(date -u +%FT%TZ)"
} > "$LOG" 2>&1
