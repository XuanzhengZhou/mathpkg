---
role: proof
locale: en
of_concept: properties-of-holomorphically-convex-hull
source_book: gtm038
source_chapter: "II"
source_section: "3. Holomorphic Convexity"
---

1. For $z \in K$, $|f(z)| \leq \sup|f(K)|$, hence $z \in \hat{K}$.
2. Let $z \in B - \hat{K}$. Then there exists $f$ holomorphic on $B$ with $|f(z)| > \sup|f(K)|$. Since $|f|$ is continuous, these inequalities hold on a neighborhood $U(z) \subset B - \hat{K}$. Therefore $B - \hat{K}$ is open, so $\hat{K}$ is closed in $B$.
3. $\sup|f(K)| = \sup|f(\hat{K})|$, hence $\widehat{\hat{K}} = \hat{K}$.
4. Follows from $\sup|f(K_1)| \leq \sup|f(K_2)|$.
5. If $K$ is bounded then there exists $R > 0$ with $K \subset \{z: |z_\nu| \leq R\}$. The coordinate functions $f_\nu(z) \equiv z_\nu$ are holomorphic, so for $z \in \hat{K}$, $|z_\nu| = |f_\nu(z)| \leq \sup|f_\nu(K)| \leq R$. Hence $\hat{K}$ is bounded.
