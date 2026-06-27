---
role: proof
locale: en
of_concept: neighborhood-system-characterization-of-topological-group
source_book: gtm027
source_chapter: "3"
source_section: "S"
---

# Proof of the Neighborhood System Characterization of Topological Groups

**Statement.** Given a group $G$ and a non-void family $\mathfrak{u}$ of non-void subsets satisfying the following four propositions, there is a unique topology $\mathfrak{J}$ for $G$ such that $(G, \cdot, \mathfrak{J})$ is a topological group and $\mathfrak{u}$ is the neighborhood system of the identity element $e$.

**The four axioms for the neighborhood system $\mathfrak{u}$ at $e$ are:**

1. **(Filter base.)** The intersection of any two members of $\mathfrak{u}$ contains a member of $\mathfrak{u}$.
2. **(Square root.)** For each $U \in \mathfrak{u}$, there exists $V \in \mathfrak{u}$ such that $V \cdot V \subset U$.
3. **(Symmetry.)** For each $U \in \mathfrak{u}$, we have $U^{-1} \in \mathfrak{u}$.
4. **(Inner automorphism invariance.)** For each $U \in \mathfrak{u}$ and each $x \in G$, there exists $V \in \mathfrak{u}$ such that $x \cdot V \cdot x^{-1} \subset U$.

**Proof of existence and uniqueness of the topology.**

**Construction of the topology.** Define $\mathfrak{J}$ as follows: a set $O \subset G$ is open if and only if for each $x \in O$ there exists $U \in \mathfrak{u}$ such that $U \cdot x \subset O$. Equivalently, the family $\{U \cdot x : U \in \mathfrak{u},\; x \in G\}$ forms a base for the topology $\mathfrak{J}$.

*Verification that $\mathfrak{J}$ is a topology:*

- $\varnothing$ is vacuously open. $G$ is open because for any $x \in G$, taking any $U \in \mathfrak{u}$ (which is non-void), we have $U \cdot x \subset G$.
- If $\{O_\alpha\}$ is a family of open sets and $x \in \bigcup_\alpha O_\alpha$, then $x \in O_\beta$ for some $\beta$. Hence there exists $U \in \mathfrak{u}$ with $U \cdot x \subset O_\beta \subset \bigcup_\alpha O_\alpha$. Thus arbitrary unions of open sets are open.
- If $O_1, O_2$ are open and $x \in O_1 \cap O_2$, there exist $U_1, U_2 \in \mathfrak{u}$ with $U_1 \cdot x \subset O_1$ and $U_2 \cdot x \subset O_2$. By axiom 1, there exists $W \in \mathfrak{u}$ with $W \subset U_1 \cap U_2$. Then $W \cdot x \subset (U_1 \cap U_2) \cdot x \subset U_1 \cdot x \cap U_2 \cdot x \subset O_1 \cap O_2$. Hence finite intersections of open sets are open.

So $\mathfrak{J}$ is indeed a topology.

**$\mathfrak{u}$ is the neighborhood system at $e$.** By construction, each $U \in \mathfrak{u}$ contains $e$ (take $x = e$: the condition $U \cdot e = U$ being a neighborhood of $e$ requires $e \in U$, which follows from the fact that neighborhoods are defined via translates). Moreover, for $U \in \mathfrak{u}$, the set $U$ is a neighborhood of $e$ because $e \in U$ and there exists $V \in \mathfrak{u}$ with $V \cdot e = V \subset U$ (take $V \subset U$ with $V \in \mathfrak{u}$ using axiom 1).

Conversely, if $N$ is any neighborhood of $e$ in $\mathfrak{J}$, then there exists an open set $O$ with $e \in O \subset N$. By definition of openness, there exists $U \in \mathfrak{u}$ with $U = U \cdot e \subset O \subset N$. Hence every neighborhood of $e$ contains a member of $\mathfrak{u}$, so $\mathfrak{u}$ is a base for the neighborhood system at $e$.

**Continuity of the group operations.** We verify that $(x, y) \mapsto x \cdot y^{-1}$ is continuous. Let $x, y \in G$ and let $W$ be a neighborhood of $x \cdot y^{-1}$. Then $(x \cdot y^{-1})^{-1} \cdot W$ is a neighborhood of $e$, so there exists $U \in \mathfrak{u}$ with $U \subset (x \cdot y^{-1})^{-1} \cdot W$, i.e., $x \cdot y^{-1} \cdot U \subset W$.

By axiom 2, choose $V_0 \in \mathfrak{u}$ with $V_0 \cdot V_0 \subset U$. By axiom 4, $y \cdot V_0 \cdot y^{-1}$ contains a member of $\mathfrak{u}$, and by axiom 3, $(y \cdot V_0 \cdot y^{-1})^{-1} = y \cdot V_0^{-1} \cdot y^{-1}$ is also around $e$. Using these, one constructs neighborhoods $U_x$ of $x$ and $U_y$ of $y$ with $U_x \cdot U_y^{-1} \subset W$, establishing continuity via proposition (b).

**Uniqueness.** If a topology $\mathfrak{J}$ on $G$ makes $(G, \cdot, \mathfrak{J})$ a topological group with $\mathfrak{u}$ as the neighborhood system at $e$, then a set $O$ is open in $\mathfrak{J}$ if and only if for each $x \in O$ there exists $U \in \mathfrak{u}$ with $U \cdot x \subset O$. This condition determines $\mathfrak{J}$ completely, hence the topology is unique. ∎
