---
role: proof
locale: en
of_concept: schurs-lemma
source_book: gtm042
source_chapter: "2"
source_section: "2.2"
---

The case $f = 0$ is trivial. Suppose $f \neq 0$ and let $W_1$ be its kernel. For $x \in W_1$ we have $f\rho_s^1 x = \rho_s^2 fx = 0$, whence $\rho_s^1 x \in W_1$, so $W_1$ is stable under $G$. Since $V_1$ is irreducible, $W_1$ is either $V_1$ or 0. The first case is excluded as it implies $f = 0$. Thus $W_1 = 0$ and $f$ is injective.

The same argument shows that the image $W_2$ of $f$ is equal to $V_2$ (otherwise $W_2 = 0$, contradicting $f \neq 0$). Hence $f$ is an isomorphism. This proves (1): if $\rho^1$ and $\rho^2$ are not isomorphic, we must have $f = 0$.

For (2), suppose $V_1 = V_2 = V$ and $\rho^1 = \rho^2 = \rho$. The field $\mathbb{C}$ being algebraically closed, $f$ has an eigenvalue $\lambda$. Set $f' = f - \lambda \cdot 1$. Then $\rho_s \circ f' = f' \circ \rho_s$ for all $s$, and $\ker(f') \neq 0$. Since $V$ is irreducible, $\ker(f') = V$, so $f' = 0$ and $f = \lambda \cdot 1$.
