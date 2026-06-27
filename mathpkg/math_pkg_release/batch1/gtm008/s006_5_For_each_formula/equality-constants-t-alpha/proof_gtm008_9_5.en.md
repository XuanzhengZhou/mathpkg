---
role: proof
locale: en
of_concept: equality-constants-t-alpha
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

The case $k_1 = k_2$ follows directly from Theorem 9.28.1, which states $\llbracket t = t \rrbracket_{\mathbf{T}_{\alpha}} = 1$ for all $t \in T_{\alpha}$.

For $k_1 \neq k_2$, let $\beta \triangleq \max(\rho(k_1), \rho(k_2))$. By symmetry, we may assume there exists $k$ such that $k \in k_1$ and $k \notin k_2$. Then $\rho(k) < \beta$.

We compute:
$$
\llbracket k_1 = k_2 \rrbracket_{\mathbf{T}_{\alpha}} = \prod_{t \in T_{\alpha}} \llbracket t \in k_1 \leftrightarrow t \in k_2 \rrbracket_{\mathbf{T}_{\alpha}}.
$$

In particular, for $t = k$, we have $k \in k_1$ but $k \notin k_2$, so by the induction hypothesis (on rank), $\llbracket k \in k_1 \rrbracket = 1$ and $\llbracket k \in k_2 \rrbracket = 0$, which forces the product to be $0$. Therefore $\llbracket k_1 = k_2 \rrbracket_{\mathbf{T}_{\alpha}} = 0$.
