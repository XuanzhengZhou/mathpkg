---
role: proof
locale: en
of_concept: inner-product-induced-norm
source_book: gtm015
source_chapter: "41"
source_section: "Hilbert spaces"
---

# Proof of Inner product induces a norm satisfying the parallelogram law

Let $E$ be an inner product space.  Define $\|x\| = (x, x)^{1/2}$ (real case) or $\|x\| = (x|x)^{1/2}$ (complex case).  We treat the complex case; the real case is analogous.

**(i) Parallelogram law.**  Expanding the squares,

$$
\begin{aligned}
\|x + y\|^2 + \|x - y\|^2 &= (x+y \mid x+y) + (x-y \mid x-y) \\
&= \bigl[(x|x) + (x|y) + (y|x) + (y|y)\bigr] \\
&\quad + \bigl[(x|x) - (x|y) - (y|x) + (y|y)\bigr] \\[4pt]
&= 2(x|x) + 2(y|y) = 2\|x\|^2 + 2\|y\|^2.
\end{aligned}
$$

Thus the norm satisfies the parallelogram law (P).

**(ii) Triangle inequality.**  Using the Cauchy–Schwarz inequality $|(x|y)| \leq \|x\|\,\|y\|$ (Theorem 41.7),

$$
\begin{aligned}
\|x + y\|^2 &= (x+y \mid x+y) = (x|x) + (x|y) + (y|x) + (y|y) \\
&= \|x\|^2 + \|y\|^2 + 2\,\mathrm{Re}\,(x|y) \\
&\leq \|x\|^2 + \|y\|^2 + 2|(x|y)| \\
&\leq \|x\|^2 + \|y\|^2 + 2\|x\|\,\|y\| \\
&= (\|x\| + \|y\|)^2,
\end{aligned}
$$

and taking square roots (nonnegative) yields $\|x + y\| \leq \|x\| + \|y\|$.

**(iii) Absolute homogeneity.**  For $\lambda \in \mathbb{C}$,

$$\|\lambda x\|^2 = (\lambda x \mid \lambda x) = \lambda\lambda^* (x|x) = |\lambda|^2\,\|x\|^2,$$

so $\|\lambda x\| = |\lambda|\,\|x\|$.

**(iv) Positive definiteness.**  $\|x\| = (x|x)^{1/2} \geq 0$ by definition of the inner product.  Moreover, $\|x\| = 0$ iff $(x|x) = 0$ iff $x = \theta$, by the strict positivity axiom of inner products.

Thus $\|\cdot\|$ is a norm on $E$ satisfying the parallelogram law; i.e., $E$ is a pre-Hilbert space.  $\square$
