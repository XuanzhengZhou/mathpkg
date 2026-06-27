---
role: proof
locale: en
of_concept: differentiability-of-complex-functions
source_book: gtm012
source_chapter: "3"
source_section: "3. Differentiation of complex-valued functions"
---

# Proof of Differentiability of a complex-valued function via its real and imaginary parts

**Proposition 3.2.** The function \(f: (a, b) \to \mathbb{C}\) is differentiable at \(x \in (a, b)\) if and only if the real and imaginary parts \(g = \operatorname{Re} f\) and \(h = \operatorname{Im} f\) are differentiable at \(x\). If so, then

\[
f'(x) = g'(x) + i h'(x).
\]

*Proof.* The derivative of \(f\) at \(x\) is defined by the limit

\[
f'(x) = \lim_{y \to x} \frac{f(y) - f(x)}{y - x}.
\]

Write \(f(y) - f(x) = [g(y) - g(x)] + i[h(y) - h(x)]\) with \(g, h\) real-valued. Then

\[
\frac{f(y) - f(x)}{y - x} = \frac{g(y) - g(x)}{y - x} + i\,\frac{h(y) - h(x)}{y - x}.
\]

A sequence (or limit) in \(\mathbb{C}\) converges if and only if its real and imaginary parts converge, and the limit is the sum of the two limits. Therefore the limit as \(y \to x\) on the left exists if and only if the limits of \(\frac{g(y)-g(x)}{y-x}\) and \(\frac{h(y)-h(x)}{y-x}\) exist as \(y \to x\). Those are precisely \(g'(x)\) and \(h'(x)\). In that case,

\[
f'(x) = g'(x) + i h'(x).
\]

\(\square\)
