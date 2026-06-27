---
role: proof
locale: en
of_concept: lightcone-is-lightlike
source_book: gtm048
source_chapter: "1"
source_section: "1.1"
---

Regard $(V, g)$ as a Lorentzian manifold. The lightcone $\mathcal{L}_0$ is the zero-set of the smooth function $f(v) = g(v, v)$, whose differential is $df_v(w) = 2g(v, w)$. For $v \in \mathcal{L}_0$ (so $v \neq 0$ and $g(v, v) = 0$), the differential is nonzero since $g$ is nondegenerate and $v \neq 0$. Hence $\mathcal{L}_0$ is a smooth hypersurface in $V$.

For $v \in \mathcal{L}_0$, the tangent space $T_v \mathcal{L}_0 = \ker df_v = \{ w \in V \mid g(v, w) = 0 \} = v^\perp$. Since $v \in v^\perp$ (because $g(v, v) = 0$) and $v \neq 0$, we have $v \in T_v \mathcal{L}_0 \cap (T_v \mathcal{L}_0)^\perp \neq \{0\}$, which shows $\mathcal{L}_0$ is lightlike by Proposition 1.1.3(b).
