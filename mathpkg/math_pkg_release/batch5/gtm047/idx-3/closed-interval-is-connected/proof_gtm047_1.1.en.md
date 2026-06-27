---
role: proof
locale: en
of_concept: closed-interval-is-connected
source_book: gtm047
source_chapter: "1"
source_section: "Connectivity"
---

This turns out to be the $n$th formulation of the continuity of $\mathbf{R}$. Suppose that $[a, b] = H \cup K$ (separated), with $a \in H$. Let

$$M = \{x \mid x = a \text{ or } [a, x] \subset H\}.$$

Then $M$ is bounded above. Let $c$ be the least upper bound of $M$. Then $c \in [a, b]$, $c$ is a limit point of $H$, $c \notin K$, and so $c \in H$. If $c < b$, then $c$ is a limit point of $K$, which contradicts the hypothesis for $H$ and $K$. Therefore $c = b$, $H = [a, b]$, and $K = \emptyset$. Thus $[a, b]$ is not the union of any two nonempty separated sets.
