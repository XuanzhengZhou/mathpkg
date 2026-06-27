---
role: proof
locale: en
of_concept: simple-homotopy-equivalence-characterization
source_book: gtm010
source_chapter: "5"
source_section: "5"
---

(a) $\Rightarrow$ (b): By definition, there is a formal deformation $K = K_0 \to K_1 \to \dots \to K_q = L$ such that $f$ is homotopic to any deformation associated with this formal deformation. Let $g = g_{q-1} \dots g_1 g_0$ be such a deformation, where $g_i: K_i \to K_{i+1}$. Notice that for all $i$, $M_{g_i} \searrow \text{dom } g_i = K_i$. For if $K_i \nearrow K_{i+1}$, then $M_{g_i} = (K_i \times I) \cup_{g_i} K_{i+1} \searrow (K_i \times I) \searrow K_i \times 0 \equiv K_i$. And if $K_i \searrow K_{i+1}$, then by (5.4), $M_{g_i} \searrow M_{g_i|_{K_{i+1}}} \cup K_i = (K_{i+1} \times I) \cup (K_i \times 0) \searrow K_i \times 0 \equiv K_i$. Thus $M_g \wedge M_{g_0} \cup \dots \cup M_{g_{q-1}}$ rel $K_0$, by (5.7) $\searrow (M_{g_0} \cup \dots \cup M_{g_{q-2}}) \searrow \dots \searrow M_{g_0} \searrow K_0 = K$.

(b) $\Rightarrow$ (c): Suppose $g$ is a cellular approximation to $f$ such that $M_g \wedge K$ rel $K$, and $g'$ is any cellular approximation to $f$. Then by (5.5), $M_{g'} \wedge M_g \wedge K$ rel $K$.

(c) $\Rightarrow$ (a): Let $g$ be any cellular approximation to $f$. Since $M_g \wedge K$ rel $K$ and $M_g \searrow L$, we have $K \wedge M_g \searrow L$. The composition $K \to M_g \to L$ gives a simple-homotopy equivalence homotopic to $f$.
