---
role: proof
locale: en
of_concept: associativity-of-product
source_book: gtm004
source_chapter: "II"
source_section: "5"
---

# Proof of the Associativity of the Product

Let $\mathfrak{C}$ be a category in which any two objects admit a product. Given objects $X, Y, Z$ in $\mathfrak{C}$, we have projections

$$p_1 : X \times Y \to X, \quad p_2 : X \times Y \to Y,$$
$$q_1 : (X \times Y) \times Z \to X \times Y, \quad q_2 : (X \times Y) \times Z \to Z.$$

We claim that $((X \times Y) \times Z; p_1 q_1, p_2 q_1, q_2)$ is the product of $X, Y, Z$.

Given morphisms $f : W \to X$, $g : W \to Y$, $h : W \to Z$, we first form $\{f, g\} : W \to X \times Y$ via the universal property of $X \times Y$. Then we form $\{\{f, g\}, h\} : W \to (X \times Y) \times Z$ via the universal property of $(X \times Y) \times Z$. This morphism satisfies

$$(p_1 q_1) \{\{f, g\}, h\} = p_1 \{f, g\} = f,$$
$$(p_2 q_1) \{\{f, g\}, h\} = p_2 \{f, g\} = g,$$
$$q_2 \{\{f, g\}, h\} = h,$$

and is uniquely determined by these equations. Thus $(X \times Y) \times Z$ is the ternary product of $X, Y, Z$. By symmetry, $X \times (Y \times Z)$ is also a ternary product, and by the uniqueness of products (Theorem 5.1), they are canonically isomorphic.
