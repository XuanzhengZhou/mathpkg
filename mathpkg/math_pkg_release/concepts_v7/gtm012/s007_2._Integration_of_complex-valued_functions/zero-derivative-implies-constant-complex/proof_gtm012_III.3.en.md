---
role: proof
locale: en
of_concept: zero-derivative-implies-constant-complex
source_book: gtm012
source_chapter: "3"
source_section: "3. Differentiation of complex-valued functions"
---

# Proof of Zero derivative implies constant for complex-valued functions

**Corollary 3.5.** Suppose \(f: [a, b] \to \mathbb{C}\) is continuous, and is differentiable at each point of \((a, b)\). If \(f'(x) = 0\) for each \(x \in (a, b)\), then \(f\) is constant.

*Proof.* Let \(g = \operatorname{Re} f\) and \(h = \operatorname{Im} f\) be the real and imaginary parts of \(f\). By Proposition 3.2, \(g\) and \(h\) are differentiable on \((a, b)\) and

\[
g'(x) + i h'(x) = f'(x) = 0 \quad \text{for all } x \in (a, b),
\]

hence \(g'(x) = 0\) and \(h'(x) = 0\) for all \(x \in (a, b)\).

We want to show \(g\) and \(h\) are constant. Take any \(x, y \in [a, b]\) with \(x < y\). Applying the Mean Value Theorem (Theorem 3.4) to \(g\) on \([x, y]\) (note that \(g\) is real-valued, continuous on \([x, y]\), and differentiable on \((x, y)\) with \(g' = 0\)), there exists \(c \in (x, y)\) such that

\[
g(y) - g(x) = g'(c)(y - x) = 0,
\]

so \(g(x) = g(y)\). The same argument applied to \(h\) gives \(h(x) = h(y)\). Since \(x, y\) were arbitrary, \(g\) and \(h\) are constant, and therefore \(f = g + ih\) is constant. \(\square\)
