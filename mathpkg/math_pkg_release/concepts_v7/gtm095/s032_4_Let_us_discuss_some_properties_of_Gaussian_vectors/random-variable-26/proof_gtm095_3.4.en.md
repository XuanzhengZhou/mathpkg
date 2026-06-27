---
role: proof
locale: en
of_concept: random-variable-26
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§4. Gaussian vectors, covariance matrix"
---

# Proof of Theorem 1

## (a) Uncorrelated if and only if independent

**($\Rightarrow$)** Suppose the components of $\xi = (\xi_1, \ldots, \xi_n)^*$ are uncorrelated. Since $\xi$ is a Gaussian vector, its characteristic function has the form

$$\varphi_\xi(t) = \exp\left\{ i \sum_{k=1}^n t_k m_k - \frac{1}{2} \sum_{k,l=1}^n t_k t_l r_{kl} \right\},$$

where $m_k = \mathsf{E}\xi_k$ and $r_{kl} = \operatorname{Cov}(\xi_k, \xi_l)$. By the hypothesis of uncorrelatedness, $r_{kl} = 0$ for $k \neq l$, so

$$\varphi_\xi(t) = \exp\left\{ i \sum_{k=1}^n t_k m_k - \frac{1}{2} \sum_{k=1}^n t_k^2 r_{kk} \right\}
= \prod_{k=1}^n \exp\left\{ i t_k m_k - \frac{1}{2} t_k^2 r_{kk} \right\}
= \prod_{k=1}^n \varphi_{\xi_k}(t_k).$$

Thus the joint characteristic function factorizes into a product of the marginal characteristic functions. By Theorem 4 of Sect. 12 (Chapter 2), this factorization implies that the components $\xi_1, \ldots, \xi_n$ are independent.

**($\Leftarrow$)** Conversely, if the components are independent, then they are automatically uncorrelated, since independence always implies $\operatorname{Cov}(\xi_k, \xi_l) = \mathsf{E}(\xi_k \xi_l) - \mathsf{E}\xi_k \cdot \mathsf{E}\xi_l = 0$ for $k \neq l$.

## (b) Gaussian vector if and only if every linear combination is Gaussian

**($\Rightarrow$)** Suppose $\xi = (\xi_1, \ldots, \xi_n)^*$ is a Gaussian vector with mean vector $m = (m_1, \ldots, m_n)^*$ and covariance matrix $\mathbb{R} = (r_{kl})$. For any vector $\lambda = (\lambda_1, \ldots, \lambda_n)^* \in \mathbb{R}^n$, the linear combination $(\xi, \lambda) = \sum_{k=1}^n \lambda_k \xi_k$ has characteristic function, by formula (5),

$$\mathsf{E} \exp\left\{ i t (\xi_1 \lambda_1 + \cdots + \xi_n \lambda_n) \right\}
= \mathsf{E} \exp\left\{ i (t\lambda_1) \xi_1 + \cdots + i (t\lambda_n) \xi_n \right\}
= \exp\left\{ i t \sum_{k=1}^n \lambda_k m_k - \frac{t^2}{2} \sum_{k,l=1}^n \lambda_k \lambda_l r_{kl} \right\}.$$

This is exactly the characteristic function of a Gaussian (normal) random variable with mean $\sum \lambda_k m_k$ and variance $\sum_{k,l} \lambda_k \lambda_l r_{kl}$. Hence $(\xi, \lambda)$ has a Gaussian distribution.

**($\Leftarrow$)** Conversely, suppose that for every $\lambda \in \mathbb{R}^n$, the random variable $(\xi, \lambda)$ is Gaussian. Write $m_k = \mathsf{E}\xi_k$ and $r_{kl} = \operatorname{Cov}(\xi_k, \xi_l)$. Since $(\xi, \lambda)$ is Gaussian, its characteristic function is

$$\mathsf{E} e^{i t (\xi, \lambda)} = \exp\left\{ i t \, \mathsf{E}(\xi, \lambda) - \frac{t^2}{2} \operatorname{Var}(\xi, \lambda) \right\}
= \exp\left\{ i t \sum_{k} \lambda_k m_k - \frac{t^2}{2} \sum_{k,l} \lambda_k \lambda_l r_{kl} \right\}.$$

Setting $t = 1$ and $t_k = \lambda_k$, we obtain

$$\varphi_\xi(t) = \mathsf{E} e^{i (t, \xi)} = \exp\left\{ i \sum_{k=1}^n t_k m_k - \frac{1}{2} \sum_{k,l=1}^n t_k t_l r_{kl} \right\},$$

which is precisely the characteristic function of a Gaussian vector with mean $m$ and covariance matrix $\mathbb{R}$. Therefore $\xi$ is a Gaussian vector.

---

**Remark.** Let $\binom{\theta}{\xi}$ be a Gaussian vector with $\theta = (\theta_1, \ldots, \theta_k)^*$ and $\xi = (\xi_1, \ldots, \xi_l)^*$. If $\theta$ and $\xi$ are uncorrelated, i.e., $\operatorname{Cov}(\theta_i, \xi_j) = 0$ for all $i = 1, \ldots, k$ and $j = 1, \ldots, l$, then they are independent. The proof is the same as for conclusion (a) of the theorem.
