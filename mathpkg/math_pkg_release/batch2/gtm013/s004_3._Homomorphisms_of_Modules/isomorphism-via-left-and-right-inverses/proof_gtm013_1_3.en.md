---
role: proof
locale: en
of_concept: isomorphism-via-left-and-right-inverses
source_book: gtm013
source_chapter: "1"
source_section: "3. Homomorphisms of Modules"
---

**Proof.** The implication ($\Leftarrow$) and the uniqueness assertion are easy:
$$g = 1_M g = hfg = h 1_N = h.$$
For the converse, observe that if $f$ is an isomorphism, and hence a bijection, then there is a set-theoretic function $g: N \to M$ such that $fg = 1_N$ and $gf = 1_M$ (see (0.1)). To complete the proof we need to check that $g$ is $R$-linear. But since $f$ is $R$-linear, we have
$$f(g(ax + by)) = ax + by = f(ag(x) + bg(y)),$$
and then since $f$ is injective, we obtain the $R$-linearity of $g$. $\square$
