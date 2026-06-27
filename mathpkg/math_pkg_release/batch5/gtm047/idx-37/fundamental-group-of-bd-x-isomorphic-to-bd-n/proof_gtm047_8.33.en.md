---
role: proof
locale: en
of_concept: fundamental-group-of-bd-x-isomorphic-to-bd-n
source_book: gtm047
source_chapter: "8"
source_section: "33"
---

There is a PL homeomorphism $\phi: \operatorname{Bd} N \times (0, 1) \leftrightarrow \operatorname{Int} N' - K'$. Let $X_1 = X - K'$, $X_2 = \operatorname{Int} N' - \operatorname{Int} X_1$, so that $X_1 \cup X_2 = \operatorname{Int} N' - K'$ and $X_1 \cap X_2 = \operatorname{Bd} X$.

For any choice of base point $P_0$ in $\operatorname{Bd} X$, we need consider only PL paths in forming the fundamental group $\pi(\operatorname{Bd} X) = \pi(\operatorname{Bd} X, P_0)$. Evidently every PL closed path in $\operatorname{Int} N' - K'$, with base point $P_0$, is equivalent to a finite product of PL closed paths in $X_1$ and PL closed paths in $X_2$. We show that every PL closed path $p$ in $X_1$, with base point $P_0$, is equivalent in $\pi(\operatorname{Int} N' - K', P_0)$ to a PL closed path $r$ in $\operatorname{Bd} X$.

Since $X_1$ and $X_2$ are essentially symmetric relative to the product structure induced by $\phi$, the analogous result follows for $X_2$, completing the proof.

Now $X_1$ lies in a set of one of the types $\phi(\operatorname{Bd} N \times [\varepsilon, 1])$ and $\phi(\operatorname{Bd} N \times (0, \varepsilon])$, where $0 < \varepsilon < 1$ and the indicated intervals are half open. Suppose $X_1 \subset \phi(\operatorname{Bd} N \times (0, \varepsilon])$ and that $\varepsilon$ is the smallest number for which this holds. It follows that $\operatorname{Bd} X_1$ (which equals $\operatorname{Bd} X$) intersects $\phi(\operatorname{Bd} N \times \{\varepsilon\})$ in a set $G$ that separates certain subsets in the product.

Then $G$ separates $V$ from $W$ in $[0,1]^2$, because $\psi(G)$ separates $\psi(V)$ from $\psi(W)$ in $|\psi|$. By Theorem 30.2, some component $G_1$ of $G$ also separates $V$ from $W$, and $G_1$ must intersect both boundaries. It follows that there is a broken line $B$ in $G$ from a point of one side to a point of the other. Let $r$ be a path which traverses $B$ exactly once. Then $\phi(r)$ is a PL closed path in $\operatorname{Bd} X$, with base point $P_0$, and $p \cong r$ in $\pi(\operatorname{Int} N' - K')$. As indicated earlier, this is sufficient for the proof of the lemma.
