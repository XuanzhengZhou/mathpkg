---
role: proof
locale: en
of_concept: oka-extension-theorem
source_book: gtm035
source_chapter: "7"
source_section: "7.5"
---
# Proof of Oka Extension Theorem

Let $\Pi = P^n(p_1, \ldots, p_r)$ be a $p$-polyhedron. Let $f$ be holomorphic in a neighborhood of $\Pi$.

We prove the theorem by induction on $r$, the number of defining polynomials. The assertion $A(j)$ for $1 \leq j \leq r$ is:

$$A(j): \exists F_j \text{ holomorphic in a neighborhood of } P^{n+j}(p_{j+1}, \ldots, p_r)$$

such that $F_j(z, p_1(z), \ldots, p_j(z)) = f(z)$, all $z \in \Pi$.

**Base case:** $A(1)$ holds by Lemma 7.7 (Oka Extension Lemma), which provides $F_1$ holomorphic in a neighborhood of $P^{n+1}(p_2, \ldots, p_r)$ with $F_1(z, p_1(z)) = f(z)$.

**Inductive step:** Assume $A(j)$ holds for some $j \geq 1$. Thus $F_j$ is holomorphic in a neighborhood of $P^{n+j}(p_{j+1}, \ldots, p_r)$ with

$$F_j(z, p_1(z), \ldots, p_j(z)) = f(z), \quad \text{all } z \in \Pi.$$

Now apply Lemma 7.7 to $F_j$ as a function of the variables $\zeta = (z, z_{n+1}, \ldots, z_{n+j})$ on the $p$-polyhedron $P^{n+j}(p_{j+1}, \ldots, p_r)$, with $p_{j+1}$ playing the role of $q_1$. This yields $F_{j+1}$ holomorphic in a neighborhood of $P^{n+j+1}(p_{j+2}, \ldots, p_r)$ with

$$F_{j+1}(\zeta, p_{j+1}(z)) = F_j(\zeta), \quad \zeta \in P^{n+j}(p_{j+1}, \ldots, p_r).$$

Substituting $\zeta = (z, p_1(z), \ldots, p_j(z))$, we obtain

$$F_{j+1}(z, p_1(z), \ldots, p_j(z), p_{j+1}(z)) = F_j(z, p_1(z), \ldots, p_j(z)) = f(z).$$

Thus $A(j+1)$ holds.

By induction, $A(r)$ holds, giving $F = F_r$ holomorphic in a neighborhood of $P^{n+r}(\emptyset) = \Delta^{n+r}$ such that

$$F(z, p_1(z), \ldots, p_r(z)) = f(z), \quad \text{all } z \in \Pi.$$

This completes the proof. $\square$
