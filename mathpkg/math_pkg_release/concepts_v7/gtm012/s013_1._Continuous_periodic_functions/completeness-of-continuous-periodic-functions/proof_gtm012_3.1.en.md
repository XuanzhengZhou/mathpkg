---
role: proof
locale: en
of_concept: completeness-of-continuous-periodic-functions
source_book: gtm012
source_chapter: "3"
source_section: "1. Continuous periodic functions"
---

# Proof of Completeness of the Space of Continuous Periodic Functions

**Theorem 1.1.** The set $\mathcal{C}$ of continuous periodic functions is a vector space with the operations defined by (1) and (2). The set $\mathcal{C}$ is also a metric space with respect to the metric $d$ defined by $d(u,v) = |u-v|$, and it is complete.

*Proof.* Checking that $\mathcal{C}$ satisfies the axioms for a vector space is straightforward. The axioms for a metric space are also easily checked, using (4), (5), and (6). For example,

$$d(u,w) = |u-w| = |(u-v) + (v-w)| \leq |u-v| + |v-w| = d(u,v) + d(v,w).$$

Now we prove completeness. Suppose $(u_n)_{n=1}^{\infty}$ is a Cauchy sequence of functions in $\mathcal{C}$ with respect to the sup-norm $|\cdot|$. Then for each $x \in \mathbb{R}$,

$$|u_n(x) - u_m(x)| \leq |u_n - u_m|,$$

so $(u_n(x))_{n=1}^{\infty}$ is a Cauchy sequence in $\mathbb{C}$. Since $\mathbb{C}$ is complete, we can define

$$u(x) = \lim_{n \to \infty} u_n(x), \quad x \in \mathbb{R}.$$

Given $\varepsilon > 0$, choose $N$ such that $|u_n - u_m| < \varepsilon$ for all $m, n \geq N$. Then for any $x \in \mathbb{R}$ and $n \geq N$,

$$|u_n(x) - u(x)| = \lim_{m \to \infty} |u_n(x) - u_m(x)| \leq \varepsilon.$$

Thus $u_n \to u$ uniformly on $\mathbb{R}$. By Theorem 4.2 of Chapter 2, the uniform limit of continuous functions is continuous, so $u$ is continuous. Moreover, each $u_n$ is $2\pi$-periodic, so for any $x \in \mathbb{R}$,

$$u(x + 2\pi) = \lim_{n \to \infty} u_n(x + 2\pi) = \lim_{n \to \infty} u_n(x) = u(x).$$

Hence $u$ is $2\pi$-periodic, so $u \in \mathcal{C}$. Finally, $|u_n - u| \to 0$ as $n \to \infty$ by the uniform convergence established above. Therefore $\mathcal{C}$ is complete with respect to the metric $d$, i.e., $\mathcal{C}$ is a Banach space. $\square$
