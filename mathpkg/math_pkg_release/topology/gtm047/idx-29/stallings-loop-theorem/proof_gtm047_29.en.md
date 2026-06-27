---
role: proof
locale: en
of_concept: stallings-loop-theorem
source_book: gtm047
source_chapter: ""
source_section: "29"
---

The proof of Theorem 1 occupies the remainder of Section 29 (pages 192-196) and proceeds by a complexity-reduction argument on the singular set of $D$. The singular set consists of those points in $|D|$ whose preimage under $D$ has more than one point. First, $D$ is put into normal form: $D$ is PL, locally a homeomorphism, and at most two-to-one at each point of $\Delta$. The singular set then consists of finitely many polygonal curves $\Gamma_i$ (images of two polygons in $\Delta$) and broken lines $A_j$ (images of two broken lines in $\Delta$). The complexity of $D$ is measured by $(m, n)$, ordered lexicographically, where $m$ is the number of $\Gamma_i$ and $n$ the number of $A_j$.

The proof then considers four cases that could allow a reduction in complexity while preserving the hypothesis. Case 1: a non-self-intersecting singular curve $\Gamma$ bounding a 2-cell in $\Delta$ that is mapped two-to-one — shown impossible by constructing an annulus whose replacement reduces complexity. Case 2: $m > 0$ with an innermost $\Gamma_i$ — the interior of $J_2$ can be remapped homeomorphically to eliminate the singularity, reducing $m$. Cases 3 and 4: $n > 0$ with broken lines $A_j$, distinguished by whether $D$ reverses or preserves orientation on the preimage segments — in either subcase, cutting $|D|$ apart at $A_j$ yields two normal singular 2-cells $D_1$ and $D_2$ whose boundaries are related to $L$ by conjugation, so that the hypothesis $L(B) \cap N = \emptyset$ must fail for at least one of them, allowing replacement of $D$ by $D_i$ with reduced complexity.

Since all four cases lead to contradictions under the assumption that no nonsingular 2-cell exists satisfying the conclusion, it follows that $m = n = 0$, i.e., $D$ is already nonsingular. A further reduction handles the special case where $B$ is a 2-sphere: here $B'$ is a $k$-annulus, $\pi(B', P_0)$ is free on $k$ generators, and the hypothesis forces some generator to lie outside $N'$, yielding a polyhedral 2-cell whose boundary provides the desired nonsingular 2-cell after pushing slightly into $\operatorname{Int} M$.
