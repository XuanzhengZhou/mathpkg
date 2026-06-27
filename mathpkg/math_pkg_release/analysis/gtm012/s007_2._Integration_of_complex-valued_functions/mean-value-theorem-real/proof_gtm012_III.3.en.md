---
role: proof
locale: en
of_concept: mean-value-theorem-real
source_book: gtm012
source_chapter: "3"
source_section: "3. Differentiation of complex-valued functions"
---

# Proof of the Mean Value Theorem

**Theorem 3.4 (Mean Value Theorem).** Suppose \(f: [a, b] \to \mathbb{R}\) is continuous on \([a, b]\) and differentiable at each point of \((a, b)\). Then there exists \(c \in (a, b)\) such that

\[
f'(c) = \frac{f(b) - f(a)}{b - a}.
\]

*Proof.* Define the auxiliary function

\[
g(x) = f(x) - f(a) - \frac{f(b) - f(a)}{b - a}\,(x - a), \qquad x \in [a, b].
\]

Then \(g\) is continuous on \([a, b]\) and differentiable on \((a, b)\), with

\[
g'(x) = f'(x) - \frac{f(b) - f(a)}{b - a}.
\]

Moreover, \(g(a) = 0\) and \(g(b) = f(b) - f(a) - [f(b) - f(a)] = 0\), so \(g(a) = g(b)\).

Since \(g\) is continuous on the compact interval \([a, b]\), it attains a maximum and a minimum. Let \(c_+\) be a point where \(g\) attains its maximum and let \(c_-\) be a point where \(g\) attains its minimum.

If both the maximum and minimum occur at the endpoints, then \(g(a) = g(b)\) is both the maximum and minimum value, so \(g\) is constant on \([a, b]\). In that case \(g'(x) = 0\) for all \(x \in (a, b)\), and we can choose any \(c \in (a, b)\); then \(f'(c) = \frac{f(b)-f(a)}{b-a}\) follows from \(g'(c) = 0\).

Otherwise, one of the extrema occurs at an interior point. Suppose the maximum occurs at \(c_+ \in (a, b)\). Then for \(y < c_+\),

\[
\frac{g(y) - g(c_+)}{y - c_+} \geq 0 \quad (\text{since } g(y) \leq g(c_+) \text{ and denominator is negative}),
\]

and for \(y > c_+\),

\[
\frac{g(y) - g(c_+)}{y - c_+} \leq 0 \quad (\text{since } g(y) \leq g(c_+) \text{ and denominator is positive}).
\]

Taking the limit as \(y \to c_+\) from each side, we obtain

\[
\lim_{y \to c_+^-} \frac{g(y) - g(c_+)}{y - c_+} \geq 0, \qquad
\lim_{y \to c_+^+} \frac{g(y) - g(c_+)}{y - c_+} \leq 0.
\]

Since \(g\) is differentiable at \(c_+\), these one-sided limits must equal \(g'(c_+)\). Hence \(g'(c_+) \geq 0\) and \(g'(c_+) \leq 0\), forcing \(g'(c_+) = 0\).

The same argument at a minimum \(c_- \in (a, b)\) shows \(g'(c_-) = 0\). Thus in either case there exists \(c \in (a, b)\) with \(g'(c) = 0\), which means

\[
f'(c) = \frac{f(b) - f(a)}{b - a}.
\]

\(\square\)
