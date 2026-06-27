---
role: proof
locale: en
of_concept: elementary-properties-of-faces
source_book: gtm015
source_chapter: "36. Extremal points of a convex set; Krein-Mil'man theorem"
source_section: "36"
---

# Proof of Elementary properties of faces

Let $E$ be a vector space over $\mathbb{K}$ and $A \subset E$ a convex set. Recall (36.3) that a convex subset $F \subset A$ is a **face** of $A$ if

$$\langle u, v \rangle \subset A,\ \langle u, v \rangle \cap F \neq \varnothing \implies \langle u, v \rangle \subset F.$$

**Property (1).** $A$ is a face of itself.

*Proof.* If $\langle u, v \rangle \subset A$ and $\langle u, v \rangle \cap A \neq \varnothing$, then trivially $\langle u, v \rangle \subset A$. Thus $A$ satisfies the definition of a face of itself. $\square$

**Property (2).** Let $(F_i)_{i \in I}$ be a family of faces of $A$ with $\bigcap_{i \in I} F_i \neq \varnothing$. Then $\bigcap_{i \in I} F_i$ is a face of $A$.

*Proof.* The intersection is convex (intersection of convex sets) and is contained in $A$. Suppose $\langle u, v \rangle \subset A$ and $\langle u, v \rangle \cap \big( \bigcap_i F_i \big) \neq \varnothing$. Then for each $i \in I$, $\langle u, v \rangle \cap F_i \neq \varnothing$. Since each $F_i$ is a face of $A$, we obtain $\langle u, v \rangle \subset F_i$ for every $i \in I$. Hence $\langle u, v \rangle \subset \bigcap_i F_i$. $\square$

**Property (3).** If $F$ is a face of $A$ and $G$ is a face of $F$, then $G$ is a face of $A$.

*Proof.* $G$ is convex and $G \subset F \subset A$. Suppose $\langle u, v \rangle \subset A$ and $\langle u, v \rangle \cap G \neq \varnothing$. Then $\langle u, v \rangle \cap F \neq \varnothing$ (since $G \subset F$). Because $F$ is a face of $A$, we have $\langle u, v \rangle \subset F$. Now $\langle u, v \rangle \subset F$ and $\langle u, v \rangle \cap G \neq \varnothing$; since $G$ is a face of $F$, it follows that $\langle u, v \rangle \subset G$. Hence $G$ is a face of $A$. $\square$
