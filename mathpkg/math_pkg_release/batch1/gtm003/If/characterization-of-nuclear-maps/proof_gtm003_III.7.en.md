---
role: proof
locale: en
of_concept: characterization-of-nuclear-maps
source_book: gtm003
source_chapter: "III"
source_section: "7"
---

**Necessity.** If $u$ is nuclear, then $u = \psi_B \circ \bar{u}_0 \circ \phi_U$ where $\bar{u}_0$ is nuclear in $\mathcal{L}(\tilde{E}_U, F_B)$, with $U$ a suitable $0$-neighborhood in $E$ and $B$ a suitable bounded subset of $F$ for which $F_B$ is complete. Then $\bar{u}_0$ originates from an element $v \in [E_U]' \mathbin{\widehat{\otimes}} F_B$, which by (6.4) has the form
$$v = \sum_{n=1}^{\infty} \lambda_n h_n \otimes y_n$$
with $\sum_{n=1}^{\infty} |\lambda_n| < +\infty$ and where $\{h_n\}$ and $\{y_n\}$ are null sequences in $[E_U]'$ and $F_B$ respectively. Define $f_n = h_n \circ \phi_U$ on $E$; then $\{f_n\}$ is uniformly bounded on $U$, hence equicontinuous. The mapping $u = \psi_B \circ \tau(v) \circ \phi_U$ is then of the required form.

**Sufficiency.** If $u$ has the indicated form, let $U = \{x \in E : |f_n(x)| \leq 1, n \in \mathbb{N}\}$. Then $\{f_n\}$ factors through $E_U$, and $u$ factors through $\tilde{E}_U \to F_B \to F$, with the middle map being nuclear by construction.
