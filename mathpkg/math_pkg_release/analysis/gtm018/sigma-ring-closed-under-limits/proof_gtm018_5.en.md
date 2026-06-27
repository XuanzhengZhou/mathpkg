---
role: proof
locale: en
of_concept: sigma-ring-closed-under-limits
source_book: gtm018
source_chapter: "I"
source_section: "5"
---

First, a $\sigma$-ring is closed under countable intersections. If $\mathbf{S}$ is a $\sigma$-ring and $E_i \in \mathbf{S}$ for $i = 1, 2, \dots$, let $E = \bigcup_{i=1}^{\infty} E_i \in \mathbf{S}$. Then
$$\bigcap_{i=1}^{\infty} E_i = E - \bigcup_{i=1}^{\infty} (E - E_i).$$
Since $E - E_i \in \mathbf{S}$ (closed under differences) and $\mathbf{S}$ is closed under countable unions, the right side belongs to $\mathbf{S}$, hence $\bigcap_i E_i \in \mathbf{S}$.

Now for the limits. If $\mathbf{S}$ is a $\sigma$-ring and $E_i \in \mathbf{S}$, then using the characterizations
$$\liminf_i E_i = \bigcup_{n=1}^{\infty} \bigcap_{m=n}^{\infty} E_m, \quad \limsup_i E_i = \bigcap_{n=1}^{\infty} \bigcup_{m=n}^{\infty} E_m,$$
each inner expression $\bigcap_{m=n}^{\infty} E_m$ and $\bigcup_{m=n}^{\infty} E_m$ belongs to $\mathbf{S}$ (by closure under countable intersections and unions respectively). Then the outer countable union or intersection again stays in $\mathbf{S}$. Thus $\liminf_i E_i \in \mathbf{S}$ and $\limsup_i E_i \in \mathbf{S}$.
