---
role: proof
locale: en
of_concept: neighborhood-characterization-of-topological-group
source_book: gtm027
source_chapter: "3"
source_section: "S"
---

# Proof of the Neighborhood Characterization of Topological Groups

**Statement.** Let $(G, \cdot)$ be a group and $\mathfrak{J}$ a topology for $G$. Then $(G, \cdot, \mathfrak{J})$ is a topological group if and only if for each $x$ and $y$ in $G$ and each neighborhood $W$ of $x \cdot y^{-1}$, there exist neighborhoods $U$ of $x$ and $V$ of $y$ such that $U \cdot V^{-1} \subset W$.

**Proof.** A topological group is defined by the continuity of the map $\varphi: G \times G \to G$ given by $\varphi(x, y) = x \cdot y^{-1}$, where $G \times G$ carries the product topology.

**($\Rightarrow$)** Assume $(G, \cdot, \mathfrak{J})$ is a topological group, so $\varphi$ is continuous. Fix $x, y \in G$ and let $W$ be a neighborhood of $\varphi(x, y) = x \cdot y^{-1}$. By continuity of $\varphi$ at $(x, y)$, there exists a neighborhood of $(x, y)$ in the product topology whose image under $\varphi$ lies in $W$. By definition of the product topology, such a neighborhood contains a basic open set $U \times V$, where $U$ is a neighborhood of $x$ and $V$ is a neighborhood of $y$. Thus $\varphi(U \times V) \subset W$, which means

$$
\varphi(U \times V) = \{ u \cdot v^{-1} : u \in U,\; v \in V \} = U \cdot V^{-1} \subset W.
$$

This establishes the neighborhood condition.

**($\Leftarrow$)** Conversely, assume the neighborhood condition holds. To prove $\varphi$ is continuous, take any point $(x, y) \in G \times G$ and any neighborhood $W$ of $\varphi(x, y) = x \cdot y^{-1}$. By hypothesis, there exist neighborhoods $U$ of $x$ and $V$ of $y$ such that $U \cdot V^{-1} \subset W$. Then $U \times V$ is a neighborhood of $(x, y)$ in the product topology, and

$$
\varphi(U \times V) = U \cdot V^{-1} \subset W.
$$

This shows that $\varphi$ is continuous at every point $(x, y)$, hence $(G, \cdot, \mathfrak{J})$ is a topological group.

**Equivalent local form at the identity.** The condition can be reformulated in terms of neighborhoods of the identity element $e$. Setting $y = x$, the condition says: for each $x \in G$ and each neighborhood $W$ of $e = x \cdot x^{-1}$, there exist neighborhoods $U$ of $x$ and $V$ of $x$ (in particular, neighborhoods of $x$) such that $U \cdot V^{-1} \subset W$. Equivalently, for each $x \in G$ and each neighborhood $W$ of $e$, there exists a neighborhood $U$ of $x$ such that $U \cdot U^{-1} \subset W$.

In particular, taking the special case $x = e$, we obtain: for each neighborhood $W$ of $e$, there exists a neighborhood $V$ of $e$ such that $V \cdot V^{-1} \subset W$. This is one of the fundamental properties of the neighborhood system at the identity in a topological group. ∎
