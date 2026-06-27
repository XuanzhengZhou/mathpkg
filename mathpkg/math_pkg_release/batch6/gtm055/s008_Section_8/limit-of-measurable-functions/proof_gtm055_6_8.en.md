---
role: proof
locale: en
of_concept: limit-of-measurable-functions
source_book: gtm055
source_chapter: "6"
source_section: "8"
---

The set $E$ of convergence of $\{f_n(x)\}$ can be expressed as

$$E = \bigcap_{k=1}^{\infty} \bigcup_{N=1}^{\infty} \bigcap_{m,n \geq N} \{x \in X : |f_m(x) - f_n(x)| < 1/k\}.$$

Since each $f_n$ is measurable, each set $\{x : |f_m(x) - f_n(x)| < 1/k\}$ is measurable. The operations of countable intersection and union preserve measurability, so $E$ is measurable. For the limit function $f$ on $E$, the set $\{x \in E : \operatorname{Re} f(x) > a\}$ can be written as a countable union/intersection of measurable sets, hence $f$ is measurable.
