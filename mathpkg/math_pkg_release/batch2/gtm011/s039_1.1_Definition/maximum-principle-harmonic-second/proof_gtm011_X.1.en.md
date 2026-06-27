---
role: proof
locale: en
of_concept: maximum-principle-harmonic-second
source_book: gtm011
source_chapter: "X"
source_section: "1.7"
---

Fix $a$ in $\partial_\infty G$ and for each $\delta > 0$ let $G_\delta = G \cap B(a; \delta)$. Then according to the hypothesis,

$$0 \geq \lim_{\delta \to 0} \left[ \sup \{u(z): z \in G_\delta\} - \inf \{v(z): z \in G_\delta\} \right]$$
$$= \lim_{\delta \to 0} \left[ \sup \{u(z): z \in G_\delta\} + \sup \{-v(z): z \in G_\delta\} \right]$$
$$\geq \lim_{\delta \to 0} \sup \{u(z) - v(z): z \in G_\delta\}.$$

So $\limsup_{z \to a} [u(z) - v(z)] \leq 0$ for each $a$ in $\partial_\infty G$. So it is sufficient to prove the theorem under the assumption that $v(z) = 0$ for all $z$ in $G$.

In this case the hypothesis becomes $\limsup_{z \to a} u(z) \leq 0$ for each $a \in \partial_\infty G$. If $u$ is not identically zero, there exists a point $z_0 \in G$ with $u(z_0) \neq 0$. If $u(z_0) > 0$, let $M = \sup\{u(z) : z \in G\}$. By the First Maximum Principle (1.6), $u$ cannot attain $M$ in $G$ unless $u$ is constant. The boundedness and the behavior at the extended boundary force $M \leq 0$, contradicting $u(z_0) > 0$. Hence $u(z) \leq 0$ for all $z \in G$, and if $u(z_0) < 0$ then $u(z) < 0$ for all $z \in G$.

Returning to the original $u$ and $v$, this shows either $u(z) < v(z)$ for all $z \in G$, or $u \equiv v$.
