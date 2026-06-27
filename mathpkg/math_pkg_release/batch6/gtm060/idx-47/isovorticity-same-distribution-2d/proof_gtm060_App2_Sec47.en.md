---
role: proof
locale: en
of_concept: isovorticity-same-distribution-2d
source_book: gtm060
source_chapter: "Appendix 2"
source_section: "Section 47"
---

In the two-dimensional simply connected case, the isovorticity condition means that there exists a volume-preserving diffeomorphism $g$ carrying the vorticity $r_1$ to $r_2$. The scalar vorticity $r$ determines the velocity field uniquely (up to a harmonic gradient) in a simply connected domain via $r = -\Delta \psi$.

If $r_1$ and $r_2$ have the same distribution function, i.e., $\operatorname{mes}\{x \in D: r_1(x) \leq c\} = \operatorname{mes}\{x \in D: r_2(x) \leq c\}$ for all $c$, then by the theory of measure-preserving rearrangements, there exists a volume-preserving diffeomorphism $g$ such that $r_2 = r_1 \circ g^{-1}$ almost everywhere. This $g$ gives the required isovorticity.

Conversely, if such a $g$ exists, then for any $c$,
$$\{x \in D: r_2(x) \leq c\} = g(\{x \in D: r_1(x) \leq c\}),$$
and since $g$ preserves volume, the measures are equal.

The equality of moments $\int_D r_1^k dS = \int_D r_2^k dS$ follows directly from the equality of distribution functions and the fact that any moment can be expressed as an integral with respect to the distribution function:
$$\int_D r^k dS = \int_{-\infty}^{\infty} k c^{k-1} \operatorname{mes}\{x: r(x) > c\} \, dc.$$
