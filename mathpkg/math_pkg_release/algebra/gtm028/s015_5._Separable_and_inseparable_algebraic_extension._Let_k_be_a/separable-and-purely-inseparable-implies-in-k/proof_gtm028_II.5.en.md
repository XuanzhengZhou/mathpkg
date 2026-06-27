---
role: proof
locale: en
of_concept: separable-and-purely-inseparable-implies-in-k
source_book: gtm028
source_chapter: "II"
source_section: "5. Separable and inseparable algebraic extension"
---

If $e$ is the least non-negative integer such that $x^{p^e} \in k$ and if $x^{p^e} = a$, then by Corollary 3, the minimal polynomial of $x$ over $k$ is $X^{p^e} - a$. Since $x$ is separable over $k$, the derivative of this minimal polynomial must be non-zero. But the derivative of $X^{p^e} - a$ is $p^e X^{p^e - 1}$, which is zero if $e \geq 1$ (since $\operatorname{char}(k) = p$). Hence we must have $e = 0$, which means $x = x^{p^0} \in k$, as asserted.
