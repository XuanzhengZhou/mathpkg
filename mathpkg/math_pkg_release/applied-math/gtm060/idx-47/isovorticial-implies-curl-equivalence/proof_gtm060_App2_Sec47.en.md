---
role: proof
locale: en
of_concept: isovorticial-implies-curl-equivalence
source_book: gtm060
source_chapter: "Appendix 2"
source_section: "Section 47"
---

By definition of isovorticial fields, there exists a volume-preserving diffeomorphism $g: D \to D$ such that for every closed contour $\gamma$ in $D$,
$$\oint_{\gamma} v_1 = \oint_{g \circ \gamma} v_2.$$

By the change of variables formula for the line integral,
$$\oint_{g \circ \gamma} v_2 = \oint_{\gamma} g^* v_2,$$
where $g^* v_2$ denotes the pullback of the 1-form associated to $v_2$ by the metric. Since $g$ is a diffeomorphism, we have equivalently
$$\oint_{\gamma} v_1 = \oint_{\gamma} g^* v_2$$
for all closed contours $\gamma$. By Stokes' theorem applied to the circulation integral,
$$\oint_{\gamma} v = \int_{\sigma} \operatorname{curl} v \cdot dS$$
for any surface $\sigma$ with boundary $\gamma$. Hence the equality of circulations for all closed contours implies the equality of the vorticity fluxes, which yields $g_* \operatorname{curl} v_1 = \operatorname{curl} v_2$ in the three-dimensional case.

In the simply connected case, the implication reverses: if the vorticities are equivalent under a volume-preserving diffeomorphism, then by integrating along any closed contour and applying Stokes' theorem, the circulations match and the fields are isovorticial.
