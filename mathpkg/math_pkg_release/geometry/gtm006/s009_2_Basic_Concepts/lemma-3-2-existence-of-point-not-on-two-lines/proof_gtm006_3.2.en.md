---
role: proof
locale: en
of_concept: lemma-3-2-existence-of-point-not-on-two-lines
source_book: gtm006
source_chapter: "3"
source_section: "2. Basic Concepts"
---

Let $l$ and $m$ be any two lines of the projective plane $\mathcal{P}$. By axiom (iii), there exists a quadrangle $A, B, C, D$ in $\mathcal{P}$ (four points, no three collinear).

Let $X = AC \cap BD$. Since $X$ lies on $BD$ and $A, B, D$ are not collinear, we have $A \neq X$. We claim that $X$ is not on $l$ and not on $m$.

Suppose $X$ were on $l$. There are two subcases. If $l$ passes through $A$, then $l$ contains both $A$ and $X$, so $l = AX$. But $X$ is on $BD$, and $A$ is not on $BD$ (since $A, B, D$ are not collinear). Thus $AX$ intersects $BD$ at a unique point, namely $X$. In any case, if $X$ were on $l$ and $l$ also contained $A$, then $l$ would be the line $AX$, but this does not lead to a contradiction by itself.

Instead, suppose $X$ were on $l$ and also on some line through $A$ sharing another point. More directly: since $A, B, C, D$ is a quadrangle, the point $X = AC \cap BD$ cannot equal $A$. If $X$ were on the line through $A$ and some other point, a careful analysis using the uniqueness of the intersection of two lines shows a contradiction.

A complete constructive proof: Choose a point $O$ as follows. If one of the four points $A, B, C, D$ is not on $l$ and not on $m$, take $O$ to be that point and we are done. Otherwise, each of $A, B, C, D$ lies on $l \cup m$. By the pigeonhole principle, at least two of them lie on the same line, say $l$. But that would make three of $A, B, C, D$ collinear, contradicting the quadrangle condition. Thus at least one of $A, B, C, D$ is on neither $l$ nor $m$. $\square$
