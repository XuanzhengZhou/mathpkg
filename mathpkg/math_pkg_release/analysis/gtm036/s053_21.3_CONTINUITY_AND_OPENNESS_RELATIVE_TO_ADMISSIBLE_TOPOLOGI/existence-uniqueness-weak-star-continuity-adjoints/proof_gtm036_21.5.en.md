---
role: proof
locale: en
of_concept: existence-uniqueness-weak-star-continuity-adjoints
source_book: gtm036
source_chapter: "21"
source_section: "21.3"
---

These results are immediate consequences of Theorem 21.1 applied to the natural pairings $\langle E, E^*\rangle$ and $\langle F, F^*\rangle$.

**Proof of (i):** If $T$ is continuous in the original locally convex topology, then it is certainly weakly continuous, since the weak topology is weaker. By 21.1, $T$ has a dual if and only if $T$ is weakly continuous; in the natural pairing setting, this dual is precisely the adjoint $T^*$. The uniqueness of $T^*$ follows from the fact that $E$ distinguishes elements of $E^*$ (so there is at most one dual transformation). Weak$^*$ continuity of $T^*$ follows from 21.1, which states that the dual of a weakly continuous transformation is weak$^*$ continuous.

**Proof of (ii):** By 21.1, $S$ is the dual of some $T$ (i.e., the adjoint) if and only if $S$ is weak$^*$ continuous. The transformation $T$ is then weakly continuous by the same theorem, and uniqueness follows since $E$ and $F$ distinguish their respective duals.
