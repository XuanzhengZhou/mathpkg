---
role: proof
locale: en
of_concept: induced-map-topological-inverse
source_book: gtm027
source_chapter: "7"
source_section: "S"
---

# Proof of Induced Map of a Homeomorphism Is an Isomorphism with Inverse

Let $F : X \to Y$ be a topological map (homeomorphism) between compact Hausdorff spaces. We prove $(F^{-1})^* = (F^*)^{-1}$.

Since $F$ is a homeomorphism, $F^{-1} : Y \to X$ is continuous. The induced maps are $F^* : C(Y) \to C(X)$ and $(F^{-1})^* : C(X) \to C(Y)$.

For any $g \in C(X)$ and $y \in Y$:

$$F^*((F^{-1})^*(g))(y) = (F^{-1})^*(g)(F(y)) = g(F^{-1}(F(y))) = g(y),$$

so $F^* \circ (F^{-1})^* = \operatorname{id}_{C(X)}$. Similarly,

$$(F^{-1})^*(F^*(h))(x) = F^*(h)(F^{-1}(x)) = h(F(F^{-1}(x))) = h(x)$$

for $h \in C(Y)$, $x \in X$, so $(F^{-1})^* \circ F^* = \operatorname{id}_{C(Y)}$.

Thus $(F^{-1})^* = (F^*)^{-1}$.
