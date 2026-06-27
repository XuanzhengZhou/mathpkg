---
role: proof
locale: en
of_concept: rip-lip-transitivity-equivalence
source_book: gtm006
source_chapter: "V"
source_section: "6"
---

(i) Suppose $\mathcal{P}$ is $((0,0), [0,0])$-transitive. Let $\alpha$ be the $((0,0), [0,0])$-elation mapping $(\infty)$ onto $(0, -1)$. For any $m \in R$, $m \neq 0$, $(m)^\alpha$ lies on $[m, 0]^\alpha = [m, 0]$ and $[\infty]^\alpha = [0, -1]$. Hence if $(m)^\alpha = (t, -1)$, then $mt - 1 = 0$, so $t = m^{-1}$. From this, using the action of $\alpha$, we deduce that

$$(ab)^{-1} = b^{-1}a^{-1}$$

or equivalently

$$b^{-1} = (ab)^{-1}a,$$

which yields $b = (b^{-1})^{-1} = [(ab)^{-1}a]^{-1} = a^{-1}(ab)$. Thus $R$ has LIP.

(ii) Suppose $R$ has LIP. The mapping $\alpha$ defined by the same coordinate formulas as in the RIP-to-elation construction (with an additional condition reflecting LIP) serves as a $((0,0), [0,0])$-elation mapping $(\infty)$ onto $(0, -1)$, and thus sends $[\infty]$ onto $[0, -1]$. By Exercise 4.13, $[0, -1]$ is then a translation line, and by Theorem 4.20, every line through $(0)$ becomes a translation line. In particular, $[0,0]$ is a translation line, so $\mathcal{P}$ is $((0,0), [0,0])$-transitive.
