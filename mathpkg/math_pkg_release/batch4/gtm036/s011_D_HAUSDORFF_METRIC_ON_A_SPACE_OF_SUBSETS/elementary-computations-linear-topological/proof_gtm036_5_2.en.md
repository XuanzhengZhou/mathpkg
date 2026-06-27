---
role: proof
locale: en
of_concept: elementary-computations-linear-topological
source_book: gtm036
source_chapter: "5"
source_section: "2"
---

\textbf{(i)} This is a direct consequence of the fact that translation and multiplication by non-zero scalars are homeomorphisms.

\textbf{(ii)} If $x \in A^-$ and $y \in B^-$, then $(x, y) \in (A \times B)^-$ in the product; and since addition is continuous, $x + y \in (A + B)^-$.

\textbf{(iii)} Observe that $A + U = \bigcup \{x + U : x \in A\}$, and $x + U$ is open for every $x$.

\textbf{(iv)} This follows from the fact that $C + D$ is the image of the compact set $C \times D$ under the continuous map, addition.

\textbf{(v)} A point $x$ belongs to $A^-$ if and only if for each neighborhood $V$ of $0$, $x + V$ intersects $A$; that is, if and only if $x \in A - V$. Hence $A^- = \bigcap \{A - V : V \in \mathcal{U}\}$, but $V$ is a neighborhood of $0$ if and only if $-V$ is a neighborhood of $0$. The required result follows.

\textbf{(vi)} Suppose that for each neighborhood $V$ in the neighborhood system $\mathcal{U}$ of $0$ there is an element $x_V$ in $C$ such that $x_V + V$ intersects the complement of $U$. Consider the net $\{x_V, V \in \mathcal{U}, \subset\}$. Since $C$ is compact, this net has a cluster point $x_0$ in $C$. Thus every neighborhood of $x_0$ intersects the complement of $U$. This situation is impossible since $x_0$ is an element in the open set $U$.

\textbf{(vii)} If $x$ does not belong to $C + F$, then the compact set $x - C$ is disjoint from $F$. Hence, by (vi), there is a neighborhood $V$ of $0$ such that $V + x - C$ is disjoint from $F$. Consequently, $x + V$ is disjoint from $C + F$, and $x$ does not belong to the closure of $C + F$. Hence, $C + F$ is closed.
