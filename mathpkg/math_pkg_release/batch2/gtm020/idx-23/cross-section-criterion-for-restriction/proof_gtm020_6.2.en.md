---
role: proof
locale: en
of_concept: cross-section-criterion-for-restriction
source_book: gtm020
source_chapter: "6"
source_section: "2"
---

($\Rightarrow$) Let $f: Y \rightarrow X$ be a map defining a restriction of principal bundles. Then the composition of $f: Y \rightarrow X$ and the quotient map $X \rightarrow X \bmod H$ is a map $\sigma^*$ such that $\sigma^*(ys) = \sigma^*(y)s$ for each $s \in H$. This map $\sigma^*$ defines a cross section of $\xi \bmod H$ (or, by Theorem 1.1, of $\xi[G \bmod H]$).

($\Leftarrow$) Conversely, a cross section $\sigma$ of $\xi[G \bmod H]$ defines a map $g: X \rightarrow G \bmod H$ such that
$$
g(xs) = s^{-1}g(x)
$$
for each $s \in G$ by Theorem 4(8.1). Since the action of $G$ on $G \bmod H$ is given by left multiplication on representatives, we also have $g(xs) = g(x)s$ in the natural sense.

Let $Y$ be the closed subset $g^{-1}(eH)$ of $X$, let $q$ be the restriction $p|_Y$, and let $\eta = (Y, q, B)$. Let $y_1, y_2 \in Y$ such that $q(y_1) = q(y_2)$. For some $s \in G$ we have $y_2 = y_1 s$. Then
$$
eH = g(y_2) = g(y_1 s) = s^{-1}g(y_1) = s^{-1}eH,
$$
which implies $s \in H$. Thus the fibres of $\eta$ are precisely the $H$-orbits, and $\eta$ is a principal $H$-bundle.

The restriction of the translation function of the principal $G$-space $X$ is the translation function of the principal $H$-space $Y$, and the inclusion $Y \hookrightarrow X$ provides the required $H$-equivariant homeomorphism onto a closed subset, establishing $\eta$ as a restriction of $\xi$.
