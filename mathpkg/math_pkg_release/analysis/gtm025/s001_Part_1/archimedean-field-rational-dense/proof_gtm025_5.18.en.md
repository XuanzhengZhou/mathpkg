---
role: proof
locale: en
of_concept: archimedean-field-rational-dense
source_book: gtm025
source_chapter: "5"
source_section: "5.18"
---

Since $b - a > 0$, we have $(b - a)^{-1} > 0$; and so, since $F$ is Archimedean ordered, there is a positive integer $n$ such that $n \cdot 1 > (b-a)^{-1}$, i.e., $\frac{1}{n} < b - a$.

Since $\frac{1}{n} > 0$ and $F$ is Archimedean ordered, we have $S = \{k \in Z : \frac{k}{n} > a\} \neq \varnothing$. Also, again by the Archimedean order property of $F$, there is a positive integer $p$ such that $p \frac{1}{n} > -a$, hence $(-p) \frac{1}{n} < a$.

It follows that $-p, -(p+1), -(p+2), \ldots$ lie outside of $S$. Hence $S$ is a nonvoid set of integers which is bounded below, and so it contains a least element $m$. Since $m \in S$, we have $a < \frac{m}{n}$.

Since $m-1 \notin S$, we have $\frac{m-1}{n} \leq a$; and so
$$\frac{m}{n} = \frac{m-1}{n} + \frac{1}{n} \leq a + \frac{1}{n} < a + (b-a) = b;$$
i.e., $a < \frac{m}{n} < b$.
