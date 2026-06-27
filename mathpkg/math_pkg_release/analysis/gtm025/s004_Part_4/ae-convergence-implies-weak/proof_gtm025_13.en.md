---
role: proof
locale: en
of_concept: ae-convergence-implies-weak
source_book: gtm025
source_chapter: "4"
source_section: "13"
---

Let $\|f_n\|_p \leq \alpha$. By Fatou's lemma, $\|f\|_p \leq \alpha$. Given $\varepsilon > 0$ and $g \in \mathfrak{L}_{p'}$, use (12.34) to get $\delta > 0$ with $2\alpha(\int_E |g|^{p'})^{1/p'} < \varepsilon/3$ when $\mu(E) < \delta$. Choose $A$ with finite measure where the tail of $g$ is small. Apply Egorov's theorem on $A$ to get $B$ of small complement where $f_n \to f$ uniformly. Split the integral over $B$, $A \cap B'$, and $A'$.
