---
role: proof
locale: en
of_concept: theorem-14-16-existence-formula-pairsets
source_book: gtm008
source_chapter: "14"
source_section: "14"
---

We know that $V^{(\mathbf{B})}$ satisfies the Axiom of Pairing. Boolean-valued pairsets and ordered pairs allow the following reduction.

Let $\varphi(x,y)$ be a formula and $k_1 \in V$. By Theorem 14.15 (which establishes $[\{\check{k}_2, \check{k}_3\} = \check{k}_1] = 1$ iff $\{k_2, k_3\} = k_1$), we compute:

$$
[(\exists x)(\exists y)[\{x, y\} = \check{k}_1 \land \varphi(x, y)]] = \sum_{\{k_2, k_3\} \in k_1} [\{\check{k}_2, \check{k}_3\} = \check{k}_1] [\varphi(\check{k}_2, \check{k}_3)]
$$

$$
= \sum_{\{k_2, k_3\} = k_1} [\varphi(\check{k}_2, \check{k}_3)].
$$

Similarly, for the $\in$ version, in $ZF$:

$$
(\exists x)(\exists y)[\{x, y\} \in \check{k}_1 \land \varphi(x, y)] \leftrightarrow (\exists z \in \check{k}_1)(\exists x)(\exists y)[\{x, y\} = z \land z \in \check{k}_1 \land \varphi(x, y)]
$$

Therefore

$$
[(\exists x)(\exists y)[\{x, y\} \in \check{k}_1 \land \varphi(x, y)]] = \sum_{k \in k_1} [(\exists x)(\exists y)[\{x, y\} = \check{k} \land \varphi(x, y)]]
$$

$$
= \sum_{k \in k_1} \sum_{\{k_2, k_3\} = k} [\varphi(\check{k}_2, \check{k}_3)]
$$

$$
= \sum_{k \in k_1} [\varphi(\check{k}_2, \check{k}_3)].
$$

These reduction formulas express the Boolean value of existential quantifiers bounded by $\check{k}_1$ in terms of ordinary $V$-sums over the check-names for elements of $k_1$.
