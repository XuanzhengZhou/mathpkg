---
role: proof
locale: en
of_concept: schlicht-function-lemma
source_book: gtm035
source_chapter: "18"
source_section: "18.4"
---
# Proof of Schlicht Function Lemma for Bishop Disk

**Lemma 18.4.** Let $w_2, \dots, w_n$ be smooth boundary functions on $\Gamma = \{|\zeta|=1\}$ with $|w_j| < \delta$ for all $j$, and such that $w_2$ is schlicht (i.e., its analytic extension $\tilde{w}_2$ is univalent on the disk $|\zeta| < 1$). Let $U$ be the neighborhood of $x^0$ on $\Sigma^{2n-1}$ as in Theorem 18.3. Choose $\delta > 0$ such that the point described by the parametrization
$$z_1 = x_1 + i h(x_1, w), \quad z_j = w_j \; (2 \leq j \leq n)$$
lies in $U$ whenever $|x_1| < \delta$ and $|w_j| < \delta$ for $2 \leq j \leq n$. Then the analytic disk $E$ constructed in Theorem 18.3 with these boundary functions is embedded (one-to-one).

**Proof.** Let $\Phi: |\zeta| \leq 1 \to \mathbb{C}^n$ be the map defining the analytic disk, given by

$$\Phi(\zeta) = (\psi(\zeta), w_2(\zeta), \dots, w_n(\zeta)),$$

where $\psi(\zeta)$ is the analytic extension of $x^* + i h(x^*, w)$ to $|\zeta| < 1$, with $x^*$ the fixed point of the contraction $A_w$.

Suppose $\Phi(\zeta_1) = \Phi(\zeta_2)$ for some $\zeta_1, \zeta_2$ with $|\zeta_i| \leq 1$. Then comparing coordinates:

1. $w_j(\zeta_1) = w_j(\zeta_2)$ for $j = 2, \dots, n$.
2. $\psi(\zeta_1) = \psi(\zeta_2)$.

Since $w_2$ is schlicht (univalent) by hypothesis, condition (1) for $j = 2$ implies $\zeta_1 = \zeta_2$. Hence $\Phi$ is one-to-one, i.e., the Bishop disk is embedded.

**Remark.** The schlicht property of $w_2$ guarantees that the projection of $E$ onto the $z_2$-coordinate is one-to-one, which forces the entire map $\Phi$ to be one-to-one. This lemma is an essential ingredient in ensuring that the analytic disks constructed by Bishop's method are genuine embedded analytic disks, not parametrized with self-intersections. If $w_2$ is not schlicht but only a smooth boundary function, the fixed-point argument still produces an analytic disk, but it may self-intersect.
