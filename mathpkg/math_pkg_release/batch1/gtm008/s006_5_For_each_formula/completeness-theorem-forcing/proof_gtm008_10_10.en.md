---
role: proof
locale: en
of_concept: completeness-theorem-forcing
source_book: gtm008
source_chapter: "10"
source_section: "10"
---

Using the one-to-one correspondence between $P$-generic sets over $M$ and $M$-complete homomorphisms from $B$ into $2$, we need only show:
$$
p \Vdash \varphi \leftrightarrow (\forall h')\bigl[h' : |B| \to |2| \text{ is an } M\text{-complete homomorphism} \land h'([p]^{-0}) = 1 \to h'(\llbracket \varphi \rrbracket) = 1\bigr].
$$

The right-hand side is equivalent to
$$
[p]^{-0} \leq \llbracket \varphi \rrbracket,
$$
which in turn is equivalent to each of the following:
$$
p \in \llbracket \varphi \rrbracket,
$$
$$
p \Vdash \varphi.
$$

The last equivalence follows directly from Definition 10.2, which defines $p \Vdash \varphi$ as $p \in \llbracket \varphi \rrbracket$.
