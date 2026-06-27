---
role: proof
locale: en
of_concept: ends-parametrized
source_book: gtm005
source_chapter: "IX"
source_section: "7"
---

For a trifunctor $T: P \times C^{\mathrm{op}} \times C \to X$, we define the parametrized end:
$$\left(\int_c T(p, c, c)\right)_{p \in P}: P \to X.$$

For each fixed $p$, take the end over $c$. This extends to a functor $P \to X$: given $f: p \to q$ in $P$, the universal property of ends gives an induced morphism between the ends, using the natural transformation $T(f, -, -): T(p, -, -) \Rightarrow T(q, -, -)$.

The key property: for any functor $H: P \to X$,
$$\operatorname{Nat}_P\left(H, \int_c T(-, c, c)\right) \cong \int_c \operatorname{Nat}_P(H, T(-, c, c)).$$
This is a "Fubini" exchange: an end of natural transformations equals a natural transformation into an end (when the codomain has the relevant limits).
