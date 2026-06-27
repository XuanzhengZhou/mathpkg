---
role: proof
locale: en
of_concept: fourier-inversion-theorem
source_book: gtm025
source_chapter: "21"
source_section: "§21"
---

By (21.43) and (21.45.a), $f(x) = \lim_{n\to\infty} (2\pi)^{-\frac{1}{2}} \int_R \hat{f}(y) \exp(-|y|/n)\exp(ixy)dy$. Since $|\hat{f}(y)\exp(-|y|/n)\exp(ixy)| \leq |\hat{f}(y)|$ and $\exp(-|y|/n) \to 1$, dominated convergence yields the inversion formula. By (21.39), the left side is in $\mathfrak{C}_0(R)$, so $f$ equals a.e. a function in $\mathfrak{C}_0(R) \cap \mathfrak{L}_1(R)$. Two continuous functions equal a.e. are identical, proving the last statement.
