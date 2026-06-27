---
role: proof
locale: en
of_concept: palmquist-bijection
source_book: gtm005
source_chapter: "IV"
source_section: "7"
---

Given adjunctions $F \dashv G$, $F' \dashv G'$ with $F, F': D \to C$ and $G, G': C \to D$, there is a bijection
$$\operatorname{Nat}(F', F) \cong \operatorname{Nat}(G, G'),$$
called the mates correspondence.

Given $\sigma: F' \Rightarrow F$, define its mate $\bar{\sigma}: G \Rightarrow G'$ by:
$$G \xrightarrow{\eta' G} G' F' G \xrightarrow{G' \sigma G} G' F G \xrightarrow{G' \varepsilon} G'.$$

Conversely, given $\tau: G \Rightarrow G'$, define its mate $\bar{\tau}: F' \Rightarrow F$ by:
$$F' \xrightarrow{F' \eta} F' G F \xrightarrow{F' \tau F} F' G' F \xrightarrow{\varepsilon' F} F.$$

The triangle identities of the adjunctions ensure these are mutually inverse. The naturality follows from the naturality of the units and counits.
