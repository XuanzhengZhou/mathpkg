---
role: proof
locale: en
of_concept: continuity-equivalent-conditions
source_book: gtm011
source_chapter: "II"
source_section: "5"
---

(a) implies (b): Let $\Delta$ be open in $\Omega$ and let $x \in f^{-1}(\Delta)$. If $\omega = f(x)$ then $\omega$ is in $\Delta$; by definition, there is an $\epsilon > 0$ with $B(\omega; \epsilon) \subset \Delta$. Since $f$ is continuous, there is a $\delta > 0$ with $f(B(x; \delta)) \subset B(\omega; \epsilon)$, so $B(x; \delta) \subset f^{-1}(B(\omega; \epsilon)) \subset f^{-1}(\Delta)$. Hence, $f^{-1}(\Delta)$ is open.

(b) implies (c): If $\Gamma \subset \Omega$ is closed then let $\Delta = \Omega - \Gamma$. By (b), $f^{-1}(\Delta) = X - f^{-1}(\Gamma)$ is open, so that $f^{-1}(\Gamma)$ is closed.

(c) implies (a): Suppose there is a point $x$ in $X$ at which $f$ is not continuous. Then there is an $\epsilon > 0$ and a sequence $\{x_n\}$ such that $\rho(f(x_n), f(x)) \geq \epsilon$ for every $n$ while $x = \lim x_n$. Let $\Gamma = \Omega - B(f(x); \epsilon)$; then $\Gamma$ is closed and each $x_n$ is in $f^{-1}(\Gamma)$. Since (by (c)) $f^{-1}(\Gamma)$ is closed we have $x \in f^{-1}(\Gamma)$. But this implies $\rho(f(x), f(x)) \geq \epsilon > 0$, a contradiction.
