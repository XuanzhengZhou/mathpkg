---
role: proof
locale: en
of_concept: convex-hull-of-precompact-is-precompact
source_book: gtm003
source_chapter: "II"
source_section: "4.3"
---

Since the circled hull of a precompact set is clearly precompact (cf. Chapter I, 5.1), it is enough to prove the assertion for convex hulls.

Observe first that the convex hull $P$ of a finite set $\{a_i: i=1, \ldots, n\}$ is compact, for $P$ is the image of the compact simplex $\{(\lambda_1, \ldots, \lambda_n): \lambda_i \geq 0, \sum_{i=1}^{n} \lambda_i = 1\} \subset \mathbb{R}^n$ under the continuous map $(\lambda_1, \ldots, \lambda_n) \rightarrow \sum \lambda_i a_i$. (This is a special case of (10.2) below.)

Now let $B \subset E$ be precompact. Given any convex 0-neighborhood $V$, there exists a finite set $F \subset B$ such that $B \subset F + V$. Let $P_F$ be the convex hull of $F$; $P_F$ is compact by the observation above. The convex hull $\operatorname{co}(B)$ satisfies $\operatorname{co}(B) \subset P_F + V$, showing that $\operatorname{co}(B)$ can be covered by finitely many translates of $V$. Since $V$ was arbitrary, $\operatorname{co}(B)$ is precompact.
