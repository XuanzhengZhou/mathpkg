---
role: proof
locale: en
of_concept: a-neq-0-wedge-texttra-rightarrow-textstma-textax1
source_book: gtm001
source_chapter: "11"
source_section: ""
---

Since Axiom 1 assures us that

(1) $x = y \wedge x \in z \rightarrow y \in z$

holds for all $x, y$, and $z$, it also assures us that (1) holds for all $x, y, z \in A$, that is

$(\forall x, y, z \in A)[x = y \wedge x \in z \rightarrow y \in z]$.

But since (1) is absolute with respect to $A$, it follows that

$(\forall x, y, z \in A)[x = y \wedge x \in z \rightarrow y \in z]^A$.

But this is Axiom 1 relativized to $A$, i.e., $[\text{Ax. 1}]^A$.

Since Axiom 1 is closed we have from Proposition 12.5

$A \models \text{Ax. 1} \leftrightarrow [\text{Ax. 1}]^A$.

Hence $A$ satisfies Axiom 1, i.e.,

$A \models \text{Ax. 1}$.

Since $A$ is nonempty and transitive we conclude that $A$ is a standard transitive model of Axiom 1.
