---
role: proof
locale: en
of_concept: hausdorff-quotient-and-closed-relation
source_book: gtm027
source_chapter: "3"
source_section: "Quotient Spaces"
---

# Proof of Theorem 11: Hausdorff Quotient Space and Closed Equivalence Relation

**Theorem 11.** Let $X$ be a topological space, $R$ an equivalence relation on $X$, and $P: X \to X/R$ the quotient projection.

1. If the quotient space $X/R$ is Hausdorff, then $R$ is closed in the product space $X \times X$.

2. If the projection $P$ is open and $R$ is closed in $X \times X$, then $X/R$ is Hausdorff.

**Proof.**

(1) Suppose $X/R$ is Hausdorff. Let $(x,y) \in X \times X$ be a point not in $R$; that is, $x$ and $y$ are not $R$-related. Then $P(x) \neq P(y)$ in $X/R$. Since $X/R$ is Hausdorff, there exist disjoint open neighborhoods $W_1$ and $W_2$ of $P(x)$ and $P(y)$ respectively. By continuity of $P$, the sets $U = P^{-1}[W_1]$ and $V = P^{-1}[W_2]$ are open neighborhoods of $x$ and $y$ in $X$. Moreover, $U \times V$ is disjoint from $R$: if there existed $(u,v) \in R \cap (U \times V)$, then $P(u) = P(v)$ would lie in $W_1 \cap W_2$, contradicting disjointness. Thus $(x,y)$ has a neighborhood $U \times V$ not intersecting $R$, showing $R$ is closed.

(2) Suppose $P$ is open and $R$ is closed in $X \times X$. Let $P(x)$ and $P(y)$ be distinct points of $X/R$. Then $(x,y) \notin R$. Since $R$ is closed, there exists a basic open neighborhood $U \times V$ of $(x,y)$ in $X \times X$ disjoint from $R$, where $U$ and $V$ are open neighborhoods of $x$ and $y$ respectively. The condition $U \times V \cap R = \varnothing$ means that no point of $U$ is $R$-related to any point of $V$; equivalently, no member of $X/R$ intersects both $U$ and $V$. Hence the images $P[U]$ and $P[V]$ are disjoint. Since $P$ is open, $P[U]$ and $P[V]$ are open neighborhoods of $P(x)$ and $P(y)$ respectively. Thus $X/R$ is Hausdorff. $\square$
