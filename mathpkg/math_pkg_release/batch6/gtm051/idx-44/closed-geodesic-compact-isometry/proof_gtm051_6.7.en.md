---
role: proof
locale: en
of_concept: closed-geodesic-compact-isometry
source_book: gtm051
source_chapter: "6"
source_section: "6.7"
---

**Proof.** Consider the function $f(p) = d(p, \gamma p)$. As in the proof of Theorem 6.7.1, we can easily show that $f$ is continuous. Since $M$ is compact, $f$ assumes a minimum value, say $\omega$, at some point $p$. Since $\gamma$ is fixed-point free, $\omega = d(p, \gamma p) > 0$. Let $c(t)$ be a unit-speed geodesic with $c(0) = p$ and $c(\omega) = \gamma p$. As in the proof of Theorem 6.7.1, using the first variation formula and the minimizing property of $f$ at $p$, we can show that

$$\gamma \circ c(t) = c(t + \omega)$$

for all $t$. If $\gamma^n = \text{id}$ for some $n$, then iterating the relation gives $c(t + n\omega) = \gamma^n c(t) = c(t)$, which means $c(t)$ for $0 \leq t \leq n\omega$ is a closed geodesic.
