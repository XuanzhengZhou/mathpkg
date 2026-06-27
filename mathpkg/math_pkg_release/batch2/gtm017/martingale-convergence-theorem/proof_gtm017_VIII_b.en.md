---
role: proof
locale: en
of_concept: martingale-convergence-theorem
source_book: gtm017
source_chapter: "VIII"
source_section: "b"
---
Assume no convergence. Then there exist $a < b$ such that $P(\liminf X_n < a < b < \limsup X_n) > 0$. By considering upcrossings, one constructs sets $D_k$ where $X$ oscillates. Using the supermartingale property, for even $k$:
$$\int_{D_k} X_j \geq b P(D_k), \quad \int_{D_k} X_j \leq a P(D_k) \text{ (odd k)}$$
for large $j$, implying $E|X_j| \geq \frac{2}{3}r(b-a)P(D)$ for arbitrarily large $r$, contradicting $\sup_j E|X_j| \leq M$. Thus $\lim X_n$ exists almost surely with $E|\lim X_n| \leq M$ by Fatous lemma.
