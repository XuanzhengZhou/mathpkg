---
role: proof
locale: en
of_concept: induced-map-star-homomorphism
source_book: gtm027
source_chapter: "7"
source_section: "S"
---

# Proof of Induced Map Is an Algebra Homomorphism

Let $X, Y$ be compact Hausdorff spaces and $F : X \to Y$ a continuous map. The induced map $F^* : C(Y) \to C(X)$ is defined by

$$F^*(h) = h \circ F, \qquad h \in C(Y).$$

We prove $F^*$ is a homomorphism of the algebra $C(Y)$ into $C(X)$.

For $h_1, h_2 \in C(Y)$ and $x \in X$:

- **Additivity:** $F^*(h_1 + h_2)(x) = (h_1 + h_2)(F(x)) = h_1(F(x)) + h_2(F(x)) = F^*(h_1)(x) + F^*(h_2)(x)$.

- **Multiplicativity:** $F^*(h_1 h_2)(x) = (h_1 h_2)(F(x)) = h_1(F(x)) h_2(F(x)) = F^*(h_1)(x) F^*(h_2)(x)$.

- **Scalar multiplication:** $F^*(\lambda h)(x) = (\lambda h)(F(x)) = \lambda h(F(x)) = \lambda F^*(h)(x)$ for $\lambda \in \mathbb{R}$.

- **Unit preservation:** $F^*(1_Y)(x) = 1_Y(F(x)) = 1 = 1_X(x)$.

Thus $F^*$ is a unital algebra homomorphism.
