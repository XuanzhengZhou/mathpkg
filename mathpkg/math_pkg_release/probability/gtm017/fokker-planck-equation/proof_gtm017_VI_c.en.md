---
role: proof
locale: en
of_concept: fokker-planck-equation
source_book: gtm017
source_chapter: "VI"
source_section: "c"
---
By considering a small time transition at the forward end (instead of the backward end) and using the adjoint of the backward operator, one obtains the forward equation in $(t, x)$:
$$\frac{\partial f}{\partial t} = \frac{1}{2}\frac{\partial^2}{\partial x^2}(a(t,x)f) - \frac{\partial}{\partial x}(b(t,x)f).$$

This is derived by considering $\int \phi(x) f(\tau, \xi; t, x) dx$ for smooth test functions $\phi$, differentiating with respect to $t$, using the backward equation and integration by parts.
