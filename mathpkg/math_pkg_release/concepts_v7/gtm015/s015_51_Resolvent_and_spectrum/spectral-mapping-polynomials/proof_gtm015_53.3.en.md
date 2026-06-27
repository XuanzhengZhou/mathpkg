---
role: proof
locale: en
of_concept: spectral-mapping-polynomials
source_book: gtm015
source_chapter: "53"
source_section: "53.3"
---

# Proof of Spectral mapping theorem for polynomials

**Proof.** If $p$ is constant, $p = a_0$, then $\sigma(p(x)) = \sigma(a_0 1) = \{a_0\} = p(\sigma(x))$.

Assume $p$ nonconstant, $\deg p = n \ge 1$. Let $\mu \in \mathbb{C}$. Factor $p - \mu$:
$$p(t) - \mu = a_0(t - \lambda_1)\cdots(t - \lambda_n)$$
where $a_0 \neq 0$. Then
$$p(x) - \mu 1 = a_0(x - \lambda_1 1)\cdots(x - \lambda_n 1).$$
Since the factors commute, $p(x) - \mu 1$ is invertible iff each $x - \lambda_k 1$ is invertible. Thus $\mu \in \sigma(p(x))$ iff $\lambda_k \in \sigma(x)$ for some $k$, iff $p(\lambda) - \mu = 0$ for some $\lambda \in \sigma(x)$, iff $\mu \in p(\sigma(x))$.
