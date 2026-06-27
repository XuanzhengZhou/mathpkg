---
role: proof
locale: en
of_concept: products-unique-up-to-isomorphism
source_book: gtm026
source_chapter: "2"
source_section: "1"
---

Suppose $p_i: A \longrightarrow A_i$ and $q_i: B \longrightarrow A_i$ are both products of $(A_i)$. By the universal property of $A$ applied to the family $q_i: B \longrightarrow A_i$, there exists a unique $f: B \longrightarrow A$ such that $f.p_i = q_i$ for all $i \in I$. By the universal property of $B$ applied to the family $p_i: A \longrightarrow A_i$, there exists a unique $g: A \longrightarrow B$ such that $g.q_i = p_i$ for all $i \in I$.

Now consider $fg: A \longrightarrow A$. For all $i \in I$,
$$(fg).p_i = f.(g.p_i) = f.q_i = p_i = \mathrm{id}_A.p_i.$$
By the uniqueness clause of the universal property of $A$, we conclude $fg = \mathrm{id}_A$. Similarly,
$$(gf).q_i = g.(f.q_i) = g.p_i = q_i = \mathrm{id}_B.q_i,$$
so $gf = \mathrm{id}_B$. Therefore $f$ is an isomorphism (with inverse $g$) transforming one set of projections into the other.
