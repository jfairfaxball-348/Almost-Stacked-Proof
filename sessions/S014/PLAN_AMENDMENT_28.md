# CAM-S014-28: retain the source singleton in heavy elimination

2026-10-15 BEFORE execution. H2 from CAM27 is FALSE, already on P3 critical
(3,3,0): removing the ENTIRE source forbids the real AS loser(1,5,0).
Do not call that absence a global obstruction. New distinct hypothesis H2r:
for EVERY critical non-AS STACK loser, some ordered heavy s,t, residual
r in{0,1}, k in{0,1,2} with r+k<=c_s, and k initially empty sites U give

    d=c-(c_s-r)*s+(c_s-r-k)*t+1_U

losing. Each d has exactly ONE fewer heavy site and same mass, so the
UNIVERSAL hypothesis would imply ASH* by induction. It is unproved.
The r1,k0 case includes the established even/parity concentration; r0,k1
includes long/nonlocal heads; r0/1,k2 handles additional parity choices.

Use precisely the SAME444 fixed STACK critical cases and ALL1230 non-AS
inputs as CAM27. No cutoff/graph expansion. Enumerate EVERY ordered heavy
pair, r/k/U candidate, record first four input-existence failures. Separate
v2 code/output/preflight; CAM27 files/failed hypothesis retained. Packed
membership producer versus separately regenerated coordinate-key checker,
same300000 candidates/input,600s/2GiB/process. Freeze every original input/
certificate/code/plan/environment hash. No universal extrapolation or closeout.
