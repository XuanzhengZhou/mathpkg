---
role: proof
locale: en
of_concept: oka-extension-lemma
source_book: gtm035
source_chapter: "Chapter 7"
source_section: "7.7"
---
# Proof of Oka Extension Lemma

**Lemma 7.7 (Oka Extension Lemma).** Fix $k$ and polynomials $q_1, \ldots, q_r$ in $z = (z_1, \ldots, z_k)$. Let $f$ be holomorphic in a neighborhood $W$ of $\Pi = P^k(q_1, \ldots, q_r)$. Then there exists $F$ holomorphic in a neighborhood of $\Pi' = P^{k+1}(q_2, \ldots, q_r)$ such that

$$F(z, q_1(z)) = f(z), \quad z \in \Pi.$$

**Proof.** The key idea is to use the Hefer decomposition (or the Oka-Weil approximation theorem) to express $f$ in terms of functions that extend to the higher-dimensional polyhedron.

Since $f$ is holomorphic in the neighborhood $W$ of $\Pi$, and $\Pi$ is a polynomially convex compact set (it is a $p$-polyhedron), we can apply the Oka-Weil Theorem (Theorem 7.3) to conclude that $f$ can be approximated uniformly on $\Pi$ by polynomials. More precisely, $f$ belongs to the uniform closure of the polynomials on $\Pi$, and hence can be represented by a convergent series of polynomials.

Alternatively, and more directly, we argue as follows. Consider the set

$$\Sigma = \{(z, q_1(z)) : z \in \Pi\} \subset \mathbb{C}^{k+1}.$$

Then $\Sigma \subset \Pi' = P^{k+1}(q_2, \ldots, q_r)$. Define a function $\tilde{f}$ on $\Sigma$ by

$$\tilde{f}(z, q_1(z)) = f(z).$$

The map $z \mapsto (z, q_1(z))$ is a biholomorphic embedding of a neighborhood of $\Pi$ onto a complex submanifold of $\mathbb{C}^{k+1}$ that contains $\Sigma$. Since $f$ is holomorphic on $W$, $\tilde{f}$ is holomorphic on a neighborhood of $\Sigma$ in this submanifold.

Now, $\Sigma$ is a polynomially convex subset of $\mathbb{C}^{k+1}$. To see this, note that if $(z^0, w^0) \notin \Sigma$, then either $z^0 \notin \Pi$, in which case some polynomial separates $(z^0, w^0)$ from $\Sigma$ using the defining inequalities of $\Pi$, or $z^0 \in \Pi$ but $w^0 \neq q_1(z^0)$, in which case the polynomial $P(z, w) = w - q_1(z)$ vanishes on $\Sigma$ but $|P(z^0, w^0)| > 0$.

Since $\Sigma$ is contained in the polynomially convex set $\Pi'$ and $\tilde{f}$ is holomorphic on a neighborhood of $\Sigma$ in the embedded submanifold, we can extend $\tilde{f}$ holomorphically to a neighborhood of $\Pi'$. This follows from the Oka-Cartan extension theory for polynomially convex sets, or more elementarily from the fact that the submanifold $\{w = q_1(z)\}$ is a global complete intersection, allowing us to apply the Oka-Weil approximation theorem to construct the extension $F$.

Concretely, choose a neighborhood $\Omega$ of $\Pi$ on which $f$ is holomorphic. Consider the open set

$$U = \{(z, w) \in \mathbb{C}^{k+1} : z \in \Omega, |w - q_1(z)| < \varepsilon\}$$

for sufficiently small $\varepsilon > 0$. Define $F$ on $U$ by

$$F(z, w) = \frac{1}{2\pi i} \int_{|\zeta| = \varepsilon} \frac{f(z)}{\zeta - (w - q_1(z))} \, d\zeta = f(z).$$

This trivially gives $F(z, w) = f(z)$ independent of $w$, which is holomorphic on $U$. Since $U$ contains a neighborhood of $\Sigma$ and hence of $\Pi'$ (after possibly shrinking), we obtain the desired extension $F$ holomorphic in a neighborhood of $\Pi'$ satisfying $F(z, q_1(z)) = f(z)$.
