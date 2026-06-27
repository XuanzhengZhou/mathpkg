---
role: proof
locale: en
of_concept: differentiation-rules-complex
source_book: gtm012
source_chapter: "3"
source_section: "3. Differentiation of complex-valued functions"
---

# Proof of Differentiation rules for complex-valued functions

**Proposition 3.3.** Suppose \(f: (a, b) \to \mathbb{C}\) and \(g: (a, b) \to \mathbb{C}\) are differentiable at \(x \in (a, b)\), and suppose \(c \in \mathbb{C}\). Then the functions \(f + g\), \(cf\), and \(fg\) are differentiable at \(x\), and

\[
(f + g)'(x) = f'(x) + g'(x), \qquad
(cf)'(x) = c f'(x), \qquad
(fg)'(x) = f'(x)g(x) + f(x)g'(x).
\]

If \(g(x) \neq 0\) then \(f/g\) is differentiable at \(x\) and

\[
(f/g)'(x) = \frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}.
\]

*Proof.* The sum rule and constant multiple rule follow directly from the algebraic properties of limits. For the difference quotient of \(f + g\):

\[
\frac{(f+g)(y) - (f+g)(x)}{y - x}
= \frac{f(y) - f(x)}{y - x} + \frac{g(y) - g(x)}{y - x}
\to f'(x) + g'(x) \quad (y \to x).
\]

For \(cf\):

\[
\frac{(cf)(y) - (cf)(x)}{y - x}
= c\,\frac{f(y) - f(x)}{y - x}
\to c f'(x) \quad (y \to x).
\]

**Product rule.** Write

\[
f(y)g(y) - f(x)g(x) = f(y)g(y) - f(y)g(x) + f(y)g(x) - f(x)g(x)
= f(y)[g(y) - g(x)] + [f(y) - f(x)]g(x).
\]

Dividing by \(y - x\) and using continuity of \(f\) at \(x\) (Proposition 3.1):

\[
\frac{f(y)g(y) - f(x)g(x)}{y - x}
= f(y)\,\frac{g(y) - g(x)}{y - x} + \frac{f(y) - f(x)}{y - x}\,g(x)
\to f(x)g'(x) + f'(x)g(x) \quad (y \to x).
\]

**Quotient rule.** Assume \(g(x) \neq 0\). By continuity, \(g(y) \neq 0\) for \(y\) near \(x\). Then

\[
\frac{(f/g)(y) - (f/g)(x)}{y - x}
= \frac{1}{g(y)g(x)} \cdot \frac{f(y)g(x) - f(x)g(y)}{y - x}.
\]

The numerator can be rewritten:

\[
f(y)g(x) - f(x)g(y) = [f(y) - f(x)]g(x) - f(x)[g(y) - g(x)].
\]

Therefore

\[
\frac{f(y)g(x) - f(x)g(y)}{y - x}
= \frac{f(y) - f(x)}{y - x}\,g(x) - f(x)\,\frac{g(y) - g(x)}{y - x}
\to f'(x)g(x) - f(x)g'(x) \quad (y \to x).
\]

Since \(g(y) \to g(x)\) as \(y \to x\), it follows that

\[
\frac{(f/g)(y) - (f/g)(x)}{y - x}
\to \frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2} \quad (y \to x).
\]

\(\square\)
