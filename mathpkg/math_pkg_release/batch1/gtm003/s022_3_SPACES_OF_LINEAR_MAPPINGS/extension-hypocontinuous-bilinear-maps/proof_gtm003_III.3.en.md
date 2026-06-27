---
role: proof
locale: en
of_concept: extension-hypocontinuous-bilinear-maps
source_book: gtm003
source_chapter: "III"
source_section: "3"
---

We may assume \(\mathfrak{S}, \mathfrak{T}\) are directed under \(\subset\) (no loss of generality); then so are \(\{S \times T : S \in \mathfrak{S}, T \in \mathfrak{T}\}\) and \(\{S_1 \times T_1\}\).

For each \(S \in \mathfrak{S}\) and \(T \in \mathfrak{T}\), \(S \times T\) is dense in the uniform space \(S_1 \times T_1\). By Proposition 5.3, the restriction \(f_{S,T}\) of the bilinear map \(f\) to \(S \times T\) maps into a bounded subset of \(G\). Since \(G\) is quasi-complete and Hausdorff, the bounded set \(f(S \times T)\) is contained in a complete subset, and the uniform continuity of \(f\) on \(S \times T\) (which follows from \(\mathfrak{S}\)-hypocontinuity and the identity expressing \(f(x,y) - f(x',y')\) as a sum of three terms) allows unique extension to a continuous map \(\overline{f}_{S_1,T_1} : S_1 \times T_1 \to G\).

These extensions are compatible on overlaps because the families are directed. Since \(\mathfrak{S}_1\) and \(\mathfrak{T}_1\) cover \(E_1\) and \(F_1\) respectively, the extensions piece together to define a bilinear map on \(E_1 \times F_1\). The bilinearity follows from the density of \(E \times F\) and separate continuity. The \((\mathfrak{S}_1, \mathfrak{T}_1)\)-hypocontinuity follows from the construction using the closures.
