---
role: proof
locale: en
of_concept: "let-be-a-nonvoid-open-subset-of-then"
source_book: gtm025
source_chapter: "Topology"
source_section: "6.59"
---

Let $x \in U$ and define $a_x = \inf \{t : ]t, x] \subset U\}$ and $b_x = \sup \{t : [x, t] \subset U\}$. Since $U$ is open, it is clear that $a_x$ and $b_x$ exist in $R^\#$. We first assert that $]a_x, b_x[ \subset U$ and begin by proving that $]a_x

$a \in ]c, d[$. Thus $]a, b[ \neq ]c, d[$, but $]a, b[ \cap ]c, d[ = ]a, \min\{b, d\}[ \neq \varnothing$. This contradiction shows that $a \notin U$. Likewise $b \notin U$. Let $x \in ]a, b[$. Then $]a, x] \subset U$ and $[x, b[ \subset U$ so $]a, b[ \subset ]a_x, b_x[ \subset U$. Since $a \notin U$ and $b \notin U$, we have $]a, b[ = ]a_x, b_x[ \in \mathcal{I}$. Therefore $\mathcal{I} \subset \mathcal{I}$. If there exists $]a_x, b_x[ \in \mathcal{I} \cap \mathcal{I}'$, then $x \in U$ while $x \notin \cup \mathcal{I} = U$, a contradiction. Therefore $\mathcal{I} = \mathcal{I}'$.

(6.60) Remark. The simple structure of open sets in $R$ has no analogue in Euclidean spaces of dimension $> 1$. For example, in the plane $R^2$ open disks play the role that open intervals play on the line as the building blocks for open sets, i.e., the base for the topology. But it is plain that the open square $\{(x, y): 0 < x < 1, 0 < y < 1\}$ is not a union of disjoint open disks, for if it were, the diagonal $\{(x, x): 0 < x < 1\}$ would be a union of [more than one] disjoint open intervals, contrary to the uniqueness statement of (6.59).

Neither do the closed subsets of $R$ have such a simple structure as the open ones do. The next few paragraphs show this rather complicated structure. We begin with a definition.
