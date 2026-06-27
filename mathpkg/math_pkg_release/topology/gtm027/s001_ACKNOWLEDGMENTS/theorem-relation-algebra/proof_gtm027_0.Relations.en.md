---
role: proof
locale: en
of_concept: theorem-relation-algebra
source_book: gtm027
source_chapter: "0"
source_section: "Relations"
---

# Proof of Theorem 5: Algebra of Relations

**Proof of (a).** By definition, $(x,y) \in (R^{-1})^{-1}$ iff $(y,x) \in R^{-1}$ iff $(x,y) \in R$. Hence $(R^{-1})^{-1} = R$. For the second identity: $(x,y) \in (R \circ S)^{-1}$ iff $(y,x) \in R \circ S$, which holds iff there exists $z$ such that $(y,z) \in S$ and $(z,x) \in R$. This is equivalent to: there exists $z$ such that $(z,y) \in S^{-1}$ and $(x,z) \in R^{-1}$, i.e., $(x,y) \in S^{-1} \circ R^{-1}$. Hence $(R \circ S)^{-1} = S^{-1} \circ R^{-1}$.

**Proof of (b).** $(x,y) \in R \circ (S \circ T)$ iff there exists $u$ such that $(x,u) \in S \circ T$ and $(u,y) \in R$. But $(x,u) \in S \circ T$ iff there exists $v$ such that $(x,v) \in T$ and $(v,u) \in S$. Hence $(x,y) \in R \circ (S \circ T)$ iff there exist $u$ and $v$ with $(x,v) \in T$, $(v,u) \in S$, $(u,y) \in R$. This is equivalent to: there exists $v$ with $(x,v) \in T$ and $(v,y) \in R \circ S$, i.e., $(x,y) \in (R \circ S) \circ T$. Hence $R \circ (S \circ T) = (R \circ S) \circ T$.

For the second identity: $y \in (R \circ S)[A]$ iff there exists $x \in A$ with $(x,y) \in R \circ S$, i.e., there exist $x \in A$ and $z$ such that $(x,z) \in S$ and $(z,y) \in R$. This is equivalent to: there exists $z \in S[A]$ such that $(z,y) \in R$, i.e., $y \in R[S[A]]$. Hence $(R \circ S)[A] = R[S[A]]$.

**Proof of (c).** $y \in R[A \cup B]$ iff there exists $x \in A \cup B$ with $(x,y) \in R$, which holds iff $x \in A$ or $x \in B$ and $(x,y) \in R$. This is the case iff $y \in R[A]$ or $y \in R[B]$, i.e., $y \in R[A] \cup R[B]$. Hence $R[A \cup B] = R[A] \cup R[B]$.

For the second identity: $y \in R[A \cap B]$ iff there exists $x \in A \cap B$ with $(x,y) \in R$. Then $x \in A$ and $x \in B$, so $y \in R[A]$ and $y \in R[B]$. Hence $y \in R[A] \cap R[B]$. This shows $R[A \cap B] \subset R[A] \cap R[B]$. (Equality does not hold in general; a single $y$ could be the $R$-image of a point in $A$ and of a different point in $B$, without being the $R$-image of any point in $A \cap B$.)
