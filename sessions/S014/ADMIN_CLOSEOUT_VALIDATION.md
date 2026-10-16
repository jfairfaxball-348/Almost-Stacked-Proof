# Administrative final validation recovery

The initial scope81 rehash failed with a MemoryError. Its raw record and exact
validator source are preserved. A later closed-state validation was externally
terminated at its600second administrative bound; the raw record is
evidence/S014/admin_recovery/closeout_validation_timeout.json. Neither failed
administrative attempt is a mathematical result or an evidence mismatch.

The final retry independently runs ALL existing historical and S014 comparisons,
streaming exact decoded-archive SHA256 and releasing the parsed gap metadata after
its last use. Unbuffered file-backed stdout/stderr avoids undrained-pipe blocking.
The administrative bound is1800seconds/2GiB, with no change to any mathematical
campaign's original600second/state/memory bounds. One worker only; no new search,
later session, scientific claim or stage advancement. Phase progress is printed
without altering comparisons. The recursive final manifest is regenerated after
the resulting log is written, then independently rechecked read-only.

The first file-backed run completed25seconds in with an intentional version
conflict: the S006 manifest pins the original .gitattributes, while S014 needs
raw-byte preservation for already-frozen CRLF metadata and process logs. Preserve
the exact original7a49bb6909edb009cdeae26a1fe0c24997695a097bffbb416e97ce838ade111e
attributes as a separate S014 archive, retain the S006 manifest unchanged, and
validate that exact old path/digest against the archive. Current attributes must
explicitly protect the four S014 scopes. This is version reconciliation, not a
generic hash bypass or a rewrite of frozen scientific evidence. Raw failure and
exact validator source remain archived. Future entries must use this current
reconciliation rather than rerun historical entry scripts against changed mirrors.

The following full retry passed every historical comparison, all S014 preflights,
execution rows and exact summaries, then found a checker name collision: an older
summary variable `re` shadowed the regex module used by the new final manifest.
Its source/raw failure are separately preserved. Rename only that local summary
variable and retain all comparisons. Also resolve backslashes in the96 archived
relative Windows formula arguments when hashing on Linux CI, without rewriting
any log or relaxing expected digests. These administrative issues add no
mathematical failure, proof or counterexample.
