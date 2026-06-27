---
role: proof
locale: en
of_concept: contractible-coequalizer-equivalent-conditions
source_book: gtm026
source_chapter: "3"
source_section: "1"
---

If $(f, g, h; d, d')$ is a contractible coequalizer as in diagram 1.3, then
$$f \cdot d \cdot g = f \cdot h \cdot d' = g \cdot h \cdot d' = g \cdot d \cdot g.$$

Conversely, suppose $d: B \to A$ exists subject to condition 2. As $f \cdot d \cdot g = g \cdot d \cdot g$ and $h = \operatorname{coeq}(f, g)$, there exists a unique $d': C \to B$ such that $h \cdot d' = d \cdot g$. As $h$ is epi and
$$h \cdot d' \cdot h = d \cdot g \cdot h = d \cdot f \cdot h = h,$$
we have $d' \cdot h = \mathrm{id}_C$. Together with $d \cdot f = \mathrm{id}_B$, this shows that $(f, g, h; d, d')$ is a contractible coequalizer.
