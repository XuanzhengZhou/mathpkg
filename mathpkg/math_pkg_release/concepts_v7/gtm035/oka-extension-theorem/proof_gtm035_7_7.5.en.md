---
role: proof
locale: en
of_concept: oka-extension-theorem
source_book: gtm035
source_chapter: "Chapter 7"
source_section: "7.5"
---
# Proof of Oka Extension Theorem

**Theorem 7.5 (Oka Extension Theorem).** Let $\Pi = P^n(p_1, \ldots, p_r)$ be a $p$-polyhedron in $\mathbb{C}^n$, where $p_1, \ldots, p_r$ are polynomials. Let $f$ be holomorphic in a neighborhood of $\Pi$. Then there exists $F$ holomorphic in a neighborhood of $\Delta^{n+r}$ such that

$$F(z, p_1(z), \ldots, p_r(z)) = f(z)$$

for all $z \in \Pi$.

**Proof.** We proceed by induction on $r$, the number of defining polynomials.

For $r = 0$, $\Pi = \Delta^n$ and the result is trivial with $F(z) = f(z)$, as $f$ is holomorphic in a neighborhood of $\Delta^n$.

Assume the result holds for some $r$ and all $n$. We prove the assertion $A(j)$ for $j = 1, \ldots, r+1$:

$$A(j): \exists\, F_j \text{ holomorphic in a neighborhood of } P^{n+j}(p_{j+1}, \ldots, p_{r+1})$$

such that $F_j(z, p_1(z), \ldots, p_j(z)) = f(z)$ for all $z \in \Pi$.

**Base case $A(1)$:** Apply Lemma 7.7 with $k = n$, $q_1 = p_1$, and $q_2, \ldots, q_r = p_2, \ldots, p_r$. The function $f$ is holomorphic in a neighborhood of $\Pi = P^n(p_1, \ldots, p_r)$. By Lemma 7.7, there exists $F_1$ holomorphic in a neighborhood of $P^{n+1}(p_2, \ldots, p_r)$ such that

$$F_1(z, p_1(z)) = f(z), \quad z \in \Pi.$$

Thus $A(1)$ holds.

**Inductive step:** Assume $A(j)$ holds for some $j < r+1$. Then $F_j$ is holomorphic in a neighborhood of $P^{n+j}(p_{j+1}, \ldots, p_{r+1})$. Apply Lemma 7.7 to $F_j$ with the polynomial $p_{j+1}$:

Write $F_j$ as a function of $\zeta = (z, z_{n+1}, \ldots, z_{n+j}) \in \mathbb{C}^{n+j}$ holomorphic in a neighborhood of $P^{n+j}(p_{j+1}, \ldots, p_{r+1})$. By Lemma 7.7, there exists $F_{j+1}$ holomorphic in a neighborhood of $P^{n+j+1}(p_{j+2}, \ldots, p_{r+1})$ with

$$F_{j+1}(\zeta, p_{j+1}(\zeta)) = F_j(\zeta).$$

By the induction hypothesis, $F_j(z, p_1(z), \ldots, p_j(z)) = f(z)$. Hence

$$F_{j+1}(z, p_1(z), \ldots, p_j(z), p_{j+1}(z)) = f(z),$$

which is precisely $A(j+1)$.

By induction, $A(1), A(2), \ldots, A(r+1)$ all hold. The statement $A(r+1)$ provides $F = F_{r+1}$ holomorphic in a neighborhood of $P^{n+r+1}(\varnothing) = \Delta^{n+r+1}$ satisfying

$$F(z, p_1(z), \ldots, p_{r+1}(z)) = f(z)$$

for all $z \in \Pi = P^n(p_1, \ldots, p_{r+1})$. This completes the proof.
