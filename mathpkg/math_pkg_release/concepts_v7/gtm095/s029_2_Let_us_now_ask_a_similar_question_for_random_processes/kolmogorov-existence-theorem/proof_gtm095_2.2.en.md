---
role: proof
locale: en
of_concept: kolmogorov-existence-theorem
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Kolmogorov's Existence Theorem for Random Processes

**Kolmogorov's Existence Theorem.** Let $\{F_{t_1, \ldots, t_n}(x_1, \ldots, x_n)\}$ be a consistent family of finite-dimensional distribution functions (in the sense of (2) with the natural consistency conditions). Then there exist a probability space $(\Omega, \mathcal{F}, P)$ and a random process $X = (\xi_t)_{t \in T}$ defined on it such that

$$P\{\xi_{t_1} \leq x_1, \ldots, \xi_{t_n} \leq x_n\} = F_{t_1, \ldots, t_n}(x_1, \ldots, x_n)$$

for all $t_1, \ldots, t_n \in T$, $t_1 < t_2 < \cdots < t_n$, and all $x_1, \ldots, x_n$.

*Proof.* It follows from Theorem 1 of Sect. 3 that there is a probability measure $P$ (and only one) on $(R, \mathcal{B}(R))$ for which $P(a, b] = F(b) - F(a)$, $a < b$.

Put $\xi(\omega) \equiv \omega$. Then

$$P\{\omega : \xi(\omega) \leq x\} = P\{\omega : \omega \leq x\} = P(-\infty, x] = F(x).$$

Consequently we have constructed the required probability space and the random variable on it.

For the general case, let $X = (\xi_t)_{t \in T}$ be a random process defined on $(\Omega, \mathcal{F}, P)$, with $t \in T \subseteq \mathbb{R}$. The finite-dimensional distributions

$$F_{t_1, \ldots, t_n}(x_1, \ldots, x_n) = P\{\omega : \xi_{t_1} \leq x_1, \ldots, \xi_{t_n} \leq x_n\}$$

must satisfy the Kolmogorov consistency condition:

$$\lim_{x_k \uparrow \infty} F_{t_1, \dots, t_n}(x_1, \dots, x_n) = F_{t_1, \dots, t_{k-1}, t_{k+1}, \dots, t_n}(x_1, \dots, x_{k-1}, x_{k+1}, \dots, x_n).$$

Given a consistent family $\{F_{\tau}\}$, let $P_{\tau}$ be the probability measure on $(R^n, \mathcal{B}(R^n))$ corresponding to $F_{\tau}$ for each finite ordered set $\tau = [t_1, \ldots, t_n]$. The consistency condition implies that the family $\{P_{\tau}\}$ is consistent. By Theorem 4 of Sect. 3 (Kolmogorov's extension theorem for product spaces), there is a unique probability measure $P$ on $(R^T, \mathcal{B}(R^T))$ such that

$$P\{\omega : (\omega_{t_1}, \ldots, \omega_{t_n}) \in B\} = P_{\tau}(B)$$

for every finite set $\tau = [t_1, \ldots, t_n]$ and every $B \in \mathcal{B}(R^n)$. Therefore the required random process $X = (\xi_t)_{t \in T}$ can be taken to be the process defined by the coordinate method:

$$\xi_t(\omega) = \omega_t, \quad t \in T.$$

This completes the proof of the theorem. $\square$

**Remark 1.** The probability space $(R^T, \mathcal{B}(R^T), P)$ that we have constructed is called *canonical*, and the construction given by $\xi_t(\omega) = \omega_t$ is called the *coordinate method* of constructing the process.

**Remark 2.** The theorem generalizes to arbitrary complete separable metric spaces $(E_{\alpha}, \mathcal{E}_{\alpha})$: given a consistent family of finite-dimensional distributions on product spaces, there exists a probability space and a family of measurable functions realizing those distributions.
