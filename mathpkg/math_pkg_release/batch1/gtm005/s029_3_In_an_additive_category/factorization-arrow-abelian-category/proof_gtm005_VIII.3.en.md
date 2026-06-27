---
role: proof
locale: en
of_concept: factorization-arrow-abelian-category
source_book: gtm005
source_chapter: "VIII"
source_section: "3"
---

Set $m = \ker(\operatorname{coker} f)$ and $e = \operatorname{coker}(\ker f)$. By construction, $m$ is monic (as a kernel) and $e$ is epi (as a cokernel). Since $(\operatorname{coker} f) \circ f = 0$, the arrow $f$ factors through $m = \ker(\operatorname{coker} f)$ as $f = m e$ for a unique $e$. Dually, since $f \circ (\ker f) = 0$, $f$ factors through $e = \operatorname{coker}(\ker f)$. The uniqueness of these factorizations via universal properties ensures the two constructions of $e$ coincide, yielding $f = me$ with $m$ monic and $e$ epi.

For the functoriality: given two factorizations $f = me$ and $f' = m'e'$, any morphism $\langle g, h \rangle : f \rightarrow f'$ (i.e., arrows $g : \operatorname{dom} f \rightarrow \operatorname{dom} f'$ and $h : \operatorname{cod} f \rightarrow \operatorname{cod} f'$ with $h f = f' g$) induces a unique arrow $k$ between the intermediate objects making the diagram commute:

\[
\begin{CD}
\cdot @>e>> \cdot @>m>> \cdot \\
@V{g}VV @V{k}VV @V{h}VV \\
\cdot @>e'>> \cdot @>m'>> \cdot
\end{CD}
\]

In particular, taking $f = f'$ and the identity morphism $\langle 1, 1 \rangle : f \rightarrow f$, the induced $k$ is an isomorphism, proving that any two monic-epi factorizations of $f$ are isomorphic.
