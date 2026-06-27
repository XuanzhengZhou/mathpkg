---
role: proof
locale: en
of_concept: product-as-functor
source_book: gtm004
source_chapter: "II"
source_section: "5"
---

# Proof that the Product is a Functor

Assume $\mathfrak{C}$ admits products for all families indexed by a fixed set $I$. For each $I$-indexed family $\{X_i\}_{i \in I}$ of objects of $\mathfrak{C}$, choose a product $(\prod_i X_i; p_i)$.

Given a morphism $\{f_i : X_i \to Y_i\}$ in the product category $\mathfrak{C}^I$, we define $\prod_i f_i : \prod_i X_i \to \prod_i Y_i$ as the unique morphism satisfying $q_i (\prod_i f_i) = f_i p_i$ for all $i$, where $(Y; q_i) = \prod_i Y_i$.

To verify functoriality:
- **Identity**: $\prod_i 1_{X_i} = 1_{\prod_i X_i}$, since $p_i 1_{\prod_i X_i} = 1_{X_i} p_i = p_i$.
- **Composition**: Given $\{f_i\}$ followed by $\{g_i\}$, we have $r_i (\prod_i g_i)(\prod_i f_i) = g_i q_i (\prod_i f_i) = g_i f_i p_i = r_i (\prod_i (g_i f_i))$, where $(Z; r_i) = \prod_i Z_i$. By uniqueness, $(\prod_i g_i)(\prod_i f_i) = \prod_i (g_i f_i)$.

Thus $\prod_i : \mathfrak{C}^I \to \mathfrak{C}$ is a functor.
