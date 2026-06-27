---
role: proof
locale: en
of_concept: corollary-4-3
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. If $f'(x) = 0$ for all $x$ then $(\text{Re } f)'(x) = (\text{Im } f)'(x) = 0$ for all $x$. It follows that $\text{Re } f$ and $\text{Im } f$ are constant and, hence, so is $f$.

One important theorem about the derivative of a real valued function which is not true for complex valued functions is the Mean Value Theorem. In fact, if $f(x) = x^2 + ix^3$ it is easy to show that

$$f(b) - f(a) = f'(c)(b - a)$$

for some point $c$ in $[a, b]$ only when $a = b$.

One of the principal applications of the Mean Value Theorem for derivatives is the proof of the Chain Rule. In light of the discussion in the preceding paragraph one might well doubt the validity of the Chain Rule for complex valued functions. The Chain Rule tells us how to calculate the derivative of the composition of two differentiable functions; this leads to two different situations. First suppose that $f:[a, b] \to \mathbb{C}$ is differentiable and let $g:[c, d] \to [a, b]$ also be differentiable. Then $f(g(t)) = \text{Re}f(g(t)) + i\text{Im}f(g(t))$; from here the Chain Rule follows by applying the Chain Rule from Calculus. In the second case the result still holds. Let $G$ be an open subset of $\mathbb{C}$ such that $f([a, b]) \subset G$ and suppose $h: G \to \mathbb{C}$ is analytic. We wish to show that $h \circ f$ is differentiable and calculate $(h \circ f)'$. Since the proof of this Chain Rule follows the line of argument used to prove the Chain Rule for the composition of two analytic functions (Proposition III.2.4) we will not repeat it here. We summarize this discussion in the following.

A.4 Proposition. Let $f: [a, b] \to \mathbb{C}$ be a differentiable function.

(a) If $g: [c, d] \to [a, b]$ is differentiable then $f

A.6 Fundamental Theorem of Calculus. A continuous function $f: [a, b] \to \mathbb{C}$ has a primitive and any two primitives differ by a constant. If $F$ is any primitive of $f$ then

$$\int_{a}^{b} f(x) \, dx = F(b) - F(a)$$

Proof. If $g$ and $h$ are primitives of $\Re f$ and $\Im f$ then $F = g + ih$ is a primitive of $f$. The result now easily follows.
