# S014 active administrative snapshot memory recovery

The first resumable scope81 snapshot terminated with MemoryError while
reading a1MiB chunk after saving39,500/50,857 file hashes. It did not finish
or replace the old working_hashes.json. The persisted cache/progress and
exact initial snapshot source are retained. This was administrative hashing,
not a new mathematical search/check or a proof result. No mathematical
certificate, frozen plan, source or failed bounded-run evidence was changed.

Read-only OS diagnostics found repeated resource-exhaustion event2004 entries
on2026-10-16, including13:00:46,13:43:38,13:46:25 host-local timestamps.
They report low virtual memory and name the antimalware and desktop
processes among the largest consumers. This supports resource pressure as
a possible contributor to the owner's reported app exits; it does not
prove which process caused any particular exit. A subsequent snapshot had
10,286,476KiB free physical and55,003,260KiB free virtual memory.

The resumed snapshot uses64KiB streaming chunks and retains its cache every
500 files, with a system memory floor check before starting and after each
saved batch. The governance validator hashes real files independently with
streaming reads and reuses only unchanged in-process stat keys, avoiding
repeated whole-file allocation. All comparisons remain. No security, pagefile,
app or process settings were changed. Universal ASH* remains OPEN; S014 ACTIVE.
