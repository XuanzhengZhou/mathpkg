---
role: exercise
locale: en
chapter: "1"
section: "The Brouwer Reduction Theorem"
exercise_number: 1
---

# Exercise T(a)

State and prove the Brouwer Reduction Theorem in the following form. Let $X$ be a topological space such that every subspace is a Lindelöf space. Let $\mathcal{F}$ be a family of closed subsets of $X$ which is *inductive*: whenever $\{F_n\}_{n \in \omega}$ is a countable nested family ($F_0 \supset F_1 \supset F_2 \supset \cdots$) of members of $\mathcal{F}$, then the intersection $\bigcap_{n \in \omega} F_n$ belongs to $\mathcal{F}$. Prove that every member $A$ of $\mathcal{F}$ contains an irreducible member of $\mathcal{F}$ (that is, a member of $\mathcal{F}$ that is minimal with respect to inclusion).

*Hint.* Apply Zorn's Lemma to the collection of all members of $\mathcal{F}$ contained in $A$, ordered by reverse inclusion. Use the Lindelöf property to show that for any chain, the intersection of a countable cofinal subfamily equals the intersection of the whole chain; the inductive hypothesis then guarantees that this intersection belongs to $\mathcal{F}$ and serves as a lower bound.
