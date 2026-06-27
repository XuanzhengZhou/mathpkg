---
role: proof
locale: en
of_concept: bounded-convergence-theorem-for-integrable-functions
source_book: gtm018
source_chapter: "IX"
source_section: "§26. Sequences of Integrable Functions"
---

In the case of convergence in measure, the theorem is an immediate corollary of Theorem C---the uniformities required in that theorem are all consequences of the inequality

$$\int_E |f_n| \, d\mu \leq \int_E |g| \, d\mu.$$

The case of convergence a.e. may be reduced to that of convergence in measure (even though the integrals are not necessarily over a set of finite measure, cf. 22.4 and 22.5) by making use of the existence of $g$. If we assume, as we may without any loss of generality, that $|f_n(x)| \leq |g(x)|$ and $|f(x)| \leq |g(x)|$ for every $x$ in $X$, then we have, for every fixed positive number $\epsilon$,

$$E_n = \bigcup_{i=n}^{\infty} \{x: |f_i(x) - f(x)| \geq \epsilon\} \subset \{x: |g(x)| \geq \tfrac{\epsilon}{2}\},$$

and therefore $\mu(E_n) < \infty$, $n = 1, 2, \dots$. Since the assumption of convergence a.e. implies that $\mu(\bigcap_{n=1}^{\infty} E_n) = 0$, it follows from 9.E that

$$\limsup_n \mu(\{x: |f_n(x) - f(x)| \geq \epsilon\}) \leq \lim_n \mu(E_n) = \mu(\lim_n E_n) = 0.$$

In other words, convergence a.e., together with being bounded by an integrable function, implies convergence in measure, and the proof of the theorem is complete.
