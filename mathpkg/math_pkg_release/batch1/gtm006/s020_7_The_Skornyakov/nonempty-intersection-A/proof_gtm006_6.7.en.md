---
role: proof
locale: en
of_concept: intersection-of-associator-subgroups
source_book: gtm006
source_chapter: "6"
source_section: "7. The Skornyakov-San Soucie Theorem"
---

Let $x \in A(a, b) \cap A(a, ba)$. Since $x \in A(a, b)$, by (5) $(xa)b = x(ba)$, and hence by the Moufang identity (M):
$$x((ab)a) = ((xa)b)a = (x(ba))a.$$

Since $x \in A(a, ba) = A(ba, a)$ by (5)(iv), we have $(x(ba))a = x(a(ba))$. Therefore
$$0 = (x(ba))a - (x(ba))a = x((ab)a) - x(a(ba)) = x[a, a, b] = -x[a, a, b].$$

Since $[a, a, b] \neq 0$ by hypothesis and $D$ is a division ring, this forces $x = 0$. $\square$
