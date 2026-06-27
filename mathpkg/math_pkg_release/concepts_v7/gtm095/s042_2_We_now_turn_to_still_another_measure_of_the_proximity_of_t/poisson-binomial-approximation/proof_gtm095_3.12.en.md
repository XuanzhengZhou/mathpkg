---
role: proof
locale: en
of_concept: poisson-binomial-approximation
source_book: gtm095
source_chapter: "3"
source_section: "12.2"
---

# Proof of the Poisson approximation theorem

**Theorem.** Let $\xi_1, \ldots, \xi_n$ be independent Bernoulli random variables with $\mathbb{P}(\xi_k = 1) = p_k$, $\mathbb{P}(\xi_k = 0) = 1 - p_k$. Set $\lambda = \sum_{k=1}^{n} p_k$. Let $B$ denote the distribution of $S_n = \xi_1 + \cdots + \xi_n$ (the Poisson-binomial distribution) and $\Pi$ the Poisson distribution with parameter $\lambda$. Then

$$\|B - \Pi\| = \sum_{k=0}^{\infty} |B_k - \pi_k| \leq 2 \sum_{k=1}^{n} p_k^2 \leq 2\lambda \max_{1 \leq k \leq n} p_k.$$

**Proof.** The distribution $B$ can be expressed as the convolution

$$B = B(p_1) * B(p_2) * \cdots * B(p_n),$$

where $B(p_k) = (1 - p_k, p_k)$ is the Bernoulli distribution on $\{0, 1\}$. Similarly, the Poisson distribution $\Pi$ is

$$\Pi = \Pi(p_1) * \Pi(p_2) * \cdots * \Pi(p_n),$$

where $\Pi(p_k)$ is the Poisson distribution with parameter $p_k$ supported on $\{0, 1, 2, \ldots\}$.

The difference $B - \Pi$ can be represented as

$$B - \Pi = R_1 + \cdots + R_n, \tag{10}$$

where

$$R_k = (B(p_k) - \Pi(p_k)) * F_k, \tag{11}$$

with

$$F_1 = \Pi(p_2) * \cdots * \Pi(p_n),$$

$$F_k = B(p_1) * \cdots * B(p_{k-1}) * \Pi(p_{k+1}) * \cdots * \Pi(p_n), \quad 2 \leq k \leq n-1,$$

$$F_n = B(p_1) * \cdots * B(p_{n-1}).$$

By Problem 6 in Sect. 9, the total variation distance satisfies $\|R_k\| \leq \|B(p_k) - \Pi(p_k)\|$. Consequently, from (10),

$$\|B - \Pi\| \leq \sum_{k=1}^{n} \|B(p_k) - \Pi(p_k)\|. \tag{12}$$

It remains to calculate the variation $\|B(p_k) - \Pi(p_k)\|$. The Bernoulli distribution $B(p_k)$ puts mass $1 - p_k$ at $0$ and $p_k$ at $1$, while $\Pi(p_k)$ puts mass $e^{-p_k} p_k^j / j!$ at $j \geq 0$. Hence,

$$\|B(p_k) - \Pi(p_k)\| = |(1 - p_k) - e^{-p_k}| + |p_k - p_k e^{-p_k}| + \sum_{j \geq 2} \frac{p_k^j e^{-p_k}}{j!}$$

$$= |(1 - p_k) - e^{-p_k}| + p_k(1 - e^{-p_k}) + 1 - e^{-p_k} - p_k e^{-p_k}$$

$$= (e^{-p_k} - (1 - p_k)) + p_k(1 - e^{-p_k}) + (1 - e^{-p_k} - p_k e^{-p_k})$$

$$= e^{-p_k} - 1 + p_k + p_k - p_k e^{-p_k} + 1 - e^{-p_k} - p_k e^{-p_k}$$

$$= 2p_k(1 - e^{-p_k}) \leq 2p_k^2,$$

using the inequality $1 - e^{-x} \leq x$ for $x \geq 0$.

Substituting into (12) yields

$$\|B - \Pi\| \leq \sum_{k=1}^{n} 2p_k^2 = 2 \sum_{k=1}^{n} p_k^2 \leq 2 \max_{1 \leq k \leq n} p_k \cdot \sum_{k=1}^{n} p_k = 2\lambda \max_{1 \leq k \leq n} p_k.$$

This completes the proof with constant $C_3(\lambda) = 2\lambda$.
