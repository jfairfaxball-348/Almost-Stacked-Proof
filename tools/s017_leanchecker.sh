#!/usr/bin/env bash
# S017 PLAN_AMENDMENT_2 (addendum 2-i, v2): replay every formal/ module except the root
# `AlmostStacked` with leanchecker, one process at a time, 12 GiB watchdog.
set -u
cd "$(dirname "$0")/../formal"
LOG=../evidence/S017/leanchecker.txt
: > "$LOG"
mods=$(find AlmostStacked Challenge.lean Solution.lean -name '*.lean' | sed 's/\.lean$//; s|/|.|g' | sort)
n=0; ok=0
for m in $mods; do
  n=$((n+1)); t0=$(date +%s); peak=0; capped=0
  lake env leanchecker "$m" > ../evidence/S017/leanchecker_last.txt 2>&1 &
  pid=$!
  while kill -0 $pid 2>/dev/null; do
    sleep 3
    mb=$(powershell -NoProfile -Command "[math]::Round(((Get-Process leanchecker -ErrorAction SilentlyContinue | Measure-Object PrivateMemorySize64 -Sum).Sum)/1MB)")
    mb=${mb:-0}; [ "$mb" -gt "$peak" ] && peak=$mb
    if [ "$mb" -gt 12288 ]; then taskkill //IM leanchecker.exe //F > /dev/null 2>&1; capped=1; fi
  done
  wait $pid; rc=$?
  status=$([ $capped -eq 1 ] && echo CAP_UNKNOWN || ([ $rc -eq 0 ] && echo OK || echo FAIL))
  echo "module $m rc=$rc status=$status wall_s=$(( $(date +%s) - t0 )) peak_MB=$peak $(tail -1 ../evidence/S017/leanchecker_last.txt | cut -c1-160)" >> "$LOG"
  [ "$status" = OK ] && ok=$((ok+1))
done
rm -f ../evidence/S017/leanchecker_last.txt
echo "LEANCHECKER modules=$n ok=$ok" >> "$LOG"
