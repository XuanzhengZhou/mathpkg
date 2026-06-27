---
role: proof
locale: en
of_concept: lemma-inverse-identity-in-loops
source_book: gtm006
source_chapter: "VI"
source_section: "6. Division Rings with Inverse Properties"
---

Suppose $G$ has RIP. Since $(yx)x^{-1} = y$ for all $y \in G$, set $y = x^{-1}$ to obtain $(x^{-1}x)x^{-1} = x^{-1}$. In a loop, the equation $b x^{-1} = x^{-1}$ has the unique solution $b = 1$. Hence $x^{-1}x = 1$.

Now set $y = 1$ in the RIP identity: $(1 \cdot x)x^{-1} = 1$, which yields $x x^{-1} = 1$. Thus
$$x^{-1}x = 1 = x x^{-1}.$$

From $x^{-1}x = 1 = x x^{-1}$ and the uniqueness of inverses (in any loop, if $ab = 1 = ba$ then $a$ and $b$ are mutual inverses), it follows immediately that $(x^{-1})^{-1} = x$.

The proof for LIP is entirely symmetric, using $x^{-1}(xy) = y$ in place of $(yx)x^{-1} = y$.
