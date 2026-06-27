---
role: proof
locale: en
of_concept: lebesgue-bounded-convergence-theorem
source_book: gtm018
source_chapter: "V"
source_section: "26"
---
**Proof (convergence in measure).** The theorem follows from Theorem C, since the domination $|f_n| \leq |g|$ implies that the indefinite integrals of $|f_n|$ inherit uniform absolute continuity and equicontinuity from the indefinite integral of $|g|$:
$$\int_E |f_n| d\mu \leq \int_E |g| d\mu.$$

**(convergence a.e.).** Assume $|f_n(x)| \leq |g(x)|$ and $|f(x)| \leq |g(x)|$ everywhere. For $\epsilon > 0$,
$$E_n = \bigcup_{i=n}^{\infty} \{x : |f_i(x) - f(x)| \geq \epsilon\} \subset \{x : |g(x)| \geq \epsilon/2\},$$
so $\mu(E_n) < \infty$. Since $\mu(\bigcap_n E_n) = 0$ (a.e. convergence), 9.E gives
$$\limsup_n \mu(\{x : |f_n(x)-f(x)| \geq \epsilon\}) \leq \lim_n \mu(E_n) = \mu(\lim_n E_n) = 0.$$
Thus a.e. convergence plus domination implies convergence in measure, reducing to the previous case.
