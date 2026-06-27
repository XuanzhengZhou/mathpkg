---
role: proof
locale: en
of_concept: delbar-representation-lemma
source_book: gtm035
source_chapter: "14"
source_section: "14.5"
---
# Proof of $\bar{\partial}$ Representation Lemma for $C_0^1$

Let $\phi \in C_0^1(N)$ be a compactly supported $C^1$ function on the neighborhood $N$ of $X$. Fix $z \in N$. We must prove
$$
\phi(z) = -\frac{(n-1)!}{(2\pi i)^n} \int_N \bar{\partial}\phi(\zeta) \wedge K(\zeta, z).
$$

**Step 1: The kernel $K(\zeta, z)$ as a $\bar{\partial}$-closed form off the diagonal.** For fixed $z$, the Cauchy-Fantappiè kernel $K(\zeta, z)$ satisfies
$$
\bar{\partial}_\zeta K(\zeta, z) = 0, \quad \zeta \in N \setminus \{z\}.
$$
This follows from the construction of $K$ using the generating functions $w_j(\zeta, z)$ as in the Bochner-Martinelli theory; $K$ is the pullback of the Martinelli kernel under the map defined by the $H_j$.

**Step 2: Localization via excision.** Choose $\varepsilon > 0$ sufficiently small so that the closed ball $B_\varepsilon(z) = \{\zeta : |\zeta - z| \leq \varepsilon\}$ is contained in $N$. Let $D_\varepsilon = N \setminus B_\varepsilon(z)$. Apply Stokes' theorem to the form $\phi(\zeta) K(\zeta, z)$ on $D_\varepsilon$:
$$
\int_{D_\varepsilon} \bar{\partial}(\phi K) = \int_{\partial D_\varepsilon} \phi K.
$$

Since $\phi$ is compactly supported in $N$ and vanishes near $\partial N$, the boundary term consists only of the inner boundary $\partial B_\varepsilon(z)$ (with reversed orientation):
$$
\int_{\partial D_\varepsilon} \phi K = -\int_{|\zeta - z| = \varepsilon} \phi(\zeta) K(\zeta, z).
$$

On the other hand,
$$
\bar{\partial}(\phi K) = \bar{\partial}\phi \wedge K + (-1)^{\deg \phi} \phi \wedge \bar{\partial}K = \bar{\partial}\phi \wedge K,
$$
since $\bar{\partial}K = 0$ on $D_\varepsilon$.

Thus
$$
\int_{D_\varepsilon} \bar{\partial}\phi \wedge K = -\int_{|\zeta - z| = \varepsilon} \phi(\zeta) K(\zeta, z).
$$

**Step 3: Passing to the limit.** As $\varepsilon \to 0$, the left-hand side tends to $\int_N \bar{\partial}\phi \wedge K$ by dominated convergence (the singularity of $K$ is $O(|\zeta - z|^{-(2n-1)})$, which is integrable in $\mathbb{C}^n$).

For the right-hand side, the residue computation for the Cauchy-Fantappiè kernel (analogous to the Bochner-Martinelli formula; cf. Theorem 13.3 and Leray's formula) gives
$$
\lim_{\varepsilon \to 0} \int_{|\zeta - z| = \varepsilon} K(\zeta, z) = \frac{(2\pi i)^n}{(n-1)!}.
$$

Since $\phi$ is continuous, $\phi(\zeta) \to \phi(z)$ as $\zeta \to z$, and we obtain
$$
\lim_{\varepsilon \to 0} \int_{|\zeta - z| = \varepsilon} \phi(\zeta) K(\zeta, z) = \phi(z) \frac{(2\pi i)^n}{(n-1)!}.
$$

**Step 4: Conclusion.** Substituting back,
$$
\int_N \bar{\partial}\phi \wedge K = -\phi(z) \frac{(2\pi i)^n}{(n-1)!},
$$
or equivalently,
$$
\phi(z) = -\frac{(n-1)!}{(2\pi i)^n} \int_N \bar{\partial}\phi(\zeta) \wedge K(\zeta, z).
$$

$\square$
