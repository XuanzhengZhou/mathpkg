---
role: proof
locale: en
of_concept: poincare-series-characterizes-homogeneous-isomorphism
source_book: gtm023
source_chapter: "VI"
source_section: "§1. G-graded vector spaces"
---

**Forward direction.** Suppose $\varphi: E \rightarrow F$ is a homogeneous linear isomorphism of degree $0$. Writing $\varphi = \sum_{k=0}^{\infty} \varphi_k$ (the decomposition from Section 6.2), each $\varphi_k$ is a linear isomorphism $\varphi_k: E_k \xrightarrow{\cong} F_k$. Hence $\dim E_k = \dim F_k$ for $k = 0, 1, \ldots$, and so $P_E = P_F$.

**Converse direction.** Assume $P_E = P_F$. Then $\dim E_k = \dim F_k$ for all $k = 0, 1, \ldots$. Thus there exist linear isomorphisms $\varphi_k: E_k \xrightarrow{\cong} F_k$. Since $E = \sum_{k=0}^{\infty} E_k$ is a direct sum, we can construct the linear mapping
$$\varphi = \sum_{k=0}^{\infty} \varphi_k: E \rightarrow F$$
by defining $\varphi$ on each $E_k$ via $\varphi_k$ and extending linearly. This map is clearly homogeneous of degree zero (it maps $E_k$ to $F_k$). Moreover, since each $\varphi_k$ is an isomorphism, $\varphi$ is both injective and surjective, hence a linear isomorphism.
