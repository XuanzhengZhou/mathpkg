---
role: proof
locale: en
of_concept: lebesgue-dominated-convergence-theorem
source_book: gtm040
source_chapter: "1"
source_section: "4"
---
By property (7) of Proposition 1-39, $f$ is integrable and so is $f_n$ for every $n$. Apply Fatou's Lemma to $f_n + g \geq 0$:
$$\int_E (f + g) d\mu \leq \liminf \int_E (f_n + g) d\mu,$$
so $\int_E f d\mu \leq \liminf \int_E f_n d\mu$. Apply Fatou's Lemma to $g - f_n \geq 0$:
$$\int_E (g - f) d\mu \leq \liminf \int_E (g - f_n) d\mu,$$
so $-\int_E f d\mu \leq -\limsup \int_E f_n d\mu$, i.e., $\limsup \int_E f_n d\mu \leq \int_E f d\mu$. Combining yields equality.
