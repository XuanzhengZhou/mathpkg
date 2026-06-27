---
role: proof
locale: en
of_concept: lambda0-characterization
source_book: gtm048
source_chapter: "5"
source_section: "5.6"
---

There exists at least one such $\chi$; for example, the 3-form

$$\chi = [(1/u^4) du^1 \wedge du^2 \wedge du^3] \circ \iota$$

works by the coordinate expressions for $\omega$, $\Lambda_0$, and $\Omega$. We must show uniqueness of $\Lambda_0$. Let $\chi, \chi'$ be 3-forms over $\iota$ with $(\omega \circ \iota) \wedge \chi = \Omega \circ \iota$ and $(\omega \circ \iota) \wedge \chi' = \Omega \circ \iota$.

Then $(\omega \circ \iota) \wedge \chi' = \Omega \circ \iota$ iff $(\omega \circ \iota) \wedge (\chi - \chi') = 0$ iff $\chi - \chi' = (\omega \circ \iota) \wedge \eta$ for some 2-form $\eta$ over $\iota$ (Bishop-Goldberg p. 95). But for every vector $W$ tangent to $\mathcal{L}_0^+$ at $w \in \mathcal{L}_0$, $\omega(W) = 0$ (Section 5.0.5). Thus if $\chi$ and $\chi'$ both obey the stated conditions, $\iota^*(\chi w) = \iota^*(\chi' w)$ for all $w \in \mathcal{L}_0^+$. Thus $\Lambda_0$ is unique.
