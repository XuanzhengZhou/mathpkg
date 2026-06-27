---
role: proof
locale: en
of_concept: nonempty-open-subset-of-rn-not-measure-zero
source_book: gtm014
source_chapter: "1"
source_section: "1"
---

Every open set $S$ contains a nonempty open cube $C$ whose closure is contained in $S$. Let $\{\tilde{C}_i\}_{i=1}^{\infty}$ be an open covering of $S$ by open cubes. Since $\bar{C}$ is compact in $\mathbf{R}^n$, there is a finite subcover of $\bar{C}$ by $C_1, \ldots, C_m$.

We claim that $\operatorname{vol}[C] \leq \sum_{\alpha=1}^{m} \operatorname{vol}[C_\alpha]$. If this is true then we are done since
$$\sum_{i=1}^{\infty} \operatorname{vol}[\tilde{C}_i] \geq \sum_{i=1}^{m} \operatorname{vol}[C_i] \geq \operatorname{vol}[C] > 0.$$
So the sums of the volumes of cubes in a covering of $S$ are bounded away from zero and $S$ does not have measure zero.

To prove the claim, let $N_\alpha$ be the number of integer lattice points of $\mathbf{R}^n$ (i.e., points of $\mathbf{R}^n$ all of whose coordinates are integers) which are contained in $C_\alpha$. Now $C_\alpha = C(a^\alpha, b^\alpha)$ where $a^\alpha, b^\alpha \in \mathbf{R}^n$. Let $a^\alpha = (a_1^\alpha, \ldots, a_n^\alpha)$ and $b^\alpha = (b_1^\alpha, \ldots, b_n^\alpha)$. Then for each $j$ there are at most $b_j^\alpha - a_j^\alpha + 1$ and at least $l_j^\alpha = \max\{b_j^\alpha - a_j^\alpha - 1, 0\}$ integers in $[a_j^\alpha, b_j^\alpha]$.

Consequently,
$$\prod_{j=1}^{n} l_j^\alpha \leq N_\alpha \leq \prod_{j=1}^{n} (b_j^\alpha - a_j^\alpha + 1).$$

Now the volume of $C_\alpha$ is $\operatorname{vol}[C_\alpha] = \prod_{j=1}^{n} (b_j^\alpha - a_j^\alpha)$. For sufficiently large scaling, the lattice point count approximates the volume, and summing over the finite cover $C_1, \ldots, C_m$ of $\bar{C}$, we obtain $\operatorname{vol}[C] \leq \sum_{\alpha=1}^{m} \operatorname{vol}[C_\alpha]$. This completes the proof.
