---
role: proof
locale: en
of_concept: product-of-morphisms
source_book: gtm004
source_chapter: "II"
source_section: "5"
---

# Proof of the Product of Morphisms

Let $\{f_i : X_i \to Y_i\}_{i \in I}$ be a family of morphisms in $\mathfrak{C}$. Let $(X; p_i) = \prod_i X_i$ and $(Y; q_i) = \prod_i Y_i$ be the respective products.

For each $i \in I$, consider the morphism $f_i p_i : X \to Y_i$. By the universal property of the product $(Y; q_i)$, there exists a unique morphism $\prod_i f_i : X \to Y$ such that

$$q_i \left( \prod_i f_i \right) = f_i p_i \quad \text{for all } i \in I.$$

This defines the product of morphisms. Moreover, if $\mathfrak{C}$ admits products for all families indexed by $I$, then $\prod_i$ is a functor

$$\prod_i : \mathfrak{C}^I \to \mathfrak{C},$$

where $\mathfrak{C}^I$ is the category of $I$-indexed families of objects of $\mathfrak{C}$ (the $I$-fold product category).
