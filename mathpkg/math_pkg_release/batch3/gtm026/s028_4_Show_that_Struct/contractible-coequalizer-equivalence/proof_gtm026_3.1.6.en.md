---
role: proof
locale: en
of_concept: contractible-coequalizer-equivalent-conditions
source_book: gtm026
source_chapter: "3"
source_section: "1.6"
---

If $(f, g, h; d, d')$ is a contractible coequalizer, then $f.d.g = f.h.d' = g.h.d' = g.d.g$. Conversely, suppose $d: B \longrightarrow A$ exists subject to $d.f = \mathrm{id}_B$ and $f.d.g = g.d.g$. As $f.d.g = g.d.g$ and $h = \mathrm{coeq}(f, g)$, there exists a unique $d': C \longrightarrow B$ such that $h.d' = d.g$; as $h$ is epi and $h.d'.h = d.g.h = d.f.h = h$, we have $d'.h = \mathrm{id}_C$.
