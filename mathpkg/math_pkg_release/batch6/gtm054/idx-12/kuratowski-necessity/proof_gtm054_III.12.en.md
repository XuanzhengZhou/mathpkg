---
role: proof
locale: en
of_concept: kuratowski-necessity
source_book: gtm054
source_chapter: "III"
source_section: "12"
---

By Exercise E15, it suffices to prove only that neither $K_5$ nor $K_{3,3}$ is planar.

By Proposition D13, $\mathcal{X}(K_5)$ is not graphic, and since $K_5$ has no isthmus, $K_5$ is not planar by Proposition E6.

Now suppose that $K_{3,3}$ is planar. By substituting $\nu_1(K_{3,3}) = 9$ and $\rho(K_{3,3}) = 3$ (since $K_{3,3}$ is $3$-valent) into Corollary F4, we obtain:
$$\frac{1}{\rho^{\perp}} = \frac{1}{2} + \frac{1}{9} - \frac{1}{3} = \frac{9}{18} + \frac{2}{18} - \frac{6}{18} = \frac{5}{18},$$
hence $\rho^{\perp} = \frac{18}{5} = 3.6$.

But every region of a planar imbedding of a bipartite graph (and $K_{3,3}$ is bipartite) must have covalence at least $4$ (since odd cycles are impossible in a bipartite graph, regions must be bounded by even cycles). Therefore $\rho^{\perp} \geq 4$, contradicting $\rho^{\perp} = 3.6$. Hence $K_{3,3}$ is not planar.
