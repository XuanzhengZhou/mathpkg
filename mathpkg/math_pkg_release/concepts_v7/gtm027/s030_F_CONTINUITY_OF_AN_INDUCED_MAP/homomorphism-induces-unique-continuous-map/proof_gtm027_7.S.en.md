---
role: proof
locale: en
of_concept: homomorphism-induces-unique-continuous-map
source_book: gtm027
source_chapter: "7"
source_section: "S"
---

# Proof of Homomorphisms Between Function Algebras Are Induced by Continuous Maps

Let $H : C(Y) \to C(X)$ be a homomorphism of real algebras which carries the unit $1_Y$ to the unit $1_X$. We prove there exists a unique continuous map $F : X \to Y$ such that $H = F^*$.

**Proof.** For each $x \in X$, define the evaluation functional $\phi_x : C(X) \to \mathbb{R}$ by $\phi_x(g) = g(x)$. The composition $\phi_x \circ H : C(Y) \to \mathbb{R}$ is a nonzero real homomorphism (since $H(1_Y) = 1_X$, we have $\phi_x \circ H(1_Y) = 1$).

By the theory of maximal ideals in $C(Y)$ for $Y$ compact Hausdorff, every nonzero real homomorphism $C(Y) \to \mathbb{R}$ is given by evaluation at a unique point of $Y$. Thus there exists a unique $y = F(x) \in Y$ such that $\phi_x \circ H = \phi_y$, i.e., $H(h)(x) = h(F(x))$ for all $h \in C(Y)$.

This defines a map $F : X \to Y$. We verify continuity: a subbasic open set in $Y$ has the form $h^{-1}(U)$ for $h \in C(Y)$ and $U \subseteq \mathbb{R}$ open. Then

$$F^{-1}(h^{-1}(U)) = (h \circ F)^{-1}(U) = H(h)^{-1}(U),$$

which is open in $X$ since $H(h) \in C(X)$ is continuous. Thus $F$ is continuous.

Uniqueness follows from the fact that $C(Y)$ separates points of $Y$: if $F_1, F_2$ both satisfy $H = F_1^* = F_2^*$, then for each $x \in X$ and all $h \in C(Y)$, $h(F_1(x)) = h(F_2(x))$, so $F_1(x) = F_2(x)$.
