---
role: proof
locale: en
of_concept: eulers-criterion
source_book: gtm028
source_chapter: "V"
source_section: "12"
---

The multiplicative group of the finite field $\mathbb{F}_p = \mathbb{Z}/(p)$ is cyclic of order $p-1$. An element $s \not\equiv 0 \pmod{p}$ is a square iff it is an even power of a generator, which is equivalent to $s^{(p-1)/2} \equiv 1 \pmod{p}$. Conversely, if $s$ is not a square, it is an odd power of a generator, so $s^{(p-1)/2} \equiv -1 \pmod{p}$.

Thus $\left(\frac{s}{p}\right) \equiv s^{(p-1)/2} \pmod{p}$, where the Legendre symbol is $+1$ for squares and $-1$ for non-squares. This is Euler's criterion.
