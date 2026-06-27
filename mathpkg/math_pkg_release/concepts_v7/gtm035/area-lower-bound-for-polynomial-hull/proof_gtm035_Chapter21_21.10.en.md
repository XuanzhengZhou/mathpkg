---
role: proof
locale: en
of_concept: area-lower-bound-for-polynomial-hull
source_book: gtm035
source_chapter: "Chapter 21"
source_section: "21.10"
---
# Proof of Corollary 21.10 (Area Lower Bound for Polynomial Hulls)

**Corollary 21.10.** Let $X$ be a compact subset of $\mathbb{C}^n$. Suppose that $p \in \widehat{X}$ and that $B(p, r) \subseteq \mathbb{C}^n \setminus X$. Then

$$H^2(\widehat{X} \cap B(p, r)) \geq \pi r^2,$$

where $H^2$ denotes two-dimensional Hausdorff measure.

**Proof.** If $H^2(\widehat{X} \cap B(p, r)) < \infty$, then Theorem 21.9 implies that $\widehat{X} \cap B(p, r)$ is a one-dimensional analytic set, and Rutishauser's theorem on the area of analytic varieties intersecting a ball applies, giving the desired lower bound. (Rutishauser's theorem states that for a one-dimensional analytic subvariety $V$ of an open set containing $\overline{B(p, r)}$, one has $\operatorname{area}(V \cap B(p, r)) \geq \pi r^2$.)

If $H^2(\widehat{X} \cap B(p, r)) = \infty$, the conclusion is obvious. ∎

**Context.** This corollary relies on Theorem 21.9, which states that if $p \in \widehat{X} \setminus X$ and for some neighborhood $N$ of $p$ in $\mathbb{C}^n$, $H^2(\widehat{X} \cap N) < \infty$, then $\widehat{X} \cap N$ is a one-dimensional analytic subvariety of $N$. This yields a generalization of Rutishauser's result from analytic varieties to polynomial hulls.
