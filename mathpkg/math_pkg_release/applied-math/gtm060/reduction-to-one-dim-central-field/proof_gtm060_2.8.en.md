---
role: proof
locale: en
of_concept: reduction-to-one-dim-central-field
source_book: gtm060
source_chapter: "2"
source_section: "8"
---

Differentiating $\dot{r} = \dot{r} e_r + r\dot{\varphi} e_\varphi$ (Section 7), we find
$$\ddot{r} = (\ddot{r} - r\dot{\varphi}^2)e_r + (2\dot{r}\dot{\varphi} + r\ddot{\varphi})e_\varphi.$$

Since the field is central, $\partial U/\partial r = (\partial U/\partial r)e_r$. The equation of motion gives
$$\ddot{r} - r\dot{\varphi}^2 = -\frac{\partial U}{\partial r}, \quad 2\dot{r}\dot{\varphi} + r\ddot{\varphi} = 0.$$

By conservation of angular momentum, $\dot{\varphi} = M/r^2$ where $M$ is constant. Substituting:
$$\ddot{r} = -\frac{\partial U}{\partial r} + r\frac{M^2}{r^4} = -\frac{\partial}{\partial r}\left(U + \frac{M^2}{2r^2}\right) = -\frac{\partial V}{\partial r}.$$
