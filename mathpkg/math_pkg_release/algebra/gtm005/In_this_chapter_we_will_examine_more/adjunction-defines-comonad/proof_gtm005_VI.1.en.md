---
role: proof
locale: en
of_concept: adjunction-defines-comonad
source_book: gtm005
source_chapter: "VI. Monads and Algebras"
source_section: "1. Monads in a Category"
---

This statement is the formal dual of the proposition that every adjunction defines a monad. The verification is obtained by reversing all arrows in the proof for monads.

Explicitly, let $L = FG$, $\varepsilon$ be the counit of the adjunction, and $\delta = F\eta G$. We verify the comonad axioms.

\textbf{Coassociativity:} We must show $\delta L \circ \delta = L\delta \circ \delta$. Computing,
$$
\delta L \circ \delta = (F\eta GFG) \circ (F\eta G) = F(\eta GF \circ \eta)G,
$$
$$
L\delta \circ \delta = (FGF\eta G) \circ (F\eta G) = F(F\eta \circ \eta)G.
$$
By naturality of $\eta$, $\eta GF \circ \eta = F\eta \circ \eta$, so the two compositions agree.

\textbf{Left counit law:} We must show $\varepsilon L \circ \delta = \mathrm{id}_L$. Computing,
$$
\varepsilon L \circ \delta = (\varepsilon FG) \circ (F\eta G) = F(G\varepsilon \circ \eta G) \circ \mathrm{id}_A.
$$
By the triangular identity $G\varepsilon \circ \eta G = \mathrm{id}_G$, this equals $F\mathrm{id}_G = \mathrm{id}_{FG} = \mathrm{id}_L$.

\textbf{Right counit law:} We must show $L\varepsilon \circ \delta = \mathrm{id}_L$. Computing,
$$
L\varepsilon \circ \delta = (FG\varepsilon) \circ (F\eta G) = F(\varepsilon F \circ F\eta)G.
$$
By the other triangular identity $\varepsilon F \circ F\eta = \mathrm{id}_F$, this equals $\mathrm{id}_{FG} = \mathrm{id}_L$.

Thus $\langle FG, \varepsilon, F\eta G \rangle$ is a comonad in $A$.
