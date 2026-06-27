---
role: proof
locale: en
of_concept: pl-schoenflies-theorem
source_book: gtm047
source_chapter: ""
source_section: "21"
---

**Proof.** The proof proceeds by induction on a combinatorial index $\operatorname{Ind} S$ defined for the polyhedral 2-sphere $S$. Let $J$ be a simple closed curve in $S$ and let $P \in J$.

By a PLH $E \leftrightarrow E$, we can reduce the configuration to one in which $D_J$ is convex, and $D_J - \{P\}$ (which may be all of $D_J$) lies on one side of a line $L \subset E$, containing $P$. This homeomorphism then has a PLH extension which preserves $z$-coordinates, and hence preserves horizontal planes. This PLH preserves the topology of each set $E' \cap S$. Note that it does not preserve general position except in trivial cases; we introduce many new vertices.

Now $J$ decomposes $S$ into two polyhedral 2-cells $D_1, D_2$, such that $D_1 \cap D_2 = J$. Let

$$S_i = D_i \cup D_J \quad (i = 1, 2).$$

Now $D_i$ approaches $J - \{P\}$ from only one side of $E$. Assume that $D_1$ approaches $J - \{P\}$ from above $E$, and that $D_2$ approaches from below. We rotate the axes very slightly, using $L$ as a line of fixed points, so that the new horizontal plane $E'$ through $P$ passes below $J$. By a slight alteration in the direction of the $z$-axis, we restore general position. The PLH that made $D_J$ convex may have introduced plenty of new vertices in $S$, but it created no new singular points, and it preserved horizontal planes. Thus, in computing $\operatorname{Ind} S_1$, we find that (1) every singular point $Q$ of $S_1$ is a singular point of $S$, (2) the index of $Q$ in $S_1$ is no greater than the index of $Q$ in $S$, and (3) the index of $P$ is reduced by one, when we pass from $S$ to $S_1$ (since $J$ is gone). Therefore

$$\operatorname{Ind} S_1 \leqslant \operatorname{Ind} S - 1 = n - 1.$$

By the induction hypothesis, $S_1$ is simply imbedded. Rotating the axes in the opposite direction gives the same conclusion for $S_2$.

Suppose now that $C_1^3$ and $C_2^3$ are the closures of the components of $\mathbb{R}^3 - S$, so that $C_1^3 \cup C_2^3 = \mathbb{R}^3$ and $C_1^3 \cap C_2^3 = S$. Two cases arise:

(1) $D_1 \subset C_1^3$ and $D_2 \subset C_2^3$, or
(2) Both $D_1$ and $D_2$ lie in $C_1^3$ (or symmetrically in $C_2^3$).

Suppose that (1) holds. By Theorem 8, $\operatorname{Bd} C_1^3$ has the push property at $D_1$. Thus there is a PLH $f_1: \mathbb{R}^3 \leftrightarrow \mathbb{R}^3$, $D_1 \leftrightarrow D$, such that $f_1|(\mathbb{R}^3 - W)$ and $f_1|D_2$ are identity mappings. (To get the latter, we use a closed neighborhood $N$ of $C_1^3 - J$ such that $N \cap \operatorname{Int} D_2 = \emptyset$.) Thus $f_1(S) = S_2$. Let $f_2: \mathbb{R}^3 \leftrightarrow \mathbb{R}^3$, $S_2 \leftrightarrow \operatorname{Bd} \sigma^3$ be a PLH such that $f_2|(\mathbb{R}^3 - W)$ is the identity. Thus $S$ is simply imbedded, the desired PLH being $f_2 f_1$.

Suppose that (2) holds. Then $C_2^3 \subset C_1^3 - \operatorname{Int} D_1$. As in Case (1), there is a PLH $f_1: \mathbb{R}^3 \leftrightarrow \mathbb{R}^3$, $S \leftrightarrow S_1$, such that $f_1|(\mathbb{R}^3 - W)$ is the identity; and since $S_1$ is simply imbedded, the theorem follows as in Case (1).
