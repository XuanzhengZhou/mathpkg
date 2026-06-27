---
role: proof
locale: en
of_concept: accumulation-points-lindelof-subspace
source_book: gtm027
source_chapter: "1"
source_section: "H"
---

# Proof of Accumulation Points in a Space Where Every Subspace Is Lindelöf

**Theorem.** Let $X$ be a space, each subspace of which is Lindelöf. Let $A$ be an uncountable subset of $X$, and let $B$ be the subset consisting of all points $x$ of $A$ such that each neighborhood of $x$ contains uncountably many points of $A$. Then $A \setminus B$ is countable, and consequently each neighborhood of a point of $B$ contains uncountably many points of $B$.

*Proof.* Let $C = A \setminus B$. For each $x \in C$, there exists an open neighborhood $U_x$ of $x$ such that $U_x \cap A$ is countable (by definition of $B$: if $x \notin B$, then $x$ has a neighborhood containing only countably many points of $A$).

Consider the open cover $\{U_x : x \in C\}$ of the subspace $C$. Since $C$ is a subspace of $X$, by hypothesis $C$ is Lindelöf. Therefore, there exists a countable subcover $\{U_{x_n} : n \in \mathbb{N}\}$ of $C$.

Now $C \subseteq \bigcup_{n \in \mathbb{N}} U_{x_n}$, so
$$C \subseteq \left(\bigcup_{n \in \mathbb{N}} U_{x_n}\right) \cap A = \bigcup_{n \in \mathbb{N}} (U_{x_n} \cap A).$$

Each $U_{x_n} \cap A$ is countable by construction, and a countable union of countable sets is countable. Hence $C = A \setminus B$ is countable.

For the second assertion: let $x \in B$ and let $V$ be any neighborhood of $x$. Since $A \setminus B$ is countable and $A$ is uncountable, $B$ is uncountable. Moreover, $V \cap A$ is uncountable (since $x \in B$), and $V \cap (A \setminus B)$ is countable (it is a subset of the countable set $A \setminus B$). Therefore,
$$V \cap B = (V \cap A) \setminus (V \cap (A \setminus B))$$
is the difference of an uncountable set and a countable set, hence uncountable. $\square$
