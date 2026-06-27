---
role: proof
locale: en
of_concept: metric-completeness-implies-geodesic-completeness
source_book: gtm051
source_chapter: "6"
source_section: "6.4"
---

**Proof.**

1. Let $X \in T_pM$ be a unit vector. We wish to show that the geodesic $c_X(t) = \exp_p tX$ is defined for all $t \in \mathbb{R}^+ = \{t \in \mathbb{R} \mid t \geq 0\}$. We know that $c_X(t)$ is defined for an interval of the form $[0, t^*]$. Let $\{t_n\}$ be a sequence in $[0, t^*]$ with $\lim_n t_n = t^*$. Since $d(\exp_p t_kX, \exp_p t_lX) \leq |t_k - t_l|$, the sequence $\{p_n = \exp_p t_nX\}$ is a Cauchy sequence. The assumption that $M$ is metrically complete implies that there exists a $q \in M$ with $\lim_n p_n = q$.

2. According to (5.2.5), there exists a neighborhood $M_0$ of $q$ and a $\rho > 0$ such that for every $p^* \in M_0$ the exponential map $\exp_{p^*}$ is defined on $B_\rho(0) \subset T_{p^*}M$.

By choosing $n$ large enough to make $t^* - t_n < \rho/2$, we may ensure that $p_n \in M_0$. This means that the geodesic ray emanating from $c_X(t_n)$ with initial direction $\dot{c}_X(t_n) \in T_{p_n}M$ is defined for all parameter values in $[0, \rho]$. Hence the original geodesic $c_X$ can be extended beyond $t^*$ to $t^* + \rho - (t^* - t_n) > t^*$, contradicting the definition of $t^*$ as the supremum of the domain of definition. Therefore $t^* = \infty$, and the geodesic $c_X(t)$ is defined for all $t \geq 0$.

Note: The hypothesis is certainly satisfied if $M$ is compact.
