---
role: proof
locale: en
of_concept: cyclic-group-direct-product-decomposition
source_book: gtm030
source_chapter: "V"
source_section: "9"
---

Let $\mathfrak{G}_i$ be the unique subgroup of $\mathfrak{G}$ of order $p_i^{e_i}$ (Theorem 4). Set $\mathfrak{G}' = \mathfrak{G}_1 \mathfrak{G}_2 \cdots \mathfrak{G}_s$. The order of $\mathfrak{G}'$ is divisible by each $p_i^{e_i}$ since $\mathfrak{G}_i \subseteq \mathfrak{G}'$, hence by their product $n$. Since $\mathfrak{G}' \subseteq \mathfrak{G}$ and $|\mathfrak{G}| = n$, we have $\mathfrak{G}' = \mathfrak{G}$.

Let $\mathfrak{H}_i$ be the subgroup of $\mathfrak{G}$ of order $n/p_i^{e_i}$ and let $\mathfrak{Z}_i = \mathfrak{H}_i \cap \mathfrak{G}_i$. Then $|\mathfrak{Z}_i|$ divides both $n/p_i^{e_i}$ and $p_i^{e_i}$, which are coprime, so $\mathfrak{Z}_i = 1$. Since $\mathfrak{H}_i = \mathfrak{G}_1 \cdots \mathfrak{G}_{i-1} \mathfrak{G}_{i+1} \cdots \mathfrak{G}_s$, condition (2) of the criterion holds. By the internal direct product criterion, $\mathfrak{G} \cong \mathfrak{G}_1 \times \cdots \times \mathfrak{G}_s$.
