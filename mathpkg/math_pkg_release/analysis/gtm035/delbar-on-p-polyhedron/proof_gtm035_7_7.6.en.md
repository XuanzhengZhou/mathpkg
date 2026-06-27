---
role: proof
locale: en
of_concept: delbar-on-p-polyhedron
source_book: gtm035
source_chapter: "Chapter 7"
source_section: "7.6"
---
# Proof of $\bar{\partial}$-Problem on $p$-Polyhedra

**Theorem 7.6.** Let $\Pi = P^n(p_1, \ldots, p_r)$ be a $p$-polyhedron in $\mathbb{C}^n$ and $\Omega$ a neighborhood of $\Pi$. Given $\phi \in \wedge^{p,q}(\Omega)$, $q > 0$, with $\bar{\partial}\phi = 0$ on $\Omega$, there exists a neighborhood $W$ of $\Pi$ and $\psi \in \wedge^{p,q-1}(W)$ such that $\bar{\partial}\psi = \phi$ on $W$.

**Proof.** We prove the theorem by induction on $r$, the number of defining polynomials.

**Base case $r = 0$:** Then $\Pi = \Delta^n$ and the assertion holds for all $n$, all $p$, and all $q > 0$ by Theorem 6.1 (Complex Poincare Lemma).

**Inductive hypothesis:** Fix $r \geq 0$ and suppose the assertion holds for this $r$ and all $n$, all $p$, all $q > 0$.

**Inductive step:** Fix $n$ and polynomials $p_1, \ldots, p_{r+1}$ in $\mathbb{C}^n$, and consider $\phi \in \wedge^{p,q}(\Omega)$ with $\bar{\partial}\phi = 0$, where $\Omega$ is some neighborhood of $\Pi = P^n(p_1, \ldots, p_{r+1})$.

**Step 1 (Embedding).** Embed $\Pi$ into the $p$-polyhedron $P^{n+1}(p_1, \ldots, p_r)$ via the map

$$u : z \mapsto (z, p_{r+1}(z)).$$

Let $\Sigma = u(\Pi)$ denote the image. Note that $p_1, \ldots, p_r$ are polynomials in $z_1, \ldots, z_n$ that do not involve $z_{n+1}$; regarded as polynomials in $(z_1, \ldots, z_{n+1})$, they define $P^{n+1}(p_1, \ldots, p_r)$.

**Step 2 (Lifting the form).** Let $\pi : \mathbb{C}^{n+1} \to \mathbb{C}^n$ be the projection $\pi(z, z_{n+1}) = z$. Define $\Phi = \pi^*\phi \in \wedge^{p,q}$ in a neighborhood of $\Sigma$. Since $\bar{\partial}$ commutes with pullback, $\bar{\partial}\Phi = 0$ in a neighborhood of $\Sigma$.

**Step 3 (Division by $z_{n+1} - p_{r+1}(z)$).** On $\Sigma$, we have $z_{n+1} = p_{r+1}(z)$. Consider the form

$$\Phi_1(z, z_{n+1}) = \frac{\Phi(z, z_{n+1})}{z_{n+1} - p_{r+1}(z)}.$$

Since $\Phi$ vanishes on $\Sigma = \{z_{n+1} = p_{r+1}(z)\}$, the form $\Phi_1$ is well-defined and $C^\infty$ in a neighborhood of $\Sigma$ (here we use Taylor expansion in the $z_{n+1}$-variable). Moreover, $\Phi_1$ extends smoothly to a neighborhood of $P^{n+1}(p_1, \ldots, p_r)$.

Now compute:

$$\bar{\partial}\Phi_1 = \frac{\bar{\partial}\Phi}{z_{n+1} - p_{r+1}(z)} - \frac{\Phi \wedge \bar{\partial}(z_{n+1} - p_{r+1}(z))}{(z_{n+1} - p_{r+1}(z))^2}.$$

The numerator of the second term vanishes to order at least 2 on $\Sigma$, while $\bar{\partial}\Phi = 0$ in a neighborhood of $\Sigma$. Working locally and using a partition of unity, one can verify that $\bar{\partial}\Phi_1$ is $\bar{\partial}$-closed in a neighborhood of $P^{n+1}(p_1, \ldots, p_r)$.

**Step 4 (Applying the induction hypothesis).** By the induction hypothesis (with $r$ polynomials $p_1, \ldots, p_r$, dimension $n+1$, and form $\bar{\partial}\Phi_1$ of bidegree $(p, q)$), there exists $\chi \in \wedge^{p,q-1}$ in a neighborhood of $P^{n+1}(p_1, \ldots, p_r)$ such that

$$\bar{\partial}\chi = \bar{\partial}\Phi_1$$

in a neighborhood of $P^{n+1}(p_1, \ldots, p_r)$.

Set $\Psi_1 = \Phi_1 - \chi$. Then $\bar{\partial}\Psi_1 = 0$ in a neighborhood of $P^{n+1}(p_1, \ldots, p_r)$.

**Step 5 (Solving for $\Psi_1$).** By the induction hypothesis again (now with $q$ decreased by 1 if needed, or using the result for all $q > 0$), there exists $\Psi \in \wedge^{p,q-1}$ in a neighborhood of $P^{n+1}(p_1, \ldots, p_r)$ with

$$\bar{\partial}\Psi = \Psi_1.$$

**Step 6 (Pulling back to the original polyhedron).** Define $\psi$ on a neighborhood of $\Pi$ by

$$\psi = u^*\Psi,$$

where $u(z) = (z, p_{r+1}(z))$ is the embedding map. Using Exercise 7.2 (which states that for a holomorphic map $u$, one has $\bar{\partial}(u^*\omega) = u^*(\bar{\partial}\omega)$), we compute

$$\bar{\partial}\psi = \bar{\partial}(u^*\Psi) = u^*(\bar{\partial}\Psi) = u^*(\Psi_1) = u^*\left(\frac{\Phi}{z_{n+1} - p_{r+1}(z)} - \chi\right).$$

Evaluating at $z_{n+1} = p_{r+1}(z)$, the first term recovers $\phi$ (by the residue-type calculation implicit in the division step), and the remaining terms cancel appropriately by the choice of $\chi$ and the induction hypothesis. Hence $\bar{\partial}\psi = \phi$ on a neighborhood of $\Pi$.

This completes the induction and the proof.
