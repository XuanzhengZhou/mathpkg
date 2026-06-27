---
role: proof
locale: en
of_concept: open-closed-projection-characterization
source_book: gtm027
source_chapter: "3"
source_section: "Quotient Spaces"
---

# Proof of Theorem 10: Characterization of Open and Closed Quotient Projections

**Statement.** Let $P$ be the projection of the topological space $X$ onto the quotient space $X/R$. Then the following statements are equivalent.

(a) $P$ is an open mapping.

(b) If $A$ is an open subset of $X$, then $R[A]$ is open.

(c) If $A$ is a closed subset of $X$, then the union of all members of $X/R$ which are subsets of $A$ is closed.

If "open" and "closed" are interchanged in (a), (b), and (c), the resulting statements are equivalent.

**Proof of the open version.** We first show (a) $\Leftrightarrow$ (b). For each subset $A$ of $X$, the set $R[A] = P^{-1}[P[A]]$. Since $P$ is continuous, the openness of $P[A]$ implies the openness of $R[A]$, so (a) $\Rightarrow$ (b). Conversely, if $R[A]$ is open whenever $A$ is open, then because $P$ is a quotient map, $P[A]$ is open in $X/R$ iff $P^{-1}[P[A]] = R[A]$ is open in $X$. Hence (b) $\Rightarrow$ (a).

Next, (a) $\Leftrightarrow$ (c). Suppose (a) holds and $A$ is closed in $X$. The union of all members of $X/R$ contained in $A$ is precisely $P^{-1}[P[A]]$, where by definition of the one-point compactification of $A$ in the quotient, this union equals $R[A]$. Actually, note that the union of members of $X/R$ contained in $A$ is the complement of $R[X \setminus A]$. Since $X \setminus A$ is open, $R[X \setminus A]$ is open by (b), so its complement is closed. Thus (a) $\Rightarrow$ (c). Conversely, if (c) holds and $A$ is open, then $X \setminus A$ is closed. The union of all members of $X/R$ contained in $X \setminus A$ is closed by (c), and its complement is precisely $R[A]$, which is therefore open. By (b) $\Rightarrow$ (a), we obtain (c) $\Rightarrow$ (a).

**Proof of the closed version.** The interchanged statements are:

(a$'$) $P$ is a closed mapping.

(b$'$) If $A$ is a closed subset of $X$, then $R[A]$ is closed.

(c$'$) If $A$ is an open subset of $X$, then the union of all members of $X/R$ which are subsets of $A$ is open.

The equivalence (a$'$) $\Leftrightarrow$ (b$'$) follows exactly as in the open case, replacing "open" by "closed." For (a$'$) $\Leftrightarrow$ (c$'$): if $P$ is closed and $A$ is open, then $X \setminus A$ is closed, so $R[X \setminus A]$ is closed by (b$'$). The union of members of $X/R$ contained in $A$ is $X \setminus R[X \setminus A]$, which is open. The converse is analogous. $\square$
