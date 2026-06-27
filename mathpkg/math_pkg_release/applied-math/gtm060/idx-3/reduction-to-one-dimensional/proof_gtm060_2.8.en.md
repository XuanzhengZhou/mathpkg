---
role: proof
locale: en
of_concept: reduction-to-one-dimensional
source_book: gtm060
source_chapter: "2"
source_section: "8"
---

Differentiating the relation shown in Section 7 ($\dot{\mathbf{r}} = \dot{r}\mathbf{e}_r + r\dot{\phi}\mathbf{e}_\varphi$), we find

$$\ddot{\mathbf{r}} = (\ddot{r} - r\dot{\phi}^2)\mathbf{e}_r + (2\dot{r}\dot{\phi} + r\ddot{\phi})\mathbf{e}_\varphi.$$

Since the field is central,

$$\frac{\partial U}{\partial \mathbf{r}} = \frac{\partial U}{\partial r}\mathbf{e}_r.$$

Therefore the equation of motion in polar coordinates takes the form

$$\ddot{r} - r\dot{\phi}^2 = -\frac{\partial U}{\partial r}, \quad 2\dot{r}\dot{\phi} + r\ddot{\phi} = 0.$$

But, by the law of conservation of angular momentum,

$$\dot{\phi} = \frac{M}{r^2},$$

where $M$ is a constant independent of $t$, determined by the initial conditions. Therefore,

$$\ddot{r} = -\frac{\partial U}{\partial r} + r \frac{M^2}{r^4} \quad \text{or} \quad \ddot{r} = -\frac{\partial V}{\partial r}, \quad \text{where} \quad V = U + \frac{M^2}{2r^2}.$$

The total energy in the derived one-dimensional problem

$$E_1 = \frac{\dot{r}^2}{2} + V(r)$$

is the same as the total energy in the original problem

$$E = \frac{\dot{r}^2}{2} + U(\mathbf{r}),$$

since

$$\frac{\dot{r}^2}{2} = \frac{\dot{r}^2}{2} + \frac{r^2 \dot{\phi}^2}{2} = \frac{\dot{r}^2}{2} + \frac{M^2}{2r^2}.$$
