---
role: proof
locale: en
of_concept: plane-irrational-coordinate-connected
source_book: gtm027
source_chapter: "1"
source_section: "O"
---

# Proof that the Plane with At Least One Irrational Coordinate Is Connected

**Theorem.** Let $X$ be the set of all points in the Euclidean plane with at least one irrational coordinate, with the relative topology. Then $X$ is connected.

*Proof.* Let $X = \{(x,y) \in \mathbb{R}^2 : x \in \mathbb{R} \setminus \mathbb{Q} \text{ or } y \in \mathbb{R} \setminus \mathbb{Q}\}$. Equivalently, $X = \mathbb{R}^2 \setminus (\mathbb{Q} \times \mathbb{Q})$, the complement of the countable dense set $\mathbb{Q} \times \mathbb{Q}$.

**Key observation:** The Euclidean plane $\mathbb{R}^2$ is connected (in fact, path-connected). We claim that removing a countable set from a connected, locally path-connected space (that is "strongly connected" enough) leaves a connected space.

More concretely: Suppose $X = U \cup V$ where $U$ and $V$ are disjoint, nonempty, and open in $X$. Then $U = U' \cap X$ and $V = V' \cap X$ for some open sets $U', V' \subseteq \mathbb{R}^2$.

Consider $U'$ and $V'$ in $\mathbb{R}^2$. The points of $\mathbb{Q} \times \mathbb{Q}$ (the removed set) must be distributed between the closures of $U'$ and $V'$.

**Proof by contradiction:** Assume $X$ is disconnected. Then there exists a separation $X = A \cup B$ with $A, B$ nonempty, disjoint, and both open and closed in $X$.

Let $\overline{A}$ and $\overline{B}$ be their closures in $\mathbb{R}^2$. Since $A$ and $B$ are separated in $X$, we have $A \cap \overline{B} = \emptyset$ and $\overline{A} \cap B = \emptyset$ in $X$. Thus any common limit point must be in $\mathbb{Q} \times \mathbb{Q}$.

Since $\mathbb{Q} \times \mathbb{Q}$ is countable, and $\mathbb{R}^2$ is a complete metric space, a connected space minus a countable set remains connected. This is because any two points in $X$ can be joined by a path that avoids the countable set $\mathbb{Q} \times \mathbb{Q}$: between any two points there are uncountably many disjoint paths (e.g., a family of circular arcs), and only countably many can hit the countable removed set.

Thus $X$ is connected (in fact, path-connected). $\square$

**Remark.** More generally, removing a countable set from $\mathbb{R}^n$ ($n \geq 2$) leaves a path-connected (hence connected) space. The result fails for $n = 1$: $\mathbb{R} \setminus \mathbb{Q}$ is totally disconnected.
