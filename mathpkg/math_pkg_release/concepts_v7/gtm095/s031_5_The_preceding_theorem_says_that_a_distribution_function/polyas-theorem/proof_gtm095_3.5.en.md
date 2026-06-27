---
role: proof
locale: en
of_concept: polyas-theorem
source_book: gtm095
source_chapter: "Chapter 3"
source_section: "§5. Inversion formula, moments and semi-invariants"
---

# Proof of Pólya's Theorem

**Pólya's Theorem.** Let a continuous even function $\varphi(t) \geq 0$, $\varphi(0) = 1$, $\varphi(t) \to 0$ as $t \to \infty$, and let $\varphi(t)$ be convex on $(-\infty, 0)$ (hence also on $(0, \infty)$). Then $\varphi(t)$ is a characteristic function.

*The proof is not included in the source text. The reader is referred to [31], XV.2.*

This theorem provides a convenient method for constructing characteristic functions. Examples include:

- $\varphi_1(t) = e^{-|t|}$ (Laplace/Two-sided exponential distribution)
- $\varphi_2(t) = \begin{cases} 1 - |t|, & |t| \leq 1, \\ 0, & |t| > 1 \end{cases}$ (Triangular distribution)

The theorem also shows that two characteristic functions can coincide on a finite interval without the corresponding distribution functions being identical (see Fig. 34 in the text).
