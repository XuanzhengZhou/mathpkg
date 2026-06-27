---
role: proof
locale: en
of_concept: phi-functional-equation
source_book: gtm041
source_chapter: "3"
source_section: "3.5"
---

The functional equation $\Phi(\alpha,\beta,-s) = \Phi(1-\beta,\alpha,s)$ is a consequence of Hurwitz's formula for the Hurwitz zeta function. Hurwitz's formula states that for $0 < \alpha \leq 1$ and $\operatorname{Re}(s) > 1$,

$$\zeta(1-s, \alpha) = \frac{\Gamma(s)}{(2\pi)^s} \Bigl\{ e^{-\pi i s/2} F(\alpha, s) + e^{\pi i s/2} F(-\alpha, s) \Bigr\}.$$

By applying this formula to both $\zeta(s,\alpha)$ and $\zeta(s,1-\alpha)$ with appropriate transformations, and using the periodicity properties of $F(x,s)$ (in particular $F(1-\beta,s) = F(-\beta,s)$ for real $\beta$), the identity $\Phi(\alpha,\beta,-s) = \Phi(1-\beta,\alpha,s)$ follows after algebraic manipulation. A full derivation is outlined in Exercise 7 of the text. The functional equation is then used in equation (24) of the proof of Iseki's formula for $\Lambda(\alpha,\beta,z)$: substituting $s \mapsto -s$ in the contour integral gives

$$\frac{1}{2\pi i} \int_{(3/2)} z^u \Phi(\alpha,\beta,-u)\, du = \frac{1}{2\pi i} \int_{(3/2)} z^u \Phi(1-\beta,\alpha,u)\, du = \Lambda(1-\beta,\alpha,z^{-1}),$$

which is the critical step in establishing $\Lambda(\alpha,\beta,z) = \Lambda(1-\beta,\alpha,z^{-1}) + R$.
