---
role: proof
locale: en
of_concept: group-unit-element
source_book: gtm077
source_chapter: "II"
source_section: "5"
---
# Proof of Theorem 16: Existence and Uniqueness of the Unit Element

**Theorem 16.** In every group $\mathfrak{G}$ there exists a uniquely determined element $E$ (the *unit element*) such that for every $A \in \mathfrak{G}$,

$$AE = EA = A.$$

*Proof.* From the four group axioms (i)--(iv) we construct the unit element in three steps.

**Step 1: Right identity.** For an arbitrarily chosen element $A \in \mathfrak{G}$, axiom (iv) guarantees the existence of an element $E$ with $AE = A$. We claim that this same $E$ satisfies $BE = B$ for *every* $B \in \mathfrak{G}$.

Indeed, given any $B$, by axiom (iv) there exists $Y$ such that $YA = B$. Then by the associative law (ii),

$$BE = (YA)E = Y(AE) = YA = B.$$

Thus $E$ acts as a right identity for the whole group, and is independent of the particular $A$ used to construct it.

**Step 2: Left identity.** Symmetrically, axiom (iv) also provides an element $E'$ such that $E'A = A$ for every $A \in \mathfrak{G}$. (Fix any $A$, find $E'$ with $E'A = A$; for arbitrary $B$, choose $X$ with $AX = B$ by (iv), and then $E'B = E'(AX) = (E'A)X = AX = B$.) Hence $E'$ is a left identity.

**Step 3: Equality and uniqueness.** Setting $A = E$ in the left identity relation $E'A = A$ gives $E'E = E$. Setting $B = E'$ in the right identity relation $BE = B$ gives $E'E = E'$. Therefore $E = E'$, so the right and left identities coincide. This unique element $E$ satisfies

$$AE = EA = A \qquad \text{for all } A \in \mathfrak{G}.$$

The unit element is also denoted by $1$, by analogy with ordinary multiplication, and may be omitted as a factor in any product without changing its value. $\square$
