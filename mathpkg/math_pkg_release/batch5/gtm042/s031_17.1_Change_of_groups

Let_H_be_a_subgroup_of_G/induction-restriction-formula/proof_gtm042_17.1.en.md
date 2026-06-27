---
role: proof
locale: en
of_concept: induction-restriction-formula
source_book: gtm042
source_chapter: "17"
source_section: "17.1"
---

Using the associativity of the tensor product, we obtain the formula

$$\text{Ind}_H^G(x \cdot \text{Res}_H^G y) = \text{Ind}_H^G(x) \cdot y$$

in each of the three situations. The proof is the same in all cases: induction is given by the tensor product $\text{Ind}_H^G(-) = k[G] \otimes_{k[H]} (-)$ (or $K[G] \otimes_{K[H]} (-)$ in case (a)), and restriction $\text{Res}_H^G$ simply views a $k[G]$-module as a $k[H]$-module. The associativity of the tensor product yields the required identity. Specifically, for case (b): if $x$ corresponds to a $k[H]$-module $X$ and $y$ to a $k[G]$-module $Y$, then

$$\text{Ind}_H^G(x \cdot \text{Res}_H^G y) = k[G] \otimes_{k[H]} (X \otimes_k Y) \cong (k[G] \otimes_{k[H]} X) \otimes_k Y = \text{Ind}_H^G(x) \cdot y,$$

where we use that $k[G] \otimes_{k[H]} (X \otimes_k Y) \cong (k[G] \otimes_{k[H]} X) \otimes_k Y$ by associativity of the tensor product and the fact that $Y$ is a $k[G]$-module (so the $k[H]$-action on $X \otimes_k Y$ comes only from the $X$ factor). The same argument applies mutatis mutandis for cases (a) and (c).
