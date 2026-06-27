---
role: proof
locale: en
of_concept: upper-semicontinuous-iff-closed-projection
source_book: gtm027
source_chapter: "3"
source_section: "Quotient Spaces"
---

# Proof of Theorem 12: Upper Semi-continuity Equivalent to Closed Projection

**Statement.** A decomposition $\mathfrak{D}$ of a topological space $X$ is upper semi-continuous if and only if the projection $P$ of $X$ onto $\mathfrak{D}$ is closed.

**Proof.** Recall that $\mathfrak{D}$ is upper semi-continuous iff for each $D \in \mathfrak{D}$ and each open set $U$ containing $D$, there exists an open set $V$ such that $D \subset V \subset U$ and $V$ is the union of members of $\mathfrak{D}$.

According to Theorem 10 (the closed version), $P$ is a closed map iff for each open subset $U$ of $X$, the union $V$ of all members of $\mathfrak{D}$ which are subsets of $U$ is an open set.

($\Rightarrow$) Suppose $P$ is closed. Let $D \in \mathfrak{D}$ and let $U$ be an open set containing $D$. Let $V$ be the union of all members of $\mathfrak{D}$ which are subsets of $U$. By the characterization from Theorem 10 (condition (c$'$)), $V$ is open. Moreover, $D \subset V \subset U$ and $V$ is a union of members of $\mathfrak{D}$. Thus $\mathfrak{D}$ is upper semi-continuous.

($\Leftarrow$) Suppose $\mathfrak{D}$ is upper semi-continuous and let $U$ be an open subset of $X$. Let $V$ be the union of all members of $\mathfrak{D}$ which are subsets of $U$. To apply Theorem 10, we must show $V$ is open. Let $x \in V$; then $x \in D \subset U$ for some $D \in \mathfrak{D}$. By upper semi-continuity, there exists an open set $W$, itself a union of members of $\mathfrak{D}$, such that $D \subset W \subset U$. Since $W$ consists of members of $\mathfrak{D}$ each contained in $U$, we have $W \subset V$. Hence $V$ is a neighborhood of $x$. As $x$ was arbitrary, $V$ is a neighborhood of each of its points, so $V$ is open. By Theorem 10 (condition (c$'$)), $P$ is a closed map. $\square$
