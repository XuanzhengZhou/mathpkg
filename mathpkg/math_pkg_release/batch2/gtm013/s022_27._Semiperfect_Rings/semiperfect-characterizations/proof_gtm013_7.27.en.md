---
role: proof
locale: en
of_concept: semiperfect-characterizations
source_book: gtm013
source_chapter: "7"
source_section: "27. Semiperfect Rings"
---

Throughout this proof let $J = J(R)$ be the radical of $R$.

$(a) \Rightarrow (b)$. If $R$ is semiperfect, then we can, by (27.4), lift the idempotents (7.2) for a semisimple decomposition of $R/J$ to obtain a complete orthogonal set $e_1, \ldots, e_n$ of idempotents in $R$ with each

$$Re_i/Je_i \cong (R/J)(e_i + J)$$

simple. Then by (17.20) each $e_i R e_i$ is local.

$(b) \Rightarrow (c)$. Given (b), each $Re_i/Je_i$ is simple by (17.20), and has a projective cover by (27.3). But each simple left $R$-module is isomorphic to a factor of $R/J \cong Re_1/Je_1 \oplus \ldots \oplus Re_n/Je_n$, and so is isomorphic to one of the $Re_i/Je_i$ (see (9.4)).

$(c) \Rightarrow (d)$. Assume (c) and let $\mathcal{P}$ be a complete set of projective covers of simple left $R$-modules. Then by (17.9) and (8.9), $\mathcal{P}$ generates every left $R$-module. Let ${}_R M$ be finitely generated. Then there is a sequence $P_1, \ldots, P_n$ in $\mathcal{P}$ and an epimorphism

$$P = P_1 \oplus \ldots \oplus P_n \xrightarrow{f} M \rightarrow 0.$$

Since $f(JP) = JM$, the induced map $P/JP \to M/JM$ is an isomorphism, and because $JP \ll P$, $f$ is a projective cover.

$(d) \Rightarrow (a)$. Assuming (d), $R/J$ has a projective cover, so by (27.3) $R/J$ is semisimple and idempotents lift modulo $J$.
