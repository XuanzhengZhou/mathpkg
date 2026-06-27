---
role: proof
locale: en
of_concept: coset-lemma
source_book: gtm077
source_chapter: "II"
source_section: "6"
---

# Proof: Disjointness of Cosets

Let $\mathfrak{G}$ be a group and $\mathfrak{U}$ a subgroup. For $A, B \in \mathfrak{G}$, define the left cosets

$$A\mathfrak{U} = \{AU : U \in \mathfrak{U}\}, \quad B\mathfrak{U} = \{BU : U \in \mathfrak{U}\}.$$

**Lemma.** Two cosets of a subgroup are either disjoint or identical.

**Proof.** Suppose $A\mathfrak{U} \cap B\mathfrak{U} \neq \emptyset$. Then there exist $U_1, U_2 \in \mathfrak{U}$ such that $AU_1 = BU_2$. Hence $B = A U_1 U_2^{-1}$.

Now for any $U \in \mathfrak{U}$,

$$BU = A U_1 U_2^{-1} U \in A\mathfrak{U}$$

since $U_1 U_2^{-1} U \in \mathfrak{U}$. Thus $B\mathfrak{U} \subseteq A\mathfrak{U}$.

By symmetry, $A = B U_2 U_1^{-1}$, so $A\mathfrak{U} \subseteq B\mathfrak{U}$. Therefore $A\mathfrak{U} = B\mathfrak{U}$.

This shows that the relation $A \sim B \iff A\mathfrak{U} = B\mathfrak{U}$ is an equivalence relation on $\mathfrak{G}$, and the cosets are the equivalence classes. Hence the distinct cosets form a partition of the group $\mathfrak{G}$.

**Application.** This lemma is the foundation for Lagrange's Theorem: if $\mathfrak{G}$ is finite of order $h$ and $\mathfrak{U}$ has order $N$, then the group is partitioned into $j$ disjoint cosets each of size $N$, yielding $h = j \cdot N$. ∎
