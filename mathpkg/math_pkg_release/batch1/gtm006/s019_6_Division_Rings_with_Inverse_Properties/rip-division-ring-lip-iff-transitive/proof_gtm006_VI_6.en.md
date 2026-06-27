---
role: proof
locale: en
of_concept: rip-division-ring-lip-iff-transitive
source_book: gtm006
source_chapter: "VI"
source_section: "6. Division Rings with Inverse Properties"
---

**(i) Suppose $\mathcal{P}$ is $((0,0),[0,0])$-transitive.**

Let $\alpha$ be the $((0,0),[0,0])$-elation mapping $(\infty)$ onto $(0,-1)$. For any $m \in R$, $m \neq 0$, the point $(m)^\alpha$ lies on the line $[m,0]^\alpha = [m,0]$, and $[\infty]^\alpha = [0,-1]$. Thus if $(m)^\alpha = (t,-1)$, we have $mt - 1 = 0$, i.e., $t = m^{-1}$.

Now consider two arbitrary elements $a, b \in R^*$. Using the properties of the elation $\alpha$, one obtains through a geometric computation that $(ab)^{-1} = b^{-1}a^{-1}$, which is equivalent to $b^{-1} = (ab)^{-1}a$. Taking inverses (using Lemma 6.10), $b = (b^{-1})^{-1} = [(ab)^{-1}a]^{-1} = a^{-1}(ab)$. This last equality is precisely the left inverse property for the element $a$, showing that $R$ has LIP.

**(ii) Suppose $R$ has LIP.**

Consider the mapping $\alpha$ defined on the projective plane by the formulas derived from the planar ternary ring structure. One verifies that this mapping is a $((0,0),[0,0])$-elation sending $(\infty)$ to $(0,-1)$, and consequently sending $[\infty]$ to $[0,-1]$. By Exercise 4.13, $[0,-1]$ is a translation line, and applying Theorem 4.20, every line through the point $(0)$ is a translation line. In particular, $[0,0]$ is a translation line, and therefore $\mathcal{P}$ is $((0,0),[0,0])$-transitive.
