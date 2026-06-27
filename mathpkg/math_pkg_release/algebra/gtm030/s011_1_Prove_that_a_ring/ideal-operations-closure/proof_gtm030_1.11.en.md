---
role: proof
locale: en
of_concept: ideal-operations-closure
source_book: gtm030
source_chapter: "1"
source_section: "1.11"
---
The proof is a straightforward verification using the definitions. Let $\mathfrak{B}$ and $\mathfrak{C}$ be left ideals of $\mathfrak{A}$.

**Intersection:** Let $x, y \in \mathfrak{B} \cap \mathfrak{C}$ and $a \in \mathfrak{A}$. Then $x + y \in \mathfrak{B}$ and $x + y \in \mathfrak{C}$ since each is a subgroup, so $x + y \in \mathfrak{B} \cap \mathfrak{C}$. Also $ax \in \mathfrak{B}$ and $ax \in \mathfrak{C}$ since each is a left ideal, so $ax \in \mathfrak{B} \cap \mathfrak{C}$. Thus $\mathfrak{B} \cap \mathfrak{C}$ is a left ideal.

**Sum:** $\mathfrak{B} + \mathfrak{C} = \{b + c \mid b \in \mathfrak{B}, c \in \mathfrak{C}\}$. This is a subgroup of $\mathfrak{A}$ since both are subgroups. For any $a \in \mathfrak{A}$ and $b + c \in \mathfrak{B} + \mathfrak{C}$, we have $a(b + c) = ab + ac \in \mathfrak{B} + \mathfrak{C}$ since $ab \in \mathfrak{B}$ and $ac \in \mathfrak{C}$. Hence $\mathfrak{B} + \mathfrak{C}$ is a left ideal.

**Product:** $\mathfrak{B}\mathfrak{C} = \{\sum_i b_i c_i \mid b_i \in \mathfrak{B}, c_i \in \mathfrak{C}\}$. This is a subgroup by construction. For any $a \in \mathfrak{A}$, $a(\sum_i b_i c_i) = \sum_i (ab_i)c_i \in \mathfrak{B}\mathfrak{C}$ since $ab_i \in \mathfrak{B}$. Thus $\mathfrak{B}\mathfrak{C}$ is a left ideal.

The proofs for right ideals are symmetric.
