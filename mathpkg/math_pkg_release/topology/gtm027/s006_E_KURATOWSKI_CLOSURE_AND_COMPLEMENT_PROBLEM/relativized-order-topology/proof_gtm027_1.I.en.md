---
role: proof
locale: en
of_concept: relativized-order-topology
source_book: gtm027
source_chapter: "1"
source_section: "I"
---

# Proof that Relativized Order Topology May Differ from Subspace Order Topology

**Proposition.** Let $Y$ be a subset of a set $X$ which is linearly ordered by $<$. Then $Y$ is linearly ordered by $<$ (the restriction), but the order topology on $Y$ induced by this restricted order may differ from the relativization (subspace topology) of the order topology on $X$.

*Proof by example.* Let $X = \mathbb{R}$ with the usual order and the usual order topology. Let $Y = [0,1) \cup \{2\}$.

Under the restricted order $<$, $Y$ has the order topology whose subbase consists of sets $\{y \in Y : y < a\}$ and $\{y \in Y : y > a\}$ for $a \in Y$.

In the order topology of $Y$, the singleton $\{2\}$ is open because:
$$\{2\} = \{y \in Y : y > 1\} \cap \{y \in Y : y < 3\}$$
where $1 \in Y$ and $3$ is not in $Y$ but the sets $\{y \in Y : y > 1\}$ and $\{y \in Y : y < 3\}$ are subbasic open sets in the order topology on $Y$. More simply, $2$ is the immediate successor of $1$ in $Y$, so $(1, \infty) \cap Y = \{2\}$ is open in the order topology of $Y$.

However, in the subspace topology inherited from $\mathbb{R}$, any open set containing $2$ must contain an interval $(2-\varepsilon, 2+\varepsilon) \cap Y$ for some $\varepsilon > 0$. For $\varepsilon < 1$, this contains points of $[0,1)$ that are not in $\{2\}$. Hence $\{2\}$ is not open in the subspace topology.

Therefore the two topologies on $Y$ are distinct. $\square$
