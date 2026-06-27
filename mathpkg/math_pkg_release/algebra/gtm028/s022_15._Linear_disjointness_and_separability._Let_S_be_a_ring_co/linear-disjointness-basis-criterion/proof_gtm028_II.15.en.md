---
role: proof
locale: en
of_concept: linear-disjointness-basis-criterion
source_book: gtm028
source_chapter: "II"
source_section: "§15. Linear disjointness and separability"
---

**Proof.** First consider the case where $L$ and $L'$ have finite bases $\{u_1, \dots, u_s\}$ and $\{u'_1, \dots, u'_t\}$ respectively. If $L$ and $L'$ are linearly disjoint, then by definition the products $\{u_i u'_j\}$ are linearly independent over $k$, since the basis elements are linearly independent sets.

Conversely, suppose the $st$ products $u_i u'_j$ are linearly independent over $k$. Let $x_1, \dots, x_n \in L$ be linearly independent over $k$ and $x'_1, \dots, x'_m \in L'$ be linearly independent over $k$. Express each $x_i$ as a linear combination of the $u_p$ and each $x'_j$ as a linear combination of the $u'_q$. The $mn$ products $x_i x'_j$ can then be expressed as linear combinations of the $u_p u'_q$. If a nontrivial $k$-linear relation held among the $x_i x'_j$, then by the independence of the $u_p u'_q$ we would obtain a contradiction to the linear independence of the $x_i$ and $x'_j$. More precisely, any $k$-linear relation among the $x_i x'_j$ would, after expansion, yield a relation among the $u_p u'_q$. The coefficients of this relation would force the original relation to be trivial. Hence the $mn$ products $x_i x'_j$ are linearly independent over $k$, and this proves the linear disjointness of $L$ and $L'$ over $k$. This also establishes the second half of the lemma.

In the general case, we can always find a finite subset $\{u_1, u_2, \dots, u_s\}$ of the set $\{u_\alpha\}$ such that the elements $x_1, x_2, \dots, x_n$ belong to the finite-dimensional space $L_0$ spanned by $u_1, u_2, \dots, u_s$. Similarly, there exists an integer $t$ such that $x'_j \in L'_0 = k u'_1 + k u'_2 + \cdots + k u'_t$, $j = 1, 2, \dots, m$. If the products $u_\alpha u'_\beta$ are linearly independent over $k$, then a fortiori the products $u_i u'_j$ ($i = 1, \dots, s$; $j = 1, \dots, t$) are linearly independent over $k$. Since $L_0$ and $L'_0$ are linearly disjoint over $k$ by the preceding finite-dimensional case, the products $x_i x'_j$ are linearly independent over $k$. This completes the proof of the lemma.
