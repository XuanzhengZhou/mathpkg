---
role: proof
locale: en
of_concept: adjunction-defines-monad
source_book: gtm005
source_chapter: "VI. Monads and Algebras"
source_section: "1. Monads in a Category"
---

We verify that $\langle GF, \eta, G\varepsilon F \rangle$ satisfies the monad axioms. Let $T = GF$ and $\mu = G\varepsilon F$.

\textbf{Associativity:} We must show $\mu \circ T\mu = \mu \circ \mu T$. Computing,
$$
\mu \circ T\mu = (G\varepsilon F) \circ (GFG\varepsilon F) = G(\varepsilon \circ FG\varepsilon)F.
$$
On the other hand,
$$
\mu \circ \mu T = (G\varepsilon F) \circ (G\varepsilon F GF) = G(\varepsilon \circ \varepsilon FG)F.
$$
By naturality of $\varepsilon$, we have $\varepsilon \circ FG\varepsilon = \varepsilon \circ \varepsilon FG$, hence the two compositions agree.

\textbf{Left unit law:} We must show $\mu \circ \eta T = \mathrm{id}_T$. Computing,
$$
\mu \circ \eta T = (G\varepsilon F) \circ (\eta GF) = G(\varepsilon \circ F\eta) \circ F.
$$
By one of the triangular identities for the adjunction $\langle F, G, \eta, \varepsilon \rangle$, we have $\varepsilon F \circ F\eta = \mathrm{id}_F$. Therefore $\mu \circ \eta T = G\mathrm{id}_F \circ F = \mathrm{id}_{GF} = \mathrm{id}_T$.

\textbf{Right unit law:} We must show $\mu \circ T\eta = \mathrm{id}_T$. Computing,
$$
\mu \circ T\eta = (G\varepsilon F) \circ (GF\eta) = G(\varepsilon \circ \eta G) \circ F.
$$
By the other triangular identity, $G\varepsilon \circ \eta G = \mathrm{id}_G$. Therefore $\mu \circ T\eta = \mathrm{id}_{GF} = \mathrm{id}_T$.

Thus all three monad axioms hold, and $\langle GF, \eta, G\varepsilon F \rangle$ is a monad in $X$.
