# CAM-S014-21: challenge larger odd donors without assuming the size-three pattern

2026-10-15 BEFORE execution. CAM20 completed252 graph boxes/24192 inputs,
with4080 eligible ordered pairs and no failure, but its smaller donor is
ALWAYS3. It says nothing about smaller donors5/7 or arbitrary graphs.

Test ALL4096 edge completions on vertices0..5 containing01,02, excluding12;
the remaining twelve possible edges vary independently. Retain exactly the
connected graphs. No isomorphism quotient. Fix c2=0, c0 in{3,5,7},
c1 in{3,5,7,9} with c0<=c1; c3,c4,c5 independently0/1. At most294912 inputs,
mass6..19. For each LOSER examine pair(0,1), and ALSO(1,0) when counts equal,
and every empty private true head. Labels0/1 select the proposed donor pair;
02/non12 supply a guaranteed candidate, not an assertion about all n6 inputs.
This is a precise bridge-lemma challenge, not a general threshold census.

Use the CAM20 complete negative-DAG/positive-move certificate algorithm;
separately written coordinate verifier repeats exact input generation and
checks every legal negative child and positive dependency down to a pure
pile. No producer imports in checker. Separate source files/input/preflight/
certificates/logs; do not modify CAM20 frozen files. Cap300000 states per graph,
600seconds/2GiB per process; interrupted or capped scopes UNKNOWN.

Record ALL failures, first four exact cases for any later threshold campaign.
Do not infer criticality/global-Q from losing inputs; no ASH* refutation or
universal positive theorem from agreement. Investigate the symbolic count
replacement: for donor3, replacing t->s by s->v has exactly the required
balance; this identity fails for donor5. Follow actual failures/proofs toward
the unrestricted global comparison, keeping even/nonadjacent sites explicit.
