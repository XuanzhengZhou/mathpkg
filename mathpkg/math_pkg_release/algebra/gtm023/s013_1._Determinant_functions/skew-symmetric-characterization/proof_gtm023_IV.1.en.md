---
role: proof
locale: en
of_concept: skew-symmetric-characterization
source_book: gtm023
source_chapter: "IV"
source_section: "§1. Determinant functions"
---

**(i) $\Rightarrow$ (ii).** Suppose $\Phi$ is skew symmetric and $x_i = x_j$ ($i \neq j$). Let $\tau$ be the transposition interchanging $i$ and $j$. Since $x_i = x_j$, we have $(\tau\Phi)(x_1,\ldots,x_p) = \Phi(x_1,\ldots,x_p)$. On the other hand, skew symmetry gives $(\tau\Phi)(x_1,\ldots,x_p) = -\Phi(x_1,\ldots,x_p)$. Hence $2\Phi(x_1,\ldots,x_p) = 0$, and since $\Gamma$ has characteristic zero, $\Phi(x_1,\ldots,x_p) = 0$.

**(ii) $\Rightarrow$ (i).** Assume $\Phi$ satisfies (ii). Fix a pair $i, j$ ($i < j$) and define
$$\Psi(x, y) = \Phi(x_1, \ldots, x, \ldots, y, \ldots, x_p)$$
where the vectors $x_v$ ($v \neq i, j$) are fixed. Then $\Psi(x, x) = 0$ for all $x \in E$. It follows that
\begin{align*}
\Psi(x, y) + \Psi(y, x) &= \Psi(x+y, x+y) - \Psi(x, x) - \Psi(y, y) = 0,
\end{align*}
so $\Psi(y, x) = -\Psi(x, y)$. This gives $\tau\Phi = -\Phi$ for any transposition $\tau$. Since every permutation is a product of transpositions and $\varepsilon$ is a homomorphism, $\sigma\Phi = \varepsilon_\sigma \cdot \Phi$ for all $\sigma \in S_p$.

**(ii) $\Leftrightarrow$ (iii).** Suppose $\Phi$ satisfies (ii) and $x_1,\ldots,x_p$ are linearly dependent. Without loss of generality, assume $x_p = \sum_{v=1}^{p-1} \lambda_v x_v$. By $p$-linearity,
$$\Phi(x_1,\ldots,x_p) = \sum_{v=1}^{p-1} \lambda_v \Phi(x_1,\ldots,x_{p-1}, x_v),$$
and each term on the right vanishes by (ii) since $x_v$ appears twice. Hence $\Phi$ satisfies (iii). The converse (iii) $\Rightarrow$ (ii) is trivial, since $x_i = x_j$ implies linear dependence.
