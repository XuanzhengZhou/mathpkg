---
role: proof
locale: en
of_concept: complex-algebraic-curve-connected
source_book: gtm044
source_chapter: "II"
source_section: "8"
---

# Proof of Connectedness of Complex Algebraic Curves (Theorem 8.4)

**Theorem 8.4.** Any complex algebraic curve $C \subset \mathbb{P}^2(\mathbb{C})$ is connected.

*Proof.* Let $C \subset \mathbb{P}^2(\mathbb{C})$ be defined by the homogeneous polynomial $q(X, Y, Z) \in \mathbb{C}[X, Y, Z]$. Factor $q$ into irreducibles:

$$q = q_1^{r_1} q_2^{r_2} \cdots q_k^{r_k},$$

so that $C = V(q) = V(q_1) \cup V(q_2) \cup \cdots \cup V(q_k)$. Each $C_i = V(q_i)$ is an irreducible projective curve. By the dimension theorem (Theorem 6.1), any two distinct projective curves in $\mathbb{P}^2(\mathbb{C})$ intersect. Hence $C_i \cap C_j \neq \emptyset$ for all $i, j$. By Lemma 8.2, if each $C_i$ is connected, then their union $C$ is also connected. Thus it suffices to prove the theorem for an irreducible curve.

**Reduction to the affine case.** Assume therefore that $q$ is irreducible. Choose a projective line $L \subset \mathbb{P}^2(\mathbb{C})$ that intersects $C$ but does not contain $C$ (for instance, the line $Z = 0$ does not contain $C$ unless $C$ itself is the line $Z = 0$, in which case $C \cong \mathbb{P}^1(\mathbb{C})$ is clearly connected). By dehomogenizing with respect to $Z$, we obtain an irreducible affine curve $V(p) \subset \mathbb{C}_{XY}$ where $p(X, Y) = q(X, Y, 1)$. The complement $C \setminus V(p)$ consists of the finitely many points of $C$ lying on the line $Z = 0$. Since a finite set does not affect connectedness (adding finitely many limit points to a connected set keeps it connected), it suffices to prove that the affine curve $V(p)$ is connected.

**The discriminant locus and the branched cover.** Since $p(X, Y)$ is irreducible, after a linear change of coordinates (if necessary) we may assume $p$ is monic in $Y$ of degree $n = \deg_Y p$. Let $\mathcal{D} \subset \mathbb{C}_X$ be the discriminant locus of $p$ with respect to $Y$—the set of $x \in \mathbb{C}$ for which $p(x, Y)$ has fewer than $n$ distinct roots. Since $p$ has no repeated factors, $\mathcal{D}$ consists of finitely many points (the zeros of the discriminant $\Delta_Y(p)$). Consider the branched cover

$$\pi_Y: V(p) \setminus \pi_Y^{-1}(\mathcal{D}) \longrightarrow \mathbb{C} \setminus \mathcal{D},$$

where $\pi_Y(X, Y) = X$ is projection onto the first coordinate. Above each point $x \in \mathbb{C} \setminus \mathcal{D}$, the fiber $\pi_Y^{-1}(x)$ consists of exactly $n$ distinct points. By the Implicit Function Theorem (Theorem 3.6), this is an $n$-sheeted covering space in the analytic topology.

**Analytic function elements and chains.** Near each point $x_0 \in \mathbb{C} \setminus \mathcal{D}$, there is a connected open neighborhood $\mathcal{O}$ that is evenly covered: $\pi_Y^{-1}(\mathcal{O})$ is a disjoint union of $n$ open sets, each projecting homeomorphically onto $\mathcal{O}$. Each such sheet is the graph of a holomorphic function $y = \sigma(x)$ defined on $\mathcal{O}$, called an *analytic function element*. We denote such an element by $\mathcal{Q}$.

Let $\mathcal{O}_1, \ldots, \mathcal{O}_m$ be connected open subsets of $\mathbb{C} \setminus \mathcal{D}$. A *chain* is a sequence $(\mathcal{O}_1, \ldots, \mathcal{O}_m)$ such that $\mathcal{O}_i \cap \mathcal{O}_{i+1}$ is connected and nonempty for $i = 1, \ldots, m-1$. A chain $(\mathcal{Q}_1, \ldots, \mathcal{Q}_m)$ of analytic function elements lifts the chain $(\mathcal{O}_1, \ldots, \mathcal{O}_m)$ if each $\mathcal{Q}_i$ is a lifting of $\mathcal{O}_i$ and $\mathcal{Q}_i |_{\mathcal{O}_i \cap \mathcal{O}_{i+1}} = \mathcal{Q}_{i+1} |_{\mathcal{O}_i \cap \mathcal{O}_{i+1}}$. This is called *analytic continuation* along the chain.

An open set $\mathcal{O} \subset \mathbb{C} \setminus \mathcal{D}$ is called *allowable* if it is evenly covered by $\pi_Y$ (i.e., $\pi_Y^{-1}(\mathcal{O})$ consists of $n$ disjoint sheets). By definition, small connected open sets are allowable.

**Key lemma (Lemma 8.13).** Any simply connected open subset of $\mathbb{C} \setminus \mathcal{D}$ is allowable. This follows from the Monodromy Theorem (Theorem 8.14): if we analytically continue an analytic function element along any closed polygonal path in a simply connected domain, we return to the same element. Hence the $n$ sheets cannot be permuted by continuation in a simply connected set, so the set is allowable.

**Strategy of the proof.** We proceed by showing that any two points $P, Q \in V(p)$ can be connected by a chain of analytic function elements, and therefore lie in the same connected component. Since $V(p)$ is locally connected, this implies $V(p)$ is connected.

Choose a finite set $\Phi \subset \mathbb{C} \setminus \mathcal{D}$ large enough so that for each connected component $F_1, \ldots, F_n$ of $\pi_Y^{-1}(\mathbb{C} \setminus \Phi)$ (there are finitely many such components because $\pi_Y^{-1}(\mathbb{C} \setminus \Phi)$ is a finite-sheeted cover over the finitely punctured plane), each $F_i$ is connected. The set $\mathbb{C} \setminus \Phi$ is connected and acts as a "base" for chain constructions.

**Constructing the chain between two arbitrary points.** Let $P, Q \in V(p)$. We may assume $\pi_Y(P), \pi_Y(Q) \in \mathbb{C} \setminus \Phi$ (by moving slightly if needed, since $V(p)$ is locally path-connected). Let $P \in F_i$ and $Q \in F_j$ for some components of $\pi_Y^{-1}(\mathbb{C} \setminus \Phi)$.

Consider analytic continuation along polygonal paths in $\mathbb{C} \setminus \mathcal{D}$. By a standard argument in covering space theory and the Riemann Extension Theorem (Theorem 4.12), the symmetric functions $\sigma_1, \ldots, \sigma_n$ of the $n$ sheets extend to entire functions on $\mathbb{C}$. Moreover, by analyzing the behavior at infinity (setting $X = 1/X'$ and examining the growth), these symmetric functions are bounded by polynomials, hence are polynomials by Liouville's theorem.

The polynomial $\prod_{j=1}^n (Y - \sigma_j(X))$ must equal $p(X, Y)$ (up to a constant factor), since they have the same zero set. This shows that the coefficients of $p(X, Y)$ as a polynomial in $Y$ are polynomials in $X$, which is consistent with $p \in \mathbb{C}[X, Y]$.

Now, the analytic continuation of a sheet along a closed path in $\mathbb{C} \setminus \mathcal{D}$ permutes the $n$ sheets by some permutation. The set of all allowable chains in $\mathbb{C} \setminus \mathcal{D}$ from $\mathbb{C} \setminus \Phi$ to $\mathbb{C} \setminus \Phi$ defines a group of permutations acting on the set $\{F_1, \ldots, F_n\}$.

**Connectedness argument.** Suppose for contradiction that $P$ and $Q$ lie in different connected components of $V(p)$. Then no allowable chain can connect them, meaning the permutation group defined above is not transitive. This would imply that the set $\{F_1, \ldots, F_n\}$ splits into at least two orbits under the action of the monodromy group, corresponding to the connected components of $V(p)$. But then the symmetric functions would factor, contradicting the irreducibility of $p(X, Y)$. (A nontrivial factorization of the symmetric functions would yield a factorization of $p$.)

Therefore, any two points $P, Q \in V(p)$ can be connected by an allowable chain, so $V(p)$ is connected.

**Returning to the projective case.** We have shown $V(p) \subset \mathbb{C}_{XY}$ is connected. Its closure in $\mathbb{P}^2(\mathbb{C})$ is $C$, and by Lemma 8.3, the closure of a connected set is connected. Hence $C$ is connected. $\square$
