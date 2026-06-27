---
role: proof
locale: en
of_concept: derangement-formula
source_book: gtm054
source_chapter: "I"
source_section: "2"
---

Letting $r = 0$ in Proposition E16 (the formula for permutations with exactly $r$ fixed points) gives:
$$D_n = \frac{n!}{0!} \sum_{i=0}^{n} \frac{(-1)^i}{i!} = n! \sum_{i=0}^{n} \frac{(-1)^i}{i!}.$$

The $(n+1)$-st partial sum of the power series expansion $e^{-1} = \sum_{i=0}^{\infty} \frac{(-1)^i}{i!}$ equals $\frac{D_n}{n!}$, so $\lim_{n \to \infty} \frac{D_n}{n!} = e^{-1}$.
