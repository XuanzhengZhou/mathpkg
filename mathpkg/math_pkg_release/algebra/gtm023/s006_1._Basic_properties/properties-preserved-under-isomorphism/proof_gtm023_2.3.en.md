---
role: proof
locale: en
of_concept: properties-preserved-under-isomorphism
source_book: gtm023
source_chapter: "2"
source_section: "§3. Linear isomorphisms, 2.13"
---
All three properties follow directly from the fact that $\varphi$ is a bijective linear map, so it preserves all linear relations.

**Property I.** Since $\varphi$ is injective, a relation $\sum \lambda_i \varphi(e_i) = 0$ implies $\varphi(\sum \lambda_i e_i) = 0$, hence $\sum \lambda_i e_i = 0$. Thus linear independence is preserved. Since $\varphi$ is surjective, every $y \in F$ can be written as $\varphi(x)$ with $x$ expressible as a linear combination of the generating set, so the image is generating. A basis, being both linearly independent and generating, is therefore preserved.

**Property II.** The restriction $\varphi|_{E_1}: E_1 \to \varphi(E_1)$ is injective (as a restriction of an injective map) and surjective by definition of $\varphi(E_1)$, hence an isomorphism. For the quotient, define $\bar{\varphi}(x + E_1) = \varphi(x) + \varphi(E_1)$. This is well-defined because if $x - y \in E_1$, then $\varphi(x) - \varphi(y) = \varphi(x - y) \in \varphi(E_1)$. Bijectivity of $\varphi$ then yields bijectivity of $\bar{\varphi}$, and linearity follows as in the induced map construction.

**Property III.** The map $\psi \mapsto \psi \circ \varphi^{-1}$ is linear and has inverse $\chi \mapsto \chi \circ \varphi$, so it is an isomorphism. Similarly, $\psi \mapsto \varphi \circ \psi$ has inverse $\chi \mapsto \varphi^{-1} \circ \chi$.
