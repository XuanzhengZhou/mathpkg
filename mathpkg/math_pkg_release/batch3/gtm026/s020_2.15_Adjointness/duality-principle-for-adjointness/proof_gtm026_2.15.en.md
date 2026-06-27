---
role: proof
locale: en
of_concept: duality-principle-for-adjointness
source_book: gtm026
source_chapter: "2"
source_section: "2.15"
---

The duality principle follows immediately by inspecting the defining data of an adjointness under the passage to opposite categories. Consider the diagram

$$
\mathcal{K}^{\text{op}} \xrightarrow{U^{\text{op}}} \mathcal{A}^{\text{op}}.
$$

The opposite functors $F^{\text{op}}: \mathcal{A}^{\text{op}} \longrightarrow \mathcal{K}^{\text{op}}$ and $U^{\text{op}}: \mathcal{K}^{\text{op}} \longrightarrow \mathcal{A}^{\text{op}}$ reverse the direction of the original functors. The natural transformations $\varepsilon: UF \longrightarrow \text{id}_{\mathcal{A}}$ and $\eta: \text{id}_{\mathcal{K}} \longrightarrow FU$ become $\varepsilon^{\text{op}}: \text{id}_{\mathcal{A}^{\text{op}}} \longrightarrow F^{\text{op}}U^{\text{op}}$ and $\eta^{\text{op}}: U^{\text{op}}F^{\text{op}} \longrightarrow \text{id}_{\mathcal{K}^{\text{op}}}$ respectively (note the reversal of both domain and codomain and the reversal of arrows within the natural transformation). The triangular identities are preserved under this reversal, yielding the adjointness $(\mathcal{K}^{\text{op}}, \mathcal{A}^{\text{op}}, F^{\text{op}}, U^{\text{op}}, \varepsilon, \eta)$.
