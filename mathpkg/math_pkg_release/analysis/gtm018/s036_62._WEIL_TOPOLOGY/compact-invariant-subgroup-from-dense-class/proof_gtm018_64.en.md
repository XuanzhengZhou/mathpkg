---
role: proof
locale: en
of_concept: compact-invariant-subgroup-from-dense-class
source_book: gtm018
source_chapter: "64"
source_section: "Weil Topology"
---

**Theorem D.** Let $Y_0 = \{y : \rho(yE, E) = 0,\ E \in \mathbf{T}\}$. Since $\mathbf{E}$ is dense in the metric space of finite measure sets in $\mathbf{T}$, for any $E_0 \in \mathbf{T}$ with finite measure and any $\varepsilon > 0$, there exists a set $E \in \mathbf{E}$ such that $\rho(E_0, E) < \frac{\varepsilon}{2}$. It follows that if $y \in Y$, then

$$0 \leq \rho(yE_0, E_0) \leq \rho(yE_0, yE) + \rho(yE, E) + \rho(E, E_0) < \varepsilon.$$

Since $\varepsilon$ is arbitrary, this implies that $y \in Y_0$, and hence that $Y = Y_0$.

If $y_1$ and $y_2$ are in $Y$ and $E$ is in $\mathbf{T}$, then

$$0 \leq \rho(y_1^{-1}y_2E, E) \leq \rho(y_1^{-1}y_2E, y_2E) + \rho(y_2E, E).$$

Since $y_2E \in \mathbf{T}$ and $\rho(y_1^{-1}y_2E, y_2E) = \rho(y_2E, y_1y_2E)$, it follows that $y_1^{-1}y_2 \in Y$, so that $Y$ is indeed a subgroup of $X$. 

If $y \in Y$, $x \in X$, and $E \in \mathbf{T}$, then $xE \in \mathbf{T}$ and therefore $\rho(x^{-1}yxE, E) = \rho(yxE, xE) = 0$, so that $Y$ is invariant.

If $E_0$ is a bounded set of positive measure in $\mathbf{T}$, then the fact that $\rho(yE_0, E_0) = 0$ for every $y$ in $Y$ implies that $yE_0 \cap E_0 \neq 0$. It follows that $y \in E_0E_0^{-1}$ and hence that $Y \subset E_0E_0^{-1}$, which is bounded. To prove, finally, that $Y$ is closed, we observe that

$$Y = \bigcap_{E \in \mathbf{E}} \{y : \rho(yE, E) = 0\};$$

the desired result follows from 61.A (which states that the set $\{y : \rho(yE, E) = 0\}$ is closed for each Baire set $E$). Since $Y$ is closed and contained in a bounded set, it is compact. $\blacksquare$
