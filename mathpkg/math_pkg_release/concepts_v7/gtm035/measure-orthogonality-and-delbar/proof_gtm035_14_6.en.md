---
role: proof
locale: en
of_concept: measure-orthogonality-and-delbar
source_book: gtm035
source_chapter: "14"
source_section: "14.6"
---
# Proof of Measure Orthogonality and the $\bar{\partial}$-Operator

Let $\mu$ be a finite measure on $X$ with $\mu \perp \mathfrak{A}$. Fix $z \in N$ such that
$$
\int_X \frac{d|\mu|(\zeta)}{|\zeta - z|^{2n-1}} < \infty.
$$
We must show that $\int_X K_j(\zeta, z) \, d\mu(\zeta) = 0$ for each $j = 1, \ldots, n$.

**Step 1: Approximation of the kernel.** For each fixed $z$, the functions $K_j(\cdot, z)$ are $C^\infty$ on $N \setminus \{z\}$ and satisfy the growth estimate
$$
|K_j(\zeta, z)| \leq \frac{C}{|\zeta - z|^{2n-1}}
$$
established in the Claim (inequality (19)) preceding the statement of the lemma.

Since the measure $\mu$ satisfies the integrability condition, $K_j(\cdot, z) \in L^1(|\mu|)$.

**Step 2: Using the algebra $\mathfrak{A}$.** Recall that
$$
\mathfrak{A} = [z_1, \ldots, z_n, \bar{z}_1 + R_1, \ldots, \bar{z}_n + R_n].
$$
The key observation is that for each fixed $z$, the functions $\zeta \mapsto H_j(\zeta, z)$ belong to $\mathfrak{A}$ (as functions of $\zeta$). Indeed, each $H_j(\zeta, z) = \bar{\zeta}_j + R_j(\zeta) - (\bar{z}_j + R_j(z))$ is built from elements of $\mathfrak{A}$ by addition of a constant (in $z$), and $G(\zeta, z)$ is also constructed from elements of $\mathfrak{A}$.

Moreover, $1/G(\zeta, z)^n$ can be approximated uniformly on the compact set $X$ (avoiding $z$) by polynomials in the functions generating $\mathfrak{A}$, using the fact that $\operatorname{Re} G(\zeta, z) > 0$ and $|G(\zeta, z)| \geq (1-k)|\zeta - z|^2 > 0$ on $X \setminus \{z\}$ (from inequalities (17) and (18)). By Runge-type approximation in the right half-plane, $1/w^n$ can be approximated by polynomials in $w$ on the compact set $G(X, z) \subset \{\operatorname{Re} w > 0\}$.

**Step 3: Vanishing of the integrals.** Since each $K_j(\cdot, z)$ is a limit, uniformly on compact subsets of $X \setminus \{z\}$, of functions in $\mathfrak{A}$ (or more precisely, of products of elements of $\mathfrak{A}$ with approximating polynomials), and $\mu \perp \mathfrak{A}$, we conclude that for the approximating functions $f_m \in \mathfrak{A}$ with $f_m \to K_j(\cdot, z)$ pointwise on $X \setminus \{z\}$,
$$
\int_X f_m(\zeta) \, d\mu(\zeta) = 0.
$$

By the integrability condition and the estimate (19),
$$
|f_m(\zeta)| \leq \frac{C'}{|\zeta - z|^{2n-1}},
$$
with a uniform constant $C'$. Since $|\zeta - z|^{-(2n-1)} \in L^1(|\mu|)$ by hypothesis, dominated convergence yields
$$
\int_X K_j(\zeta, z) \, d\mu(\zeta) = \lim_{m \to \infty} \int_X f_m(\zeta) \, d\mu(\zeta) = 0.
$$

Thus $\int_X K_j(\zeta, z) d\mu(\zeta) = 0$ for every $j = 1, \ldots, n$, completing the proof.

$\square$
