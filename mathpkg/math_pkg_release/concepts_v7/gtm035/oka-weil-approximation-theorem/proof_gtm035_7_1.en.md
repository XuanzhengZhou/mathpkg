---
role: proof
locale: en
of_concept: oka-weil-approximation-theorem
source_book: gtm035
source_chapter: "Chapter 7"
source_section: "7.1"
---
# Proof of Oka-Weil Approximation Theorem

Let $\mathcal{L}$ denote the space of all finite linear combinations of functions $1/(z-a)^p$, where $a \in \mathbb{C}\setminus \Omega$, $p$ an integer $\geq 0$. By Runge's theorem (Theorem 2.9), $F|_K$ lies in the uniform closure of $\mathcal{L}$ on $K$.

We claim that $\mathcal{L} \subset P(K)$. For let $\mu$ be a measure on $K$, $\mu \perp P(K)$. Then for $|a|$ large,

$$\int \frac{d\mu(z)}{z-a} = -\int \left( \sum_{0}^{\infty} \frac{z^n}{a^{n+1}} \right) d\mu = 0.$$

But the integral on the left is analytic as a function of $a$ in $\mathbb{C}\setminus K$ and, since $\mathbb{C}\setminus K$ is connected, vanishes for all $a$ in $\mathbb{C}\setminus K$. By differentiation,

$$\int \frac{d\mu(z)}{(z-a)^p} = 0, \quad p = 1, 2, \ldots, \quad a \in \mathbb{C}\setminus K.$$

Thus $\mu \perp \mathcal{L}$, so $\mathcal{L} \subset P(K)$, as claimed.

Since $F|_K$ is in the uniform closure of $\mathcal{L}$ and $\mathcal{L} \subset P(K)$, we conclude $F|_K \in P(K)$.
