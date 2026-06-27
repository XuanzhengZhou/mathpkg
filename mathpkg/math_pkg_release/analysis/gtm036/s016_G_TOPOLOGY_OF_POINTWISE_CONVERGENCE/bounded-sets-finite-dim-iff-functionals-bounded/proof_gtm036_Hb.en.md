---
role: proof
locale: en
of_concept: bounded-sets-finite-dim-iff-functionals-bounded
source_book: gtm036
source_chapter: "H"
source_section: "H(b)"
---

($\Rightarrow$) Suppose every bounded subset of $E$ is contained in a finite-dimensional subspace. Let $f$ be any linear functional on $E$ and let $B$ be any bounded set. Then $B \subseteq F$ for some finite-dimensional subspace $F$. On the finite-dimensional Hausdorff linear topological space $F$, every linear functional is continuous (since there is a unique Hausdorff vector topology on a finite-dimensional space), hence bounded. Thus $f|_{F}$ is bounded, so $f$ is bounded on $B$.

($\Leftarrow$) Suppose every linear functional on $E$ is bounded. Assume, for contradiction, that there exists a bounded set $A \subseteq E$ not contained in any finite-dimensional subspace. By statement (a) of this section, there exists a linear functional $f$ on $E$ that is not bounded on $A$, contradicting the hypothesis. Therefore every bounded set must be contained in a finite-dimensional subspace.
