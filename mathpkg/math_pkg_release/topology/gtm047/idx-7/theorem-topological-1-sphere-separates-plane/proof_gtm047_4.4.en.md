---
role: proof
locale: en
of_concept: theorem-topological-1-sphere-separates-plane
source_book: gtm047
source_chapter: "4"
source_section: "4"
---

Let $\bar{I}$ be a polyhedral $2$-cell containing $J$, such that $J \cap \operatorname{Fr} I$ contains exactly two points $P$ and $R$. (Fill in the details for the construction of such an $\bar{I}$.) Then $J$ is the union of two arcs $A_1$ and $A_2$, from $P$ to $R$. Take a broken line $B$, from $S$ to $Q$, in $\bar{I}$, and intersecting $\operatorname{Fr} I$ only at $S$ and $Q$. Let $T$ be the first point of $B$ (in the order from $S$ to $Q$) which lies in $J$; let $A_1$ be the arc from $P$ to $R$ in $J$ that contains $T$; and let $A_2$ be the other arc from $P$ to $R$ in $J$. Let $X$ be the last point of $B$ that lies in $A_1$. (See Figure 4.2.)

**Lemma 1.** $A_2$ contains a point of $B$, following $X$ in the order from $S$ to $Q$ on $B$.

PROOF. Suppose not. Let $B_1$ be the arc $ST$ in $B$; let $B_2$ be the arc $TX$ in $A_1$; and let $B_3$ be the arc $XQ$ in $B$. Then $B_1 \cup B_2 \cup B_3$ is an arc $SQ$, in $\bar{I} - A_2$. Therefore $S$ and $Q$ lie in the frontier of the same component of $I - A_2$; and this contradicts the preceding theorem.

Now let $Y$ be the first point of $B$ that lies in $A_2$ and follows $X$ in $B$ (in the order from $S$ to $Q$). Let $Z$ be any point between $X$ and $Y$ in $B$.

**Lemma 2.** $Z$ lies in a bounded component of $\mathbf{R}^2 - J$.

PROOF. Suppose not. Then there is a broken line $B_1$, from $Z$ to a point $W$ of $\operatorname{Fr} I$, with $B_1 \subset \mathbf{R}^2 - J$. We may suppose that $B_1 \cap \operatorname{Fr} I = W$, since otherwise a shorter broken line would have the same properties. Consider first the case in which $W$ and $S$ lie in the same component of $\operatorname{Fr} I - \{P, R\}$. (See Figure 4.3.)

$B$ contains an arc $B_2$, from $Z$ to $Q$, not intersecting $A_1$. It follows that $W$ and $Q$ are in the frontier of the same component of $I - A_1$, and this contradicts the preceding theorem.

Suppose, second, that $W$ and $Q$ lie in the same component of $\operatorname{Fr} I - \{P, R\}$. (See Figure 4.4.) As before, let $T$ be the lowest point of $B = SQ$ that lies on $A_1$. Form the union of the arcs $B_1$, $ZX \subset QS$, $XT \subset A_1$, and $TS \subset SQ$. It follows that $W$ and $S$ lie in the frontier of the same component of $I - A_2$, and this contradicts the preceding theorem, as before.

Evidently Lemma 2 proves Theorem 3.
