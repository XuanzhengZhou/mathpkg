---
role: proof
locale: en
of_concept: compact-uniform-space-neighborhoods-of-diagonal
source_book: gtm027
source_chapter: "6"
source_section: "Compact Spaces"
---

# Proof that Neighborhoods of the Diagonal are in the Uniformity for Compact Spaces (Theorem 6.29)

**Theorem 6.29.** If $(X, \mathcal{U})$ is a compact uniform space, then every neighborhood of the diagonal $\Delta$ in $X \times X$ is a member of $\mathcal{U}$ and every pseudo-metric which is continuous on $X \times X$ is a member of the gage of $\mathcal{U}$.

**Proof.** Let $\mathcal{B}$ be the family of closed members of $\mathcal{U}$. Since $\mathcal{U}$ is a uniformity, $\mathcal{B}$ is a base for $\mathcal{U}$ (by Theorem 6.8). Let $V$ be an arbitrary open neighborhood of the diagonal $\Delta$.

For each $U \in \mathcal{B}$, $U$ is closed in $X \times X$. The family $\{U : U \in \mathcal{B}\}$ has the property that $\bigcap \{U : U \in \mathcal{B}\} \subset \Delta$ (since the space is Hausdorff in the uniform topology—if not Hausdorff, we consider the intersection as the closure of the diagonal).

Now consider $X \times X \setminus V$, which is closed in $X \times X$ and disjoint from $\Delta$. If $(x,y) \in X \times X \setminus V$, then $(x,y) \notin \Delta$, so $(x,y) \notin \bigcap \{U : U \in \mathcal{B}\}$. Hence there exists $U_{(x,y)} \in \mathcal{B}$ with $(x,y) \notin U_{(x,y)}$.

The family $\{X \times X \setminus U : U \in \mathcal{B}\}$ covers $X \times X \setminus V$. Since each $U \in \mathcal{B}$ is closed in the compact space $X \times X$, the sets $X \times X \setminus U$ are open. By compactness of $X \times X \setminus V$ (it's a closed subset of compact $X \times X$), there exist finitely many $U_1, \ldots, U_n \in \mathcal{B}$ such that

$$X \times X \setminus V \subset \bigcup_{i=1}^{n} (X \times X \setminus U_i) = X \times X \setminus \bigcap_{i=1}^{n} U_i.$$

Thus $\bigcap_{i=1}^{n} U_i \subset V$. Since $\mathcal{B} \subset \mathcal{U}$ and $\mathcal{U}$ is closed under finite intersections, $\bigcap_{i=1}^{n} U_i \in \mathcal{U}$, and consequently $V \in \mathcal{U}$.

For pseudo-metrics: if $d$ is continuous on $X \times X$, then for each $r > 0$, $V_{d,r} = \{(x,y) : d(x,y) < r\}$ is an open neighborhood of $\Delta$. By the first part, $V_{d,r} \in \mathcal{U}$, and by Theorem 6.11, $d$ belongs to the gage of $\mathcal{U}$.
