---
role: proof
locale: en
of_concept: z-matrix-characterization-strong-ergodic
source_book: gtm040
source_chapter: "9"
source_section: "5. Strong ergodic chains"
---

**Forward direction:** Suppose $P$ is strong ergodic. Since $\alpha(I - A) = 0$, each column of $I - A$ is a charge with potential

$$-G(I - A) = \sum_{n=0}^{\infty} G(P - A)^n (I - A) = \sum_{n=0}^{\infty} (P - A)^n - A = Z - A.$$

Thus $Z = A - G(I - A)$ exists and is finite-valued.

**Reverse direction:** Suppose $Z$ exists. Then

$$(\alpha M)_j \alpha_j = (\alpha M D^{-1})_j = (\alpha C)_j$$

$$\leq \liminf_{n} \sum_{k} \left[\alpha_k \left(N_{jj}^{(n-1)} - N_{kj}^{(n-1)}\right)\right] \quad \text{by Fatou's Theorem}$$

$$= \liminf_{n} \left(N_{jj}^{(n-1)} - n \alpha_j\right)$$

$$= \liminf_{n} \sum_{m=0}^{n-1} (P^m - A)_{jj}$$

$$= \liminf_{n} \sum_{m=0}^{n-1} \left[(P - A)^m\right]_{jj} - A_{jj}$$

$$= Z_{jj} - \alpha_j.$$

Hence $\alpha M$ is finite-valued, and $P$ is strong ergodic.
