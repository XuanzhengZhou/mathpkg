---
role: proof
locale: en
of_concept: if-a-is-nonempty-and-transitive-then-a-is-a-standard-transitive-model-of-the-axi
source_book: gtm001
source_chapter: "11"
source_section: ""
---

** Ax. 4 $\leftrightarrow (\forall x)(\exists y)(\forall z)[z \in y \leftrightarrow z \subseteq x]$. Since $A$ is nonempty and transitive we have

$$\text{STM}(A, \text{Ax. 4})$$

if and only if

$$(\forall x \in A)(\exists y \in A)(\forall z \in A)[z \in y \leftrightarrow z \subseteq x]^A.$$

But since $b \in c \leftrightarrow b \subseteq a$ is absolute w.r.t. $A$, this holds if and only if

$$(\forall x \in A)(\exists y \in A)(\forall z \in A)[z \in y \leftrightarrow z \subseteq x].$$

Since $A$ is transitive it follows that if $y \in A$ then

$$(\forall z \in A)[z \in y \leftrightarrow z \
