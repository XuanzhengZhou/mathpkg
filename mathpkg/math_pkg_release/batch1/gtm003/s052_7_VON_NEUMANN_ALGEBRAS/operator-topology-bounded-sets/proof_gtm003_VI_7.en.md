---
role: proof
locale: en
of_concept: operator-topology-bounded-sets
source_book: gtm003
source_chapter: "VI"
source_section: "7"
---

Denote by $\mathfrak{B}_j$ ($j = 1, 2, 3, 4$) the families of bounded sets for: the norm topology, the $\sigma$-weak topology, the strong operator topology, and the weak operator topology respectively.

$\mathfrak{B}_1 = \mathfrak{B}_2$: Since $\mathcal{L}(H)$ is the Banach dual of the projective tensor product $H \hat{\otimes} H$ (the space of trace class operators), the norm-bounded sets and the $\sigma$-weakly bounded sets coincide by the general duality theory of Banach spaces.

$\mathfrak{B}_1 = \mathfrak{B}_3$: This follows from the principle of uniform boundedness. If a set $B \subset \mathcal{L}(H)$ is strongly bounded (i.e., $\sup_{u \in B} \|u\xi\| < \infty$ for each $\xi \in H$), then by the Banach-Steinhaus theorem, $\sup_{u \in B} \|u\| < \infty$, so $B$ is norm-bounded. The converse is trivial.

$\mathfrak{B}_3 = \mathfrak{B}_4$: The strong and weak operator topologies have the same dual space $H \otimes H$ (the space of finite-rank operators). For locally convex spaces with the same dual, the bounded sets coincide.

The final assertion about multiplication being $(\mathfrak{B}, \mathfrak{B})$-hypocontinuous and uniformly continuous on $B \times B$ for bounded $B$ follows from (III, 5.2) and (III, 5.3).
