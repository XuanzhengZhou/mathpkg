---
role: proof
locale: en
of_concept: finitely-generated-galois-group-over-iwasawa-algebra
source_book: gtm059
source_chapter: "5"
source_section: "§6. The Galois Group as Module over the Iwasawa Algebra"
---

**Proof.** By definition,

$$G/G^{\gamma-1} = \operatorname{Gal}(Q/K_0)^{\mathrm{ab}}(p),$$

the maximal $p$-abelian $p$-ramified extension of $K_0$. The rank over $\mathbb{Z}_p$ of a subgroup of finite index in this Galois group was determined to be $[K_0 : \mathbb{Q}] - r_p$ in Theorem 5.2, where $r_p = \operatorname{rank}_{\mathbb{Z}_p}(\overline{E} \cap U_p)$ is the $\mathbb{Z}_p$-rank of the closure of the global units in the local units.

Taking into account the factor $\Gamma = \operatorname{Gal}(K_\infty/K_0) \cong \mathbb{Z}_p$ itself, which is the Galois group of the cyclotomic (or more generally any) $\mathbb{Z}_p$-extension, we find that $G/XG \cong \mathbb{Z}_p^\rho$ where $\rho = [K_0 : \mathbb{Q}] - r_p - 1$. Here $X = \gamma - 1$ is the generator of the augmentation ideal of $\Lambda$.

Now $G/XG$ being a finitely generated $\mathbb{Z}_p$-module of finite rank implies, by Nakayama's lemma (since $X$ lies in the maximal ideal of the local ring $\Lambda = \mathbb{Z}_p[\![X]\!]$), that $G$ is finitely generated over $\Lambda$. This proves assertion (i).

For part (ii), the Leopoldt conjecture states precisely that $r_p = r_1 + r_2 - 1$, where $r_1$ is the number of real places and $r_2$ the number of complex places of $K_0$. Since $[K_0 : \mathbb{Q}] = r_1 + 2r_2$, we obtain:

$$\rho = [K_0 : \mathbb{Q}] - r_p - 1 = (r_1 + 2r_2) - (r_1 + r_2 - 1) - 1 = r_2.$$

Thus under the Leopoldt conjecture, $G/G^{\gamma-1} \cong \mathbb{Z}_p^{r_2}$. $\square$
