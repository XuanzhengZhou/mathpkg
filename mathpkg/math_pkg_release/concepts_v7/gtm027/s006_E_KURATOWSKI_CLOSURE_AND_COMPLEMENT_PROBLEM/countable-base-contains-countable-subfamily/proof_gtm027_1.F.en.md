---
role: proof
locale: en
of_concept: countable-base-contains-countable-subfamily
source_book: gtm027
source_chapter: "1"
source_section: "F"
---

# Proof that Every Base Contains a Countable Subfamily Which Is Also a Base

**Theorem.** If the topology of a space has a countable base, then each base contains a countable subfamily which is also a base.

*Proof.* Let $X$ be a topological space whose topology has a countable base $\mathcal{B} = \{B_n : n \in \mathbb{N}\}$. Let $\mathcal{C}$ be any base for the same topology.

For each pair $(m,n) \in \mathbb{N} \times \mathbb{N}$ such that $B_m \subseteq B_n$, by the definition of a base, $B_m$ is a union of members of $\mathcal{C}$. Since $\mathcal{C}$ is a base, there exists some $C \in \mathcal{C}$ with $B_m \subseteq C \subseteq B_n$ whenever such an intermediate set exists (in particular, whenever $B_m \neq \emptyset$). More precisely, for each $x \in B_m$, choose $C_{m,n,x} \in \mathcal{C}$ such that $x \in C_{m,n,x} \subseteq B_n$.

However, a more elegant argument: For each pair $(m,n)$ with $B_m \subseteq B_n$, if such a pair admits a member of $\mathcal{C}$ between them, select one such member. Let $\mathcal{C}'$ be the collection of all members of $\mathcal{C}$ so selected. Since there are only countably many pairs $(m,n)$, $\mathcal{C}'$ is a countable subfamily of $\mathcal{C}$.

To show $\mathcal{C}'$ is a base: Let $U$ be open and $x \in U$. Since $\mathcal{B}$ is a base, there exists $B_n \in \mathcal{B}$ with $x \in B_n \subseteq U$. Since $\mathcal{C}$ is a base, $B_n$ is a union of members of $\mathcal{C}$, so there exists $C \in \mathcal{C}$ with $x \in C \subseteq B_n$. Now express $C$ as a union of members of $\mathcal{B}$: there exists $B_m \in \mathcal{B}$ with $x \in B_m \subseteq C$. Thus $B_m \subseteq C \subseteq B_n$, and the pair $(m,n)$ admits $C$ between them. By construction, $\mathcal{C}'$ contains some member $C'$ with $B_m \subseteq C' \subseteq B_n$, hence $x \in C' \subseteq U$.

Therefore $\mathcal{C}'$ is a countable base contained in $\mathcal{C}$. $\square$
