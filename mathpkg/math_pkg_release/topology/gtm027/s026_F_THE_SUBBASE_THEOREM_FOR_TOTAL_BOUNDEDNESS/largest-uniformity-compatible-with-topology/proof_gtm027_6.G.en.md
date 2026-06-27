---
role: proof
locale: en
of_concept: largest-uniformity-compatible-with-topology
source_book: gtm027
source_chapter: "6"
source_section: "G"
---

# Proof of Largest Uniformity Compatible with Topology

Let $(X, \mathfrak{t})$ be a completely regular space. We construct the largest uniformity $\mathfrak{u}^*$ on $X$ whose topology is $\mathfrak{t}$.

**Construction.** Define $\mathfrak{u}^*$ to be the family of all subsets $V \subset X \times X$ such that:
1. $V$ is a neighborhood of the diagonal $\Delta = \{(x,x) : x \in X\}$ in $X \times X$ (with respect to the product topology $\mathfrak{t} \times \mathfrak{t}$),
2. There exists a sequence $\{V_n : n \in \omega\}$ of symmetric neighborhoods of $\Delta$ such that $V_0 \subset V$ and $V_{n+1} \circ V_{n+1} \subset V_n$ for all $n \in \omega$.

**Verification that $\mathfrak{u}^*$ is a uniformity.** We check the uniformity axioms:

- *Contains the diagonal:* Each $V \in \mathfrak{u}^*$ is a neighborhood of $\Delta$, so $\Delta \subset V$.
- *Symmetry:* If $V \in \mathfrak{u}^*$ with sequence $\{V_n\}$, then $V^{-1}$ is also a neighborhood of $\Delta$. Since each $V_n$ is symmetric, the same sequence works with $V_0 \subset V$ replaced by symmetry considerations; alternatively, replace $V_0$ by $V_0 \cap V^{-1}$ and use the symmetric version.
- *Intersection property:* If $V, W \in \mathfrak{u}^*$, take the associated sequences $\{V_n\}$ and $\{W_n\}$. Then $U_n = V_n \cap W_n$ are symmetric neighborhoods of $\Delta$, and $U_0 \subset V \cap W$, $U_{n+1} \circ U_{n+1} \subset V_{n+1} \circ V_{n+1} \cap W_{n+1} \circ W_{n+1} \subset V_n \cap W_n = U_n$, so $V \cap W \in \mathfrak{u}^*$.
- *Square-root property:* For $V \in \mathfrak{u}^*$ with sequence $\{V_n\}$, set $U = V_1$. Then $U \in \mathfrak{u}^*$ (using the shifted sequence $\{V_{n+1}\}$) and $U \circ U = V_1 \circ V_1 \subset V_0 \subset V$.

Thus $\mathfrak{u}^*$ is a uniformity on $X$.

**Topology of $\mathfrak{u}^*$ coincides with $\mathfrak{t}$.** For a completely regular space, every point has a neighborhood base consisting of open sets. For any $x \in X$, the sets $V[x]$ for $V \in \mathfrak{u}^*$ form a neighborhood base at $x$. Since each $V$ is a $\mathfrak{t} \times \mathfrak{t}$-neighborhood of the diagonal, $V[x]$ is a $\mathfrak{t}$-neighborhood of $x$. Conversely, the complete regularity of $(X, \mathfrak{t})$ ensures that every $\mathfrak{t}$-open set containing $x$ contains some $V[x]$ with $V \in \mathfrak{u}^*$.

**Maximality.** Let $\mathfrak{v}$ be any uniformity on $X$ whose topology is $\mathfrak{t}$. We show $\mathfrak{v} \subset \mathfrak{u}^*$. Take any $W \in \mathfrak{v}$. By the definition of a uniformity, there exists a sequence $\{W_n\}$ of symmetric entourages in $\mathfrak{v}$ with $W_0 \subset W$ and $W_{n+1} \circ W_{n+1} \subset W_n$ for all $n$. Since the topology of $\mathfrak{v}$ is $\mathfrak{t}$, each $W_n$ is a neighborhood of the diagonal in the product topology $\mathfrak{t} \times \mathfrak{t}$. Therefore $W$ satisfies the defining condition of $\mathfrak{u}^*$, so $W \in \mathfrak{u}^*$. Hence $\mathfrak{u}^*$ contains every uniformity with topology $\mathfrak{t}$, i.e., it is the *largest* such uniformity.

**Alternative characterizations.** The uniformity $\mathfrak{u}^*$ can also be described as:
- The smallest uniformity making every continuous map from $X$ into a metric space uniformly continuous.
- The smallest uniformity making every continuous map from $X$ into any uniform space uniformly continuous.

These follow because any such continuous map is uniformly continuous with respect to $\mathfrak{u}^*$ (by the neighborhood-of-the-diagonal description), and conversely any uniformity with this property must contain $\mathfrak{u}^*$ (since the identity map on $X$, viewed as a map into the uniform space $(X, \mathfrak{u}^*)$, is continuous and hence must be uniformly continuous). $\square$
