---
role: proof
locale: en
of_concept: characterization-of-straight-line
source_book: gtm051
source_chapter: "1"
source_section: "1.4"
---

Since $c$ is parameterized by arc length, $|\dot{c}(t)| = 1$ for all $t \in I$.

($\Rightarrow$) If $\ddot{c}(t) = 0$ for all $t$, then $\dot{c}(t)$ is constant. Let $v = \dot{c}(t)$ be this constant unit vector. Integrating: $c(t) = t v + p$ for some constant $p \in \mathbb{R}^n$. This is a straight line.

($\Leftarrow$) If $c(t) = t v + p$ with $|v| = 1$, then $\dot{c}(t) = v$ and $\ddot{c}(t) = 0$. Hence $\kappa(t) = 0$ for all $t$.
