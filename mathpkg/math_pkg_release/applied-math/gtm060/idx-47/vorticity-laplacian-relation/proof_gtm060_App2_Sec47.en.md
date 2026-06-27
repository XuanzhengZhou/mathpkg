---
role: proof
locale: en
of_concept: vorticity-laplacian-relation
source_book: gtm060
source_chapter: "Appendix 2"
source_section: "Section 47"
---

By definition of the vorticity $r$ in two dimensions, for any oriented region $\sigma \subset D$,
$$\int_{\sigma} r \, dS = \oint_{\partial \sigma} v.$$

Substituting the stream function representation $v = I \operatorname{grad} \psi$ and applying Stokes' theorem:
$$\oint_{\partial \sigma} v = \oint_{\partial \sigma} I \operatorname{grad} \psi = \int_{\sigma} \operatorname{curl}(I \operatorname{grad} \psi) \, dS.$$

In Cartesian coordinates with $I(x, y) = (-y, x)$,
$$v = \left(-\frac{\partial \psi}{\partial y}, \frac{\partial \psi}{\partial x}\right).$$

The scalar curl is
$$r = \operatorname{curl} v = \frac{\partial v_2}{\partial x} - \frac{\partial v_1}{\partial y} = \frac{\partial}{\partial x}\left(\frac{\partial \psi}{\partial x}\right) - \frac{\partial}{\partial y}\left(-\frac{\partial \psi}{\partial y}\right) = \frac{\partial^2 \psi}{\partial x^2} + \frac{\partial^2 \psi}{\partial y^2} = \Delta \psi.$$

Taking into account the orientation conventions ($I$ is clockwise rotation), we obtain $r = -\Delta \psi$.
