---
role: proof
locale: en
of_concept: fiber-cardinality-bound-for-uniform-algebra
source_book: gtm035
source_chapter: "12"
source_section: "12.2"
---
# Proof of Lemma 12.2 (Fiber Cardinality Bound for Uniform Algebra)

Let $(A, X, \mathcal{M})$ be a uniform algebra. Fix $p \in \mathcal{M} \setminus X$, $f \in A$, and put $\lambda_0 = f(p)$. Define $K \subseteq \mathbb{C}$ by

$$K = \{ \lambda : |\lambda - \lambda_0| \leq r,\; \alpha \leq \arg(\lambda - \lambda_0) \leq \beta \},$$

where $-\pi/2 < \alpha < \beta < 3\pi/2$. Assume that for some compact neighborhood $\mathcal{N}$ of $p$ in $\mathcal{M} \setminus X$ we have $f(\mathcal{N}) \subseteq K$.

**Claim.** The point $p$ is not a peak-point of the algebra $\overline{A|_{f^{-1}(\lambda_0)}}$ on the space $f^{-1}(\lambda_0)$.

*Proof of Lemma.* By the Local Maximum Modulus Principle,

$$|g(p)| \leq \max_{\partial \mathcal{N}} |g|, \quad g \in A.$$

Hence there exists a representing measure $\mu$ for $p$ on $\partial \mathcal{N}$; that is,

$$g(p) = \int_{\partial \mathcal{N}} g \, d\mu, \quad g \in A.$$

Choose a function $\phi$ continuous on $K$, analytic on $\operatorname{int} K$, such that $\phi(\lambda_0) = 1$ and $|\phi(\lambda)| < 1$ for $\lambda \in K \setminus \{\lambda_0\}$. Such a $\phi$ exists because $K$ is a sector of a disk; for example one may take $\phi(\lambda) = \exp(c(\lambda - \lambda_0)^\nu)$ for suitable $c, \nu$. Moreover, $\phi$ is a uniform limit on $K$ of polynomials in $\lambda$.

For $n = 1, 2, \ldots$, define measures $\mu_n$ on $\partial \mathcal{N}$ by

$$d\mu_n = (\phi \circ f)^n \, d\mu.$$

Fix $q \in \partial \mathcal{N} \setminus f^{-1}(\lambda_0)$. Then $f(q) \in K \setminus \{\lambda_0\}$, so $|\phi(f(q))| < 1$, and hence $(\phi \circ f)^n(q) \to 0$ as $n \to \infty$. Consequently, any weak-$*$ limit point $\nu$ of the sequence $\{\mu_n\}$ is supported on $f^{-1}(\lambda_0) \cap \partial \mathcal{N}$.

Now, for any $g \in A$, the functional calculus applied to $\phi \circ f$ gives

$$\int_{\partial \mathcal{N}} g (\phi \circ f)^n \, d\mu \in A,$$

and evaluating at $p$ yields

$$g(p) \cdot \phi(f(p))^n = g(p) \cdot 1^n = \int_{\partial \mathcal{N}} g (\phi \circ f)^n \, d\mu.$$

Thus $p$ is represented by $\mu_n$ for each $n$. Passing to a weak-$*$ limit $\nu$ gives $g(p) = \int_{f^{-1}(\lambda_0)} g \, d\nu$ for all $g \in A$. Since $\nu$ is a probability measure on $f^{-1}(\lambda_0)$ representing $p$, the point $p$ cannot be a peak-point of $\overline{A|_{f^{-1}(\lambda_0)}}$. Moreover, the fiber $f^{-1}(\lambda_0)$ must contain the support of $\nu$, which imposes a cardinality bound on the fiber when combined with the finite-sheeted structure obtained from the analytic cover arguments. $\square$
