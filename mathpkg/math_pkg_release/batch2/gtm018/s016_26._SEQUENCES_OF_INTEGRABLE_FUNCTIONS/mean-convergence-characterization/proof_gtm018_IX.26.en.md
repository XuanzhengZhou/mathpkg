---
role: proof
locale: en
of_concept: mean-convergence-characterization
source_book: gtm018
source_chapter: "IX"
source_section: "§26. Sequences of Integrable Functions"
---

We prove first the necessity of the conditions. Since convergence in measure and uniform absolute continuity follow from 25.A and 24.C respectively, we have only to prove the asserted equicontinuity.

The mean convergence of $\{f_n\}$ to $f$ implies that to every positive number $\epsilon$ there corresponds a positive integer $n_0$ such that if $n \geq n_0$, then $\int |f_n - f| \, d\mu < \frac{\epsilon}{2}$. Since the indefinite integral of a non-negative integrable function is a finite measure (23.I), it follows from 9.E that such an indefinite integral is continuous from above at $0$. Consequently, if $\{E_m\}$ is a decreasing sequence of measurable sets with an empty intersection, then there exists a positive integer $m_1$ such that $m \geq m_1$ implies $\int_{E_m} |f| \, d\mu < \frac{\epsilon}{2}$. Hence for all $n \geq n_0$ and $m \geq m_1$,

$$\int_{E_m} |f_n| \, d\mu \leq \int_{E_m} |f_n - f| \, d\mu + \int_{E_m} |f| \, d\mu < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon.$$

By 9.E, each of the finitely many indefinite integrals of $|f_1|, |f_2|, \dots, |f_{n_0-1}|$ is also continuous from above at $0$; therefore $m_0 \geq m_1$ can be chosen so that for $m \geq m_0$,

$$\int_{E_m} |f_n| \, d\mu < \epsilon$$

for \emph{every} positive integer $n$, and this is exactly the desired equicontinuity result.

We turn to the proof of sufficiency. Since a countable union of measurable sets of $\sigma$-finite measure is a measurable set of $\sigma$-finite measure, it follows from 25.F that

$$E_0 = \bigcup_{n=1}^{\infty} \{x : f_n(x) \neq 0\}$$

is such a set. If $\{E_n\}$ is an increasing sequence of measurable sets of finite measure such that $\lim_n E_n = E_0$, and if $F_n = E_0 - E_n$, $n = 1, 2, \dots$, then $\{F_n\}$ is a decreasing sequence and $\lim_n F_n = 0$. The assumed equicontinuity implies that, for every positive number $\delta$, there exists a positive integer $k$ such that

$$\int_{F_k} |f_n| \, d\mu < \frac{\delta}{2},$$

and consequently

$$\int_{F_k} |f_m - f_n| \, d\mu \leq \int_{F_k} |f_m| \, d\mu + \int_{F_k} |f_n| \, d\mu < \delta.$$

If for any fixed $\epsilon > 0$ we write

$$G_{mn} = \{x : |f_m(x) - f_n(x)| \geq \epsilon\},$$

then it follows that

$$\int_{E_k} |f_m - f_n| \, d\mu \leq \int_{E_k - G_{mn}} |f_m - f_n| \, d\mu + \int_{E_k \cap G_{mn}} |f_m - f_n| \, d\mu \leq \epsilon \, \mu(E_k) + \int_{E_k \cap G_{mn}} |f_m - f_n| \, d\mu.$$

By convergence in measure and uniform absolute continuity, the second term on the dominant side of this chain of inequalities may be made arbitrarily small by choosing $m$ and $n$ sufficiently large, so that

$$\limsup_{m,n} \int_{E_k} |f_m - f_n| \, d\mu \leq \epsilon \, \mu(E_k).$$

Since

$$\int |f_m - f_n| \, d\mu = \int_{E_0} |f_m - f_n| \, d\mu = \int_{E_k} |f_m - f_n| \, d\mu + \int_{F_k} |f_m - f_n| \, d\mu,$$

we have

$$\limsup_{m,n} \int |f_m - f_n| \, d\mu < \epsilon \, \mu(E_k) + \delta,$$

and therefore, since $\epsilon$ and $\delta$ are arbitrary,

$$\lim_{m,n} \int |f_m - f_n| \, d\mu = 0.$$

We have proved, in other words, that the sequence $\{f_n\}$ is fundamental in the mean; it follows from Theorem B that there exists an integrable function $g$ such that $\{f_n\}$ mean converges to $g$. Since mean convergence implies convergence in measure, we must have $f = g$ a.e.
