---
role: proof
locale: en
of_concept: inverse-function-theorem-real
source_book: gtm012
source_chapter: "3"
source_section: "3. Differentiation of complex-valued functions"
---

# Proof of the Inverse Function Theorem for real functions

**Theorem 3.7 (Inverse Function Theorem).** Suppose \(f: [a, b] \to \mathbb{R}\) is continuous, strictly increasing, and differentiable on \((a, b)\) with \(f'(x) \neq 0\) for all \(x \in (a, b)\). Then the inverse function \(g = f^{-1}: [f(a), f(b)] \to [a, b]\) is differentiable at each point of \((f(a), f(b))\) and

\[
g'(y) = \frac{1}{f'(g(y))}, \qquad y \in (f(a), f(b)).
\]

*Proof.* **Step 1: Monotonicity.** For any \(x, y \in [a, b]\) with \(x < y\), apply the Mean Value Theorem (Theorem 3.4) to \(f\) on \([x, y]\). Since \(f\) is real-valued and differentiable on \((x, y)\), there exists \(\xi \in (x, y)\) such that

\[
f(y) - f(x) = f'(\xi)(y - x).
\]

Because \(f\) is strictly increasing, \(f'(\xi) > 0\) (or at least the difference is positive), so \(f(x) < f(y)\). In particular, \(f(a) < f(b)\).

**Step 2: Existence of the inverse.** Since \(f\) is continuous and strictly increasing, by the Intermediate Value Theorem, for each \(y \in [f(a), f(b)]\) there exists a unique \(x \in [a, b]\) with \(f(x) = y\). This defines the inverse function \(g: [f(a), f(b)] \to [a, b]\), where \(g(y) = x\) if and only if \(f(x) = y\).

**Step 3: Continuity of the inverse.** We show \(g\) is continuous. Fix \(y \in (f(a), f(b))\) and let \(\varepsilon > 0\). Choose \(y', y''\) such that

\[
f(a) \leq y' < y < y'' \leq f(b), \qquad y'' - y \leq \varepsilon, \quad y - y' \leq \varepsilon.
\]

Let \(x' = g(y'), x = g(y), x'' = g(y'')\). Then \(x' < x < x''\). Set \(\delta = \min\{x'' - x,\, x - x'\} > 0\). If \(|w - x| < \delta\), then \(w \in (x', x'')\), and by monotonicity, \(f(w) \in (y', y'')\). Hence

\[
|f(w) - f(x)| = |f(w) - y| < \varepsilon,
\]

proving continuity of \(g\) at interior points. Continuity at the endpoints \(f(a)\) and \(f(b)\) is proved similarly.

**Step 4: Differentiability of the inverse.** Let \(y, y' \in (f(a), f(b))\) with \(y' \neq y\). Set \(x = g(y)\) and \(x' = g(y')\). Then

\[
\frac{g(y') - g(y)}{y' - y} = \frac{x' - x}{f(x') - f(x)}.
\]

By continuity of \(g\), as \(y' \to y\) we have \(x' = g(y') \to g(y) = x\). Since \(f\) is differentiable at \(x\) and \(f'(x) \neq 0\),

\[
\lim_{y' \to y} \frac{g(y') - g(y)}{y' - y}
= \lim_{x' \to x} \frac{x' - x}{f(x') - f(x)}
= \frac{1}{\displaystyle \lim_{x' \to x} \frac{f(x') - f(x)}{x' - x}}
= \frac{1}{f'(x)} = \frac{1}{f'(g(y))}.
\]

Thus \(g\) is differentiable at \(y\) and \(g'(y) = 1 / f'(g(y))\). \(\square\)
