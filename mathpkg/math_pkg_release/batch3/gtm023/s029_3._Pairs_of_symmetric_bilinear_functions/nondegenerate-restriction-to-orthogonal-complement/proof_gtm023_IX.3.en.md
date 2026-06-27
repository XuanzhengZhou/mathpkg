---
role: proof
locale: en
of_concept: nondegenerate-restriction-to-orthogonal-complement
source_book: gtm023
source_chapter: "IX"
source_section: "§3, 9.15"
---

Since $\Psi$ is non-degenerate, $E_1$ has dimension $n-1$.

Assume that $z_1$ is a vector of $E_1$ such that
$$\Psi(z_1, z) = 0$$
for all vectors $z \in E_1$. We must show $z_1 = 0$.

Every vector $x \in E$ can be decomposed in the form
$$x = \xi e_1 + z, \quad z \in E_1.$$
Indeed, taking $\xi = \Psi(e_1, x) / \Psi(e_1, e_1)$ gives $z = x - \xi e_1 \in E_1$ since $\Psi(e_1, z) = \Psi(e_1, x) - \xi \Psi(e_1, e_1) = 0$.

Now compute $\Psi(z_1, x)$ for arbitrary $x \in E$:
$$\Psi(z_1, x) = \Psi(z_1, \xi e_1 + z) = \xi \Psi(z_1, e_1) + \Psi(z_1, z).$$

Since $z_1 \in E_1$, we have $\Psi(e_1, z_1) = 0$ (by symmetry of $\Psi$). And $\Psi(z_1, z) = 0$ for $z \in E_1$ by our assumption. Hence
$$\Psi(z_1, x) = 0 \quad \text{for all } x \in E.$$

The non-degeneracy of $\Psi$ on $E$ then forces $z_1 = 0$. Therefore the restriction of $\Psi$ to $E_1$ is non-degenerate.
