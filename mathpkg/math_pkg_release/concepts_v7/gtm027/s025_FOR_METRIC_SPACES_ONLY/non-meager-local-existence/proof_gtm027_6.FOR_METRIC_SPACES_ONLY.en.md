---
role: proof
locale: en
of_concept: non-meager-local-existence
source_book: gtm027
source_chapter: "6"
source_section: "FOR METRIC_SPACES ONLY"
---

# Proof of Local Existence for Non-Meager Sets

**Proposition.** Let $X$ be a topological space. If a subset $A$ of $X$ is non-meager (i.e., not of the first category), then there exists a non-void open set $V$ such that the intersection of $A$ with every neighborhood of each point of $V^{-}$ is non-meager.

**Proof.** Let $\mathcal{U}$ be a disjoint family of open sets which is maximal with respect to the property: if $U \in \mathcal{U}$, then $U \cap A$ is meager. Such a family $\mathcal{U}$ exists by the maximal principle (0.25). Let $W = \bigcup \{U : U \in \mathcal{U}\}$.

We first show that $W \cap A$ is meager. For each $U \in \mathcal{U}$, since $U \cap A$ is meager, write $U \cap A = \bigcup_{n \in \omega} U_n$ where each $U_n$ is nowhere dense. Because the family $\mathcal{U}$ is disjoint, for each fixed $n \in \omega$ the union $\bigcup_{U \in \mathcal{U}} U_n$ is nowhere dense. Hence

$$W \cap A = \bigcup_{U \in \mathcal{U}} (U \cap A) = \bigcup_{n \in \omega} \bigcup_{U \in \mathcal{U}} U_n$$

is a countable union of nowhere dense sets, and therefore is meager.

Now, $W^{-} \setminus W$ is nowhere dense (it is a closed set with empty interior). Hence $A \cap W^{-}$ is meager, because $A \cap W^{-} = (A \cap W) \cup (A \cap (W^{-} \setminus W))$ is the union of a meager set and a subset of a nowhere dense set.

From the maximality of $\mathcal{U}$, it follows that $W^{-}$ contains every open set $V$ such that $V \cap A$ is meager.

Now since $A$ is non-meager, the set $A \setminus W^{-}$ is non-meager (otherwise $A = (A \cap W^{-}) \cup (A \setminus W^{-})$ would be meager). Let $V = X \setminus W^{-}$, which is open. We claim that $V$ has the required property: for each $x \in V^{-} = X \setminus (W^{-})^{\circ} = X \setminus W^{-} = V$ (since $W^{-}$ is closed), and for any neighborhood $N$ of $x$, the intersection $A \cap N$ is non-meager. For if $A \cap N$ were meager for some neighborhood $N$ of some $x \in V$, then $N \cap A$ would be meager, contradicting the maximality of $\mathcal{U}$ (since $N$ is not contained in $W^{-}$).

Thus $V = X \setminus W^{-}$ is the desired non-void open set.
