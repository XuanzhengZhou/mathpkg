---
role: proof
locale: en
of_concept: theorem-prime-ideal-multiplicatively-closed
source_book: gtm043
source_chapter: "0"
source_section: "0.16"
---

By the maximal principle (Hausdorff Maximal Principle, 0.7), there exists a maximal chain $\mathfrak{L}$ of ideals containing $I$ and disjoint from $S$. Define $P = \bigcup \mathfrak{L}$; then $P$ is an ideal containing $I$, disjoint from $S$, and maximal with respect to this property.

Let $a \notin P$ and $b \notin P$. Because of the maximality of $P$, there exist $s, t \in S$ such that $s \in (P, a)$ and $t \in (P, b)$. Then $s \equiv xa \pmod{P}$ and $t \equiv yb \pmod{P}$, for suitable $x, y \in A$. Since $S$ is closed under multiplication, we have
$$st \in S.$$
Now,
$$xyab \equiv st \pmod{P},$$
and since $st \in S$ and $S$ is disjoint from $P$, we have $st \not\equiv 0 \pmod{P}$. Therefore $xyab \not\equiv 0 \pmod{P}$, which implies $ab \notin P$.

This shows that $P$ is prime.
