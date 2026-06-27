---
role: proof
locale: en
of_concept: "let-with-this-definition-of-norm-an-inner"
source_book: gtm025
source_chapter: "Integration on Locally Compact Spaces"
source_section: "16.3"
---

All of the verifications that $\| \|$ is a norm on $H$ are trivial except for the triangle inequality. Evidently

$$\|x + y\|^2 = \langle x + y, x + y \rangle = \langle x, x \rangle + \langle x, y \rangle + \langle y, x \rangle + \langle y, y \rangle$$

$$= \|x\|^2 + 2 \operatorname{Re} \langle x, y \rangle + \|y\|^2.$$

Applying (16.2), we have

$$2 \operatorname{Re} \langle x, y \rangle \leq 2 |\langle x, y \rangle| \leq 2 \|x\| \cdot \|y\|.$$

Therefore $\|x + y\|^2 \leq (\|x\| + \|y\|)^2$, and so $\|x + y\| \leq \|x\| + \|y\|.$

(16.4) Exercise. Find a necessary and sufficient condition that $\|x + y\| = \|x\| + \|y\|$.

(16.5) Exercise: The polar identity. Prove that if $H$ is a complex inner product space, then

$$4 \langle x, y \rangle = \|x + y\|^2 - \|x - y\|^2 + i \|x + iy\|^2 - i \|x - iy\|^2$$

for all $x, y \in H$.

(16.6) Exercise. Let

is an incomplete inner product space. To see this, approximate $\xi_{[0,1]}$ by the sequence $(g_n)_{n=1}^{\infty}$ of continuous functions defined as follows: $g_n(x) = 0$ for $-\infty < x \leq -\frac{1}{n}$ and for $1 + \frac{1}{n} \leq x < \infty$; $g_n(x) = 1$ for $0 \leq x \leq 1$; and $g_n$ is linear on $\left[-\frac{1}{n}, 0\right]$ and $\left[1, 1 + \frac{1}{n}\right]$. The sequence $(g_n)$ converges to $\xi_{[0,1]}$ in $\mathfrak{L}_2$, and so is a Cauchy sequence. However, it is clear that $(g_n)$ converges to no function in $\mathfrak{C}_{00}(R)$.

(c) The sequence space $l_2(N)$, consisting of all complex sequences $x = (x_n)$ such that $\sum_{n=1}^{\infty}|x_n|^2 < \infty$, is a Hilbert space in which $\langle(x_n), (y_n)\rangle = \sum_{n=1}^{\infty}x_n\bar{y}_n$. [As we have observed before (13.13), $l_2(N)$ is actually the space $\mathfrak{L}_2(X, \mathcal{A}, \mu)$ in which $X$ is the set $N$, $\mathcal{A}$ is all subsets of $X$, and $\mu$ is counting measure.]

(d) The space consisting of all sequences $x = (x_n)$ such that $x_n$ is ultimately zero is an incomplete inner product space [the inner product is that induced by $l_2$]. For example, the sequence $(x^{(m)})_{m=1}^{\infty}$ in which $x^{(m)} = \left(1, \frac{1}{2}, \ldots, \frac{1}{m}, 0, 0, \ldots\right)$ converges in $l_2$, but its limit has no zero terms. The reader should note the analogy between this space and $\mathfrak{C}_{00}(
