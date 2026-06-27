---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A rank structure is a pair $(V, r)$ consisting of a finite set $V$ and an integer-valued function $r$ on subsets of $V$ satisfying three axioms: normalization ($r(\emptyset) = 0$), bounded increase ($r(U \cup \{x\})$ increases by at most $1$ when a single element is added), and local semimodularity (if adding $x_1$ or $x_2$ individually does not increase the rank, then adding both together does not increase it either). Rank structures are equivalent to matroid independence systems: the rank $r(U)$ is the maximum cardinality of an independent subset of $U$, and conversely, a set is independent iff its cardinality equals its rank.
