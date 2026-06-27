---
role: proof
locale: en
of_concept: zero-functional-only-for-lebesgue-measurable
source_book: gtm036
source_chapter: "L"
source_section: "L(c)"
---

First, the convex extension of $U_n$ being all of $S(X, \mu)$ means that every $f \in S(X, \mu)$ can be written as a convex combination of finitely many elements of $U_n$. This implies that any continuous linear functional vanishing on $U_n$ must vanish identically.

For the main result, suppose $f$ is a non-negative linear functional not identically zero. Consider the constant function $1$. Define inductively an increasing sequence $\{x_k(t)\}$ and a decreasing sequence of intervals $\{I_k\}$:
- Start with $x_0(t) = 0$ and $I_0 = [0,1]$.
- Given $I_k$, split it into two halves; $I_{k+1}$ is one half.
- Define $x_{k+1}(t) = x_k(t)$ outside $I_k$, and $x_{k+1}(t) = 4x_k(t)$ on $I_k$.
- Let $\chi_k$ be the characteristic function of $I_k$.

Then $f(x_k \chi_k) \geq 2^{k-1}$ by construction. As $k \to \infty$, $x_k$ converges to some limit function $x$, and $x \chi_k \geq x_k \chi_k$ (since $x_{j+1} \geq x_j$). Hence $f(x) \geq f(x \chi_k) \geq f(x_k \chi_k) \geq 2^{k-1}$ for all $k$, contradicting that $f(x)$ is a finite real number. Therefore the only non-negative linear functional is identically zero.

Since any continuous linear functional can be decomposed into positive and negative parts (via the Jordan decomposition), the only continuous linear functional is identically zero.
