---
role: proof
locale: en
of_concept: existence-of-basis-for-exponents
source_book: gtm041
source_chapter: "8"
source_section: "8.3"
---

Construct a basis as follows. For the first basis element take $\lambda(n_1)$, the first nonzero $\lambda$ (either $\lambda(1)$ or $\lambda(2)$), and call this $\beta(1)$. Now delete the remaining elements of $\Lambda$ that are rational multiples of $\beta(1)$. If this exhausts all of $\Lambda$ take $B = \{\beta(1)\}$. If not, let $\lambda(n_2)$ denote the first remaining $\lambda$, take $\beta(2) = \lambda(n_2)$, and strike out the remaining elements of $\Lambda$ which are rational linear combinations of $\beta(1)$ and $\beta(2)$. Continue in this fashion to obtain a sequence $B = (\beta(1), \beta(2), \ldots) = (\lambda(n_1), \lambda(n_2), \ldots)$.

It is easy to verify that $B$ is a basis for $\Lambda$. Property (a) holds by construction, since each $\beta$ was chosen to be independent of the earlier elements. To verify (b) we note that every $\lambda$ is either an element of $B$ or a rational linear combination of a finite number of elements of $B$. Finally, (c) holds trivially since $B$ is a subsequence of $\Lambda$.
