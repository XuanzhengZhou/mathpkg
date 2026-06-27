---
role: proof
locale: en
of_concept: uniqueness-of-products
source_book: gtm004
source_chapter: "II"
source_section: "5"
---

# Proof of the Uniqueness of Products up to Isomorphism

Let $(X; p_i)$ and $(X'; p'_i)$ both be products of the family $\{X_i\}_{i \in I}$ in the category $\mathfrak{C}$.

By the universal property for $X$, there exists a unique morphism $\eta : X' \to X$ such that $p_i \eta = p'_i$ for all $i \in I$. Similarly, by the universal property for $X'$, there exists a unique morphism $\xi : X \to X'$ such that $p'_i \xi = p_i$ for all $i \in I$.

Now compose:

$$p_i \eta \xi = p'_i \xi = p_i = p_i 1_X \quad \text{for all } i \in I.$$

By the uniqueness property of the product $(X; p_i)$, the morphism making this diagram commute is unique; hence $\eta \xi = 1_X$. A symmetric argument gives $\xi \eta = 1_{X'}$.

Thus $\xi : X \to X'$ is an isomorphism with inverse $\eta$, uniquely determined by the condition $p'_i \xi = p_i$ for all $i \in I$.
