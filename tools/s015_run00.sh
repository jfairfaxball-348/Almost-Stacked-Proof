#!/bin/bash
# S015_BIN: directory holding binaries built from tools/s015_layers_v3.cpp and tools/s015_check_v2.c (scratch path redacted to a variable at closeout)
cd /home/user/Almost-Stacked-Proof/evidence/S015/cam85
p=$1
bash -c "ulimit -v 4000000; ${S015_BIN:-/tmp/s015}/s015_layers_v3 300 2000000000 crit_prod_$p.txt < $p > prod_$p.txt"; echo "P $p done $(date +%T)" >> runlog.txt
bash -c "ulimit -v 4000000; ${S015_BIN:-/tmp/s015}/s015_check_v2 150000000 300 crit_chk_$p.txt < $p > chk_$p.txt"; echo "C $p done $(date +%T)" >> runlog.txt
