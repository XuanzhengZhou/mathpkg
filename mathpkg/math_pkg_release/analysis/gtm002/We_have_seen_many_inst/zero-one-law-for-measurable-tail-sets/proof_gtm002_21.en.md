---
role: proof
locale: en
of_concept: zero-one-law-for-measurable-tail-sets
source_book: gtm002
source_chapter: "21"
source_section: "The Extended Principle of Duality"
---

Define the product measure $\mu$ on $X$ via the mapping $g: X \to [0,1]$ given by $g(x) = \sum_{i=1}^{\infty} x_i/2^i$, so that $\mu(E) = m(g(E))$ whenever $g(E)$ is Lebesgue measurable.

Let $E$ be a measurable tail set. For any basic cylinder set $F = A_n \times Y^n$ (where $A_n \subseteq X^n$ is finite), the image $g(F)$ is a finite union of dyadic subintervals of $[0,1]$. Because $E$ is a tail set, $E = X^n \times B_n$ for some $B_n \subseteq Y^n$, and thus $E$ is independent of the first $n$ coordinates. Consequently, the events $E$ and $F$ are independent under $\mu$, so

$$\mu(E \cap F) = \mu(E) \mu(F).$$

This equation holds for every measurable set $F$ (by approximation from cylinder sets). In particular, taking $F = E$ yields

$$\mu(E) = \mu(E \cap E) = \mu(E) \mu(E) = \mu(E)^2.$$

Hence $\mu(E) = 0$ or $\mu(E) = 1$. $\square$
