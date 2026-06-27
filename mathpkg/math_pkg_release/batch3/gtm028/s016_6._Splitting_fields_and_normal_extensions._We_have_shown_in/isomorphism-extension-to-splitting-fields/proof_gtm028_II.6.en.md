---
role: proof
locale: en
of_concept: isomorphism-extension-to-splitting-fields
source_book: gtm028
source_chapter: "II"
source_section: "6. Splitting fields and normal extensions"
---

The proof proceeds by induction on the degree $n$ of $f(X)$. If $n = 1$, then $k' = k$ and $\bar{k}' = \bar{k}$, and the statement is trivially true with $\rho = \tau$. Assume $n > 1$ and that the theorem holds for all polynomials of degree less than $n$. Let $g(X)$ be an irreducible factor of $f(X)$ in $k[X]$, and let $\bar{g}(X) = [g(X)]\tau$. Let $\alpha$ be a root of $g(X)$ in $k'$ and let $\bar{\alpha}$ be a root of $\bar{g}(X)$ in $\bar{k}'$. By the preceding lemma, $\tau$ extends uniquely to an isomorphism $\tau_1$ of $k(\alpha)$ onto $\bar{k}(\bar{\alpha})$ sending $\alpha$ to $\bar{\alpha}$. Over $k(\alpha)$, the polynomial $f(X)$ has degree $n-1$ (since $\alpha$ is a root), and $k'$ is a splitting field of $f(X)$ over $k(\alpha)$. Similarly, $\bar{k}'$ is a splitting field of $\bar{f}(X)$ over $\bar{k}(\bar{\alpha})$. By the induction hypothesis, $\tau_1$ extends to an isomorphism $\rho$ of $k'$ onto $\bar{k}'$. The property that $\rho$ sends roots of $f(X)$ to roots of $\bar{f}(X)$ follows from the fact that $\rho$ extends $\tau$ and that $f(X)^\rho = \bar{f}(X)$.
