---
role: proof
locale: en
of_concept: zero-gauss-curvature-not-developable
source_book: gtm051
source_chapter: "3"
source_section: "3.9.4"
---

**Construction.** Define the second fundamental form by $h_{ik} = P_{ik}(u,v) e^{-((1 \pm v)/u)^2}$. The exponential factor ensures smoothness at $u = 0$ by making all derivatives vanish there, while the rational functions $P_{ik}$ are chosen to satisfy the Codazzi-Mainardi equations away from the origin.

1. **Differentiability of $h_{ik}$:** The exponential factor $e^{-((1\pm v)/u)^2}$ has vanishing derivatives of all orders as $u \to 0$ (along curves where $(1\pm v)/u \to \pm\infty$), compensating for the singular behavior of $P_{ik}$. Thus the $h_{ik}$ are $C^\infty$ on the entire domain.

2. **Gauss curvature zero:** Direct computation gives
$$h_{11}h_{22} - h_{12}^2 = P_{11}P_{22} - P_{12}^2 \cdot e^{-2((1\pm v)/u)^2} = \left(\frac{u^2}{(1\pm v)^4} - \frac{u^2}{(1\pm v)^4}\right) e^{-2((1\pm v)/u)^2} = 0.$$
Since $g_{ik} = \delta_{ik}$, we have $\det(g) = 1$ and therefore $K = (h_{11}h_{22} - h_{12}^2)/\det(g) = 0$.

3. **Gauss-Codazzi equations:** The functions are constructed so that $h_{11,2} = h_{12,1}$ and $h_{22,1} = h_{12,2}$ hold. With $g_{ik} = \delta_{ik}$, the Christoffel symbols vanish, so the Gauss equation reduces to $R_{1212} = h_{11}h_{22} - h_{12}^2 = 0$, which is satisfied. The Codazzi equations reduce to the mixed partial conditions, which hold by construction.

4. **Existence:** By the fundamental theorem of surface theory (3.8.8), since the Gauss and Codazzi-Mainardi equations are satisfied, there exists a surface $f$ with these first and second fundamental forms, unique up to an isometry of $\mathbb{R}^3$.

5. **Non-developability:** The second fundamental form has been chosen so that the asymptotic directions in the region $u < 0$ are the straight lines through $(0,1)$, while in $u > 0$ they are straight lines through $(0,-1)$. As one crosses the $u$-axis through $(0,0)$, the slope of these asymptotic lines diverges discontinuously. Assume such a change of variables $\phi$ exists, giving $f \circ \phi(s,t) = sX(t) + c(t)$. Then the asymptotic lines would have to vary continuously across $u = 0$, contradicting the discontinuous behavior built into $h_{ik}$. Therefore no such parametrization exists near $(0,0)$, and $f$ is not developable.
