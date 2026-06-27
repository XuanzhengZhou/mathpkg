---
role: proof
locale: en
of_concept: weak-operator-topology
source_book: gtm015
source_chapter: "IV"
source_section: "40"
---

# Proof of Weak operator topology on the space of continuous linear mappings

**Theorem (40.25).** Let $E$ and $F$ be topological vector spaces over $\mathbb{K}$.

(i) The weak operator topology $\tau_w$ on $\mathcal{L}(E, F)$ is defined as the initial topology for the family of linear forms

$$T \mapsto g(Tx) \quad (x \in E,\ g \in F'),$$

where $F'$ denotes the continuous dual of $F$. Equivalently, $\tau_w$ is the initial topology for the family of mappings $g \circ \varphi_x$ with $\varphi_x(T) = Tx$. The topology $\tau_w$ is locally convex.

(ii) The strong operator topology $\tau_s$ is finer than the weak operator topology $\tau_w$.

(iii) If $F$ is separated and locally convex, then $\tau_w$ is also separated.

(iv) If $F$ is finite-dimensional and separated, then $\tau_s = \tau_w$. More generally, see (v).

(v) If $F'$ separates the points of $F$ (which holds when $F$ is locally convex and separated), then $\tau_w$ is separated.

**Proof.**

**(i)** For each $x \in E$ and $g \in F'$, the mapping $T \mapsto g(Tx)$ is a linear form on $\mathcal{L}(E, F)$, namely $g \circ \varphi_x$ in the notation of (40.24). Taking the initial topology for the family of all such linear forms yields, by definition, a locally convex topology on $\mathcal{L}(E, F)$. This is the weak operator topology $\tau_w$.

**(ii)** The strong operator topology $\tau_s$ is the initial topology for the mappings $\varphi_x: T \mapsto Tx$ into $F$ (40.24). Since each $g \in F'$ is continuous on $F$, the composition $g \circ \varphi_x$ is $\tau_s$-continuous. Since $\tau_w$ is the initial topology for precisely these compositions, and $\tau_s$ makes them all continuous, $\tau_s$ is finer than $\tau_w$.

**(iii)** If $F$ is separated and locally convex, then by the Hahn-Banach theorem, $F'$ separates the points of $F$. If $T_1 \neq T_2$ in $\mathcal{L}(E, F)$, there exists $x \in E$ such that $T_1 x \neq T_2 x$ in $F$. Since $F'$ separates points of $F$, there exists $g \in F'$ such that $g(T_1 x) \neq g(T_2 x)$. This means the linear form $g \circ \varphi_x$ separates $T_1$ and $T_2$, hence the initial topology $\tau_w$ is separated (Hausdorff).

**(iv)** If $F$ is finite-dimensional, every linear form on $F$ is continuous, and a linear mapping $T: E \to F$ is continuous if and only if $g \circ T$ is continuous for every $g \in F'$ (or equivalently, for each coordinate functional). The strong topology and the weak topology on $\mathcal{L}(E, F)$ coincide because convergence in $\tau_w$ implies pointwise convergence in the weak topology of $F$, which in finite dimensions is equivalent to convergence in the original topology of $F$. Thus $\tau_s = \tau_w$.

**(v)** As shown in (iii), if $F'$ separates points of $F$, then the family of linear forms $g \circ \varphi_x$ separates points of $\mathcal{L}(E, F)$. Hence the initial topology $\tau_w$ is separated.
