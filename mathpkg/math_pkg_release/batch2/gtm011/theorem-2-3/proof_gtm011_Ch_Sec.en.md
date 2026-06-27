---
role: proof
locale: en
of_concept: theorem-2-3
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Suppose that $G$ satisfies this condition and let us assume that $G$ is not connected. We will obtain a contradiction. From the definition, $G = A \cup B$ where $A$ and $B$ are both open and closed, $A \cap B = \square$, and neither $A$ nor $B$ is empty. Let $a \in A$ and $b \in B$; by hypothesis there is a polygon $P$ from $a$ to $b$ such that $P \subset G$. Now a moment's thought will show that one of the segments making up $P$ will have one end point in $A$ and another in $B$. So we can assume that $P = [a, b]$.

$$S = \{s \in [0, 1] : sb + (1-s)a \in A\}$$

$$T = \{t \in [0, 1] : tb + (1-t)a \in B\}$$

Then $S \cap T = \square$, $S \cup T = [0, 1], 0 \in S$ and $1 \in T$. However it can be shown that both $S$ and $T$ are open (Exercise 2), contradicting the connectedness of $[0

polygon in $G$ from $a$ to $b$ and then modify each of its line segments so that a new polygon is obtained with the desired properties. However, this proof is more easily executed using compactness (see Exercise 5.7). Another proof can be obtained by modifying the proof of Theorem 2.3. Define the set $A$ as in the proof of (2.3) but add the restriction that the polygon’s segments are all parallel to one of the axes. The remainder of the proof will be valid with one exception. If $z \in B(b; \epsilon)$ then $[b, z]$ may not be parallel to an axis. But it is easy to see that if $z = x + iy$, $b = p + iq$ then the polygon $[b, p + iy] \cup [p + iy, z] \subset B(b; \epsilon)$ and has segments parallel to an axis.

It will now be shown that any set $S$ in a metric space can be expressed, in a canonical way, as the union of connected pieces.
