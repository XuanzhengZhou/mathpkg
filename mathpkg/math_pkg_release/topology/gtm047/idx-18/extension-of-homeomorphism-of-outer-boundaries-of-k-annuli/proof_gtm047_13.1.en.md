---
role: proof
locale: en
of_concept: extension-of-homeomorphism-of-outer-boundaries-of-k-annuli
source_book: gtm047
source_chapter: "13"
source_section: "13"
---

**Proof.** $A$ is compact, and therefore $A'$ can be moved far from $A$ by a translation $\mathbb{R}^2 \leftrightarrow \mathbb{R}^2$. Therefore the theorem reduces to the case in which $A \cap A' = \emptyset$. (This merely makes it more convenient to draw pictures.) By the Tame imbedding theorem, we may assume that $A$ and $A'$ are polyhedra.

(I) The theorem holds for $1$-annuli (annuli). 

$A$ is connected. Therefore there is a broken line $B$, joining a point of $J_0$ to a point of $J_1$, and intersecting $\operatorname{Bd} A$ only at its end-points $P_0$ and $P_1$. We may suppose that neither $P_0$ nor $P_1$ is a vertex.

Let $P_0' = f(P_0)$, and let $B'$ be a broken line in $A'$, joining $P_0'$ to a point $P_1'$ of $J_1'$, and intersecting $\operatorname{Bd} A'$ only at its end-points. Using two disjoint broken lines $B_1, B_2$, lying close to $B$ but not intersecting $B$, we decompose $A$ into two $2$-cells $D_1, D_2$, with $B \subset D_1$. Copy this configuration in $A'$, getting $B_1', B_2'$ in $A'$, $B_3' = f(B_3)$, $B_4' = f(B_4)$, $\operatorname{Bd} D_1' = B_3' \cup B_1' \cup B_5' \cup B_2'$, $\operatorname{Bd} D_3' = J_1'$, and so on. Now extend $f$ in the following stages: $B_1 \leftrightarrow B_1'$, $B_2 \leftrightarrow B_2'$, $B_5 \leftrightarrow B_5'$, $D_1 \leftrightarrow D_1'$, $B_6 \leftrightarrow B_6'$, $D_2 \leftrightarrow D_2'$, $D_3 \leftrightarrow D_3'$; and finally map the exterior of $J_0$ onto that of $J_0'$.

(II) If the theorem holds for $k$-annuli, then it holds for $(k+1)$-annuli.

Given two $(k+1)$-annuli $A, A'$, assume that both are polyhedra. The induction proceeds by decomposing a $(k+1)$-annulus into a $k$-annulus and a $1$-annulus, applying the inductive hypothesis to the $k$-annulus parts and case (I) to the $1$-annulus parts, and assembling the resulting homeomorphisms to obtain the desired extension.
