---
role: proof
locale: en
of_concept: natural-mapping-commutes-with-induced-transformation
source_book: gtm031
source_chapter: "IV"
source_section: "2"
---

By definition, the induced transformation $\bar{A}$ satisfies $\bar{x}\bar{A} = \overline{xA}$ for every $x \in \Re$. The natural mapping $P$ is defined by $P(x) = \bar{x} = x + \mathfrak{S}$.

For any $x \in \Re$, we compute both sides:

$$(P\bar{A})(x) = (P(x))\bar{A} = \bar{x}\bar{A} = \overline{xA},$$

$$(AP)(x) = A(P(x)) = A(\bar{x})?$$

Wait — the notation requires care. $P$ maps $\Re \to \bar{\Re}$ and $\bar{A}$ maps $\bar{\Re} \to \bar{\Re}$, so $P\bar{A}$ means first apply $P$ then $\bar{A}$: $(P\bar{A})(x) = \bar{x}\bar{A} = \overline{xA}$.

On the other hand, $A$ maps $\Re \to \Re$ and $P$ maps $\Re \to \bar{\Re}$. The composition $AP$ means first apply $A$ then $P$: $(AP)(x) = P(A(x)) = P(xA) = \overline{xA}$.

Thus $(P\bar{A})(x) = \overline{xA} = (AP)(x)$ for every $x \in \Re$, which proves $P\bar{A} = AP$.
