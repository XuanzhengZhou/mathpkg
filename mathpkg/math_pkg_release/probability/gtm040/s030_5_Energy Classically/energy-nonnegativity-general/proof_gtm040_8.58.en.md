---
role: proof
locale: en
of_concept: energy-nonnegativity-general
source_book: gtm040
source_chapter: "8"
source_section: "5"
---

Write $g = Nf = Nf^+ - Nf^-$, where $Nf^+$ and $Nf^-$ are pure potentials. Then

$$\mathbf{I}(g) = (g, g) = (Nf^+ - Nf^-, Nf^+ - Nf^-)$$
$$= \mathbf{I}(Nf^+) - 2(Nf^+, Nf^-) + \mathbf{I}(Nf^-)$$
$$\geq \mathbf{I}(Nf^+) - 2\sqrt{\mathbf{I}(Nf^+)\mathbf{I}(Nf^-)} + \mathbf{I}(Nf^-)$$
$$= \left(\sqrt{\mathbf{I}(Nf^+)} - \sqrt{\mathbf{I}(Nf^-)}\right)^2$$
$$\geq 0.$$

The inequality in the third line follows from Lemma 8-57 (Schwarz's inequality for pure potentials), which gives $(Nf^+, Nf^-) \leq \sqrt{\mathbf{I}(Nf^+)\mathbf{I}(Nf^-)}$.
