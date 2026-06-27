---
role: proof
locale: en
of_concept: lies-theorem
source_book: gtm009
source_chapter: "II"
source_section: "4.1"
---
The proof uses induction on $\dim L$, with the case $\dim L = 0$ being trivial. The strategy closely parallels Engel's Theorem.

\textbf{Step 1}: Since $L$ is solvable, $[LL] \subsetneqq L$. Choose a subspace of codimension one containing $[LL]$, which is automatically an ideal $K$ of $L$. Thus $L = K + Fz$ for some $z \in L$.

\textbf{Step 2}: By induction, $K$ has a common eigenvector $v \in V$, so there exists a linear functional $\lambda: K \to F$ such that $x.v = \lambda(x)v$ for all $x \in K$. Define the weight space $W = \{w \in V \mid x.w = \lambda(x)w \text{ for all } x \in K\}$, which is nonzero since it contains $v$.

\textbf{Step 3}: Show that $L$ leaves $W$ invariant. For $w \in W$, $x \in L$, and $y \in K$, we compute $yx.w = xy.w - [x,y].w = \lambda(y)x.w - \lambda([x,y])w$. To prove $x.w \in W$, we need $\lambda([x,y]) = 0$ for all $y \in K$. This is established by a clever argument: fix $w \in W$, $x \in L$, and let $n$ be minimal such that $w, x.w, \ldots, x^n.w$ are linearly dependent. Let $W_i = \operatorname{span}\{w, x.w, \ldots, x^{i-1}.w\}$. Each $y \in K$ acts on $W_n$ with matrix having $\lambda(y)$ on the diagonal, so $\operatorname{Tr}_{W_n}(y) = n\lambda(y)$. But $[x,y] \in K$ acts with trace zero on $W_n$ (since it is a commutator on an $x$-stable subspace), so $n\lambda([x,y]) = 0$, hence $\lambda([x,y]) = 0$ (since $\operatorname{char} F = 0$). Thus $W$ is $L$-stable.

\textbf{Step 4}: Since $F$ is algebraically closed, the action of $z$ on $W$ has an eigenvector $v_0 \in W$ with eigenvalue $\mu$. Then $v_0$ is a common eigenvector for all of $L = K + Fz$.
