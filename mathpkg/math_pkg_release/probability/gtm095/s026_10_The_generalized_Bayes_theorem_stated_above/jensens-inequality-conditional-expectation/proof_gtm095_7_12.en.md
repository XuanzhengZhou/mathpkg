---
role: proof
locale: en
of_concept: jensens-inequality-conditional-expectation
source_book: gtm095
source_chapter: "7"
source_section: "12"
---

# Proof of Jensen's Inequality for Conditional Expectations

*Proof.* Let $g: \mathbb{R} \to \mathbb{R}$ be a convex Borel function and let $\xi$ be a random variable with $\mathsf{E}|g(\xi)| < \infty$. We must show

$$g(\mathsf{E}(\xi \mid \mathcal{G})) \leq \mathsf{E}(g(\xi) \mid \mathcal{G}) \quad (\mathsf{P}\text{-a.s.}).$$

A fundamental property of convex functions is that they can be represented as the supremum of a countable family of affine functions: there exist sequences $(a_n)_{n \in \mathbb{N}} \subset \mathbb{R}$ and $(b_n)_{n \in \mathbb{N}} \subset \mathbb{R}$ such that

$$g(x) = \sup_{n \in \mathbb{N}} \big( a_n x + b_n \big) \quad \text{for all } x \in \mathbb{R}.$$

(This follows from the supporting hyperplane theorem: at each rational point $q \in \mathbb{Q}$, pick a subgradient $g'(q)$ and set $L_q(x) = g(q) + g'(q)(x - q)$; the supremum over all such $q$ equals $g(x)$ by convexity.)

Now for each fixed $n$, by linearity and monotonicity of conditional expectation,

$$\mathsf{E}(g(\xi) \mid \mathcal{G}) = \mathsf{E}\!\left( \sup_{n} (a_n \xi + b_n) \mid \mathcal{G} \right) \geq \mathsf{E}(a_n \xi + b_n \mid \mathcal{G}) = a_n \mathsf{E}(\xi \mid \mathcal{G}) + b_n \quad (\mathsf{P}\text{-a.s.}).$$

Since this inequality holds for every $n$ and the right-hand side is a countable supremum taken outside the conditional expectation, we have (modulo a $\mathsf{P}$-null set depending on $n$, which being a countable union is still $\mathsf{P}$-null):

$$\mathsf{E}(g(\xi) \mid \mathcal{G}) \geq \sup_{n \in \mathbb{N}} \big( a_n \mathsf{E}(\xi \mid \mathcal{G}) + b_n \big) = g(\mathsf{E}(\xi \mid \mathcal{G})) \quad (\mathsf{P}\text{-a.s.}).$$

The last equality uses the affine supremum representation of $g$ evaluated at $x = \mathsf{E}(\xi \mid \mathcal{G})$. This completes the proof.

$\square$

**Remark.** The integrability condition $\mathsf{E}|g(\xi)| < \infty$ guarantees that $\mathsf{E}(g(\xi) \mid \mathcal{G})$ is well-defined. The inequality is strict (with positive probability) unless $g$ is affine on the convex hull of the support of the conditional distribution of $\xi$ given $\mathcal{G}$, or $\xi$ is $\mathcal{G}$-measurable.
