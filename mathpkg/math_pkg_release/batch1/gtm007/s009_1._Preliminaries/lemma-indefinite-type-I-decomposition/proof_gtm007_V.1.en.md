---
role: proof
locale: en
of_concept: lemma-indefinite-type-I-decomposition
source_book: gtm007
source_chapter: "V"
source_section: "§1. Preliminaries"
---

By Theorem 3, there exists $x \in E$, $x \neq 0$ with $x \cdot x = 0$. Being free to divide $x$ by an integer, we may assume $x$ is indivisible. By Lemma 3, there exists $y \in E$ such that $x \cdot y = 1$. We can arrange that $y \cdot y$ is odd: if $y \cdot y$ is even, pick $t \in E$ with $t \cdot t$ odd (possible since $E$ is type I) and replace $y$ by $t + (1 - x \cdot t)y$. This preserves $x \cdot y = 1$ and makes $y \cdot y \equiv t \cdot t \pmod{2}$, hence odd.

Write $y \cdot y = 2m + 1$. Set $e_1 = y - m x$ and $e_2 = y - (m+1)x$. One checks:
$$
e_1 \cdot e_1 = 1, \quad e_2 \cdot e_2 = -1, \quad e_1 \cdot e_2 = 0.
$$
The sublattice $G = \langle e_1, e_2 \rangle$ is isomorphic to $I_+ \oplus I_-$ (with Gram matrix $\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$). By Lemma 1 (orthogonal splitting), $E \simeq G \oplus G^\perp$, so $E \simeq I_+ \oplus I_- \oplus F$ with $F = G^\perp \in S_{n-2}$.
