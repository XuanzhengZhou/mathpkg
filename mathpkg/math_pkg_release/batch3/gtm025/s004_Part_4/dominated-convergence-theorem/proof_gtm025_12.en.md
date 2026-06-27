---
role: proof
locale: en
of_concept: dominated-convergence-theorem
source_book: gtm025
source_chapter: "3"
source_section: "12"
---

All $f_n$ are in $\mathfrak{L}_1^r$, so all $f_n$, and $s$, are finite a.e. on $X$. Redefine $f_n(x) = s(x) = 0$ on the null set where they are infinite or undefined. Now $|f_n(x)| \leq s(x) < \infty$ for all $n \in N$ and $x \in X$.\n\nApply Fatou's lemma (12.23) to the nonnegative sequence $(s + f_n)_{n=1}^{\infty}$:\n$$\int_X s d\mu + \int_X \lim_{n \to \infty} f_n d\mu = \int_X [\lim_{n \to \infty} (s + f_n)] d\mu \leq \liminf_{n \to \infty} \int_X (s + f_n) d\mu = \int_X s d\mu + \liminf_{n \to \infty} \int_X f_n d\mu.$$\nThus $\int_X \lim f_n d\mu \leq \liminf \int_X f_n d\mu$.\n\nSimilarly, applying Fatou to $(s - f_n)$ gives $\limsup \int_X f_n d\mu \leq \int_X \lim f_n d\mu$. Combining yields equality.
