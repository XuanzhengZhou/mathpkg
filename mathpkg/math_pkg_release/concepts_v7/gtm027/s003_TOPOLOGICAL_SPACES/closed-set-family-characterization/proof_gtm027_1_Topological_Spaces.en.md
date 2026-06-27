---
role: proof
locale: en
of_concept: closed-set-family-characterization
source_book: gtm027
source_chapter: "1"
source_section: "Topological Spaces"
---

# Proof of Characterization of the Family of Closed Sets

**Theorem.** Let $\mathfrak{F}$ be a family of subsets of a set $X$ such that:

1. The union of any finite subfamily of $\mathfrak{F}$ is a member of $\mathfrak{F}$;
2. The intersection of any arbitrary non-void subfamily of $\mathfrak{F}$ is a member of $\mathfrak{F}$;
3. $X = \bigcup \{F : F \in \mathfrak{F}\} \in \mathfrak{F}$ (equivalently, $X \in \mathfrak{F}$).

Then $\mathfrak{F}$ is precisely the family of closed sets in $X$ relative to the topology $\mathfrak{J} = \{X \setminus F : F \in \mathfrak{F}\}$.

*Proof.* Define $\mathfrak{J} = \{X \setminus F : F \in \mathfrak{F}\}$. We verify that $\mathfrak{J}$ is a topology on $X$.

Since $\mathfrak{F}$ contains $X$ (by condition 3), we have $\emptyset = X \setminus X \in \mathfrak{J}$. Also $X = X \setminus \emptyset$, and the void intersection over the empty family (or condition 3) ensures the void set belongs to $\mathfrak{F}$, so $X \in \mathfrak{J}$.

Let $\{U_\alpha\}$ be an arbitrary subfamily of $\mathfrak{J}$. For each $\alpha$, $U_\alpha = X \setminus F_\alpha$ with $F_\alpha \in \mathfrak{F}$. Then

$$\bigcup_\alpha U_\alpha = \bigcup_\alpha (X \setminus F_\alpha) = X \setminus \bigcap_\alpha F_\alpha.$$

Since $\bigcap_\alpha F_\alpha \in \mathfrak{F}$ (by condition 2, if the family is non-void; if void, the union is $\emptyset \in \mathfrak{J}$), we have $\bigcup_\alpha U_\alpha \in \mathfrak{J}$.

Let $U_1, \ldots, U_n$ be a finite subfamily of $\mathfrak{J}$, with $U_i = X \setminus F_i$, $F_i \in \mathfrak{F}$. Then

$$U_1 \cap \cdots \cap U_n = (X \setminus F_1) \cap \cdots \cap (X \setminus F_n) = X \setminus (F_1 \cup \cdots \cup F_n).$$

By condition 1, $F_1 \cup \cdots \cup F_n \in \mathfrak{F}$, hence $U_1 \cap \cdots \cap U_n \in \mathfrak{J}$.

Thus $\mathfrak{J}$ is a topology on $X$. By construction, the closed sets relative to $\mathfrak{J}$ are precisely the complements of members of $\mathfrak{J}$, i.e., the members of $\mathfrak{F}$. $\square$
