---
role: proof
locale: en
of_concept: hamiltons-equations
source_book: gtm060
source_chapter: "3"
source_section: "15"
---

By definition, the Legendre transform of $L(q, \dot{q}, t)$ with respect to $\dot{q}$ is $H(p) = p\dot{q} - L$, where $p = \partial L/\partial \dot{q}$. The differential of $H$ is:
$$dH = \frac{\partial H}{\partial p}dp + \frac{\partial H}{\partial q}dq + \frac{\partial H}{\partial t}dt.$$
Also $dH = \dot{q} dp + p d\dot{q} - \frac{\partial L}{\partial \dot{q}}d\dot{q} - \frac{\partial L}{\partial q}dq - \frac{\partial L}{\partial t}dt = \dot{q}dp - \frac{\partial L}{\partial q}dq - \frac{\partial L}{\partial t}dt$.

Comparing coefficients: $\dot{q} = \partial H/\partial p$ and $-\partial L/\partial q = \partial H/\partial q$. By Lagrange's equations $\dot{p} = \partial L/\partial q$, so $\dot{p} = -\partial H/\partial q$.
