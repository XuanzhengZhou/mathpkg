---
role: proof
locale: en
of_concept: mean-convergence-characterization
source_book: gtm018
source_chapter: "V"
source_section: "26"
---
**Proof (Necessity).** Convergence in measure follows from 25.A and uniform absolute continuity from 24.C. For equicontinuity: mean convergence gives $n_0$ such that $\int |f_n - f| d\mu < \epsilon/2$ for $n \geq n_0$. The indefinite integral of $|f|$ is continuous from above at 0 (as a finite measure, 9.E). For a decreasing sequence $\{E_m\}$ with empty intersection, choose $m_0$ so that $\int_{E_m} |f| d\mu < \epsilon/2$ and $\int_{E_m} |f_n| d\mu < \epsilon$ for $n < n_0$ and $m \geq m_0$. Then for $n \geq n_0$,
$$\int_{E_m} |f_n| d\mu \leq \int |f_n - f| d\mu + \int_{E_m} |f| d\mu < \epsilon,$$
giving equicontinuity.

**(Sufficiency).** Let $E_0 = \bigcup_n N(f_n)$, which has $\sigma$-finite measure. Let $E_n \uparrow E_0$ with $\mu(E_n) < \infty$, and $F_n = E_0 - E_n \downarrow 0$. By equicontinuity, choose $k$ with $\int_{F_k} |f_n| d\mu < \delta/2$ for all $n$. For $\epsilon > 0$, let $G_{mn} = \{x : |f_m - f_n| \geq \epsilon\}$. Then
$$\int |f_m - f_n| d\mu \leq \epsilon\mu(E_k) + \int_{E_k \cap G_{mn}} |f_m - f_n| d\mu + \delta.$$
By convergence in measure and uniform absolute continuity, the middle term becomes small for large $m,n$, so $\limsup_{m,n} \int |f_m - f_n| d\mu \leq \epsilon\mu(E_k) + \delta$. Since $\epsilon$ and $\delta$ are arbitrary, $\{f_n\}$ is mean fundamental, and by Theorem B converges in mean to some $g$. Since mean convergence implies convergence in measure, $f = g$ a.e.
