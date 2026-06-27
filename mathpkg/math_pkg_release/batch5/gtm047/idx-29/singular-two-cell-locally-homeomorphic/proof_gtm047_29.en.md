---
role: proof
locale: en
of_concept: singular-two-cell-locally-homeomorphic
source_book: gtm047
source_chapter: ""
source_section: "29"
---

The proof occupies the body of Section 29 (pages 192-196). First $D$ is put into normal form with a well-defined singular set. The singular set of $D$ is the set of points in $|D|$ whose preimage under $D$ has more than one point. Under the normal form, the singular set consists of finitely many polygonal curves $\Gamma_1, \Gamma_2, \ldots, \Gamma_m$ (each being the image of two disjoint polygons in $\Delta$) and finitely many broken lines $A_1, A_2, \ldots, A_n$ (each being the image of two disjoint broken lines in $\Delta$). Define the complexity of $D$ as $(m, n)$ ordered lexicographically.

The proof proceeds by analyzing four mutually exclusive cases:

**Case 1.** A singular curve $\Gamma$ that is the image of two polygons in $\Delta$ where identification is of the sort giving crossing rather than touching singularities. The rectangular regions in $|D|$ can be replaced by an annulus formed from a cylinder, reducing complexity — a contradiction.

**Case 2.** $m > 0$, and $\Gamma = \Gamma_i$ is the image of two disjoint polygons $J_1, J_2 \subset \Delta$. Taking $J_1$ innermost (bounding a 2-cell in $\Delta$ containing no other such polygon), $\Gamma$ bounds a 2-cell $\Delta_1 \subset |D|$. The interior of $J_2$ can be mapped homeomorphically onto $\Delta_1$ and forced off a neighborhood of $\Delta_1$, reducing $m$ — a contradiction.

Since Cases 1 and 2 cannot occur, $m = 0$.

**Case 3.** $n > 0$, and $A_j$ is the image of two disjoint broken lines $a_1b_1, a_2b_2$ where $D$ **reverses** orientation. Cutting $|D|$ apart at $A_j$ yields two normal singular 2-cells $D_1$ and $D_2$ with boundaries

$$L_1 = \sigma v^{-1}, \quad L_2 = \sigma \phi v \tau.$$

By algebraic manipulation using the group structure of conjugacy classes, $L$ is a product of transforms of $L_1$ and $L_2$. Since $L(B') \cap N' = \emptyset$ but $N'$ is normal, it follows that at least one of $L_1(B') \cap N' = \emptyset$ or $L_2(B') \cap N' = \emptyset$ holds. Replacing $D$ by the appropriate $D_i$ preserves the hypothesis while reducing complexity — a contradiction.

**Case 4.** $n > 0$, and $A_j$ is the image of two disjoint broken lines $a_1b_1, a_2b_2$ where $D$ **preserves** orientation. A similar cutting argument applies, again leading to a contradiction.

Since all four cases lead to contradictions, it must be that $m = n = 0$, i.e., $D$ has empty singular set and is therefore nonsingular. The lemma also handles the special situation where $B$ is a 2-sphere: here $B'$ is a $k$-annulus, $\pi(B')$ is free on $k$ generators, and if all generators belonged to $N'$ then $N' = \pi(B')$, contradicting $L(B') \cap N' = \emptyset$. Thus some generator $p_i \notin N'$ bounds a polyhedral 2-cell in $B$; pushing this slightly into $\operatorname{Int} M$ yields the desired $D_1$.
