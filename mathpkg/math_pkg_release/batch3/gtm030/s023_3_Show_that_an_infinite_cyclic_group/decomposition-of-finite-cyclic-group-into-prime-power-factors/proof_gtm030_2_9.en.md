---
role: proof
locale: en
of_concept: decomposition-of-finite-cyclic-group-into-prime-power-factors
source_book: gtm030
source_chapter: "2"
source_section: "9"
---

Let $\mathfrak{G}_i$ be the subgroup of order $p_i^{e_i}$ and set $\mathfrak{G}' = \mathfrak{G}_1\mathfrak{G}_2 \cdots \mathfrak{G}_s$. This subgroup has order $n'$ divisible by $p_i^{e_i}$ since $\mathfrak{G}' \supseteq \mathfrak{G}_i$. Hence $n'$ is divisible by $n = p_1^{e_1}p_2^{e_2} \cdots p_s^{e_s}$. It follows that $n' = n$ and that $\mathfrak{G}' = \mathfrak{G}$.

Next let $\mathfrak{H}_i$ be the subgroup of $\mathfrak{G}$ of order $n_i = n/p_i^{e_i}$. Let $\mathfrak{Z}_i = \mathfrak{H}_i \cap \mathfrak{G}_i$. Then $\mathfrak{Z}_i$ is a subgroup of $\mathfrak{G}$ whose order is a divisor of $n_i$ and of $p_i^{e_i}$. Since $(n_i, p_i^{e_i}) = 1$, this implies that $\mathfrak{Z}_i = 1$, that is, $\mathfrak{H}_i \cap \mathfrak{G}_i = 1$.

Since the order of $\mathfrak{G}_j$ is divisible by $p_j^{e_j}$, $j \neq i$, we have $\mathfrak{H}_i \supseteq \mathfrak{G}_j$ for $j \neq i$. Consequently, $\mathfrak{G}_i \cap \mathfrak{G}_1 \cdots \mathfrak{G}_{i-1} \mathfrak{G}_{i+1} \cdots \mathfrak{G}_n = 1$. The theorem now follows from the criterion of Theorem 5 (conditions (21) and (22)).

We remark also that the conditions (21) and (22) imply the conditions (1) and (2) of the present theorem. This was established in the proof of Theorem 5.
