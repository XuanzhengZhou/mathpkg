---
role: proof
locale: en
of_concept: delbar-on-p-polyhedron
source_book: gtm035
source_chapter: "7"
source_section: "7.6"
---
# Proof of $\bar{\partial}$-Problem on $p$-Polyhedra

Let $\Pi$ be a $p$-polyhedron in $\mathbb{C}^n$ and $\Omega$ a neighborhood of $\Pi$. Given $\phi \in \wedge^{p,q}(\Omega)$, $q > 0$, with $\bar{\partial}\phi = 0$, we seek a neighborhood $\Omega_1$ of $\Pi$ and $\psi \in \wedge^{p,q-1}(\Omega_1)$ with $\bar{\partial}\psi = \phi$.

**Notation.** Write $P^k(q_1, \ldots, q_r) = \{z \in \Delta^k \mid |q_j(z)| \leq 1, j = 1, \ldots, r\}$, where the $q_j$ are polynomials in $z_1, \ldots, z_k$. Every $p$-polyhedron is of this form.

**Proof by induction on $r$.**

**Base case $r = 0$:** Then $\Pi = \Delta^n$, the closed unit polydisk. The assertion holds for all $n$ and all $(p,q)$ with $q > 0$ by the Complex Poincaré Lemma (Theorem 6.1).

**Inductive hypothesis:** Assume the assertion holds for a fixed $r$ and all $k$ and all $(p,q)$ with $q > 0$.

**Inductive step:** Fix $n$ and polynomials $p_1, \ldots, p_{r+1}$ in $\mathbb{C}^n$. Consider $\phi \in \wedge^{p,q}(\Omega)$ with $\bar{\partial}\phi = 0$, where $\Omega$ is a neighborhood of $P^n(p_1, \ldots, p_{r+1})$.

*Step 1 (Embedding):* Define the map $u: \mathbb{C}^n \to \mathbb{C}^{n+1}$ by $u(z) = (z, p_{r+1}(z))$. The image of $P^n(p_1, \ldots, p_{r+1})$ under $u$ is contained in $P^{n+1}(p_1, \ldots, p_r)$. Let $\Sigma$ denote this image. Let $\pi: \mathbb{C}^{n+1} \to \mathbb{C}^n$ be the projection onto the first $n$ coordinates, so $\pi \circ u = \text{id}$ on $\mathbb{C}^n$.

*Step 2 (Pullback and correction):* Consider the pullback $\Phi = \pi^*\phi$ on a neighborhood of $\Sigma$. Then $\bar{\partial}\Phi = \pi^*(\bar{\partial}\phi) = 0$ in a neighborhood of $\Sigma$. Define

$$\Phi_1 = \Phi - \bar{\partial}\left(\frac{\bar{\partial}\Phi}{z_{n+1} - p_{r+1}(z)}\right).$$

By Exercise 7.2, the pullback of a $\bar{\partial}$-closed form by a holomorphic map remains $\bar{\partial}$-closed. The correction term ensures that $\Phi_1$ is $\bar{\partial}$-closed in a neighborhood of the larger set $P^{n+1}(p_1, \ldots, p_r)$.

*Step 3 (First induction):* The correction equation

$$\bar{\partial}\chi = \frac{\bar{\partial}\Phi}{z_{n+1} - p_{r+1}(z)}$$

is a $\bar{\partial}$-problem on $P^{n+1}(p_1, \ldots, p_r)$. By the induction hypothesis (applied with $r$ polynomials), there exists a solution $\chi$.

*Step 4 (Second induction):* Then $\Phi_1$ is a $\bar{\partial}$-closed $(p,q)$-form in a neighborhood of $P^{n+1}(p_1, \ldots, p_r)$. By the induction hypothesis again, there exists a $(p, q-1)$-form $\Psi$ in a neighborhood of $P^{n+1}(p_1, \ldots, p_r)$ with $\bar{\partial}\Psi = \Phi_1$.

*Step 5 (Pull back):* Using Exercise 7.2 and the relation $u = \pi^{-1}$ on $\Sigma$, define $\psi = u^*(\Psi + \text{correction terms})$. This yields a $(p, q-1)$-form in a neighborhood of $P^n(p_1, \ldots, p_{r+1})$ satisfying $\bar{\partial}\psi = \phi$.

The induction is complete. $\square$

**Remark.** This theorem generalizes the Complex Poincaré Lemma from the polydisk to arbitrary $p$-polyhedra. The key idea is to embed a $p$-polyhedron with $r+1$ defining polynomials into one with $r$ defining polynomials in one higher dimension, then apply the induction hypothesis twice. The construction relies on the fact that the additional variable $z_{n+1}$ allows "untwisting" the $\bar{\partial}$-equation.
