---
role: proof
locale: en
of_concept: lies-theorem
source_book: gtm009
source_chapter: "4"
source_section: "4.1"
---

\textbf{Proof.} Use induction on $\dim L$. The case $\dim L = 0$ is trivial.

Step (1): Since $L$ is solvable, $[LL]$ is a proper ideal of $L$. Let $K$ be a subspace of $L$ of codimension one containing $[LL]$. Then $K$ is an ideal of $L$ (since $[L, K] \subset [L, L] \subset K$), and $K$ is solvable by heredity.

Step (2): By induction, there exists a common eigenvector for $K$, i.e., nonzero $v \in V$ and a linear function $\lambda: K \rightarrow F$ such that $x.v = \lambda(x)v$ for all $x \in K$. Fix $\lambda$ and define $W = \{w \in V \mid x.w = \lambda(x)w, \text{ for all } x \in K\}$; then $W \neq 0$.

Step (3): Show that $L$ stabilizes $W$. Let $w \in W$, $x \in L$, and $y \in K$. Then
$$y x.w = x y.w - [x, y].w = \lambda(y) x.w - \lambda([x,y]) w.$$
To prove $x.w \in W$, we must show $\lambda([x,y]) = 0$ for all $y \in K$. Fix $w \in W$, $x \in L$. Let $n > 0$ be the smallest integer for which $w, x.w, \ldots, x^n.w$ are linearly dependent. Define $W_i = \text{span}\{w, x.w, \ldots, x^{i-1}.w\}$, so $\dim W_n = n$. One checks that each $y \in K$ leaves each $W_i$ invariant. With respect to the basis $w, x.w, \ldots, x^{n-1}.w$ of $W_n$, the matrix of $y$ is upper triangular with diagonal entries all equal to $\lambda(y)$. Taking traces, $\text{Tr}_{W_n}([x,y]) = x.\text{Tr}_{W_n}(y) - \text{Tr}_{W_n}(y).x = 0$. But $[x,y]$ is upper triangular with diagonal entries $\lambda([x,y])$, so $n \lambda([x,y]) = 0$. Since $\text{char } F = 0$, $\lambda([x,y]) = 0$.

Step (4): Write $L = K + Fz$, and use algebraic closure to find an eigenvector $v_0 \in W$ of $z$. Then $v_0$ is a common eigenvector for all of $L$.

\textbf{Corollary A (Lie's Theorem).} If $L$ is a solvable subalgebra of $\mathfrak{gl}(V)$, then $L$ stabilizes some flag in $V$, i.e., the matrices of $L$ relative to a suitable basis of $V$ are upper triangular.

\textbf{Corollary B.} If $L$ is solvable, then $[LL]$ is nilpotent.

\textbf{Corollary C.} $L$ is solvable if and only if $\text{ad } L$ is solvable.
