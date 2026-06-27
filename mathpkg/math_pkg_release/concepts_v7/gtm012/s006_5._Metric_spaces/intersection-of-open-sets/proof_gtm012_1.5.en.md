---
role: proof
locale: en
of_concept: intersection-of-open-sets
source_book: gtm012
source_chapter: "1"
source_section: "5. Metric spaces"
---

# Proof of Theorem: Finite Intersection of Open Sets is Open

Suppose $A_1, A_2, \ldots, A_n$ are open subsets of a metric space $(S, d)$. Let $A = \bigcap_{m=1}^{n} A_m$. We must show $A$ is open.

Suppose $x \in A = \bigcap_{m=1}^{n} A_m$. Since each $A_m$ is open, there is $r(m) > 0$ so that $B_{r(m)}(x) \subset A_m$. Let

$$r = \min \{r(1), r(2), \ldots, r(n)\}.$$

Then $r > 0$, and for each $m = 1, \ldots, n$, we have

$$B_r(x) \subset B_{r(m)}(x) \subset A_m.$$

Hence $B_r(x) \subset \bigcap_{m=1}^{n} A_m = A$. Thus $A$ is a neighborhood of each of its points, so $A$ is open. $\square$

(Note: The finiteness of the collection is essential here, for the minimum of infinitely many positive numbers need not be positive; an infinite intersection of open sets need not be open.)
