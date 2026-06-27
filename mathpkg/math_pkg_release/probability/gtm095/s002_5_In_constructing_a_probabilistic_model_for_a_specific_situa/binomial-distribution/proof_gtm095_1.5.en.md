---
role: proof
locale: en
of_concept: binomial-distribution
source_book: gtm095
source_chapter: "1"
source_section: "5"
---

# Proof of the Binomial Distribution

**Probabilistic model for $n$ tosses of a coin (Bernoulli scheme).** Consider the sample space
$$\Omega = \{\omega : \omega = (a_1, \ldots, a_n),\; a_i \in \{0,1\}\},$$
where $a_i = 1$ denotes "success" (heads) and $a_i = 0$ denotes "failure" (tails) on the $i$-th toss. To each sample point $\omega = (a_1, \ldots, a_n)$ assign the probability
$$p(\omega) = p^{\sum a_i} q^{n - \sum a_i},$$
where $p \geq 0$, $q \geq 0$, and $p + q = 1$.

**Verification of consistency.** We must show $\sum_{\omega \in \Omega} p(\omega) = 1$. Group outcomes by the number of successes $k = \sum_i a_i$, where $k = 0, 1, \ldots, n$. The number of outcomes with exactly $k$ successes is $\binom{n}{k}$ (choosing which $k$ of the $n$ positions are successes). Hence
$$\sum_{\omega \in \Omega} p(\omega) = \sum_{k=0}^n \binom{n}{k} p^k q^{n-k} = (p+q)^n = 1,$$
by the binomial theorem. Thus $(\Omega, \mathcal{A}, \mathrm{P})$ with $\mathcal{A} = 2^\Omega$ and $\mathrm{P}(A) = \sum_{\omega \in A} p(\omega)$ is a valid discrete probability space.

**Event $A_k$: exactly $k$ successes.** For $k = 0, 1, \ldots, n$,
$$A_k = \{\omega : \omega = (a_1, \ldots, a_n),\; a_1 + \cdots + a_n = k\}.$$
Since each outcome in $A_k$ has probability $p^k q^{n-k}$ and $|A_k| = \binom{n}{k}$, we obtain the **binomial distribution**:
$$\mathrm{P}(A_k) = \binom{n}{k} p^k q^{n-k}, \quad k = 0, 1, \ldots, n.$$

**Extension: Random walk interpretation.** For a random walk on $\mathbb{Z}$ starting at $0$, let each step be $+1$ (with probability $p$) or $-1$ (with probability $q$). After $n$ steps the position is $S_n = \nu(\omega) - (n - \nu(\omega)) = 2\nu(\omega) - n$, where $\nu(\omega) = \sum a_i$ is the number of $+1$ steps. The position $S_n = k$ requires $\nu(\omega) = (n + k)/2$, so
$$\mathrm{P}(S_n = k) = \binom{n}{(n+k)/2} p^{(n+k)/2} q^{(n-k)/2}, \quad k = -n, -n+2, \ldots, n.$$

In the **symmetric case** $p = q = 1/2$, every individual path has probability $2^{-n}$, giving
$$\mathrm{P}(S_n = k) = \binom{n}{(n+k)/2} \cdot 2^{-n}.$$

**Asymptotic behavior (via Stirling's formula).** For $2n$ steps in the symmetric case, the largest probability is at the origin:
$$\mathrm{P}(S_{2n} = 0) = \binom{2n}{n} 2^{-2n} \sim \frac{1}{\sqrt{\pi n}} \quad \text{as } n \to \infty.$$
