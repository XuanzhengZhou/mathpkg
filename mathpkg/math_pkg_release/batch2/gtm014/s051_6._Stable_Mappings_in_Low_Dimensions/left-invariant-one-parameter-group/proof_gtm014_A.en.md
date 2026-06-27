---
role: proof
locale: en
of_concept: left-invariant-one-parameter-group
source_book: gtm014
source_chapter: "Appendix A"
source_section: "§A. Lie Groups"
---

Let $\psi_t: U \to G$ (with $|t| < \varepsilon$, $U$ a neighborhood of $e$ in $G$) be a locally defined one-parameter group near $e$ in $G$ as given by I, Lemma 6.2. The goal is to extend $\psi_t$ globally.

Since $\zeta$ is left-invariant, $(dL_g)\zeta = \zeta$ for all $g \in G$. This implies
$$
\frac{d}{dt} g \psi_t(a) = \frac{d}{dt} \psi_t(ga)
$$
for all $g, a$, and $ga$ in $U$. Hence
$$
g \psi_t(a) = \psi_t(ga). \tag{*}
$$
In particular, $\psi_t(g) = g \psi_t(e)$ for $g$ in $U$. Using $(*)$, we can extend $\psi_t$ to be globally defined and smooth on $G$: for any $g \in G$, choose $a$ sufficiently close to $e$ so that $ga \in U$ and define $\psi_t(g)$ via the relation. The left invariance of $\zeta$ guarantees that this extended flow $\psi_t$ (for $|t| < \varepsilon$) is still a one-parameter group for $\zeta$ on all of $G$. The standard procedure of iterating the flow extends to all $t \in \mathbf{R}$.
