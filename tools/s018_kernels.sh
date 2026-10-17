#!/usr/bin/env bash
# S018 PLAN_AMENDMENT_2: standalone sequential replays of the bundled external kernels on one Solution export.
# usage: s018_kernels.sh <Solution.export> <workdir> <log>   (12 GiB watchdog runs separately: tools/s018_memcap.ps1)
set -u
EXP=$1; W=$2; LOG=$3
B=$(dirname "$(elan which lean)")
mkdir -p "$W"
python -I -c "import json,sys;json.dump(dict(use_stdin=False,export_file_path=sys.argv[1],permitted_axioms=['propext','Quot.sound','Classical.choice'],unpermitted_axiom_hard_error=False,num_threads=1,nat_extension=True,string_extension=True),open(sys.argv[2],'w'))" "$(cygpath -m "$EXP")" "$W/nanoda.json"
run() {
  local name=$1; shift
  local t0=$(date +%s)
  timeout 7200 "$@" > "$W/$name.out" 2>&1
  local rc=$?
  echo "kernel $name rc=$rc wall_s=$(( $(date +%s)-t0 )) out_tail=$(tail -c 300 "$W/$name.out" | tr '\n' ' ')" >> "$LOG"
}
echo "utc_start $(date -u +%FT%TZ) export_sha256 $(sha256sum "$EXP" | cut -d' ' -f1)" > "$LOG"
run nanoda_t1 "$B/nanoda_bin" "$(cygpath -m "$W/nanoda.json")"
run con-ron_j1 "$B/con-ron" --jobs=1 "$EXP"
run lean4lean "$B/lean4lean" --import "$EXP"
run leanchecker-paranoid "$B/leanchecker-paranoid" --silent --from-export "$EXP"
run con-leche "$B/con-leche" "$EXP"
echo "utc_end $(date -u +%FT%TZ)" >> "$LOG"
