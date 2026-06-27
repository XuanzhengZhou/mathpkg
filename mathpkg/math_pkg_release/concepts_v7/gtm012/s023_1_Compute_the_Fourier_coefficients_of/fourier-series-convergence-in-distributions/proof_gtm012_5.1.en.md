---
role: proof
locale: en
of_concept: fourier-series-convergence-in-distributions
source_book: gtm012
source_chapter: "5"
source_section: "§1. Fourier series of smooth periodic functions and of periodic distributions"
---

# Proof of Convergence of Fourier Series of Periodic Distributions

Let $F \in \mathcal{P}'$ have Fourier coefficients $(a_n)_{n=-\infty}^{\infty}$. For each $N \in \mathbb{N}$, let $F_N \in \mathcal{P}'$ be the distribution defined by the smooth periodic function

$$f_N(x) = \sum_{n=-N}^{N} a_n e^{inx}.$$

We must show that $F_N \to F$ in the sense of distributions on $\mathcal{P}$, i.e., $F_N(u) \to F(u)$ for every $u \in \mathcal{P}$.

**Proof.** For any $u \in \mathcal{P}$, Theorem 1.3 provides the $N$-th partial sum $u_N$ of the Fourier series of $u$:

$$u_N(x) = \sum_{n=-N}^{N} \hat{u}(n) e^{inx},$$

where $\hat{u}(n)$ denotes the $n$-th Fourier coefficient of $u$. Theorem 1.3 guarantees that $u_N \to u$ in the topology of $\mathcal{P}$.

The distribution $F_N$ acts on $u$ via integration against the function $f_N$, while $F$ acts on $u_N$ through its Fourier coefficients. By the defining property of Fourier coefficients — namely $F(e_n) = a_{-n}$ — we have:

$$F_N(u) = \int_{0}^{2\pi} \left(\sum_{n=-N}^{N} a_n e^{inx}\right) u(x)\,dx = \sum_{n=-N}^{N} a_n \hat{u}(-n).$$

On the other hand,

$$F(u_N) = F\!\left(\sum_{n=-N}^{N} \hat{u}(n) e_n\right) = \sum_{n=-N}^{N} \hat{u}(n) F(e_n) = \sum_{n=-N}^{N} \hat{u}(n) a_{-n} = \sum_{k=-N}^{N} a_k \hat{u}(-k).$$

Thus $F_N(u) = F(u_N)$.

Since $F$ is continuous as a linear functional on $\mathcal{P}$ and $u_N \to u$ in $\mathcal{P}$, we obtain

$$F_N(u) = F(u_N) \to F(u) \qquad (N \to \infty).$$

This holds for every $u \in \mathcal{P}$, which is the definition of convergence in $\mathcal{P}'$: $F_N \to F$ in $\mathcal{P}'$. $\square$
