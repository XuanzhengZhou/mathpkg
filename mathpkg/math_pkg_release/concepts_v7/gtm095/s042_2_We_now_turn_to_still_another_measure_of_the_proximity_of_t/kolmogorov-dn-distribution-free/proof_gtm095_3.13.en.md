---
role: proof
locale: en
of_concept: kolmogorov-dn-distribution-free
source_book: gtm095
source_chapter: "3"
source_section: "13.3"
---

# Proof of Lemma 1 (Distribution-free property of the Kolmogorov–Smirnov statistic)

Let $\xi_1, \xi_2, \ldots$ be independent identically distributed random variables with continuous distribution function $F(x) = \mathbb{P}(\xi_k \leq x)$. Define the empirical distribution function

$$F_N(x; \omega) = \frac{1}{N} \sum_{k=1}^{N} I(\xi_k(\omega) \leq x),$$

and the Kolmogorov–Smirnov statistics

$$D_N(\omega) = \sup_{x \in \mathbb{R}} |F_N(x; \omega) - F(x)|, \quad D_N^+(\omega) = \sup_{x \in \mathbb{R}} (F_N(x; \omega) - F(x)).$$

**Lemma 1 (Kolmogorov).** Let $\mathbb{F}$ be the class of continuous distribution functions $F = F(x)$. For any $N \geq 1$, the probability distribution of $D_N(\omega)$ is the same for all $F \in \mathbb{F}$. The same is true also for $D_N^+(\omega)$.

**Proof.** Let $\eta_1, \eta_2, \ldots$ be a sequence of independent identically distributed random variables with uniform distribution on $[0, 1]$, i.e., having distribution function $U(x) = \mathbb{P}(\eta_1 \leq x) = x$, $0 \leq x \leq 1$.

To prove the lemma, we show that for any continuous distribution function $F$, the distribution of $\sup_x |F_N(x; \omega) - F(x)|$ coincides with the distribution of $\sup_x |U_N(x; \omega) - U(x)|$, where

$$U_N(x; \omega) = N^{-1} \sum_{k=1}^{N} I(\eta_k(\omega) \leq x)$$

is the empirical distribution function of the variables $\eta_1, \ldots, \eta_N$.

Denote by $A$ the union of intervals $I = [a, b]$, $-\infty < a < b < \infty$, on which $F$ is constant, so that $\mathbb{P}(\xi_1 \in I) = 0$. Then

$$D_N(\omega) = \sup_{x \in \mathbb{R}} |F_N(x; \omega) - F(x)| = \sup_{x \in \overline{A}} |F_N(x; \omega) - F(x)|.$$

Introduce the variables $\tilde{\eta}_k = F(\xi_k)$. Since $F$ is continuous,

$$\mathbb{P}\{\tilde{\eta}_1 = 0\} = \mathbb{P}\{\tilde{\eta}_1 = 1\} = 0. \tag{11}$$

Now we show that the random variables $\tilde{\eta}_k$ are uniformly distributed on $[0, 1]$. For $y \in (0, 1)$, define

$$x(y) = \inf\{x \in \mathbb{R} : F(x) \geq y\}.$$

Then $F(x(y)) = y$ for $y \in (0, 1)$ (by continuity of $F$), and

$$\mathbb{P}\{\tilde{\eta}_1 \leq y\} = \mathbb{P}\{F(\xi_1) \leq y\} = \mathbb{P}\{F(\xi_1) \leq F(x(y))\} = \mathbb{P}\{\xi_1 \leq x(y)\} = F(x(y)) = y.$$

Combined with (11), this proves that $\tilde{\eta}_1$ (and hence each $\tilde{\eta}_k$) is uniformly distributed on $[0, 1]$.

The empirical distribution function of the $\tilde{\eta}_k$ at a point $x \in \overline{A}$ equals

$$\tilde{U}_N(F(x); \omega) = \frac{1}{N} \sum_{k=1}^{N} I(F(\xi_k) \leq F(x)) = \frac{1}{N} \sum_{k=1}^{N} I(\xi_k \leq x) = F_N(x; \omega),$$

where the equality $I(F(\xi_k) \leq F(x)) = I(\xi_k \leq x)$ holds on $\overline{A}$ since $F$ is strictly increasing there. Therefore,

$$D_N(\omega) = \sup_{x \in \overline{A}} |\tilde{U}_N(F(x); \omega) - F(x)| = \sup_{t \in [0,1]} |\tilde{U}_N(t; \omega) - t|,$$

and the distribution of $\tilde{U}_N(t; \omega)$ is exactly that of $U_N(t; \omega)$ for uniform variables. Hence the distribution of $D_N$ (and similarly $D_N^+$) does not depend on the particular continuous $F$.
