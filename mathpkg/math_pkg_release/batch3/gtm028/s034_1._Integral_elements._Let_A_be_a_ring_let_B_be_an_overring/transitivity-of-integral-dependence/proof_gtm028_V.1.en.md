---
role: proof
locale: en
of_concept: transitivity-of-integral-dependence
source_book: gtm028
source_chapter: "V"
source_section: "1"
---

Let $x$ be an element of $C$, and let

$$x^n + b_{n-1} x^{n-1} + \cdots + b_1 x + b_0 = 0$$

be an equation of integral dependence of $x$ over $B$, where $b_i \in B$ for $0 \leq i \leq n-1$.

Since $B$ is integral over $A$, each $b_i$ is integral over $A$. Consider the ring

$$B_0 = A[b_0, b_1, \dots, b_{n-1}].$$

By Theorem 1 (applied to $B$), $B_0$ is a finite $A$-module.

Now $x$ is integral over $B_0$ (the same equation with coefficients $b_i \in B_0$ shows this). Therefore $B_0[x]$ is a finite $B_0$-module by condition (c'), hence a finite $A$-module by Remark 3 (transitivity of the finite module property).

Since $x \in B_0[x]$ and $B_0[x]$ is a finite $A$-module, $x$ is integral over $A$ by condition (c''). As $x \in C$ was arbitrary, $C$ is integral over $A$. $\square$
