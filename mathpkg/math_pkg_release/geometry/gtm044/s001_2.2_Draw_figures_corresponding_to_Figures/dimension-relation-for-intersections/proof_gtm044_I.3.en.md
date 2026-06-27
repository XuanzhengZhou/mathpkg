---
role: proof
locale: en
of_concept: dimension-relation-for-intersections
source_book: gtm044
source_chapter: "I"
source_section: "3"
---

# Proof of Dimension relation for intersections of algebraic sets

The dimension relation is a foundational result in algebraic geometry, stated as follows. For two algebraic sets $V(p_i)$ and $V(p_j)$ in $\mathbb{P}^2(\mathbb{C})$ defined by irreducible polynomials $p_i, p_j$, the codimension of their intersection satisfies:

$$\operatorname{cod}(V(p_i) \cap V(p_j)) \leqslant \operatorname{cod} V(p_i) + \operatorname{cod} V(p_j).$$

In the case of curves in $\mathbb{P}^2(\mathbb{C})$, each curve $V(p_i)$ has codimension $1$ (since $\dim V(p_i) = 1$ and $\dim \mathbb{P}^2(\mathbb{C}) = 2$). Applying the dimension relation:

$$\operatorname{cod}(V(p_i) \cap V(p_j)) \leqslant 1 + 1 = 2.$$

Rewriting in terms of dimension:

$$\dim(V(p_i) \cap V(p_j)) = \dim \mathbb{P}^2(\mathbb{C}) - \operatorname{cod}(V(p_i) \cap V(p_j)) \geqslant 2 - 2 = 0.$$

Hence $\dim(V(p_i) \cap V(p_j)) \geqslant 0$. Since by convention $\dim \emptyset = -1$, this implies

$$V(p_i) \cap V(p_j) \neq \emptyset.$$

Thus any two irreducible algebraic curves in $\mathbb{P}^2(\mathbb{C})$ must intersect. The formal proof of the dimension relation itself belongs to the general theory of dimension in algebraic geometry and is developed in later chapters.

**Remark.** The irreducibility condition (i.e., $p_i$ having no repeated factors) ensures that $V(p_i)$ is an "indecomposable" curve; the result extends to arbitrary curves without common components by decomposing into irreducible components.
