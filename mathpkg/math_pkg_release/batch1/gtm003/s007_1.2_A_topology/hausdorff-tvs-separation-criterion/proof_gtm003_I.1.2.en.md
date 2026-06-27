---
role: proof
locale: en
of_concept: hausdorff-tvs-separation-criterion
source_book: gtm003
source_chapter: "I"
source_section: "1.2"
---

By Theorem 1.3, each neighborhood of any point $x \in L$ contains a closed neighborhood; hence if $\{0\}$ is closed, then every singleton $\{x\} = x + \{0\}$ is closed (by translation invariance), so $L$ is a $T_1$-space. In a topological group, $T_1$ is equivalent to Hausdorff.

Moreover, by Proposition 1.4, every t.v.s. is uniformisable with a translation-invariant uniformity. A uniform space is separated (Hausdorff) if and only if the intersection of all entourages is the diagonal. Under the correspondence between entourages and $0$-neighborhoods in a translation-invariant uniformity, this translates to $\bigcap \{U : U \in \mathfrak{U}\} = \{0\}$. The equivalent condition stating that for each non-zero $x$ there exists a $0$-neighborhood $U$ with $x \notin U$ is immediate from Theorem 1.3: if $x \neq 0$, then $\{0\}$ is closed, so there exists a $0$-neighborhood $U$ not containing $x$.
