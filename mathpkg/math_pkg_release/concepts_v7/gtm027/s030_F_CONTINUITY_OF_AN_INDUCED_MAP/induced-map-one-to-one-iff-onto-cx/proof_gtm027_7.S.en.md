---
role: proof
locale: en
of_concept: induced-map-one-to-one-iff-onto-cx
source_book: gtm027
source_chapter: "7"
source_section: "S"
---

# Proof of Injectivity of F Characterized by F-star Mapping onto C(X)

Let $F : X \to Y$ be continuous between compact Hausdorff spaces. We prove that $F$ is one-to-one iff $F^*$ maps $C(Y)$ onto $C(X)$.

($\Rightarrow$) Suppose $F$ is injective. Then $F$ is a continuous bijection between compact Hausdorff spaces, hence a homeomorphism. Thus $F^{-1} : F(X) \to X$ is continuous. For any $g \in C(X)$, define $h = g \circ F^{-1}$ on $F(X)$. By the Tietze extension theorem, $h$ extends to a continuous function $\tilde{h}$ on $Y$. Then $F^*(\tilde{h}) = \tilde{h} \circ F = g \circ F^{-1} \circ F = g$, so $g$ is in the image of $F^*$. Hence $F^*$ is surjective.

Alternatively, since $F$ is a closed map (continuous from compact to Hausdorff) and injective, it is an embedding. The restriction map $C(Y) \to C(F(X))$ is surjective by Tietze, and composing with the homeomorphism $F^{-1} : F(X) \to X$ gives $C(Y) \to C(X)$ surjective.

($\Leftarrow$) If $F^*$ is surjective, suppose $F(x_1) = F(x_2)$ for $x_1 \neq x_2$. By Urysohn's lemma, there exists $g \in C(X)$ with $g(x_1) = 0$, $g(x_2) = 1$. Since $F^*$ is surjective, $g = F^*(h)$ for some $h \in C(Y)$. Then

$$0 = g(x_1) = h(F(x_1)) = h(F(x_2)) = g(x_2) = 1,$$

a contradiction. Hence $F$ is injective.
