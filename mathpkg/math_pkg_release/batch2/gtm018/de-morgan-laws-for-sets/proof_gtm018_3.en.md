---
role: proof
locale: en
of_concept: de-morgan-laws-for-sets
source_book: gtm018
source_chapter: "I"
source_section: "3"
---

Let $\mathbf{E}$ be a class of subsets of $X$. For any point $x \in X$,

$$x \in \left(\bigcup \{E: E \in \mathbf{E}\}\right)' \iff x \notin \bigcup \{E: E \in \mathbf{E}\} \iff \forall E \in \mathbf{E},\; x \notin E \iff \forall E \in \mathbf{E},\; x \in E' \iff x \in \bigcap \{E': E \in \mathbf{E}\}.$$

Thus $\left(\bigcup \{E: E \in \mathbf{E}\}\right)' = \bigcap \{E': E \in \mathbf{E}\}$.

Similarly,

$$x \in \left(\bigcap \{E: E \in \mathbf{E}\}\right)' \iff x \notin \bigcap \{E: E \in \mathbf{E}\} \iff \exists E \in \mathbf{E},\; x \notin E \iff \exists E \in \mathbf{E},\; x \in E' \iff x \in \bigcup \{E': E \in \mathbf{E}\}.$$

Hence $\left(\bigcap \{E: E \in \mathbf{E}\}\right)' = \bigcup \{E': E \in \mathbf{E}\}$.

In words: the complement of the union of a class of sets is the intersection of their complements, and the complement of their intersection is the union of their complements.
