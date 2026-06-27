---
role: proof
locale: en
of_concept: integrability-of-complex-functions
source_book: gtm012
source_chapter: "2"
source_section: "2. Integration of complex-valued functions"
---

# Proof of Integrability of a complex-valued function via its real and imaginary parts

**Proposition 2.1.** A bounded function \(f: [a, b] \to \mathbb{C}\) is integrable if and only if the real and imaginary parts \(\operatorname{Re} f\) and \(\operatorname{Im} f\) are integrable. If so, then

\[
\int_a^b f = \int_a^b \operatorname{Re} f + i \int_a^b \operatorname{Im} f.
\]

*Proof.* Recall that if \(z = x + iy\) with \(x, y \in \mathbb{R}\), then

\[
\tag{2.3}
\frac{1}{2}|x| + \frac{1}{2}|y| \leq |z| \leq |x| + |y|.
\]

If \(P\) is any partition of \([a, b]\), then the Riemann sum splits as

\[
S(f; P) = S(\operatorname{Re} f; P) + i \, S(\operatorname{Im} f; P),
\]

and both \(S(\operatorname{Re} f; P)\) and \(S(\operatorname{Im} f; P)\) are real numbers.

Let \(z = x + iy\) with \(x, y \in \mathbb{R}\), and apply inequality (2.3) to \(S(f; P) - z\). We obtain

\[
\frac{1}{2}\bigl|S(\operatorname{Re} f; P) - x\bigr| + \frac{1}{2}\bigl|S(\operatorname{Im} f; P) - y\bigr|
\leq |S(f; P) - z|
\leq \bigl|S(\operatorname{Re} f; P) - x\bigr| + \bigl|S(\operatorname{Im} f; P) - y\bigr|.
\]

Thus \(S(f; P) \to z\) as \(|P| \to 0\) if and only if

\[
S(\operatorname{Re} f; P) \to x \quad\text{and}\quad S(\operatorname{Im} f; P) \to y \qquad (|P| \to 0).
\]

In other words, \(f\) is integrable with integral \(z\) if and only if \(\operatorname{Re} f\) and \(\operatorname{Im} f\) are (real) Riemann integrable with integrals \(x\) and \(y\) respectively, and in that case

\[
\int_a^b f = z = x + iy = \int_a^b \operatorname{Re} f + i\int_a^b \operatorname{Im} f.
\]

\(\square\)
