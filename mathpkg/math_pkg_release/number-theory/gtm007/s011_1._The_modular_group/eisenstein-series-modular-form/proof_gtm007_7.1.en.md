---
role: proof
locale: en
of_concept: eisenstein-series-modular-form
source_book: gtm007
source_chapter: "VII"
source_section: "1"
---

**Convergence.** For $z \in H$, the number of pairs $(m, n)$ with $|mz + n|$ between $R$ and $R+1$ grows as $O(R)$. The series $\sum 1/|mz+n|^{2k}$ behaves like $\sum_R R/R^{2k} = \sum_R 1/R^{2k-1}$, which converges for $2k-1 > 1$, i.e. $k > 1$.

**Weak modularity.** For $g = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathbf{SL}_2(\mathbf{Z})$,
$$G_k\left(\frac{az+b}{cz+d}\right) = (cz+d)^{2k} G_k(z),$$
since the change of variables $(m, n) \mapsto (am+cn, bm+dn)$ permutes the nonzero pairs of $\mathbf{Z}^2$.

**Holomorphy.** First suppose $z$ is in the fundamental domain $D$. Then $|mz+n| \geq c|n|$ for some constant $c > 0$, so the series converges uniformly on compact subsets, giving holomorphy on $H$.

**Behavior at infinity.** As $\operatorname{Im}(z) \to \infty$, $q = e^{2\pi i z} \to 0$. The terms with $m = 0$ give $\sum_{n \neq 0} 1/n^{2k} = 2\zeta(2k)$. The terms with $m \neq 0$ tend to $0$. Hence $G_k(\infty) = 2\zeta(2k) \neq 0$ for $k \geq 2$.
