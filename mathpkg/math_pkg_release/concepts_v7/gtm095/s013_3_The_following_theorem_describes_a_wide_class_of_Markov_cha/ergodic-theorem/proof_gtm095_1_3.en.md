---
role: proof
locale: en
of_concept: ergodic-theorem
source_book: gtm095
source_chapter: "1"
source_section: "3"
---

# Proof of Theorem 1 (Ergodic Theorem)

Let $\mathbb{P} = \|p_{ij}\|$ be the transition matrix of a Markov chain with finite state space $X = \{1, 2, \ldots, N\}$. Define

$$m_j^{(n)} = \min_i p_{ij}^{(n)}, \qquad M_j^{(n)} = \max_i p_{ij}^{(n)}.$$

## Proof of (a)

Assume there exists $n_0$ such that $\min_{i,j} p_{ij}^{(n_0)} > 0$. Set $\varepsilon = \min_{i,j} p_{ij}^{(n_0)} > 0$.

For any $n \geq 0$, by the Chapman-Kolmogorov equation:

$$p_{ij}^{(n_0+n)} = \sum_{\alpha} p_{i\alpha}^{(n_0)} p_{\alpha j}^{(n)}.$$

Rewrite using the trick of subtracting $\varepsilon p_{j\alpha}^{(n)}$:

$$p_{ij}^{(n_0+n)} = \sum_{\alpha} \left[ p_{i\alpha}^{(n_0)} - \varepsilon p_{j\alpha}^{(n)} \right] p_{\alpha j}^{(n)} + \varepsilon \sum_{\alpha} p_{j\alpha}^{(n)} p_{\alpha j}^{(n)}$$

$$= \sum_{\alpha} \left[ p_{i\alpha}^{(n_0)} - \varepsilon p_{j\alpha}^{(n)} \right] p_{\alpha j}^{(n)} + \varepsilon p_{jj}^{(2n)}.$$

Since $\varepsilon = \min_{i,j} p_{ij}^{(n_0)}$, we have $p_{i\alpha}^{(n_0)} - \varepsilon p_{j\alpha}^{(n)} \geq 0$. Using $p_{\alpha j}^{(n)} \geq m_j^{(n)}$, we obtain:

$$p_{ij}^{(n_0+n)} \geq m_j^{(n)} \cdot \sum_{\alpha} \left[ p_{i\alpha}^{(n_0)} - \varepsilon p_{j\alpha}^{(n)} \right] + \varepsilon p_{jj}^{(2n)} = m_j^{(n)} (1 - \varepsilon) + \varepsilon p_{jj}^{(2n)}.$$

Since this holds for all $i$, taking the minimum over $i$ yields:

$$m_j^{(n_0+n)} \geq m_j^{(n)} (1 - \varepsilon) + \varepsilon p_{jj}^{(2n)}.$$

A similar argument, using the upper bound, gives:

$$M_j^{(n_0+n)} \leq M_j^{(n)} (1 - \varepsilon) + \varepsilon p_{jj}^{(2n)}.$$

Combining these two inequalities:

$$M_j^{(n_0+n)} - m_j^{(n_0+n)} \leq \left( M_j^{(n)} - m_j^{(n)} \right) \cdot (1 - \varepsilon).$$

By induction on $k$:

$$M_j^{(kn_0+n)} - m_j^{(kn_0+n)} \leq \left( M_j^{(n)} - m_j^{(n)} \right) \cdot (1 - \varepsilon)^k \to 0 \qquad (k \to \infty).$$

Since $0 < \varepsilon \leq 1$, we have $(1 - \varepsilon)^k \to 0$ as $k \to \infty$.

This shows that $\lim_{n\to\infty} (M_j^{(n)} - m_j^{(n)}) = 0$. Since $m_j^{(n)} \leq p_{ij}^{(n)} \leq M_j^{(n)}$ for all $i$, the limits

$$\pi_j = \lim_{n\to\infty} p_{ij}^{(n)}$$

exist and are independent of the initial state $i$. Moreover, $0 \leq m_j^{(n)} \leq \pi_j \leq M_j^{(n)} \leq 1$, and since $m_j^{(n)} \geq \varepsilon > 0$ (from the same inequality chain), we have $\pi_j > 0$.

To see that $\sum_j \pi_j = 1$, note that $\sum_j p_{ij}^{(n)} = 1$ for all $n$ and all $i$, so taking limits:

$$\sum_j \pi_j = \sum_j \lim_{n\to\infty} p_{ij}^{(n)} = \lim_{n\to\infty} \sum_j p_{ij}^{(n)} = 1.$$

This establishes (22) and (23).

## Proof of (c) — Stationarity

From the Chapman-Kolmogorov equation:

$$p_{ij}^{(n+1)} = \sum_{\alpha} p_{i\alpha}^{(n)} p_{\alpha j}.$$

Taking the limit $n \to \infty$ and using (23):

$$\pi_j = \lim_{n\to\infty} p_{ij}^{(n+1)} = \lim_{n\to\infty} \sum_{\alpha} p_{i\alpha}^{(n)} p_{\alpha j} = \sum_{\alpha} \pi_{\alpha} p_{\alpha j}.$$

This is equation (24). Thus $(\pi_1, \ldots, \pi_N)$ is a stationary distribution.

### Uniqueness of the stationary distribution

Let $(\tilde{\pi}_1, \ldots, \tilde{\pi}_N)$ be any stationary distribution, i.e., $\tilde{\pi}_j = \sum_\alpha \tilde{\pi}_\alpha p_{\alpha j}$ and $\sum_\alpha \tilde{\pi}_\alpha = 1$. Iterating the stationarity equation:

$$\tilde{\pi}_j = \sum_{\alpha} \tilde{\pi}_\alpha p_{\alpha j}^{(n)}$$

for all $n \geq 1$. Taking the limit $n \to \infty$ and using (23):

$$\tilde{\pi}_j = \sum_{\alpha} \tilde{\pi}_\alpha \cdot \lim_{n\to\infty} p_{\alpha j}^{(n)} = \sum_{\alpha} \tilde{\pi}_\alpha \cdot \pi_j = \pi_j \sum_{\alpha} \tilde{\pi}_\alpha = \pi_j.$$

Hence the stationary distribution is unique and coincides with $(\pi_1, \ldots, \pi_N)$.

## Proof of (b) — Converse

Suppose there exist numbers $\pi_1, \ldots, \pi_N$ satisfying $\pi_j > 0$, $\sum_j \pi_j = 1$, and $p_{ij}^{(n)} \to \pi_j$ as $n \to \infty$ for all $i, j$.

Since $\pi_j > 0$ for all $j$, for each $j$ there exists $N_j$ such that for all $n \geq N_j$ and all $i$, $p_{ij}^{(n)} > \pi_j/2 > 0$. Take $n_0 = \max_j N_j$. Then for all $i, j$:

$$p_{ij}^{(n_0)} \geq \pi_j/2 > 0.$$

Hence $\min_{i,j} p_{ij}^{(n_0)} > 0$, which is condition (21). This completes the proof.

## Remark on convergence rate

The inequality

$$M_j^{(kn_0+n)} - m_j^{(kn_0+n)} \leq (1 - \varepsilon)^k$$

implies that the convergence $p_{ij}^{(n)} \to \pi_j$ is exponential: there exist constants $C > 0$ and $0 < \rho < 1$ such that

$$|p_{ij}^{(n)} - \pi_j| \leq C \cdot \rho^n$$

for all $i, j$ and all sufficiently large $n$. This exponential convergence is a key property that underlies the law of large numbers for Markov chains (see Corollary below).
