#!/bin/bash
# S015_BIN: directory holding binaries built from tools/s015_layers_v3.cpp and tools/s015_check_v2.c (scratch path redacted to a variable at closeout)
# runs producer then checker per chunk; 4 parallel slots via xargs
cd /home/user/Almost-Stacked-Proof/evidence/S015/cam85
job() { kind=$1; c=$2
  if [ $kind = P ]; then bash -c "ulimit -v 4000000; ${S015_BIN:-/tmp/s015}/s015_layers_v3 300 2000000000 crit_prod_$c.txt < $c > prod_$c.txt"
  else bash -c "ulimit -v 4000000; ${S015_BIN:-/tmp/s015}/s015_check_v2 150000000 300 crit_chk_$c.txt < $c > chk_$c.txt"; fi
  echo "$kind $c done rc=$? $(date +%T)" >> runlog.txt; }
export -f job
s=$(date +%s)
for c in chunk_0{7,6,5,4,3,2,1,0}; do echo P $c; echo C $c; done | xargs -P 4 -n 2 bash -c 'job "$0" "$1"'
echo "ALL DONE $(( $(date +%s)-s ))s" >> runlog.txt
