---
role: proof
locale: en
of_concept: continuous-open-closed-implies-quotient
source_book: gtm027
source_chapter: "3"
source_section: "Quotient Spaces"
---

# Proof of Theorem 8: Continuous Open or Closed Surjection Induces Quotient Topology

**Statement.** If $f$ is a continuous map of the topological space $(X, \mathfrak{I})$ onto the space $(Y, \mathfrak{U})$ such that $f$ is either open or closed, then $\mathfrak{U}$ is the quotient topology.

**Proof.** Suppose first that $f$ is an open map. Let $U \subseteq Y$ be any subset such that $f^{-1}[U]$ is open in $X$. Since $f$ is surjective, $U = f[f^{-1}[U]]$, and because $f$ is open, $U$ is open relative to $\mathfrak{U}$. This shows that every set which is open relative to the quotient topology is also open relative to $\mathfrak{U}$; that is, the quotient topology is smaller than (or equal to) $\mathfrak{U}$. On the other hand, since $f$ is continuous, each $\mathfrak{U}$-open set has open inverse image, hence is open in the quotient topology. Thus $\mathfrak{U}$ coincides with the quotient topology.

The argument for a closed map $f$ is symmetric. If $f$ is closed and $U \subseteq Y$ is such that $f^{-1}[U]$ is open in $X$, then $X \setminus f^{-1}[U] = f^{-1}[Y \setminus U]$ is closed in $X$. Because $f$ is a closed surjection, $f[f^{-1}[Y \setminus U]] = Y \setminus U$ is closed in $Y$, so $U$ is open in $\mathfrak{U}$. Hence each quotient-open set is $\mathfrak{U}$-open. Together with continuity, this yields equality of the two topologies. $\square$
