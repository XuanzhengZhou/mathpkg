---
role: proof
locale: en
of_concept: derivative-belongs-to-conductor
source_book: gtm028
source_chapter: "IV"
source_section: "11. Different and discriminant"
---

Let $R''$ be the integral closure of $R$ in $K'$, with conductor $\mathfrak{F} = \{x \in R' : x R'' \subset R'\}$.

Every element $z$ of $R''$ is contained in the complementary module $\mathfrak{C}_{R'/R}$, since for any element $x \in R'$, the product $zx$ is integral over $R$ and hence $T(zx) \in R$. Therefore we have $\mathfrak{D}_{R'/R} \cdot R'' \subset R'$; in other words, the different of $R'$ over $R$ is contained in the conductor $\mathfrak{F}$ of the integral closure of $R'$. In particular, $\mathfrak{F} \neq (0)$ since the different of $R'$ over $R$ is $\neq (0)$ (Corollary to Theorem 26).

The argument from the Lagrange interpolation formula (used in the proof of the previous theorem) applies also to the case where $R$ is not a Dedekind domain (but is integrally closed), and shows that $F'(y)$ belongs to $\mathfrak{F}$. Specifically, for any $z' \in \mathfrak{C}_{R'/R}$ and $z = z' F'(y)$, the coefficients of the polynomial $g(X)$ given by the Lagrange formula lie in $R$, hence $F'(y)z' = g(y) \in R'$. Since this holds for all $z' \in \mathfrak{C}_{R'/R}$, we obtain $F'(y) \cdot \mathfrak{C}_{R'/R} \subset R'$, which means $F'(y) \in \mathfrak{D}_{R'/R}$. The inclusion $\mathfrak{D}_{R'/R} \subset \mathfrak{F}$ then gives $F'(y) \in \mathfrak{F}$.

On the other hand, since $T(z R'') \subset R$ implies $T(z R') \subset R$, we have $\mathfrak{C}_{R''/R} \subset \mathfrak{C}_{R'/R}$. Hence, by the definition of the different, $\mathfrak{D}_{R'/R} \subset \mathfrak{D}_{R''/R}$.

When $R$ is a Dedekind domain, we have $R' = R''$ and the conductor is the unit ideal. The result then states that $\mathfrak{D}_{R'/R}$ divides the principal ideal $R' F'(y)$.
