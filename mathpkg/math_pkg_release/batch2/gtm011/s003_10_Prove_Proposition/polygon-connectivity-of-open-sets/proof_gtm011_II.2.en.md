---
role: proof
locale: en
of_concept: polygon-connectivity-of-open-sets
source_book: gtm011
source_chapter: "II"
source_section: "2"
---

Suppose that $G$ satisfies this condition and let us assume that $G$ is not connected. We will obtain a contradiction. From the definition, $G = A \cup B$ where $A$ and $B$ are both open and closed, $A \cap B = \varnothing$, and neither $A$ nor $B$ is empty. Let $a \in A$ and $b \in B$; by hypothesis there is a polygon $P$ from $a$ to $b$ such that $P \subset G$. Now a moment's thought will show that one of the segments making up $P$ will have one end point in $A$ and another in $B$. So we can assume that $P = [a, b]$.

Define
$$S = \{s \in [0, 1] : sb + (1-s)a \in A\}$$
$$T = \{t \in [0, 1] : tb + (1-t)a \in B\}$$

Then $S \cap T = \varnothing$, $S \cup T = [0, 1]$, $0 \in S$ and $1 \in T$. However it can be shown that both $S$ and $T$ are open (Exercise 2), contradicting the connectedness of $[0, 1]$.
