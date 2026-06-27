---
role: proof
locale: en
of_concept: backward-equation-diffusion
source_book: gtm017
source_chapter: "VI"
source_section: "c"
---
Starting from the Chapman-Kolmogorov equation:
$$F(\tau-\Delta\tau, \xi; t, x) = \int F(\tau, y; t, x) d_y F(\tau-\Delta\tau, \xi; \tau, y).$$

Using a Taylor expansion of $F(\tau, y; t, x)$ in $y$ about $\xi$:
$$F(\tau, y; t, x) = F(\tau, \xi; t, x) + (y-\xi)\frac{\partial F}{\partial \xi} + \frac{(y-\xi)^2}{2}\frac{\partial^2 F}{\partial \xi^2} + o((y-\xi)^2).$$

Substituting and using the diffusion conditions (3)-(5):
$$\frac{F(\tau-\Delta\tau, \xi; t, x) - F(\tau, \xi; t, x)}{\Delta\tau} = b(\tau, \xi)\frac{\partial F}{\partial \xi} + \frac{1}{2}a(\tau, \xi)\frac{\partial^2 F}{\partial \xi^2} + o(1).$$

Taking $\Delta\tau \to 0$ gives the backward equation:
$$\frac{\partial F}{\partial \tau} + \frac{1}{2}a(\tau, \xi)\frac{\partial^2 F}{\partial \xi^2} + b(\tau, \xi)\frac{\partial F}{\partial \xi} = 0.$$
