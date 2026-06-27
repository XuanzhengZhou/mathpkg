---
role: proof
locale: en
of_concept: local-c-algebra-homomorphism-preserves-maximal-ideal
source_book: gtm038
source_chapter: "V"
source_section: "1"
---

(1) Let $\sigma \in \mathfrak{m}_1$. For any $c \in \mathbb{C} \setminus \{0\}$, the element $\sigma - c \cdot 1$ is not in $\mathfrak{m}_1$. Indeed, if it were, then both $\sigma$ and $\sigma - c \cdot 1$ would be in $\mathfrak{m}_1$, implying $c \cdot 1 \in \mathfrak{m}_1$, which contradicts the fact that $\mathfrak{m}_1$ is a proper ideal (units cannot lie in the maximal ideal). Therefore, for every $c \in \mathbb{C} \setminus \{0\}$ there exists $\sigma_c \in R_1$ such that
$$\sigma_c \cdot (\sigma - c \cdot 1) = 1.$$
Applying the homomorphism $\rho$ yields
$$\rho(\sigma_c) \cdot (\rho(\sigma) - c \cdot 1) = 1.$$
Hence $\rho(\sigma) - c \cdot 1$ is a unit in $R_2$ for every $c \in \mathbb{C} \setminus \{0\}$, which means $\rho(\sigma) - c \cdot 1 \notin \mathfrak{m}_2$ for all $c \neq 0$. Since the residue field is $\mathbb{C}$, this implies $\rho(\sigma)$ lies in $\mathfrak{m}_2$. Thus $\rho(\mathfrak{m}_1) \subset \mathfrak{m}_2$.

(2) If $\rho$ is an isomorphism, apply part (1) to $\rho^{-1}: (R_2, \mathfrak{m}_2) \to (R_1, \mathfrak{m}_1)$ to obtain $\rho^{-1}(\mathfrak{m}_2) \subset \mathfrak{m}_1$. Then
$$\mathfrak{m}_2 = \rho(\rho^{-1}(\mathfrak{m}_2)) \subset \rho(\mathfrak{m}_1) \subset \mathfrak{m}_2,$$
so $\rho(\mathfrak{m}_1) = \mathfrak{m}_2$.
