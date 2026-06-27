---
role: proof
locale: en
of_concept: no-membership-cycles
source_book: gtm001
source_chapter: "5"
source_section: "5"
---

Let $a = \{a_1, a_2, \ldots, a_n\}$. Suppose, for contradiction, that $a_1 \in a_2 \in \cdots \in a_n \in a_1$.

Take any $x \in a$. Then $x = a_i$ for some $i$. By the assumed cycle, $a_{i+1} \in a_i = x$ (with indices taken modulo $n$, so $a_{n+1} = a_1$). Moreover, $a_{i+1} \in a$ since $a_{i+1}$ is one of the $a_j$. Hence $a_{i+1} \in x \cap a$, so $x \cap a \neq 0$.

Thus $(\forall x)[x \in a \rightarrow x \cap a \neq 0]$. Since $a$ is nonempty (it contains $a_1$), this contradicts the Axiom of Regularity (weak form, Axiom 6), which requires the existence of some $x \in a$ with $x \cap a = 0$.

Therefore the cycle cannot exist.
