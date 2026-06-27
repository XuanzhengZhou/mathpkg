---
role: proof
locale: en
of_concept: graded-bigraded-object-implies-stationary
source_book: gtm004
source_chapter: "VIII"
source_section: "3"
---

# Proof of Graded Bigraded Object Implies Stationarity of Exact Couple Maps

This is a direct consequence of the definitions.

Suppose $D$ is positively graded. Then, given $q$, there exists $p_0$ such that $D^{p,q} = 0$ for all $p < p_0$. For such $p$, the map

$$\alpha: D^{p,q} \longrightarrow D^{p+1,q}$$

has zero domain and zero codomain whenever $p < p_0 - 1$ (since $D^{p+1,q} = 0$ as well). Hence $\alpha$ is trivially an isomorphism on these bidegrees, which is precisely the definition of negative stationarity: given $q$, there exists $p_0 - 1$ such that $\alpha: D^{p,q} \to D^{p+1,q}$ is an isomorphism for all $p \le p_0 - 1$. Thus $\alpha$ is negatively stationary.

The argument for the remaining cases is completely symmetric:

- If $D$ is negatively graded, then for given $q$, $D^{p,q} = 0$ for $p$ sufficiently large, forcing $\alpha$ to be positively stationary.
- If $\bar{D}$ is positively graded, then $\bar{\alpha}$ is negatively stationary.
- If $\bar{D}$ is negatively graded, then $\bar{\alpha}$ is positively stationary.

In each case, the zero condition on the bigraded object forces the corresponding map $\alpha$ (or $\bar{\alpha}$) to be an isomorphism between zero modules outside a bounded range, yielding the required stationarity. $\square$
