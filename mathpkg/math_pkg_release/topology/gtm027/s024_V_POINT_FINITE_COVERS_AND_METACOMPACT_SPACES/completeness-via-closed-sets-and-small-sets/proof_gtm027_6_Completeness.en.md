---
role: proof
locale: en
of_concept: completeness-via-closed-sets-and-small-sets
source_book: gtm027
source_chapter: "6"
source_section: "Completeness"
---

# Proof of Completeness via Closed Sets with the Finite Intersection Property (Theorem 6.23)

**Theorem 6.23.** A uniform space is complete if and only if each family of closed sets which has the finite intersection property and contains small sets has a non-void intersection.

**Proof.** ($\Rightarrow$) Let $(X, \mathcal{U})$ be a complete uniform space and $\alpha$ a family of closed sets which has the finite intersection property and contains small sets. Let $\mathcal{F}$ be the family of all finite intersections of members of $\alpha$. Then $\mathcal{F}$ is directed by $\subset$ ($F_1 \geq F_2$ if $F_1 \subset F_2$), and for each $F \in \mathcal{F}$ we may choose a point $x_F \in F$.

The net $\{x_F : F \in \mathcal{F}\}$ is a Cauchy net because: if $A, B \subset F$ (i.e., $A, B$ are members of $\mathcal{F}$ contained in $F$), then $x_A, x_B \in F$. Since $\mathcal{F}$ (and hence $\alpha$) contains small sets, given any $U \in \mathcal{U}$ there exists $F \in \mathcal{F}$ such that $F$ is a subset of $U[x]$ for some $x$; then for all $A, B \subset F$ we have $(x_A, x_B) \in U \circ U^{-1}$ (after adjusting). Thus the net is Cauchy.

Since $X$ is complete, $\{x_F : F \in \mathcal{F}\}$ converges to some point $y \in X$. The net is eventually in each member of $\mathcal{F}$ (when it enters a set $F$, all later terms are in $F$), so $y$ belongs to the closure of each $F \in \mathcal{F}$. Since each member of $\alpha$ is closed, $y \in \bigcap \{A : A \in \alpha\}$. Hence the intersection is non-void.

($\Leftarrow$) Conversely, suppose each family of closed sets with the finite intersection property and containing small sets has non-void intersection. Let $\{x_n : n \in D\}$ be a Cauchy net. For each $n \in D$, let $A_n$ be the set of all points $x_m$ for $m \geq n$. Then the family $\alpha = \{A_n : n \in D\}$ has the finite intersection property (since $D$ is directed), and since the net is Cauchy, $\alpha$ contains small sets (for each $U$ there is $n$ such that $A_n \subset U[x_n]$). Taking closures, the family $\alpha^- = \{\overline{A_n} : n \in D\}$ also has the finite intersection property and contains small sets (each $\overline{A_n}$ is contained in $\overline{U}[x_n] \subset V[x_n]$ for some $V$). By hypothesis, $\bigcap \{\overline{A_n} : n \in D\}$ contains some point $y$, which by construction is a cluster point of the net. Since a Cauchy net with a cluster point converges to that point (Theorem 6.21), the net converges to $y$. Thus $X$ is complete.
