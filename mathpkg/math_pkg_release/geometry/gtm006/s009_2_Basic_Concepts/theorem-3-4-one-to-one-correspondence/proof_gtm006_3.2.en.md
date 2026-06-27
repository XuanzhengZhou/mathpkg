---
role: proof
locale: en
of_concept: theorem-3-4-one-to-one-correspondence
source_book: gtm006
source_chapter: "3"
source_section: "2. Basic Concepts"
---

**Part (a).** Let $l$ and $m$ be any two lines of $\mathcal{P}$. By Lemma 3.2, there exists a point $O$ not on $l$ and not on $m$. Define a map $\alpha$ from the points of $l$ to the points of $m$ as follows: for any point $X$ on $l$, let
\[
X^* = OX \cap m.
\]
Since $O$ and $X$ determine a unique line $OX$, and $OX$ meets $m$ in a unique point (axiom (ii)), $X^*$ is well-defined. Moreover, $X^*$ lies on $m$ because it is the intersection of $OX$ with $m$.

To show $\alpha$ is injective: if $X_1^* = X_2^*$ for $X_1, X_2$ on $l$, then $OX_1 \cap m = OX_2 \cap m$. Since $O$ is not on $m$, the line through $O$ and this common intersection point must be unique, so $OX_1 = OX_2$. Intersecting with $l$ gives $X_1 = X_2$.

To show $\alpha$ is surjective: for any $Y$ on $m$, let $Z = OY \cap l$. Then $Z^* = OZ \cap m = OY \cap m = Y$ (since $Y$ is on both $OY$ and $m$). So $Y = Z^*$.

Thus $\alpha$ is a bijection between the point sets of $l$ and $m$.

**Part (b).** Let $P$ be any point and $l$ any line. There are two cases.

*Case (a): $P$ is not on $l$.* For any $X$ on $l$, define $X^* = PX$ (the line joining $P$ and $X$). This gives a map from points of $l$ to lines through $P$. If $X_1^* = X_2^*$, then $PX_1 = PX_2$, so this line meets $l$ in both $X_1$ and $X_2$, forcing $X_1 = X_2$ (injectivity). For any line $h$ through $P$, let $X = h \cap l$; then $X^* = PX = h$, proving surjectivity. Hence $\alpha$ is a bijection.

*Case (b): $P$ is on $l$.* Since $\mathcal{P}$ contains a quadrilateral, there exists a line $m$ such that $P$ is not on $m$. By Case (a), there is a bijection between the lines through $P$ and the points of $m$, and by Part (a), there is a bijection between the points of $m$ and the points of $l$. Composing these gives the desired bijection. $\square$
