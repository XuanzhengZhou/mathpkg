---
role: proof
locale: en
of_concept: hull-of-k-union-gamma
source_book: gtm035
source_chapter: "12"
source_section: "12.5"
---
# Proof of Polynomial Hull of $K \cup \gamma$

**Statement.** Let $\gamma$ be a finite union of smooth compact curves in $\mathbb{C}^N$ and let $K$ be a compact polynomially convex set in $\mathbb{C}^N$. Then $\widehat{K \cup \gamma} \setminus (K \cup \gamma)$ is a (possibly empty) one-dimensional analytic subvariety of $\mathbb{C}^N \setminus (K \cup \gamma)$.

**Proof (sketch).** When $K = \emptyset$, this reduces to Theorem 12.1, so assume $K \neq \emptyset$. Suppose there exists $x^0 \in \widehat{K \cup \gamma} \setminus (K \cup \gamma)$. We must show that $\widehat{K \cup \gamma}$ is a one-dimensional analytic set near $x^0$.

**Step 1.** Produce a polynomial $f$ in $z_1, \ldots, z_N$ such that $f(x^0) = 0$ and $0 \notin f(K \cup \gamma)$. This is possible because $x^0 \notin K \cup \gamma$, and the polynomial hull is defined as points where $|p(x)| \leq \|p\|_{K \cup \gamma}$ for all polynomials $p$. Since $x^0 \notin K \cup \gamma$ but $x^0 \in \widehat{K \cup \gamma}$, there exists a polynomial $p$ such that $|p(x^0)| > \|p\|_{K \cup \gamma}$. Adjusting by a constant gives the desired $f$.

**Step 2.** Choose a simply connected neighborhood $\mathcal{U}$ of $0$ in $\mathbb{C}$ such that $f^{-1}(\mathcal{U})$ is a neighborhood of $x^0$ in $\widehat{K \cup \gamma}$, and study the fibration of $f^{-1}(\mathcal{U})$ over $\mathcal{U}$.

Since $K$ is polynomially convex, $K \cap f^{-1}(z) = \emptyset$ for $z$ near $0$ (otherwise $z$ would be in $f(K)$, but $f$ is chosen so that $0 \notin f(K)$). Thus near $x^0$, the space $\widehat{K \cup \gamma}$ is essentially just $\hat{\gamma}$ with $K$ removed from consideration.

**Step 3.** Apply the same boundary-arc analysis as in Theorem 12.1. The components of $\mathbb{C} \setminus f(K \cup \gamma)$ are bounded by arcs from $f(\gamma)$ and $f(K)$. Since $f(K)$ is compact, polynomially convex (as $K$ is), and disjoint from $0$, the relevant boundary arcs come only from $\gamma$. The same sequence of component transitions as in Steps 2-4 of Theorem 12.1 yields that $f^{-1}(U^*)$ (where $U^*$ contains $0$) lies finite-sheeted over $U^*$.

**Step 4.** By Corollary 11.11, $f^{-1}(U^*)$ is a finite-sheeted analytic cover of $U^*$, providing a neighborhood of $x^0$ in $\widehat{K \cup \gamma}$ that is an analytic variety. Since this holds for every $x^0 \in \widehat{K \cup \gamma} \setminus (K \cup \gamma)$, the complement is a one-dimensional analytic subvariety of $\mathbb{C}^N \setminus (K \cup \gamma)$. $\square$
