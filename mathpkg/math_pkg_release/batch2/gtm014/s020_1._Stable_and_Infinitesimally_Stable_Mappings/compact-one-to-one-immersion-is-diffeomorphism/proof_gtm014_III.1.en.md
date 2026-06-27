---
role: proof
locale: en
of_concept: compact-one-to-one-immersion-is-diffeomorphism
source_book: gtm014
source_chapter: "III"
source_section: "§1. Stable and Infinitesimally Stable Mappings"
---

By II, Proposition 5.8 there is a neighborhood of $f$ in $C^\infty(X, X)$ which consists of one-to-one immersions. Let $g: X \to X$ be a one-to-one immersion and let $X^0$ be a connected component of $X$. Then $g(X^0)$ is closed since $X^0$ is compact, while it is open since $g$ is a submersion (a one-to-one immersion between manifolds of the same dimension is a submersion at each point by dimensionality). So $g(X^0)$ is a connected component of $X$.

We claim that $g|_{X^0}: X^0 \to g(X^0)$ is a diffeomorphism. The inverse $(g|_{X^0})^{-1}$ exists since $g$ is one-to-one. At each point of $g(X^0)$, $(g|_{X^0})^{-1}$ is smooth by the Inverse Function Theorem, because $g$ is an immersion and hence a local diffeomorphism. Therefore $g$ is a diffeomorphism.
