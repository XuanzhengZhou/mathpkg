---
role: proof
locale: en
of_concept: regular-functions-of-3d-srw-are-constants
source_book: gtm040
source_chapter: "10"
source_section: "13"
---

Choose $\pi$ to be a unit mass at $0$. It is enough to prove that $K(\cdot, x) = 1$ for every $x$ in the boundary. That is, it suffices to prove that for every $i$,

$$\lim_{j \to \infty} K(i, j) = 1.$$

We shall prove the following estimate for $N_{0j}$: If $j \neq 0$, then

$$N_{0j} = \frac{3}{2\pi|j|} + O(|j|^{-2}).$$

Once we have this estimate, we also have, for $i \neq j$,

$$K(i, j) = \frac{N_{ij}}{N_{0j}} = \frac{\frac{3}{2\pi|j-i|} + O(|j-i|^{-2})}{\frac{3}{2\pi|j|} + O(|j|^{-2})}$$

$$= \frac{|j-i|^{-1} + O(|j|^{-2})}{|j|^{-1} + O(|j|^{-2})}$$

$$= \frac{|j|}{|j-i|} + O(|j|^{-1}).$$

Hence, $\lim_{j} K(i, j) = 1$, as asserted.
