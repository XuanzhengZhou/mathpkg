---
role: proof
locale: en
of_concept: brownian-motion
source_book: gtm095
source_chapter: "3"
source_section: "6"
---

# Proof of Theorem 3 (Quadratic Variation of Brownian Motion)

**Theorem 3.** Let $B = (B_t)_{t \geq 0}$ be the standard Brownian motion. Then, with probability one,

$$\lim_{n \to \infty} \sum_{k=1}^{2^n} \left[ B_{k2^{-n}} - B_{(k-1)2^{-n}} \right]^2 = T$$

for any $T > 0$.

*Proof.* The proof illustrates an elegant application of the Borel--Cantelli lemma (Sect. 10 of Chapter 2, Corollary 1).

Without loss of generality we may take $T = 1$; the general case follows by Brownian scaling. For each $n \geq 1$ and $\varepsilon > 0$, set

$$A_n^\varepsilon = \left\{ \omega : \left| \sum_{k=1}^{2^n} \left( B_{k2^{-n}} - B_{(k-1)2^{-n}} \right)^2 - 1 \right| \geq \varepsilon \right\}.$$

The increments $\Delta_k^{(n)} = B_{k2^{-n}} - B_{(k-1)2^{-n}}$ are independent Gaussian random variables with $\mathbb{E}[\Delta_k^{(n)}] = 0$ and $\operatorname{Var}(\Delta_k^{(n)}) = 2^{-n}$. For $X \sim \mathcal{N}(0, \sigma^2)$, we have $\mathbb{E}[X^2] = \sigma^2$ and $\operatorname{Var}(X^2) = 2\sigma^4$. Hence

$$\mathbb{E}\!\left[(\Delta_k^{(n)})^2\right] = 2^{-n}, \qquad \operatorname{Var}\!\left((\Delta_k^{(n)})^2\right) = 2 \cdot 2^{-2n}.$$

Let $S_n = \sum_{k=1}^{2^n} (\Delta_k^{(n)})^2$. By independence of the increments,

$$\mathbb{E}[S_n] = 2^n \cdot 2^{-n} = 1, \qquad \operatorname{Var}(S_n) = 2^n \cdot 2 \cdot 2^{-2n} = 2^{-n+1}.$$

Applying Chebyshev's inequality,

$$\mathsf{P}(A_n^\varepsilon) = \mathsf{P}(|S_n - 1| \geq \varepsilon) \leq \frac{\operatorname{Var}(S_n)}{\varepsilon^2} = \frac{2^{-n+1}}{\varepsilon^2}.$$

Consequently,

$$\sum_{n=1}^{\infty} \mathsf{P}(A_n^\varepsilon) \leq \varepsilon^{-2} \sum_{n=1}^{\infty} 2^{-n+1} = 2\varepsilon^{-2} < \infty.$$

By the Borel--Cantelli lemma, $\mathsf{P}(\limsup_n A_n^\varepsilon) = 0$. Thus, for almost every $\omega$, there exists $N = N(\omega, \varepsilon)$ such that for all $n \geq N$,

$$\left| \sum_{k=1}^{2^n} \left( B_{k2^{-n}} - B_{(k-1)2^{-n}} \right)^2 - 1 \right| < \varepsilon.$$

Since $\varepsilon$ is arbitrary, $\lim_{n \to \infty} \sum_{k=1}^{2^n} (B_{k2^{-n}} - B_{(k-1)2^{-n}})^2 = 1$ almost surely. For an arbitrary $T > 0$, the same argument applied to the partition $\{k T/2^n\}_{k=0}^{2^n}$ gives the limit $T$. $\square$
