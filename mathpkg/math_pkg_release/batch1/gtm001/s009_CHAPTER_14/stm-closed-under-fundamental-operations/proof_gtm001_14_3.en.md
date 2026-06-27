---
role: proof
locale: en
of_concept: stm-closed-under-fundamental-operations
source_book: gtm001
source_chapter: "14"
source_section: "The Fundamental Operations"
---
From Proposition 13.25, $a \in M \land b \in M \land \mathrm{STM}(M, \text{Ax. 2}) \rightarrow \mathcal{F}_1(a, b) \in M$.

Since $M$ is a model of Axiom 2, $c = \langle a, b \rangle$ and $d = \langle a, b, c \rangle$ are each absolute with respect to $M$. Since $M$ is also a model of Axiom 5, it follows from Proposition 13.34 and properties of absoluteness that for $a, b \in M$:

$$\mathcal{F}_2(a, b) = \{x \in a \mid (\exists y, z)[x = \langle y, z \rangle \land y \in z]\} = \{x \in a \mid (\exists y, z \in M)[x = \langle y, z \rangle \land y \in z]^M\} \in M.$$

Similar reasoning applies to $\mathcal{F}_3$ through $\mathcal{F}_8$.
