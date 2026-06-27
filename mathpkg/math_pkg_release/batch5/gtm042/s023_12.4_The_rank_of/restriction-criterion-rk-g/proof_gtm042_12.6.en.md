---
role: proof
locale: en
of_concept: restriction-criterion-rk-g
source_book: gtm042
source_chapter: "12"
source_section: "12.6"
---

Using Theorem 27, we have an identity

$$1 = \sum_{H \in X_K} \operatorname{Ind}_H^G f_H, \quad \text{with} \ f_H \in R_K(H).$$

Multiplying by $\varphi$, this gives

$$\varphi = \sum_{H \in X_K} \operatorname{Ind}_H^G( f_H \cdot \operatorname{Res}_H^G \varphi ).$$

If $\operatorname{Res}_H^G \varphi \in R_K(H)$ for every $\Gamma_K$-elementary subgroup $H$, then each term $f_H \cdot \operatorname{Res}_H^G \varphi$ belongs to $R_K(H)$ (since $R_K(H)$ is a ring), and $\varphi$ is a sum of induced characters from $\Gamma_K$-elementary subgroups, hence $\varphi \in R_K(G)$.

Conversely, if $\varphi \in R_K(G)$, then for any subgroup $H$ (in particular any $\Gamma_K$-elementary $H$), the restriction $\operatorname{Res}_H^G \varphi$ automatically belongs to $R_K(H)$ by functoriality of restriction.
