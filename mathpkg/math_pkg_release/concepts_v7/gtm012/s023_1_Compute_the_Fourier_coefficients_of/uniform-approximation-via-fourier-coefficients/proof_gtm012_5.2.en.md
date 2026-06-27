---
role: proof
locale: en
of_concept: uniform-approximation-via-fourier-coefficients
source_book: gtm012
source_chapter: "5"
source_section: "§2. Fourier series, convolutions, and approximation"
---

# Proof of Uniform Approximation via Fourier Coefficients

Let $(u_m)_{m=1}^{\infty} \subset \mathcal{P}$ with Fourier coefficients $(a_{m,n})_{n=-\infty}^{\infty}$. Suppose there exist $r > 0$ and a constant $c = c(r)$ such that

$$|a_{m,n}| \leq c|n|^{-r}, \quad \text{for all } m \geq 1,\ \text{all } n \neq 0.$$

Suppose further that for each $n \in \mathbb{Z}$,

$$a_{m,n} \to a_n \quad \text{as } m \to \infty.$$

Then $(a_n)_{n=-\infty}^{\infty}$ is the sequence of Fourier coefficients of some $u \in \mathcal{P}$, and $u_m \to u$ uniformly, together with all derivatives: $D^k u_m \to D^k u$ uniformly for each $k \geq 0$.

**Proof.** First, the limit condition and the uniform bound imply that $|a_n| \leq c|n|^{-r}$ for all $n \neq 0$. Thus $(a_n)$ is a rapidly decreasing sequence, and by the characterization theorem for smooth periodic functions (Theorem 1.2), there exists $u \in \mathcal{P}$ with Fourier coefficients $(a_n)$:

$$u = \sum_{n=-\infty}^{\infty} a_n e_n, \qquad u_m = \sum_{n=-\infty}^{\infty} a_{m,n} e_n.$$

We must show $u_m \to u$ uniformly and each derivative converges uniformly.

Given $\varepsilon > 0$, choose an integer $N$ so large that

$$\sum_{|n| > N} c|n|^{-r} < \varepsilon.$$

(This is possible because $r > 0$, making the series converge.) Then for every $m$,

$$\sum_{|n| > N} |a_{m,n}| < \varepsilon, \qquad \sum_{|n| > N} |a_n| < \varepsilon.$$

Now for the finite range $-N \leq n \leq N$, the pointwise convergence $a_{m,n} \to a_n$ guarantees the existence of $M$ such that $m \geq M$ implies

$$\sum_{n=-N}^{N} |a_{m,n} - a_n| < \varepsilon.$$

Combining these estimates, for $m \geq M$ we obtain

$$\sum_{n=-\infty}^{\infty} |a_{m,n} - a_n| = \sum_{n=-N}^{N} |a_{m,n} - a_n| + \sum_{|n| > N} |a_{m,n}| + \sum_{|n| > N} |a_n| < \varepsilon + \varepsilon + \varepsilon < 3\varepsilon.$$

Since $|e_n(x)| = 1$ for every $x \in \mathbb{R}$,

$$|u_m(x) - u(x)| = \left|\sum_{n=-\infty}^{\infty} (a_{m,n} - a_n) e^{inx}\right| \leq \sum_{n=-\infty}^{\infty} |a_{m,n} - a_n| < 3\varepsilon$$

for all $x$, provided $m \geq M$. Therefore $u_m \to u$ uniformly.

For the derivatives, apply the same argument to $D^k u_m$, whose Fourier coefficients are $((in)^k a_{m,n})$. The bounds $|(in)^k a_{m,n}| \leq c|n|^{k-r}$ are still rapidly decreasing (or can be handled by repeating the argument with $r$ replaced by $r-k$ when $k < r$, and using the full hypothesis that the bound holds for every $r > 0$). The exact same tail-estimate argument shows $D^k u_m \to D^k u$ uniformly for each $k \geq 0$. $\square$
