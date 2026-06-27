---
role: exercise
locale: en
chapter: "10"
section: "52"
exercise_number: 14
---

If $m$ is an odd prime, show that the number of patterns induced by $G = G_0(\Delta_m)$ when $Y$ is an $n$-set is

$$\pi_n(G) = (n^{m-1} + mn^{(m-1)/2} + m - 1)n/2m.$$

Let us refine the necklace question as follows. Given $k_1, k_2, \ldots \in \mathbb{N}$, how many necklaces can one string using exactly $k_i$ beads of color $i$, where it is of course understood that $\sum_{i=1}^{\infty} k_i$ is finite? Pólya’s theorem addresses itself to this question while the lemmas of this section are inadequate. What we are in fact asking is, how many patterns $Q$ have been given weight $w(Q) = \prod_{i=1}^{\infty} y_i^{k_i}$? The answer is to be found by determining the coefficient of $\prod_{i=1}^{\infty} y_i^{k_i}$ in the right-hand member of the formula in Theorem C7.

For example, how many necklaces can be made with two orange beads, two blue beads and one white bead? With $m = 5$, $k_1 = k_2 = 2$, $k_3 = 1$, and $|G| = 10$, we shudder at the prospect of having to use Pólya’s formula, but since in
