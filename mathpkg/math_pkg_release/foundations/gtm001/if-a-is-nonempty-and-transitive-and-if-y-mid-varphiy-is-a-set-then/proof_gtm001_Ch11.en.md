---
role: proof
locale: en
of_concept: if-a-is-nonempty-and-transitive-and-if-y-mid-varphiy-is-a-set-then
source_book: gtm001
source_chapter: "11"
source_section: ""
---

If all of the free variables of $\varphi(y)$ are among $a_1, \ldots, a_n$, $y$ then

$$[a = \{y \mid \varphi(y)\}] \text{ Abs } A$$

$$\leftrightarrow a_1, \ldots, a_n, a \in A \rightarrow [(\forall y)[y \in a \leftrightarrow \varphi(y)]$$

$$\leftrightarrow (\forall y \in A)[y \in a \leftrightarrow \varphi^A(y)]$$

$$\leftrightarrow a_1, \ldots, a_n, a \in A \rightarrow [(\forall y)[y \in a \leftrightarrow \varphi(y)]$$

$$\leftright

(1) $a \subseteq b \leftrightarrow (\forall x)[x \in a \rightarrow x \in b]$.

Since $A$ is transitive $a \in A$ implies $a \subseteq A$, i.e., $x \in a \land a \in A$ implies $x \in A$. From Propositions 13.17, 13.3, and 13.6 it then follows that

$$a \subseteq b \text{ Abs } A.$$

(2) $a = b \leftrightarrow a \subseteq b \land b \subseteq a.$

Remark. The requirement in Proposition 13.18 that $A$ be transitive cannot be dropped. For example if $A = \{0, 1, \{0, 1, 2\}, \{0, 1, 3\}\}$ then from an internal vantage point the sets $\{0, 1, 2\}$ and $\{0, 1, 3\}$ are indistinguishable, i.e.,

$$(\forall x \in A)[x \in \{0, 1, 2\} \leftrightarrow x \in \{0, 1, 3\}].$$

Since the membership property is absolute with respect to any class (Proposition 13.17) if $b \in A$ then those individuals in $A$ that play the role of elements of $b$ are individuals in $V$ that are elements in $b$. But not conversely. In the foregoing example we have, relative to $A$

$$0 \in \{0, 1, 2\}, \quad 1 \in \{0, 1, 2\}, \quad 2 \notin \{0, 1, 2\}.$$

Similarly with subsets, if $A$ is a nonempty transitive class then containment is absolute with respect to $A$. This means that if $b \in A$ then every element of $A$ that is a subset of $b$ relative to $A$ is a subset of $b$ in the “real” universe $V$. But not conversely

(3) If $a, b \in A$ then

$$\{a, b\}^A = \{x \in A | [x = a \lor x = b]^A\}$$

$$= \{x | x = a \lor x = b\}$$

$$= \{a, b\}.$$

(4) If $a \in A$ then

$$[\cup(a)]^A = \{x \in A | (\exists y \in A)[x \in y \land y \in a]^A\}$$

$$= \{x \in A | (\exists y \in A)[x \in y \land y \in a]\}$$

$$= \{x | (\exists y)[x \in y \land y \in a]\}$$

$$= \cup(a).$$

(5) If $a, b \in A$ then

$$[a - b]^A = \{x \in A | [x \in a \land x \notin b]^A\}$$

$$= \{x \in A | x \in a \land x \notin b\}$$

$$= a - b.$$

Remark. The proofs of several of the theorems to follow are similar to the proof of Proposition 13.18 involving repeated applications of foregoing theorems on absoluteness. To avoid rather dull repetitions we omit most of the details.
