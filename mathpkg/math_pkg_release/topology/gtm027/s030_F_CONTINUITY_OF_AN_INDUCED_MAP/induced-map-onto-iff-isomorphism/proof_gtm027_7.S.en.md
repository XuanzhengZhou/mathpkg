---
role: proof
locale: en
of_concept: induced-map-onto-iff-isomorphism
source_book: gtm027
source_chapter: "7"
source_section: "S"
---

# Proof of Surjectivity of F Characterized by F-star Being an Isomorphism onto a Unital Subalgebra

Let $F : X \to Y$ be continuous between compact Hausdorff spaces. We prove that $F$ maps $X$ onto $Y$ iff $F^* : C(Y) \to C(X)$ is an isomorphism of $C(Y)$ onto a subalgebra of $C(X)$ containing the unit.

($\Rightarrow$) If $F$ is surjective, then for $h_1 \neq h_2 \in C(Y)$, there exists $y \in Y$ with $h_1(y) \neq h_2(y)$. Since $F$ is onto, $y = F(x)$ for some $x \in X$, so $F^*(h_1)(x) = h_1(F(x)) \neq h_2(F(x)) = F^*(h_2)(x)$. Thus $F^*$ is injective. Since $F^*$ is always a homomorphism and preserves the unit, it is an algebra isomorphism onto its image $F^*(C(Y))$, a subalgebra of $C(X)$ containing the unit $1_X = F^*(1_Y)$.

($\Leftarrow$) Suppose $F^*$ is injective. If $F$ were not surjective, then $Y \setminus F(X)$ is a nonempty open set. By Urysohn's lemma for compact Hausdorff spaces, there exists a nonzero continuous function $h : Y \to \mathbb{R}$ with support in $Y \setminus F(X)$. Then $F^*(h) = h \circ F = 0$ (since $h$ vanishes on $F(X)$), but $h \neq 0$, contradicting injectivity. Hence $F$ must be surjective.
