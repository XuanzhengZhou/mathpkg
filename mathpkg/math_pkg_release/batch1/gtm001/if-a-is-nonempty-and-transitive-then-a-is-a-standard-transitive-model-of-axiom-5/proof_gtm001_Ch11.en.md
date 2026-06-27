---
role: proof
locale: en
of_concept: if-a-is-nonempty-and-transitive-then-a-is-a-standard-transitive-model-of-axiom-5
source_book: gtm001
source_chapter: "11"
source_section: ""
---

Since $A$ is nonempty and transitive $A$ is a standard transitive model of Axiom 5$\varphi$ iff for $a \in A$

$$(\forall x, y, z \in A)[\varphi^A(x, y) \wedge \varphi^A(x, z) \rightarrow y = z]$$

implies that

$$(\exists z \in A)(\forall y \in A)[y \in z \leftrightarrow (\exists x \in A)[\varphi^A(x, y) \wedge x \in a]].$$

But since $A$ is transitive this is the case iff

$$(\exists z \in A)(\forall y)[y \in z \leftrightarrow (\exists x)[\varphi^A(x, y) \wedge x \in a] \wedge y \in A]$$

i.e.

$$(\exists z \in A)[z = \{y \in A | (\exists x \in a)[\varphi^A(x, y)]\}.$$

Hence

$$\{y \in A | (\exists x \in a)[\varphi^A(x, y)]\} \in A.$$
