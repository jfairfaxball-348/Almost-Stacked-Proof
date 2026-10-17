#!/usr/bin/env bash
# S018 staged build (copy of tools/s017_staged_build.sh; only the evidence directory differs) of formal/: every heavy kernel-check module is built ALONE (one lake
# invocation per module, so at most one heavy kernel evaluation runs at a time; each can commit
# several GB), then the full `lake build`, which replays the cached modules.
# Logs: evidence/S018/staged_build.txt (one line per step) and evidence/S018/staged/<step>.txt.
set -u
cd "$(dirname "$0")/../formal"
mkdir -p ../evidence/S018/staged
LOG=../evidence/S018/staged_build.txt
: > "$LOG"
step() {
  local name=$1; shift
  local t0=$(date +%s)
  lake build "$@" > ../evidence/S018/staged/$name.txt 2>&1
  local rc=$?
  echo "step $name rc=$rc wall_s=$(( $(date +%s) - t0 )) targets: $*" >> "$LOG"
  return $rc
}
step base AlmostStacked.G9.Graph || exit 1
for g in Stack Clear; do
  for t in $(seq 2 15); do
    step check$g$t AlmostStacked.G9.Check$g$t || exit 1
  done
done
step full || exit 1
echo STAGED_BUILD_OK >> "$LOG"
