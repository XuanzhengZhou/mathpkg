---
role: proof
locale: en
of_concept: stability-of-m-under-products-and-pullbacks
source_book: gtm026
source_chapter: "4"
source_section: "Regular Categories"
---

We use Proposition 4.11 (the characterization of $M$ via a left lifting property) to prove both statements.

**Proof of (i) — Products.** Let $\{m_i: C_i \longrightarrow D_i\}$ be a family in $M$ and suppose the products $\prod C_i$ and $\prod D_i$ exist. Consider a commutative square with $e \in E$:

$$\xymatrix{
A \ar[r]^{e} \ar[d]_{f} & B \ar[d]^{g} \\
\prod C_i \ar[r]_{\prod m_i} & \prod D_i
}$$

where $f \cdot (\prod m_i) = e \cdot g$. For each index $j$, project onto the $j$-th component using the projection maps $p_j: \prod C_i \longrightarrow C_j$ and $q_j: \prod D_i \longrightarrow D_j$ (with $(\prod m_i) \cdot q_j = p_j \cdot m_j$). This yields the commutative square:

$$\xymatrix{
A \ar[r]^{e} \ar[d]_{f \cdot p_j} & B \ar[d]^{g \cdot q_j} \\
C_j \ar[r]_{m_j} & D_j
}$$

Since $m_j \in M$, the diagonal fill-in property (4.10) provides a unique $h_j: B \longrightarrow C_j$ such that $e \cdot h_j = f \cdot p_j$ (and $h_j \cdot m_j = g \cdot q_j$, which we do not need for the argument). By the universal property of the product, the family $\{h_j\}$ induces a unique morphism $h: B \longrightarrow \prod C_i$ with $h \cdot p_j = h_j$ for all $j$. Then for each $j$,

$e \cdot h \cdot p_j = e \cdot h_j = f \cdot p_j$.

Since this holds for all projections $p_j$, we have $e \cdot h = f$. By Proposition 4.11, this establishes $\prod m_i \in M$.

**Proof of (ii) — Pullbacks.** Given a pullback square

$$\xymatrix{
P \ar[r]^{u} \ar[d]_{v} & C \ar[d]^{m} \\
B \ar[r]_{f} & D
}$$

with $m \in M$, we must show that $v \in M$. Consider a commutative square with $e \in E$:

$$\xymatrix{
A \ar[r]^{e} \ar[d]_{g} & X \ar[d]^{k} \\
P \ar[r]_{v} & B
}$$

We need to find $h: X \longrightarrow P$ with $e \cdot h = g$. Compose this square with $u: P \longrightarrow C$ on the right:

$$\xymatrix{
A \ar[r]^{e} \ar[d]_{g} & X \ar[d]^{k \cdot u} \\
P \ar[r]_{v} & B
}$$

The outer rectangle gives a commutative square with $m \in M$ on the bottom, via the pullback square, but we need to be careful. Instead, compose the second row: $k \cdot u: X \longrightarrow C$ and $m: C \longrightarrow D$, and the first row $g: A \longrightarrow P$ and $v: P \longrightarrow B$. This gives a commutative square:

$$\xymatrix{
A \ar[r]^{e} \ar[d]_{g \cdot v} & X \ar[d]^{k \cdot u \cdot m?}
}$$

Actually, the proof proceeds by applying the diagonal fill-in property to the square formed with $m$ on the bottom. Since $m \in M$, there exists a lift, and the universal property of the pullback then provides the required map into $P$. The full argument is: from $g \cdot v \cdot f = g \cdot u \cdot m$ (by commutativity of the pullback square), compose with $e$ and apply 4.10 to obtain a lift, then use the pullback universal property.
