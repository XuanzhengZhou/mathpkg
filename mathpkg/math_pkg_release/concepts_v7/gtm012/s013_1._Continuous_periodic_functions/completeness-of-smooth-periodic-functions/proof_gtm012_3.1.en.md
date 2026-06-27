---
role: proof
locale: en
of_concept: completeness-of-smooth-periodic-functions
source_book: gtm012
source_chapter: "3"
source_section: "1. Continuous periodic functions"
---

# Proof of Completeness of Smooth Periodic Functions under the Metric $d'$

**Theorem 2.2.** A sequence of functions $(u_n)_{n=1}^{\infty} \subset \mathcal{P}$ is a Cauchy sequence in the sense of $\mathcal{P}$ if and only if it is a Cauchy sequence in the sense of the metric $d'$. Thus $(\mathcal{P}, d')$ is a complete metric space.

Recall the definitions. A sequence $(u_n) \subset \mathcal{P}$ is Cauchy in the sense of $\mathcal{P}$ if for each $k = 0, 1, 2, \ldots$,

$$|D^k u_n - D^k u_m| \to 0 \quad \text{as} \quad m, n \to \infty.$$

The metric $d'$ is defined by

$$d'(u, v) = \sum_{k=0}^{\infty} 2^{-k-1} \frac{|D^k u - D^k v|}{1 + |D^k u - D^k v|}.$$

Let $d^*(u,v) = |u-v|(1+|u-v|)^{-1}$, so that $d'(u,v) = \sum_{k=0}^{\infty} 2^{-k-1} d^*(D^k u, D^k v)$.

*Proof.* **($\Leftarrow$)** Suppose $(u_n)$ is Cauchy with respect to $d'$. Let $\varepsilon > 0$ and fix an integer $k \geq 0$. Choose $N$ such that $d'(u_n, u_m) < 2^{-k-2}\varepsilon$ for all $m, n \geq N$. Then

$$2^{-k-1} d^*(D^k u_n, D^k u_m) \leq d'(u_n, u_m) < 2^{-k-2}\varepsilon,$$

so $d^*(D^k u_n, D^k u_m) < \varepsilon/2$. When $\varepsilon < 2$, this implies

$$|D^k u_n - D^k u_m| < \varepsilon.$$

Thus $(D^k u_n)_{n=1}^{\infty}$ is Cauchy in the sup-norm for each $k$, so $(u_n)$ is Cauchy in the sense of $\mathcal{P}$.

**($\Rightarrow$)** Conversely, suppose $(u_n)$ is Cauchy in the sense of $\mathcal{P}$. Given $\varepsilon > 0$, choose $K$ so large that $\sum_{k=K+1}^{\infty} 2^{-k-1} = 2^{-K-1} < \varepsilon/2$. Since $(u_n)$ is Cauchy in the sense of $\mathcal{P}$, for each $k = 0, 1, \ldots, K$ there exists $N_k$ such that

$$|D^k u_n - D^k u_m| < \frac{\varepsilon}{2(K+1)}, \quad m, n \geq N_k.$$

Let $N = \max\{N_0, \ldots, N_K\}$. Then for $m, n \geq N$,

$$\begin{aligned}
d'(u_n, u_m) &= \sum_{k=0}^{K} 2^{-k-1} d^*(D^k u_n, D^k u_m) + \sum_{k=K+1}^{\infty} 2^{-k-1} d^*(D^k u_n, D^k u_m) \\
&\leq \sum_{k=0}^{K} 2^{-k-1} |D^k u_n - D^k u_m| + \sum_{k=K+1}^{\infty} 2^{-k-1} \\
&< \frac{\varepsilon}{2(K+1)} \sum_{k=0}^{K} 2^{-k-1} + \frac{\varepsilon}{2} \\
&< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
\end{aligned}$$

Thus $(u_n)$ is Cauchy with respect to $d'$.

**Completeness.** The same argument shows that $d'(u_n, u) \to 0$ if and only if $u_n \to u$ in the sense of $\mathcal{P}$. Now suppose $(u_n)$ is a Cauchy sequence in $(\mathcal{P}, d')$. By the equivalence proved above, $(u_n)$ is Cauchy in the sense of $\mathcal{P}$. Then for each $k$, $(D^k u_n)$ is Cauchy in the sup-norm, hence converges uniformly to some continuous function $v_k$. By Theorem 4.2 of Chapter 2, the uniform limit of derivatives yields $D v_k = v_{k+1}$ for all $k$. Therefore $u = v_0 \in \mathcal{P}$, and $u_n \to u$ in the sense of $\mathcal{P}$. By equivalence, $d'(u_n, u) \to 0$. Hence $(\mathcal{P}, d')$ is complete. $\square$
