---
role: proof
locale: en
of_concept: lemma-8-10
source_book: gtm055
source_chapter: "7-8"
source_section: "Section 09_Section_9"
---

Proof. A point $t$ of $(a, b)$ belongs to $R_0$ if and only if there exists a point $u$ in $(t, b)$ such that $f(t) < f(u)$. From this and the fact

upper and lower left-hand derivates of $f$ at $b$, denoted by $D_-(b) = D_-(b; f)$ and $d_-(b) = d_-(b; f)$, are defined as

$$\limsup_{t \uparrow b} \frac{f(t) - f(b)}{t - b} \quad \text{and} \quad \liminf_{t \uparrow b} \frac{f(t) - f(b)}{t - b},$$

respectively.

The basic significance of these derivates in differentiation theory is clear. A real-valued function $f$ is differentiable to the left [right] at a point $t$ if and only if $D_-(t) = d_-(t)$ $[D_+(t) = d_+(t)]$. Hence $f$ is differentiable at a point $t$ in the interior of its domain of definition if and only if $D_-(t) = d_-(t) = D_+(t) = d_+(t)$. (We are here admitting $\pm \infty$ as possible values of the derivative.)

Suppose now that $f$ is a continuous real-valued function defined on an interval $[a, b]$ and that the upper right-hand derivate of $f$ at a point $t$, $a < t < b$, exceeds some real number $m$. Then for any open subset $U$ of $[a, b]$ such that $t \in U$ we have $t \in R_m(f; U)$. Similarly, if $d_-(t; f) < m$, then $t \in L_m(f; U)$ whenever $t \in U \subset [a, b]$. These observations are exploited in the following lemma.
