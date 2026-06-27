---
role: proof
locale: en
of_concept: transversality-submersion-characterization
source_book: gtm014
source_chapter: "1"
source_section: "4. Transversality"
---

One can show easily that $\operatorname{Ker}(d\phi)_{f(p)} = T_{f(p)}W$. So $f \pitchfork W$ at $p$

$$\text{iff } T_{f(p)}Y = T_{f(p)}W + (df)_p(T_p X)$$

$$\text{iff } T_{f(p)}Y = \operatorname{Ker}(d\phi)_{f(p)} + (df)_p(T_p X).$$

Since $(d\phi)_{f(p)}$ is onto we see that $(d(\phi \circ f))_p$ is onto iff this last equality holds. Thus $\phi \circ f$ is a submersion at $p$ iff $f \pitchfork W$ at $p$.
