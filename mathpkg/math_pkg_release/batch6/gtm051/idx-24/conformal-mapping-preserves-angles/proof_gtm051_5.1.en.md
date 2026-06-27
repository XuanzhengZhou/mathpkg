---
role: proof
locale: en
of_concept: conformal-mapping-preserves-angles
source_book: gtm051
source_chapter: "5"
source_section: "5.1"
---

Let $X, Y \in T_u U$ be two non-zero tangent vectors. The angle $\theta$ between $X$ and $Y$ with respect to the metric $g$ is given by

$$\cos \theta = \frac{g_u(X, Y)}{\sqrt{g_u(X, X)} \sqrt{g_u(Y, Y)}}.$$

Since $\phi$ is conformal, there exists a positive function $\lambda(u)$ such that

$$\tilde{g}_{\phi(u)}(d\phi(X), d\phi(Y)) = \lambda(u) g_u(X, Y)$$

for all tangent vectors. Applying this to the angle formula for the image vectors:

$$\cos \tilde{\theta} = \frac{\tilde{g}_{\phi(u)}(d\phi(X), d\phi(Y))}{\sqrt{\tilde{g}_{\phi(u)}(d\phi(X), d\phi(X))} \sqrt{\tilde{g}_{\phi(u)}(d\phi(Y), d\phi(Y))}}$$

$$= \frac{\lambda(u) g_u(X, Y)}{\sqrt{\lambda(u) g_u(X, X)} \sqrt{\lambda(u) g_u(Y, Y)}} = \frac{\lambda(u) g_u(X, Y)}{\lambda(u) \sqrt{g_u(X, X)} \sqrt{g_u(Y, Y)}}$$

$$= \frac{g_u(X, Y)}{\sqrt{g_u(X, X)} \sqrt{g_u(Y, Y)}} = \cos \theta.$$

Therefore $\tilde{\theta} = \theta$, and the mapping $\phi$ preserves angles.