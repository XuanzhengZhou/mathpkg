---
role: proof
locale: en
of_concept: neighborhood-of-acyclic-linear-graph-is-2-cell
source_book: gtm047
source_chapter: "22"
source_section: "1"
---

If $L$ consists of a single edge of $K$, the statement is clear, since $N(e) = N(v) \cup N'(e) \cup N(v')$ is a $2$-cell by definition.

The proof proceeds by induction on the number of edges of $L$. Let $e$ be any edge of $L$. Since $L$ is acyclic, removing $e$ disconnects $L$ into two components: the complex $L - e$ decomposes as $L_1 \cup L_2$, where $L_1$ and $L_2$ are disjoint, connected, acyclic, and each has fewer edges than $L$.

Now
$$N(L) = N(L_1) \cup N'(e) \cup N(L_2).$$

Because $|L_1| \cap |L_2| = \emptyset$, we have $N(L_1) \cap N(L_2) = \emptyset$. By the induction hypothesis, $N(L_1)$ and $N(L_2)$ are $2$-cells. The edge interior neighborhood $N'(e)$ joins them, and since $N'(e)$ is itself a $2$-cell whose intersections with $N(L_1)$ and $N(L_2)$ are arcs in their boundaries, $N(L)$ is the union of three $2$-cells "laid end to end." Hence $N(L)$ is a $2$-cell. $\square$
