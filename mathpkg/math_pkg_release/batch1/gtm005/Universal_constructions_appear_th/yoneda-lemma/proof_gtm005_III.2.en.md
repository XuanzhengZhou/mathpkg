---
role: proof
locale: en
of_concept: yoneda-lemma
source_book: gtm005
source_chapter: "III"
source_section: "2. The Yoneda Lemma"
---

Define the map $y \colon \operatorname{Nat}(D(r, -), K) \to Kr$ by $y(\alpha) = \alpha_r(1_r)$. For an element $x \in Kr$, we must construct a natural transformation $\alpha$ with $\alpha_r(1_r) = x$. For any object $d \in D$ and any arrow $f \colon r \to d$, naturality of $\alpha$ would require

$$
\alpha_d(f) = \alpha_d \circ D(r, f)(1_r) = K(f) \circ \alpha_r(1_r) = K(f)(x).
$$

This forces the definition $\alpha_d(f) = K(f)(x)$ for all $f \in D(r, d)$. To verify naturality of the $\alpha$ so defined: for any $g \colon d \to d'$ and $f \colon r \to d$, we have

$$
\alpha_{d'} \circ D(r, g)(f) = \alpha_{d'}(g \circ f) = K(g \circ f)(x) = K(g) \circ K(f)(x) = K(g) \circ \alpha_d(f),
$$

which is the required naturality condition. Thus $y$ is a bijection, with inverse $x \mapsto \alpha$ defined by $\alpha_d(f) = K(f)(x)$. The map $y$ is natural in both $K$ and $r$, as can be verified by considering the functor category $\mathbf{Set}^D$.
