---
locale: en
of_concept: let-h-be-a-closed-subgroup-of-g-every-principal-h-bundle-eta
role: proof
source_book: gtm020
source_chapter: 6. Change of Structure Group
source_section: '1'
---

Let $f: Y \rightarrow X$ be a map defining a restriction of principal bundles. Then the composition of $f: Y \rightarrow X$ and the quotient map $X \rightarrow X \bmod H$ is a map $\sigma^*$ such that $\sigma^*(ys) = \sigma^*(y)s$ for each $s \in H$. This map $\sigma^*$ defines a cross section of $\xi \bmod H$ (or $\xi[G \bmod H]$).

Conversely, a cross section $\sigma$ of $\xi[G \bmod H]$ defines a map $g: X \rightarrow G \bmod H$ such that $g(xs) = s^{-1}g(x) = g(x)s$ for each $s \in G$ by Theorem 4(8.1). Let $Y$ be the closed subset $g^{-1}(eH)$ of $X$, let $q$ be the restriction $p|Y$, and let $\eta = (Y, q, B)$. Let $y_1, y_2 \in Y$ such that $q(y_1) = q(y_2)$. For some $s \in G$ we have $y_2 = y_1s$, $eH = g(y_2) = g(y_1s) = s^{-1}g(y_1) = s^{-1}eH$, and $s \in H$. Finally, the restriction of the translation function of the principal $G$-space $X$ is the translation function of the principal $H$-space $Y$.

If $\xi$ is trivial, we have $H$-morphisms $Y \rightarrow X$, $X \rightarrow G$, and $G \rightarrow H$ which compose to an $H$-morphism $Y \rightarrow H$, and $\eta$ is trivial by 4(8.3). For the statement concerning local triviality we can use 4(6.4).
