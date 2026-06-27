---
role: proof
locale: en
of_concept: linearity-of-complex-integral
source_book: gtm012
source_chapter: "2"
source_section: "2. Integration of complex-valued functions"
---

# Proof of Linearity of the integral for complex-valued functions

**Proposition 2.2.** Suppose \(f: [a, b] \to \mathbb{C}\) and \(g: [a, b] \to \mathbb{C}\) are bounded integrable functions, and suppose \(c \in \mathbb{C}\). Then \(f + g\) and \(cf\) are integrable, and

\[
\int_a^b (f + g) = \int_a^b f + \int_a^b g, \qquad
\int_a^b cf = c \int_a^b f.
\]

*Proof.* For any partition \(P\) of \([a, b]\), the Riemann sum is additive and homogeneous:

\[
S(f + g; P) = \sum_{i=1}^n (f + g)(x_i)(x_i - x_{i-1})
= \sum_{i=1}^n f(x_i)(x_i - x_{i-1}) + \sum_{i=1}^n g(x_i)(x_i - x_{i-1})
= S(f; P) + S(g; P),
\]

\[
S(cf; P) = \sum_{i=1}^n cf(x_i)(x_i - x_{i-1})
= c \sum_{i=1}^n f(x_i)(x_i - x_{i-1})
= c \, S(f; P).
\]

Since \(f\) and \(g\) are integrable, we have

\[
\lim_{|P| \to 0} S(f; P) = \int_a^b f, \qquad
\lim_{|P| \to 0} S(g; P) = \int_a^b g.
\]

By the algebraic limit theorem for sequences (or limits of functions of partitions), it follows that

\[
\lim_{|P| \to 0} S(f + g; P) = \lim_{|P| \to 0} \bigl(S(f; P) + S(g; P)\bigr)
= \int_a^b f + \int_a^b g,
\]

\[
\lim_{|P| \to 0} S(cf; P) = \lim_{|P| \to 0} c\,S(f; P)
= c \int_a^b f.
\]

Hence \(f + g\) and \(cf\) are integrable and the integral formulas hold. \(\square\)
