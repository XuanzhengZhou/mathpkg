---
role: proof
locale: en
of_concept: distribution-approximation-via-fourier-coefficients
source_book: gtm012
source_chapter: "5"
source_section: "§2. Fourier series, convolutions, and approximation"
---

# Proof of Distribution Approximation via Fourier Coefficients

Let $(F_m)_{m=1}^{\infty} \subset \mathcal{P}'$ with Fourier coefficients $(a_{m,n})_{n=-\infty}^{\infty}$. Suppose there exist $r > 0$ and a constant $c$ such that

$$|a_{m,n}| \leq c|n|^r, \quad \text{for all } m \geq 1,\ \text{all } n \neq 0.$$

Suppose further that for each $n \in \mathbb{Z}$,

$$a_{m,n} \to a_n \quad \text{as } m \to \infty.$$

Then $(a_n)_{n=-\infty}^{\infty}$ is the sequence of Fourier coefficients of some $F \in \mathcal{P}'$, and $F_m \to F$ in $\mathcal{P}'$.

**Proof.** Taking the limit as $m \to \infty$ in the growth bound yields

$$|a_n| \leq c|n|^r, \quad \text{for all } n \neq 0.$$

Thus $(a_n)_{n=-\infty}^{\infty}$ is a slowly growing sequence. By the characterization theorem for periodic distributions (Theorem 1.1), there exists a unique $F \in \mathcal{P}'$ having $(a_n)$ as its Fourier coefficients.

It remains to prove convergence in the sense of distributions. Choose an integer $k \geq r + 2$ and define, for $n \neq 0$,

$$b_{m,n} = (in)^{-k} a_{m,n}, \qquad b_n = (in)^{-k} a_n,$$

together with $b_{m,0} = b_0 = 0$. Then for $n \neq 0$,

$$|b_{m,n}| = |n|^{-k} |a_{m,n}| \leq c|n|^{r-k} \leq c|n|^{-2},$$

since $r - k \leq -2$ (because $k \geq r+2$). The same bound holds for $|b_n|$.

Consequently, the sequences $(b_{m,n})$ and $(b_n)$ are rapidly decreasing. Let $u_m, u \in \mathcal{P}$ be the smooth periodic functions whose Fourier coefficients are $(b_{m,n})$ and $(b_n)$, respectively. By Theorem 2.2 (the uniform approximation theorem), $u_m \to u$ uniformly together with all derivatives, i.e., $u_m \to u$ in $\mathcal{P}$.

Now observe the relationship between the original sequences and the smoothed ones:

$$a_{m,n} = (in)^k b_{m,n} \quad (n \neq 0), \qquad a_n = (in)^k b_n \quad (n \neq 0).$$

In terms of distributions, this means

$$F_m = a_{m,0} \delta_0 + D^k u_m, \qquad F = a_0 \delta_0 + D^k u,$$

where $D^k: \mathcal{P} \to \mathcal{P}'$ is the $k$-th distributional derivative. Indeed, the Fourier coefficient of $D^k u_m$ at frequency $n$ is $(in)^k b_{m,n} = a_{m,n}$ for $n \neq 0$, and the zeroth coefficient of $D^k u_m$ is $0$ (since differentiation kills constants).

Since $a_{m,0} \to a_0$ (by the hypothesis for $n = 0$) and $D^k: \mathcal{P} \to \mathcal{P}'$ is continuous (differentiation is a continuous operator on distributions), we have

$$F_m = a_{m,0} \delta_0 + D^k u_m \;\to\; a_0 \delta_0 + D^k u = F \quad \text{in } \mathcal{P}'.$$

Thus $F_m \to F$ in $\mathcal{P}'$, completing the proof. $\square$
