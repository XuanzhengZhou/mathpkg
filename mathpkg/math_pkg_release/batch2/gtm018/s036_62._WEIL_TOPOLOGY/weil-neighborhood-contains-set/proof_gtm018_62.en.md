---
role: proof
locale: en
of_concept: weil-neighborhood-contains-set
source_book: gtm018
source_chapter: "62"
source_section: "Weil Topology"
---

**Theorem A.** It is sufficient to treat the case in which $F$ has finite measure. If $T(x, y) = (yx, y)$, then $T(E \times F)$ is a measurable set of finite measure in $X \times X$ and hence there exists a set $A$ in $X \times X$ such that $A$ is a finite union of measurable rectangles and

$$\frac{\varepsilon}{4}\mu(F) > \rho(T(E \times F), A).$$

If we write $C = \{y : \int |\chi_E(y^{-1}x) - \chi_A(x,y)| d\mu(x) \geq \frac{\varepsilon}{2}\}$, then it follows that $\mu(F \cap C) \leq \frac{1}{2}\mu(F)$ and hence that

$$\mu(F - C) \geq \frac{1}{2}\mu(F) > 0.$$

If $y \in F - C$, then

$$\rho(yE, A^y) = \int |\chi_E(y^{-1}x) - \chi_A(x,y)| d\mu(x) < \frac{\varepsilon}{2}.$$

Since $A$ is a finite union of measurable rectangles, there are only a finite number of distinct sets of the form $A^y$; we denote them by $A_1, \dots, A_n$. What we have proved may now be expressed by the relation

$$F - C \subset \bigcup_{i=1}^{n} \{y : \rho(yE, A_i) < \frac{\varepsilon}{2}\}.$$

Since $\frac{\varepsilon}{2} < \mu(E) = \mu(yE)$, it follows from 59.F that each of the sets $\{y : \rho(yE, A_i) < \frac{\varepsilon}{2}\}$ is measurable, and therefore, since $\mu(F - C) > 0$, that at least one of them intersects $F - C$ in a set of positive measure. We select an index $i$ such that if

$$G_0 = (F - C) \cap \{y : \rho(yE, A_i) < \frac{\varepsilon}{2}\},$$

then $\mu(G_0) > 0$. It is clear that $G_0$ is a measurable set of positive, finite measure and that $G_0 \subset F$. If $y_1 \in G_0^{-1}$ and $y_2 \in G_0^{-1}$, then

$$\rho(y_1 y_2^{-1} E, E) = \rho(y_2^{-1}E, y_1^{-1}E) \leq \rho(y_2^{-1}E, A_i) + \rho(A_i, y_1^{-1}E) < \varepsilon.$$

This implies that $y_1 y_2^{-1} \in N$, so that $G_0^{-1}G_0^{-1} \subset N$. Taking $G = G_0^{-1}$ yields $GG^{-1} \subset N$, and clearly $\mu(G) = \mu(G_0^{-1}) > 0$ with $G \subset F^{-1}$. Since the measure is not necessarily invariant, we note that we may apply the same argument symmetrically. $\blacksquare$
