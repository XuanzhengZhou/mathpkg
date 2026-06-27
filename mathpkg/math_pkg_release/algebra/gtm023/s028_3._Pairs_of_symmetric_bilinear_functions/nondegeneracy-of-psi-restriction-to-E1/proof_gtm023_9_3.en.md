---
role: proof
locale: en
of_concept: nondegeneracy-of-psi-restriction-to-E1
source_book: gtm023
source_chapter: "9"
source_section: "3. Pairs of symmetric bilinear functions"
---

Since $\Psi(e_1, e_1) \neq 0$, the linear functional $x \mapsto \Psi(e_1, x)$ is non-zero on $E$. Therefore $E_1 = \ker(\Psi(e_1, \cdot))$ is a proper subspace of codimension $1$, so $\dim E_1 = n-1$.

To show $\Psi|_{E_1}$ is non-degenerate, suppose $z_1 \in E_1$ satisfies $\Psi(z_1, z) = 0$ for all $z \in E_1$. We must show $z_1 = 0$.

Take any $x \in E$. Since $e_1 \notin E_1$ (because $\Psi(e_1, e_1) \neq 0$), every $x \in E$ can be decomposed as
$$x = \xi e_1 + z$$
with $z \in E_1$. Specifically, choose $\xi = \Psi(e_1, x)/\Psi(e_1, e_1)$ and $z = x - \xi e_1$, then $\Psi(e_1, z) = 0$ so $z \in E_1$.

Now
$$\Psi(z_1, x) = \Psi(z_1, \xi e_1 + z) = \xi \Psi(z_1, e_1) + \Psi(z_1, z).$$
Since $z_1 \in E_1$, we have $\Psi(z_1, e_1) = \Psi(e_1, z_1) = 0$ by definition of $E_1$. And $\Psi(z_1, z) = 0$ by our assumption (since $z \in E_1$). Hence $\Psi(z_1, x) = 0$ for all $x \in E$. By non-degeneracy of $\Psi$ on $E$, this forces $z_1 = 0$.

Thus $\Psi|_{E_1}$ is non-degenerate.
