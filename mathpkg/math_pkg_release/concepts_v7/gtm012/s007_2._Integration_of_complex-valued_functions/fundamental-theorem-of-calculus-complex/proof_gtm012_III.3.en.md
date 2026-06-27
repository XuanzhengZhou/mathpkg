---
role: proof
locale: en
of_concept: fundamental-theorem-of-calculus-complex
source_book: gtm012
source_chapter: "3"
source_section: "3. Differentiation of complex-valued functions"
---

# Proof of the Fundamental Theorem of Calculus for complex-valued functions

**Theorem 3.6 (Fundamental Theorem of Calculus).** Suppose \(f: [a, b] \to \mathbb{C}\) is continuous and suppose \(c \in [a, b]\). Define the function \(F: [a, b] \to \mathbb{C}\) by

\[
F(x) = \int_c^x f(t)\,dt, \qquad x \in [a, b].
\]

Then \(F\) is differentiable at each point of \((a, b)\) and

\[
F'(x) = f(x), \qquad x \in (a, b).
\]

*Proof.* Fix \(x \in (a, b)\). For \(y \in [a, b]\) with \(y \neq x\),

\[
F(y) - F(x) = \int_c^y f(t)\,dt - \int_c^x f(t)\,dt = \int_x^y f(t)\,dt.
\]

(Here, if \(y < x\), the integral \(\int_x^y\) is interpreted as \(-\int_y^x\).) Therefore

\[
\frac{F(y) - F(x)}{y - x} - f(x) = \frac{1}{y - x} \int_x^y f(t)\,dt - f(x)
= \frac{1}{y - x} \int_x^y \bigl[f(t) - f(x)\bigr]\,dt.
\]

Given \(\varepsilon > 0\), by continuity of \(f\) at \(x\) there exists \(\delta > 0\) such that

\[
|f(t) - f(x)| < \varepsilon \quad \text{whenever } |t - x| < \delta, \; t \in [a, b].
\]

Take any \(y\) with \(0 < |y - x| < \delta\). For all \(t\) between \(x\) and \(y\), we have \(|t - x| < \delta\), so

\[
\bigl|f(t) - f(x)\bigr| < \varepsilon.
\]

Then

\[
\left| \frac{1}{y - x} \int_x^y \bigl[f(t) - f(x)\bigr]\,dt \right|
\leq \frac{1}{|y - x|} \int_{\min(x,y)}^{\max(x,y)} \bigl|f(t) - f(x)\bigr|\,dt
< \frac{1}{|y - x|} \cdot \varepsilon \cdot |y - x| = \varepsilon.
\]

Thus

\[
\left| \frac{F(y) - F(x)}{y - x} - f(x) \right| < \varepsilon \quad \text{whenever } 0 < |y - x| < \delta,
\]

which proves that \(\displaystyle \lim_{y \to x} \frac{F(y) - F(x)}{y - x} = f(x)\). Hence \(F\) is differentiable at \(x\) with \(F'(x) = f(x)\). \(\square\)
