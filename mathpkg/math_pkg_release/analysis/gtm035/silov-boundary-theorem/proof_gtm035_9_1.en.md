---
role: proof
locale: en
of_concept: silov-boundary-theorem
source_book: gtm035
source_chapter: "Chapter 9"
source_section: "9.1"
---
# Proof of the Existence of the Šilov Boundary

Let $X$ be a compact space and $\mathcal{F}$ an algebra of continuous complex-valued functions on $X$ which separates the points of $X$. Let $S$ denote the intersection of all boundaries for $\mathcal{F}$. We prove that $S$ is a boundary for $\mathcal{F}$.

Let $W$ be an open set containing $S$. For each $x \in X \setminus W$, by Lemma 9.2, there exists a neighborhood $U_x$ of $x$ with the property that if $\beta$ is a boundary, then $\beta \setminus U_x$ is also a boundary.

Since $X \setminus W$ is compact, we can find finitely many such neighborhoods, say $U_1, U_2, \ldots, U_r$, whose union covers $X \setminus W$.

Now we construct a sequence of boundaries. $X$ itself is a boundary (trivially). By the property of $U_1$, $X \setminus U_1$ is a boundary. Applying the property of $U_2$, $(X \setminus U_1) \setminus U_2$ is a boundary. Continuing this process, after $r$ steps we obtain that

$$X^* = X \setminus (U_1 \cup U_2 \cup \cdots \cup U_r)$$

is a boundary. But $X^* \subseteq W$ by construction, since the $U_i$ cover $X \setminus W$.

Hence for any $f \in \mathcal{F}$,

$$\max_X |f| \leq \sup_W |f|.$$

Since $W$ was an arbitrary open neighborhood of $S$, and $f$ is continuous, we conclude that

$$\max_X |f| \leq \max_S |f|.$$

Thus $S$ is a boundary for $\mathcal{F}$. Moreover, $S$ is the intersection of all boundaries, so it is contained in every boundary — it is the unique smallest boundary. $\square$

*Note.* The only properties of $\mathcal{F}$ used in the proof are that it is an algebra of continuous functions on a compact space that separates points.
