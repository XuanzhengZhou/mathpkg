---
role: proof
locale: en
of_concept: conditional-expectation-smoothing-atoms
source_book: gtm046
source_chapter: "28"
source_section: "28.2"
---

The first assertion follows from the fact that $E^{\mathcal{B}}X$ is a $\mathcal{B}$-measurable function defined up to a $P_{\mathcal{B}}$-equivalence and a $\mathcal{B}$-measurable function is constant on atoms of $\mathcal{B}$. Therefore, on every atom $B$ of $\mathcal{B}$,

$$
E_B X \cdot P B = \int_B (E^{\mathcal{B}}X) \, dP_{\mathcal{B}} = \int_B X \, dP
$$

and, for $P B > 0$,

$$
E_B X = \frac{1}{P B} \int_B X \, dP.
$$

This proves the second assertion and completes the proof.

Thus, $E^{\mathcal{B}}X$ is a $\mathcal{B}$-smoothed $X$, in the sense that on atoms of $\mathcal{B}$ which are not atoms of $\alpha$, $E^{\mathcal{B}}X$ is an "averaged $X$" and, on the whole, has "fewer values" than $X$. In particular, if $\mathcal{B}$ is the minimal $\sigma$-field over a countable partition $\{B_j\}$ of $\Omega$, so that the $B_j$ are atoms of $\mathcal{B}$, then

$$
E^{\mathcal{B}}X = \sum_j (E_{B_j} X) I_{B_j} \quad \text{a.s.}
$$
