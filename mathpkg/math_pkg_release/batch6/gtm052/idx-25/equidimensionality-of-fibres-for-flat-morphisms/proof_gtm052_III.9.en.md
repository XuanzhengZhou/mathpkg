---
role: proof
locale: en
of_concept: equidimensionality-of-fibres-for-flat-morphisms
source_book: gtm052
source_chapter: "III"
source_section: "9"
---
(i) $\Rightarrow$ (ii): Given $y \in Y$, let $Z \subseteq X_y$ be an irreducible component, and let $x \in Z$ be a closed point not in any other irreducible component of $X_y$. Applying (9.5) we have $\dim_x Z = \dim_x X - \dim_y Y$. Now $\dim_x Z = \dim Z$ since $x$ is a closed point (II, Ex. 3.20). Since $Y$ is irreducible and $X$ is equidimensional, $\dim_x X = \dim X - \dim \overline{\{x\}}$ and $\dim_y Y = \dim Y - \dim \overline{\{y\}}$. Since $x$ is a closed point of the fibre $X_y$, $k(x)$ is a finite algebraic extension of $k(y)$ and so $\dim \overline{\{x\}} = \dim \overline{\{y\}}$. Combining these with (i) yields $\dim Z = n$.

(ii) $\Rightarrow$ (i): Let $Z$ be an irreducible component of $X$, and let $x \in Z$ be a closed point not contained in any other irreducible component of $X$. Then $\dim_x(X_y) = \dim_x X - \dim_y Y$ by (9.5). But $\dim_x(X_y) = n$ by (ii), $\dim_x X = \dim Z$, and $\dim_y Y = \dim Y$, yielding $\dim Z = \dim Y + n$.
