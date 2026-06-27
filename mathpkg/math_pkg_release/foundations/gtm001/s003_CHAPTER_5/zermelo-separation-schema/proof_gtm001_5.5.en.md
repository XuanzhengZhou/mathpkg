---
role: proof
locale: en
of_concept: zermelo-separation-schema
source_book: gtm001
source_chapter: "5"
source_section: "5"
---

Applying Axiom 5 (Replacement) to the well-formed formula $b \in A \wedge b = c$ where $b$ and $c$ do not occur in $A$, we verify the single-valuedness condition:

$$(\forall x, y, z) [x \in A \wedge x = y] \wedge [x \in A \wedge x = z] \rightarrow y = z.$$

This holds because if $x = y$ and $x = z$, then $y = z$. Therefore, by Axiom 5,

$$\mathcal{M}(\{y \mid (\exists x \in a) [x \in A \land x = y]\}).$$

But $\{y \mid (\exists x \in a) [x \in A \land x = y]\} = a \cap A$, hence

$$\mathcal{M}(a \cap A).$$
