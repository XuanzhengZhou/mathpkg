---
role: proof
locale: en
of_concept: t-i-delta-functor
source_book: gtm052
source_chapter: "III"
source_section: "12"
---

Clearly each $T^i$ is an additive, covariant functor. Since $\mathcal{F}$ is flat over $Y$, for any exact sequence

$$0 \to M' \to M \to M'' \to 0$$

of $A$-modules, we get an exact sequence

$$0 \to \mathcal{F} \otimes M' \to \mathcal{F} \otimes M \to \mathcal{F} \otimes M'' \to 0$$

of sheaves on $X$. Taking cohomology, we obtain a long exact sequence

$$\cdots \to T^i(M') \to T^i(M) \to T^i(M'') \to T^{i+1}(M') \to \cdots$$

which shows that each $T^i$ is exact in the middle and the collection $(T^i)$ forms a $\delta$-functor.

To verify the $\delta$-functor property formally, we use a Cech resolution. Let $\mathfrak{U}$ be a finite affine open cover of $X$. Then for each $A$-module $M$, we have

$$C^\bullet(\mathfrak{U}, \mathcal{F} \otimes_A M) = C^\bullet(\mathfrak{U}, \mathcal{F}) \otimes_A M,$$

since tensor product commutes with finite products. Writing $C^\bullet = C^\bullet(\mathfrak{U}, \mathcal{F})$, we obtain

$$T^i(M) = h^i(C^\bullet \otimes_A M)$$

for each $M$. The exactness in the middle property then follows from the fact that for any short exact sequence of $A$-modules, the sequence of complexes $C^\bullet \otimes M' \to C^\bullet \otimes M \to C^\bullet \otimes M''$ is exact (since $C^\bullet$ is a complex of flat $A$-modules, because $\mathcal{F}$ is flat over $Y$), and applying $h^i$ gives exactness in the middle.
