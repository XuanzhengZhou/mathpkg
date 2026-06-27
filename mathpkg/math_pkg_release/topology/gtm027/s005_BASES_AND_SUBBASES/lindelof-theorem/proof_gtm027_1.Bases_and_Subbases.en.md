---
role: proof
locale: en
of_concept: lindelof-theorem
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Lindelöf's Theorem

**Theorem 15 (Lindelöf).** There is a countable subcover of each open cover of a subset of a space whose topology has a countable base.

**Proof.** Suppose $A$ is a set, $lpha$ is an open cover of $A$, and $\mathcal{B}$ is a countable base for the topology of the space. Let $\mathcal{C}$ be the family of all members of $\mathcal{B}$ which are subsets of some member of $lpha$. Since $\mathcal{B}$ is countable, $\mathcal{C}$ is a countable family.

For each member $C$ of $\mathcal{C}$, choose a containing member of $lpha$ and so obtain a countable subfamily $\mathcal{D}$ of $lpha$. Then $\mathcal{D}$ is also a cover of $A$: for any $x \in A$, there exists $U \in lpha$ with $x \in U$. Since $\mathcal{B}$ is a base, there exists $B \in \mathcal{B}$ with $x \in B \subset U$. Thus $B \in \mathcal{C}$, and the chosen member of $\mathcal{D}$ corresponding to $B$ contains $x$. Hence $\mathcal{D}$ is a countable subcover of $lpha$. $\square$