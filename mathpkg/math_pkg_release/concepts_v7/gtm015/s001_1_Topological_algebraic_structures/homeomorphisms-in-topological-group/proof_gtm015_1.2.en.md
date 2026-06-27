---
role: proof
locale: en
of_concept: homeomorphisms-in-topological-group
source_book: gtm015
source_chapter: "1"
source_section: "2"
---

# Proof of Homeomorphisms in a Topological Group

Let $G$ be a topological group. By definition, the mappings
$$(x,y) \mapsto xy \quad \text{and} \quad x \mapsto x^{-1}$$
are continuous on $G$.

**(1) Inversion.** The map $J: G \to G$, $J(x) = x^{-1}$, is continuous by definition. Moreover, $J \circ J = \mathrm{id}_G$, so $J$ is its own inverse. Hence $J$ is a homeomorphism of $G$ onto $G$.

**(2) Left translation.** For fixed $a \in G$, define $L_a: G \to G$ by $L_a(x) = ax$. The map $x \mapsto (a,x)$ is continuous (constant in the first coordinate), and multiplication is continuous; therefore $L_a$ is the composition of continuous maps and thus continuous. Its inverse is $L_{a^{-1}}$, which is also continuous. Hence $L_a$ is a homeomorphism.

**(3) Right translation.** For fixed $b \in G$, define $R_b: G \to G$ by $R_b(x) = xb$. The same argument as in (2) shows that $R_b$ is a homeomorphism, with inverse $R_{b^{-1}}$.

**(4) Combined translation.** The map $x \mapsto axb$ is the composition $L_a \circ R_b$, hence a homeomorphism.

**(5) Inner automorphism.** For fixed $a \in G$, the map $I_a: G \to G$ defined by $I_a(x) = axa^{-1}$ is the composition $L_a \circ R_{a^{-1}}$, hence a homeomorphism.

**(6) The map $x \mapsto xax^{-1}$.** This map can be expressed as the composition
$$x \mapsto (x, a, x^{-1}) \mapsto (x a, x^{-1}) \mapsto (xa) x^{-1} = xax^{-1}.$$
More precisely, write it as $m(m(x,a), x^{-1})$ where $m$ denotes the group multiplication. Since $x \mapsto x$ is continuous, $x \mapsto a$ (constant) is continuous, $x \mapsto x^{-1}$ is continuous, and $m$ is continuous, the whole composition is continuous. This map is not necessarily a homeomorphism (it need not be injective or surjective), but it is continuous. $\square$
