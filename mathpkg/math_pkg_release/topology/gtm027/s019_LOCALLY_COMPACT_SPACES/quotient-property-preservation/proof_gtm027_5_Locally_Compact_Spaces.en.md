---
role: proof
locale: en
of_concept: quotient-property-preservation
source_book: gtm027
source_chapter: "5"
source_section: "Locally Compact Spaces"
---

# Proof of Quotient Space Preservation of Properties (Theorem 20)

Let $X$ be a topological space, let $\mathfrak{D}$ be an upper semi-continuous decomposition of $X$ whose members are compact, and let $\mathfrak{D}$ have the quotient topology (denoted also by $\mathfrak{D}$). Let $P: X \to \mathfrak{D}$ be the natural projection.

Define a subset of $X$ to be **admissible** iff it is the union of members of $\mathfrak{D}$ (equivalently, it is $P^{-1}(P(E))$ for some $E \subset X$).

## Preliminary Observations

By the definition of upper semi-continuity, each neighborhood in $X$ of a member $A \in \mathfrak{D}$ contains an admissible neighborhood. Consequently, the image under projection of a neighborhood of $A$ in $X$ is a neighborhood of $A$ in $\mathfrak{D}$. Moreover, by 3.12, the projection $P$ is a closed map.

## Hausdorff Property

Suppose $X$ is Hausdorff and let $A, B \in \mathfrak{D}$ be distinct. Since $A$ and $B$ are disjoint compact subsets of the Hausdorff space $X$, by Theorem 5.9 there exist disjoint neighborhoods $U$ and $V$ (in $X$) of $A$ and $B$ respectively. By upper semi-continuity, $U$ contains an admissible neighborhood $U'$ of $A$, and $V$ contains an admissible neighborhood $V'$ of $B$. Then $P(U')$ and $P(V')$ are disjoint neighborhoods of $A$ and $B$ in $\mathfrak{D}$. Hence $\mathfrak{D}$ is Hausdorff.

## Regularity

Suppose $X$ is regular. Let $A \in \mathfrak{D}$ and let $u$ be a neighborhood of $A$ in $\mathfrak{D}$. Then $U = P^{-1}(u)$ is an admissible neighborhood of $A$ in $X$. Since $X$ is regular, by Theorem 5.10 there exists a closed neighborhood $V$ of $A$ in $X$ with $V \subset U$. Since $P$ is closed, $P(V)$ is a closed subset of $\mathfrak{D}$, and $P(V)$ is a neighborhood of $A$ in $\mathfrak{D}$ (as it contains the image of the interior of $V$). Moreover, $P(V) \subset P(U) = u$. Thus $\mathfrak{D}$ is regular.

## Local Compactness

Suppose $X$ is locally compact. Let $A \in \mathfrak{D}$. Since $A$ is compact, by Theorem 5.10 (or more directly, covering $A$ with compact neighborhoods of its points and taking a finite subcover) there exists a compact neighborhood $C$ of $A$ in $X$. By upper semi-continuity, $C$ contains an admissible neighborhood $W$ of $A$. Then $P(C)$ is compact (continuous image of compact), and $P(W)$ is an open neighborhood of $A$ in $\mathfrak{D}$ contained in $P(C)$. Hence $\mathfrak{D}$ is locally compact.

## Second Axiom of Countability

Suppose $X$ satisfies the second axiom of countability (i.e., has a countable base). Let $\mathcal{B}$ be a countable base for $X$. Consider the family $\mathcal{B}'$ of all finite unions of members of $\mathcal{B}$ that are admissible. Since $\mathcal{B}$ is countable, $\mathcal{B}'$ is also countable. The images under $P$ of the interiors of members of $\mathcal{B}'$ form a countable family of open sets in $\mathfrak{D}$. We claim this family is a base for $\mathfrak{D}$. Let $u$ be an open neighborhood of $A \in \mathfrak{D}$. Then $P^{-1}(u)$ is an admissible open neighborhood of $A$. Each point of $A$ has a basic neighborhood (from $\mathcal{B}$) contained in $P^{-1}(u)$. Since $A$ is compact, finitely many such basic neighborhoods cover $A$; their union $B$ is admissible, belongs to $\mathcal{B}'$, and satisfies $A \subset B^0 \subset B \subset P^{-1}(u)$. Then $P(B^0)$ is a basic open set in $\mathfrak{D}$ containing $A$ and contained in $u$. Hence $\mathfrak{D}$ has a countable base.

This completes the proof of all four properties. $\square$
