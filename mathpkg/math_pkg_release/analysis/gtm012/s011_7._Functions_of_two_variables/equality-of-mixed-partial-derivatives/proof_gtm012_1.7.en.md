---
role: proof
locale: en
of_concept: equality-of-mixed-partial-derivatives
source_book: gtm012
source_chapter: "1"
source_section: "7. Functions of two variables"
---

# Proof of Theorem 7.1: Equality of Mixed Partial Derivatives

**Theorem 7.1.** If $f: A \to \mathbb{C}$ is of class $C^2$, then $D_1 D_2 f = D_2 D_1 f$.

**Proof.** Suppose $(a, b) \in A$. Choose $r > 0$ so small that $A$ contains the closed square with center $(a, b)$, edges parallel to the coordinate axes, and sides of length $2r$. Thus $(x, y) \in A$ if

$$|x - a| \leq r \quad \text{and} \quad |y - b| \leq r.$$

In this square we apply the fundamental theorem of calculus to $f$ as a function of $x$ with $y$ fixed, and conclude

$$f(x, y) = \int_a^x D_1 f(s, y) \, ds + f(a, y).$$

Let $g(y) = f(a, y)$. We claim that

$$D_2 f(x, y) = \int_a^x D_2 D_1 f(s, y) \, ds + g'(y). \tag{7.1}$$

If (7.1) holds, then differentiation with respect to $x$ shows

$$D_1 D_2 f(x, y) = D_2 D_1 f(x, y).$$

To complete the proof we must establish (7.1). We differentiate the expression

$$f(x, y) = \int_a^x D_1 f(s, y) \, ds + f(a, y)$$

with respect to $y$. Since $f$ is of class $C^2$, the partial derivative $D_2 D_1 f$ is continuous. By the remarks on differentiation under the integral sign, we may differentiate under the integral:

$$D_2 f(x, y) = \int_a^x D_2 D_1 f(s, y) \, ds + D_2 f(a, y).$$

Since $g'(y) = D_2 f(a, y)$, this proves (7.1) when $f$ is real-valued. In the general case of a complex-valued $f$, we apply the argument to the real and imaginary parts of $f$ separately. $\square$
