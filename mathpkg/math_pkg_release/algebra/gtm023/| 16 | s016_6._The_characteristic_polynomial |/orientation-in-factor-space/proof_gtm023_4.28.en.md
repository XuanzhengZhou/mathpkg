---
role: proof
locale: en
of_concept: orientation-in-factor-space
source_book: gtm023
source_chapter: "Chapter IV"
source_section: "§8. Oriented vector spaces"
---

First, show $\bar{\Delta}$ is well-defined on $E/F$: if $y_{p+1} \equiv x_{p+1} \pmod{F}$, then $y_{p+1} = x_{p+1} + \sum_{v=1}^{p} \lambda^v a_v$, and
$$\Delta(a_1, \ldots, a_p, y_{p+1}, \ldots, x_n) = \Delta(a_1, \ldots, a_p, x_{p+1}, \ldots, x_n) + \sum_{v=1}^{p} \lambda^v \Delta(a_1, \ldots, a_p, a_v, \ldots, x_n).$$
The terms in the sum vanish because $\Delta$ is alternating and $a_v$ appears twice. Thus $\bar{\Delta}$ is well-defined.

To show independence of the representing determinant function: if $\Delta' = \lambda \Delta$ with $\lambda > 0$, then $\bar{\Delta}' = \lambda \bar{\Delta}$. For a different positive basis $a'_v = \sum_{\mu} \alpha_v^\mu a_\mu$ of $F$ with $\det(\alpha_v^\mu) > 0$, we have
$$\Delta(a'_1, \ldots, a'_p, x_{p+1}, \ldots, x_n) = \det(\alpha_v^\mu) \Delta(a_1, \ldots, a_p, x_{p+1}, \ldots, x_n),$$
so the new function is a positive scalar multiple of the original. Thus the orientation is well-defined.
