---
role: proof
locale: en
of_concept: characterization-of-complex-hyperplane
source_book: gtm015
source_chapter: "III. Topological Vector Spaces"
source_section: "21. Hyperplanes and linear forms"
---

# Proof of Equivalent Characterizations of Complex Hyperplanes

Let $E$ be a vector space over $\mathbb{C}$. By restricting scalar multiplication, $E$ is also regarded as a vector space over $\mathbb{R}$. The terms $\mathbb{C}$-hyperplane and $\mathbb{R}$-hyperplane are self-explanatory.

**Theorem 21.15.** The following conditions on a subset $H$ of $E$ are equivalent:

**(a)** $H$ is a $\mathbb{C}$-hyperplane;

**(b)** there exist a maximal $\mathbb{R}$-linear subspace $M_0$ of $E$ and vectors $x_0, y_0 \in E$ such that $H = (x_0 + M_0) \cap (y_0 + iM_0)$;

**(c)** there exist a maximal $\mathbb{R}$-linear subspace $M_0$ of $E$ and a vector $z_0 \in E$ such that $H = z_0 + (M_0 \cap iM_0)$.

*Proof.*

**(c) $\iff$ (a):** The sets $M_0 \cap iM_0$ described in (c) are precisely the maximal $\mathbb{C}$-linear subspaces of $E$, by Lemma 21.14. Their translates are therefore the $\mathbb{C}$-hyperplanes, by Theorem 21.7. Thus (c) and (a) are equivalent.

**(c) $\Rightarrow$ (b):** Since translation by $z_0$ is a bijection that distributes over intersection,

$$z_0 + (M_0 \cap iM_0) = (z_0 + M_0) \cap (z_0 + iM_0).$$

Thus one may take $x_0 = y_0 = z_0$ in (b).

**(b) $\Rightarrow$ (c):** Suppose $H$ has the form described in (b), i.e.,

$$H = (x_0 + M_0) \cap (y_0 + iM_0).$$

Let $g$ be an $\mathbb{R}$-linear form on $E$ with null space $M_0$ (Theorem 21.3). By Theorem 21.13, the formula $f(x) = g(x) - ig(ix)$ defines a $\mathbb{C}$-linear form $f$ on $E$ with $\operatorname{Re} f = g$. Set

$$\lambda = g(x_0) - ig(iy_0).$$

We compute the set $\{x \in E : f(x) = \lambda\}$:

$$f(x) = \lambda \iff g(x) - ig(ix) = g(x_0) - ig(iy_0)$$
$$\iff g(x) = g(x_0) \text{ and } g(ix) = g(iy_0) \quad \text{(comparing real and imaginary parts)}$$
$$\iff x - x_0 \in M_0 \text{ and } ix - iy_0 \in M_0$$
$$\iff x \in x_0 + M_0 \text{ and } x \in y_0 + iM_0$$
$$\iff x \in (x_0 + M_0) \cap (y_0 + iM_0) = H.$$

Thus $H = \{x \in E : f(x) = \lambda\}$, which is a $\mathbb{C}$-hyperplane by Theorem 21.7. Setting $z_0$ to be any element of $H$ (e.g., $z_0 = x_0$, noting that $x_0 \in x_0 + M_0$ and also $y_0 + iM_0 = x_0 + iM_0$ after some translation adjustment), we obtain the form described in (c).

Consequently, all three conditions are equivalent.
