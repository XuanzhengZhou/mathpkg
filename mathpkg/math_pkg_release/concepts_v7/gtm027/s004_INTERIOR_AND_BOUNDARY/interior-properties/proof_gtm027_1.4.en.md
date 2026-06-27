---
role: proof
locale: en
of_concept: interior-properties
source_book: gtm027
source_chapter: "1"
source_section: "Interior and Boundary"
---

# Proof of Properties of the Interior (Theorem 9)

Let $A$ be a subset of a topological space $X$.

**1. $A^0$ is open.** If a point $x$ belongs to the interior $A^0$ of $A$, then $x$ is a member of some open subset $U$ of $A$. Every member of $U$ is also a member of $A^0$ (since $U$ is a neighborhood of each of its points, hence each point of $U$ has $A$ as a neighborhood). Consequently $A^0$ contains a neighborhood of each of its points and is therefore open.

**2. $A^0$ is the largest open subset of $A$.** If $V$ is an open subset of $A$ and $y \in V$, then $A$ is a neighborhood of $y$ and so $y \in A^0$. Hence $A^0$ contains each open subset of $A$, and it is therefore the largest open subset of $A$.

**3. $A$ is open iff $A = A^0$.** If $A$ is open, then $A$ is surely identical with the largest open subset of $A$; hence $A$ is open iff $A = A^0$.

**4. $A^0$ equals the set of points of $A$ which are not accumulation points of $X \sim A$.** If $x$ is a point of $A$ which is not an accumulation point of $X \sim A$, then there is a neighborhood $U$ of $x$ which does not intersect $X \sim A$ and is therefore a subset of $A$. Then $A$ is a neighborhood of $x$ and $x \in A^0$. Conversely, if $x \in A^0$, then $A$ is a neighborhood of $x$, so there exists an open set $U$ with $x \in U \subseteq A$. Then $U \cap (X \sim A) = \varnothing$, so $x$ is not an accumulation point of $X \sim A$. Thus $A^0$ is precisely the set of all points of $A$ which are not points of accumulation of $X \sim A$.

**5. The closure of $X \sim A$ is $X \sim A^0$.** Denote the relative complement $X \sim A$ by $A'$. From part (4), $A^0$ consists exactly of those points of $A$ that are not accumulation points of $A'$. Hence the points not in $A^0$ are exactly the points of $A'$ together with the accumulation points of $A'$, which is precisely the closure $(A')^- = (X \sim A)^-$. Therefore $(X \sim A)^- = X \sim A^0$. $\square$
