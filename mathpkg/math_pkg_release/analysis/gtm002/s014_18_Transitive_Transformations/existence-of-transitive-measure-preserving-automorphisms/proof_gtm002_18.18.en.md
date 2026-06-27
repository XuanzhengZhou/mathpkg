---
role: proof
locale: en
of_concept: existence-of-transitive-measure-preserving-automorphisms
source_book: gtm002
source_chapter: "18"
source_section: "18"
---

Let $M$ be the space of all measure-preserving automorphisms of the unit square $X = [0,1] \times [0,1]$, with the uniform metric. Let $\{U_i\}$ be a countable base for the topology of $X$.

For each pair of positive integers $i$ and $j$, define
$$E_{ij} = \left\{ T \in M : U_i \cap \bigcup_{k=1}^{\infty} T^{-k} U_j \neq \emptyset \right\}.$$

We claim each $E_{ij}$ is open and dense in $M$.

*Openness:* The condition $U_i \cap \bigcup_{k=1}^{\infty} T^{-k} U_j \neq \emptyset$ means there exist a point $x \in U_i$ and an integer $k \geq 1$ such that $T^k x \in U_j$. Since $U_i$ and $U_j$ are open and $T \mapsto T^k$ is continuous in the uniform topology, this is an open condition.

*Density:* Fix $i$, $j$ and take any $T \in M \setminus P$ (where $P$ is the first-category set of everywhere-periodic automorphisms) and any $\varepsilon > 0$. We construct a perturbation $S$ of $T$ such that $S \in E_{ij}$ and $\varrho(S, T) < \varepsilon$.

Join a point of $U_i$ to a point of $U_j$ by a line segment. Choose points $p_1, p_2, \ldots, p_{N+1}$ on this segment such that $p_1 \in U_i$, $p_{N+1} \in U_j$, and $|p_k - p_{k+1}| < \varepsilon/2$ for $k = 1, \ldots, N$. Choose $\delta > 0$ with $\delta < \frac{1}{2} \min_k |p_k - p_{k+1}|$ such that the $\delta$-neighborhoods of $p_1$ and $p_{N+1}$ are contained in $U_i$ and $U_j$ respectively.

Since $T \in M \setminus P$, $T$ has non-periodic points in every non-empty open set. Moreover, by Theorem 17.3, the recurrent points under $T$ form a residual set, and non-periodic points also form a residual set. Their intersection is non-empty. Choose a non-periodic, recurrent point $x_1$ in the $\delta$-neighborhood of $p_1$ that has some iterate $T^{n_1} x_1$ of its positive semiorbit in the same neighborhood.

Continuing this construction along the chain $p_1, \ldots, p_{N+1}$, we can find a measure-preserving automorphism $S$, arbitrarily close to $T$, such that some iterate of $S$ maps a point of $U_i$ into $U_j$. Hence $S \in E_{ij}$, proving density.

Now define
$$E = \bigcap_{i,j=1}^{\infty} E_{ij}.$$

Since each $E_{ij}$ is open and dense in the complete metric space $M$, $E$ is a dense $G_{\delta}$ in $M$, hence non-empty (by the Baire category theorem).

For any $T \in E = \bigcap_{i,j} E_{ij}$, we have
$$U_i \cap \bigcup_{k=1}^{\infty} T^{-k} U_j \neq \emptyset$$
for all $i$ and $j$. Hence the set
$$G_j = \bigcup_{k=1}^{\infty} T^{-k} U_j$$
is open and dense in $X$ (it intersects every $U_i$). Therefore $\bigcap_{j=1}^{\infty} G_j$ is non-empty, again by the Baire category theorem applied to the complete metric space $X$.

For any point $x \in \bigcap_{j=1}^{\infty} G_j$, the positive semiorbit $\{x, Tx, T^2x, \ldots\}$ intersects every $U_j$, hence is dense in $X$. Consequently, every $T \in E$ is transitive.

Thus the set of transitive measure-preserving automorphisms contains the dense $G_{\delta}$ set $E$, so it is residual in $M$ and in particular non-empty.
