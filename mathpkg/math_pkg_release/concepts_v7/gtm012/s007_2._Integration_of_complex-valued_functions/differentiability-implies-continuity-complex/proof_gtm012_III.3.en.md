---
role: proof
locale: en
of_concept: differentiability-implies-continuity-complex
source_book: gtm012
source_chapter: "3"
source_section: "3. Differentiation of complex-valued functions"
---

# Proof of Differentiability implies continuity for complex-valued functions

**Proposition 3.1.** If \(f: (a, b) \to \mathbb{C}\) is differentiable at \(x \in (a, b)\), then \(f\) is continuous at \(x\).

*Proof.* By definition of differentiability at \(x\), there exists a number \(z = f'(x) \in \mathbb{C}\) such that

\[
\lim_{y \to x} \frac{f(y) - f(x)}{y - x} = z,
\]

or equivalently,

\[
\tag{3.2}
\lim_{y \to x} \frac{f(y) - f(x) - z(y - x)}{y - x} = 0.
\]

Choose \(\delta > 0\) so that (3.2) holds with \(\varepsilon = 1\); that is, whenever \(0 < |y - x| < \delta\),

\[
\left| \frac{f(y) - f(x) - z(y - x)}{y - x} \right| < 1,
\]

which implies

\[
|f(y) - f(x) - z(y - x)| < |y - x|.
\]

Then for \(0 < |y - x| < \delta\), the triangle inequality gives

\[
|f(y) - f(x)|
\leq |f(y) - f(x) - z(y - x)| + |z(y - x)|
< |y - x| + |z|\,|y - x|
= (1 + |z|)\,|y - x|.
\]

As \(y \to x\), the right-hand side tends to zero, so \(f(y) \to f(x)\). Hence \(f\) is continuous at \(x\). \(\square\)
