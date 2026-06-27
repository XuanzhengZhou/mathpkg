---
role: proof
locale: en
of_concept: condition-for-family-to-be-a-base
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Condition for a Family to be a Base for Some Topology

**Theorem 11.** A family $\mathcal{B}$ of sets is a base for some topology for the set $X = igcup \{B : B \in \mathcal{B}\}$ if and only if for every two members $U$ and $V$ of $\mathcal{B}$ and each point $x$ in $U \cap V$ there is $W$ in $\mathcal{B}$ such that $x \in W$ and $W \subset U \cap V$.

**Proof.** If $\mathcal{B}$ is a base for some topology, $U$ and $V$ are members of $\mathcal{B}$ and $x \in U \cap V$ then, since $U \cap V$ is open, there is a member of $\mathcal{B}$ to which $x$ belongs and which is a subset of $U \cap V$.

To show the converse, let $\mathcal{B}$ be a family with the specified property and let $\mathcal{J}$ be the family of all unions of members of $\mathcal{B}$. A union of members of $\mathcal{J}$ is itself a union of members of $\mathcal{B}$ and is therefore a member of $\mathcal{J}$, and it is only necessary to show that the intersection of two members $U$ and $V$ of $\mathcal{J}$ is a member of $\mathcal{J}$. If $x \in U \cap V$, then we may choose $U'$ and $V'$ in $\mathcal{B}$ such that $x \in U' \subset U$ and $x \in V' \subset V$. By hypothesis, there exists $W \in \mathcal{B}$ with $x \in W \subset U' \cap V' \subset U \cap V$. Hence $U \cap V$ is the union of all such members $W$ of $\mathcal{B}$ and consequently $U \cap V \in \mathcal{J}$. Thus $\mathcal{J}$ is a topology, and clearly $\mathcal{B}$ is a base for $\mathcal{J}$. $\square$