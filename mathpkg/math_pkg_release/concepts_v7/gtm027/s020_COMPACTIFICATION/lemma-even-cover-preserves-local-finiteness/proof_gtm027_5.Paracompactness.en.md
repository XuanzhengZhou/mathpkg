---
role: proof
locale: en
of_concept: lemma-even-cover-preserves-local-finiteness
source_book: gtm027
source_chapter: "5"
source_section: "Paracompactness"
---

# Proof that Even Cover Spaces Preserve Local Finiteness Under Diagonal Enlargement

**Lemma 31.** Let $X$ be a topological space such that each open cover is even, and let $\mathcal{A}$ be a locally finite (respectively, a discrete) family of subsets of $X$. Then there exists a neighborhood $V$ of the diagonal $\Delta$ in $X \times X$ such that the family $\{V[A] : A \in \mathcal{A}\}$ is locally finite (respectively discrete), where $V[A] = \{y \in X : (x,y) \in V \text{ for some } x \in A\}$.

*Proof.* We prove the locally finite case; the discrete case follows by a similar argument.

**Step 1: Construct an open cover detecting local finiteness.** Since $\mathcal{A}$ is locally finite, there exists an open cover $\mathcal{U}$ of $X$ such that each member of $\mathcal{U}$ intersects only finitely many members of $\mathcal{A}$. (Take $\mathcal{U}$ to be the collection of all open sets whose closures intersect only finitely many $A \in \mathcal{A}$, or use the definition: for each $x$, pick a neighborhood intersecting only finitely many $A$.)

**Step 2: Apply the even cover property.** By hypothesis, the open cover $\mathcal{U}$ is even. Hence there exists a neighborhood $U$ of the diagonal such that for each $z \in X$, the set $U[z] = \{y : (z,y) \in U\}$ is contained in some member of $\mathcal{U}$. Consequently, each $U[z]$ intersects only finitely many members of $\mathcal{A}$.

**Step 3: Apply Lemma 30.** By Lemma 30 (which uses the hypothesis that each open cover is even), there exists a symmetric neighborhood $V$ of the diagonal such that $V \circ V \subset U$. Recall that $V \circ V = \{(x,z) : \exists y \in X \text{ with } (x,y) \in V \text{ and } (y,z) \in V\}$.

**Step 4: Verify local finiteness of $\{V[A] : A \in \mathcal{A}\}$.** Each $V[A]$ is open because $V[A] = \bigcup_{x \in A} V[x]$, and each $V[x]$ is open (sections of an open set are open). Fix $z \in X$. Suppose $V[z] \cap V[A] \neq \emptyset$ for some $A \in \mathcal{A}$. Then there exist $x \in V[z]$ and $y \in A$ with $(y, x) \in V$ (since $x \in V[A]$ means there is some $a \in A$ with $(a, x) \in V$, so by symmetry $x \in V[A]$ iff $\exists a \in A$ with $(a, x) \in V$, i.e., $x \in V^{-1}[A] = V[A]$). Actually, more directly: if $x \in V[z] \cap V[A]$, then $(z, x) \in V$ and $(y, x) \in V$ for some $y \in A$. By symmetry, $(x, y) \in V$, so $(z, y) \in V \circ V \subset U$. Hence $y \in U[z] \cap A$.

Thus $V[z] \cap V[A] \neq \emptyset$ implies $A \cap U[z] \neq \emptyset$. Since $U[z]$ meets only finitely many $A \in \mathcal{A}$, the same holds for $V[z]$ intersecting the sets $V[A]$. Therefore $\{V[A] : A \in \mathcal{A}\}$ is locally finite.

**For the discrete case:** When $\mathcal{A}$ is discrete, the open cover $\mathcal{U}$ can be chosen so that each member meets at most one $A \in \mathcal{A}$. The same argument then shows that each $V[z]$ meets $V[A]$ for at most one $A$, i.e., $\{V[A]\}$ is discrete. $\square$

*Remark.* This lemma is the crucial step in closing the cycle $(b) \Rightarrow (a)$ in Theorem 28. Given a locally finite refinement from $(b)$, Lemma 31 enlarges it to an *open* locally finite family (the sets $V[A]$), which after intersecting with members of the original cover yields an open locally finite refinement. This proves paracompactness.
