---
role: proof
locale: en
of_concept: non-polynomially-convex-arc-example
source_book: gtm035
source_chapter: "Chapter 24"
source_section: "24.15"
---
# Proof of Example of Non-Polynomially Convex Arc in $\mathbb{C}^3$

**Theorem 24.15.** Let $\gamma$ be an arc in the complex plane having positive planar (Lebesgue) measure. Define the arc $J_0 \subset \mathbb{C}^3$ as the image of $\gamma$ under the map

$$\zeta \mapsto (F(\zeta), F_2(\zeta), F_3(\zeta)),$$

where $F, F_2, F_3 \in \mathfrak{A}_\gamma$ are functions constructed in Lemma 24.14 that separate points on the Riemann sphere $S^2$. Then $J_0$ is not polynomially convex in $\mathbb{C}^3$. Consequently, $P(J_0) \neq C(J_0)$.

**Proof.** Recall that $\mathfrak{A}_\gamma$ denotes the algebra of functions continuous on the Riemann sphere $S^2$ and analytic on $S^2 \setminus \gamma$. The arc $\gamma$ has positive planar measure. By Lemma 24.14, there exist three functions $F, F_2, F_3 \in \mathfrak{A}_\gamma$ that separate points on $S^2$.

Set $J_0 = \{(F(\zeta), F_2(\zeta), F_3(\zeta)) : \zeta \in \gamma\}$, which is an arc in $\mathbb{C}^3$.

Fix $\zeta_0 \in S^2 \setminus \gamma$ and put $x^0 = (F(\zeta_0), F_2(\zeta_0), F_3(\zeta_0))$. Then $x^0 \notin J_0$ since $\zeta_0 \notin \gamma$. We claim that $x^0$ belongs to the polynomial hull $\widehat{J_0}$ of $J_0$.

To prove this, let $P$ be any polynomial in three complex variables. Consider the function

$$f(\zeta) = P(F(\zeta), F_2(\zeta), F_3(\zeta)), \quad \zeta \in S^2.$$

Since $F, F_2, F_3 \in \mathfrak{A}_\gamma$, each of these functions is continuous on $S^2$ and analytic on $S^2 \setminus \gamma$. A polynomial composed with functions in $\mathfrak{A}_\gamma$ yields another function in $\mathfrak{A}_\gamma$ (the algebra is closed under composition with polynomials). Hence $f \in \mathfrak{A}_\gamma$.

Now, any function in $\mathfrak{A}_\gamma$ satisfies the maximum modulus principle with respect to $\gamma$: for all $\zeta \in S^2$,

$$|f(\zeta)| \leq \max_{z \in \gamma} |f(z)|.$$

This is a fundamental property of the algebra $\mathfrak{A}_\gamma$ -- since $\gamma$ has positive planar measure, the functions in $\mathfrak{A}_\gamma$ achieve their maximum on $\gamma$ (a consequence of the Painleve problem / Hartogs-Rosenthal theorem; the rational functions with poles off $\gamma$ are dense, and for such rational functions the maximum on $S^2$ is attained on $\gamma$ by the maximum principle applied to each component of $S^2 \setminus \gamma$, but since $\gamma$ has positive area, $S^2 \setminus \gamma$ has no bounded components).

Applying this to $f$ at $\zeta_0$, we obtain

$$|P(x^0)| = |f(\zeta_0)| \leq \max_{\zeta \in \gamma} |f(\zeta)| = \max_{(z_1, z_2, z_3) \in J_0} |P(z_1, z_2, z_3)|.$$

This inequality holds for every polynomial $P$. Therefore, $x^0$ belongs to the polynomially convex hull $\widehat{J_0}$ of $J_0$.

Since $x^0 \notin J_0$ but $x^0 \in \widehat{J_0}$, the arc $J_0$ is **not** polynomially convex. Moreover, $P(J_0) \neq C(J_0)$ because the point evaluation at $x^0$ gives a multiplicative linear functional on $P(J_0)$ that does not arise from a point of $J_0$.

The existence of an arc with positive planar measure is classical; such an arc can be constructed by passing an arc through a compact totally disconnected subset of the plane having positive planar measure (e.g., $E \times E$ where $E \subset \mathbb{R}$ is a Cantor-type set of positive linear measure), as shown by F. Riesz.
