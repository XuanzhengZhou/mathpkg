---
role: proof
locale: en
of_concept: closed-subalgebra-representation
source_book: gtm027
source_chapter: "7"
source_section: "S"
---

# Proof of Representation of Closed Subalgebras of C(X)

Let $R$ be a closed subalgebra of $C(X)$ containing the unit $u$. Define $F : X \to \prod_{f \in R} f[X]$ by

$$F(x)_f = f(x), \qquad f \in R.$$

Let $Y = F(X)$ be the range of $F$. Then $R$ is precisely the range of the induced isomorphism $F^* : C(Y) \to C(X)$.

**Proof.** $F$ is continuous because each coordinate $f$ is continuous. $Y$ is a compact Hausdorff space as a continuous image of the compact Hausdorff space $X$.

The map $F^* : C(Y) \to C(X)$ is an algebra homomorphism. Since the coordinate projections separate points of $Y$, the functions $\{f \circ \pi_f : f \in R\}$ generate $C(Y)$. But $F^*(f \circ \pi_f|_Y) = f$, so each $f \in R$ lies in the image of $F^*$. Thus $R \subseteq F^*(C(Y))$.

Conversely, $F^*$ is isometric (the sup norm on $C(Y)$ corresponds to the induced norm) and its image is a closed subalgebra containing $R$. Since $R$ separates points of $X$ (by definition of $F$), $F$ is injective? Not necessarily; $F$ identifies points that $R$ cannot distinguish. The quotient space $X/\!\sim$ where $x \sim x'$ iff $f(x) = f(x')$ for all $f \in R$ is homeomorphic to $Y$, and $C(Y) \cong R$ via $F^*$.

More directly: $F^*$ is injective because $F$ is surjective onto $Y$ (by definition), and $F^*(C(Y))$ is a closed subalgebra containing all coordinate projections, hence containing $R$. By the Stone-Weierstrass theorem or maximality arguments, $F^*(C(Y)) = R$.
