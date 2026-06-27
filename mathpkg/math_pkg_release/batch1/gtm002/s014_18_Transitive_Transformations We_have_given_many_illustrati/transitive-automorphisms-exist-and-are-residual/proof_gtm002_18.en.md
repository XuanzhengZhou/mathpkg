---
role: proof
locale: en
of_concept: transitive-automorphisms-exist-and-are-residual
source_book: gtm002
source_chapter: "18"
source_section: "Transitive Transformations"
---

Let $M$ be the space of all measure-preserving automorphisms of the unit square $X$ equipped with the uniform metric. $M$ is topologically complete. Let $\{U_i\}$ be a countable base for $X$. For each pair $(i, j)$ define

$$E_{ij} = \left\{ T \in M : U_i \cap \bigcup_{k=1}^{\infty} T^{-k} U_j \neq \emptyset \right\}.$$

**Step 1: Each $E_{ij}$ is open and dense in $M$.**

To show $E_{ij}$ is open, observe that if $T \in E_{ij}$, then there exists $k \geq 1$ such that $U_i \cap T^{-k} U_j \neq \emptyset$. For any $S$ sufficiently close to $T$ in the uniform metric, $S^{-k} U_j$ is close to $T^{-k} U_j$, so the non-empty intersection $U_i \cap T^{-k} U_j$ implies $U_i \cap S^{-k} U_j \neq \emptyset$ for $S$ near $T$. Hence $E_{ij}$ is open.

To show $E_{ij}$ is dense, let $T \in M$ and $\varepsilon > 0$. We construct $S \in E_{ij}$ with $\varrho(S, T) < \varepsilon$. Join a point of $U_i$ to a point of $U_j$ by a line segment. Choose points $p_1, p_2, \ldots, p_{N+1}$ on this segment such that $p_1 \in U_i$, $p_{N+1} \in U_j$, and $|p_k - p_{k+1}| < \varepsilon/2$ for $k = 1, \ldots, N$. Choose $\delta < \frac{1}{2} \min |p_k - p_{k+1}|$ such that the $\delta$-neighborhoods of $p_1$ and $p_{N+1}$ are contained in $U_i$ and $U_j$ respectively. By Theorem 17.3, the set of recurrent points under $T$ is residual in the square, and the set of nonperiodic points is also residual. Choose a nonperiodic point $x_1$ in the $\delta$-neighborhood of $p_1$ such that some iterate $T^{n_1}x_1$ of its positive semiorbit lies in the same neighborhood. Then construct $S$ by modifying $T$ inside disjoint small neighborhoods to push points from near $U_i$ into $U_j$, ensuring $U_i \cap S^{-n} U_j \neq \emptyset$ for some $n$. This yields $S \in E_{ij}$ with $\varrho(S, T) < \varepsilon$, proving density.

**Step 2: The intersection is non-empty and consists of transitive automorphisms.**

Since $M$ is topologically complete and each $E_{ij}$ is open and dense, $\bigcap_{i,j} E_{ij}$ is a dense $G_{\delta}$ set in $M$, hence non-empty by the Baire category theorem.

For any $T \in \bigcap_{i,j} E_{ij}$, we have

$$U_i \cap \bigcup_{k=1}^{\infty} T^{-k} U_j \neq \emptyset$$

for all $i$ and $j$. Hence for each $j$ the set

$$G_j = \bigcup_{k=1}^{\infty} T^{-k} U_j$$

is open and dense in the square. Therefore $\bigcap_{j} G_j \neq \emptyset$ by the Baire category theorem applied to $X$. For any point $x \in \bigcap_j G_j$, the positive semiorbit $\{x, Tx, T^2x, \ldots\}$ intersects every basic open set $U_j$, hence is dense in the square. Consequently, $T$ is transitive.
