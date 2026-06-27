---
role: proof
locale: en
of_concept: lavrentieff-polynomial-approximation-theorem
source_book: gtm035
source_chapter: "Chapter 2"
source_section: "2.11"
---

# Proof of Lavrentieff Polynomial Approximation Theorem

**Theorem 2.11 (Lavrentieff).** Let $X$ be a compact set in $\mathbb{C}$. If

(8) The interior of $X$ is empty,

(9) $\mathbb{C} \setminus X$ is connected,

then $P(X) = C(X)$, i.e., every continuous function on $X$ can be uniformly approximated by polynomials.

*Proof.* We first show that $\operatorname{Re} P(X)$ is dense in $C_{\mathbb{R}}(X)$.

Let $\alpha$ be a real measure on $X$ with $\alpha \perp \operatorname{Re}(P(X))$. Then

$$\int \operatorname{Re} \zeta^n \, d\alpha(\zeta) = 0, \quad n \geq 0$$

and

$$\int \operatorname{Im} \zeta^n \, d\alpha = \int \operatorname{Re}(-i\zeta^n) \, d\alpha = 0, \quad n \geq 0,$$

so that

$$\int \zeta^n \, d\alpha = 0, \quad n \geq 0.$$

For $|z|$ large,

$$\log\left(1 - \frac{\zeta}{z}\right) = \sum_{0}^{\infty} c_n(z)\zeta^n,$$

the series converging uniformly for $\zeta \in X$. Hence

$$\int \log\left(1 - \frac{\zeta}{z}\right) d\alpha(\zeta) = \sum_{0}^{\infty} c_n(z) \int \zeta^n \, d\alpha(\zeta) = 0,$$

whence

$$\int \operatorname{Re}\left(\log\left(1 - \frac{\zeta}{z}\right)\right) d\alpha(\zeta) = 0$$

or

$$\int \log|z - \zeta| \, d\alpha(\zeta) - \int \log|z| \, d\alpha(\zeta) = 0,$$

whence

$$\int \log|z - \zeta| \, d\alpha(\zeta) = 0,$$

since $\alpha \perp 1$. The function

$$z \mapsto \int \log|z - \zeta| \, d\alpha(\zeta)$$

is harmonic in $\mathbb{C} \setminus X$, and it vanishes for large $|z|$. By harmonic continuation it vanishes for all $z$ in $\mathbb{C} \setminus X$.

Let $E$ be a component of $\mathbb{C} \setminus X$ and let $z_0 \in \partial E$. Suppose

$$(10) \qquad \int_E \left|\log\left|\frac{1}{z_0 - \zeta}\right|\right| d|\alpha|(\zeta) < \infty.$$

By Lemma 2.12 (Logarithmic Potential Boundary Limit), we then have $\alpha^*(z_0) = 0$.

If (10) fails at $z_0$, one can argue that $\alpha = 0$ in a neighborhood of $z_0$; otherwise the integral would be finite. In any case, $\alpha^*(z_0) = 0$ for all $z_0 \in X$.

By Lemma 2.4, the vanishing of the logarithmic potential a.e. implies that $\alpha^* = 0$ almost everywhere with respect to $dx\,dy$.

By Lemma 2.7, $\alpha = 0$. Hence $\operatorname{Re} P(X)$ is dense in $C_{\mathbb{R}}(X)$.

Now choose $\mu \in P(X)^\perp$. Fix $z_0 \in X$ with

$$(15) \qquad \int \left|\frac{1}{z - z_0}\right| d|\mu|(z) < \infty.$$

Because $\operatorname{Re} P(X)$ is dense in $C_{\mathbb{R}}(X)$, we can find for each positive integer $k$ a polynomial $P_k$ such that

$$(16) \qquad |\operatorname{Re} P_k(z) - |z - z_0|| \leq \frac{1}{k}, \quad z \in X$$

and

$$(17) \qquad P_k(z_0) = 0.$$

Define

$$f_k(z) = \frac{e^{-kP_k(z)} - 1}{z - z_0}.$$

This is an entire function, hence its restriction to $X$ lies in $P(X)$. Therefore

$$(18) \qquad \int f_k \, d\mu = 0.$$

From (16) we obtain

$$\operatorname{Re} kP_k(z) - k|z - z_0| \geq -1,$$

whence

$$|e^{-kP_k(z)}| \leq e^{-k|z - z_0| + 1}, \quad z \in X.$$

It follows that $f_k(z) \to -\frac{1}{z - z_0}$ for all $z \in X \setminus \{z_0\}$ as $k \to \infty$, and also

$$|f_k(z)| \leq \frac{4}{|z - z_0|}, \quad z \in X.$$

Since by (15) the function $1/|z - z_0|$ is summable with respect to $|\mu|$, dominated convergence gives

$$\int \frac{d\mu(z)}{z - z_0} = 0.$$

Condition (15) holds for almost every $z_0 \in X$ by Lemma 2.4. Since certainly

$$\int \frac{d\mu(z)}{z - z_0} = 0 \quad \text{for } z_0 \in \mathbb{C} \setminus X,$$

we conclude that $\hat{\mu} = 0$ almost everywhere, so $\mu = 0$ by Lemma 2.7.

Thus $\mu \perp P(X) \Rightarrow \mu = 0$, and therefore $P(X) = C(X)$. $\square$
