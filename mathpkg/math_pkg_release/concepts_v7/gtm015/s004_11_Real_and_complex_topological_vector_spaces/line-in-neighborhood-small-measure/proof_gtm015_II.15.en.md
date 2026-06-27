---
role: proof
locale: en
of_concept: line-in-neighborhood-small-measure
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "15. The space (S)"
---

# Proof that Every Neighborhood Contains a Line

**Theorem (15.8).** Suppose $\mu$ assumes arbitrarily small values. If $V$ is any neighborhood of $\theta$ in $[\mathcal{M}]$, then there exists a nonzero vector $u$ such that $\{\alpha u : \alpha \in \mathbb{R}\} \subset V$.

*Proof.* Choose $\varepsilon > 0$ so that $U_\varepsilon(\theta) \subset V$, where $U_\varepsilon(\theta) = \{u : d(u, \theta) < \varepsilon\}$. By the hypothesis on $\mu$, there exists a measurable set $E$ such that $0 < \mu(E) < \varepsilon$. Let $f = \chi_E$, $u = [f]$. For any $\alpha \in \mathbb{R}$, evidently

$$\frac{|\alpha f|}{1 + |\alpha f|} \leq f = \chi_E,$$

since $f$ takes only the values $0$ and $1$, and for $x \in E$, $\frac{|\alpha|}{1+|\alpha|} < 1 = f(x)$. Integration yields

$$d(\alpha u, \theta) = \int \frac{|\alpha f|}{1 + |\alpha f|} d\mu \leq \int \chi_E d\mu = \mu(E) < \varepsilon.$$

Thus $\alpha u \in U_\varepsilon(\theta) \subset V$ for all $\alpha \in \mathbb{R}$. Since $u \neq \theta$ (because $\mu(E) > 0$), the line through $u$ is contained in $V$. $\square$
