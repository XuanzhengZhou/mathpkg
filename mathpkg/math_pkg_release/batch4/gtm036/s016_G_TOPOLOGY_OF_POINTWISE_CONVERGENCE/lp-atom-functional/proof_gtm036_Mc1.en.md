---
role: proof
locale: en
of_concept: lp-atom-functional
source_book: gtm036
source_chapter: "M"
source_section: "M(c)"
---

Let $\phi(f) = \int_A f \, d\mu$. This is clearly linear. For continuity, note that on an atom $A$, the measure is essentially a point mass up to scaling. For any measurable function $f$ on $A$, since every measurable subset of $A$ has measure either $0$ or $\mu(A)$, $|f|^p$ is essentially constant almost everywhere on $A$ (otherwise we could partition $A$ into sets where $|f|^p$ takes values above and below some threshold). More precisely, $f$ is constant $\mu$-almost everywhere on $A$, so
$$
\int_A |f| \, d\mu = |c| \mu(A), \quad \int_A |f|^p \, d\mu = |c|^p \mu(A),
$$
where $c$ is the essential value of $f$ on $A$. Hence $|\phi(f)| = |c| \mu(A) = \mu(A)^{1-1/p} (\int_A |f|^p d\mu)^{1/p} \leq \mu(A)^{1-1/p} \|f\|_p$, proving continuity of $\phi$.
