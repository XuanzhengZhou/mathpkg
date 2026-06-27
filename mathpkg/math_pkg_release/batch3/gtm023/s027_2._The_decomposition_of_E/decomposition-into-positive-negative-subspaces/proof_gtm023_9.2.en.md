---
role: proof
locale: en
of_concept: decomposition-into-positive-negative-subspaces
source_book: gtm023
source_chapter: "9"
source_section: "2. The decomposition of E"
---

Since $\Phi$ is indefinite, there exists at least one vector $a$ with $\Phi(a) > 0$, so nontrivial positive definite subspaces exist. Let $E^+$ be a subspace of maximal dimension such that $\Phi$ is positive definite on $E^+$.

Define $E^-$ as the orthogonal complement of $E^+$ with respect to the scalar product defined by $\Phi$:
$$E^- = \{ y \in E : \Phi(x, y) = 0 \text{ for all } x \in E^+ \}.$$

Since $\Phi$ is positive definite on $E^+$, the intersection $E^+ \cap E^-$ consists only of the zero vector (if $x \in E^+ \cap E^-$ and $x \neq 0$, then $\Phi(x, x) > 0$ by positive definiteness, but $\Phi(x, x) = 0$ since $x \perp E^+$). Moreover, by Proposition II (the dimension relation for orthogonal complements of non-degenerate subspaces),

$$\dim E^+ + \dim E^- = \dim E.$$

Together with $E^+ \cap E^- = \{0\}$, this yields the direct sum decomposition
$$E = E^+ \oplus E^-.$$

Now we show $\Phi$ is negative definite on $E^-$. First, we argue $\Phi$ is negative semidefinite on $E^-$: if there existed $z \in E^-$ with $\Phi(z) > 0$, then the subspace $E_1$ spanned by $E^+ \cup \{z\}$ would be positive definite (since $z \perp E^+$), contradicting the maximality of $\dim E^+$.

Thus $\Phi(z) \leq 0$ for all $z \in E^-$. To prove negative definiteness, suppose $z_1 \in E^-$ satisfies $\Phi(z_1) = 0$. By the Schwarz inequality, for all $z \in E^-$:
$$\Phi(z_1, z)^2 \leq \Phi(z_1) \Phi(z) = 0,$$
so $\Phi(z_1, z) = 0$ for all $z \in E^-$. Since $z_1 \in E^-$, we also have $\Phi(z_1, y) = 0$ for all $y \in E^+$. As $E = E^+ \oplus E^-$, this implies $\Phi(z_1, x) = 0$ for all $x \in E$, so $z_1$ is in the nullspace. But $\Phi$ is non-degenerate, so $z_1 = 0$. Therefore $\Phi(z) < 0$ for all nonzero $z \in E^-$.
