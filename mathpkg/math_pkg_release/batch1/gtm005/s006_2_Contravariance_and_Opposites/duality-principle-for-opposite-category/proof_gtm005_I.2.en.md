---
role: proof
locale: en
of_concept: duality-principle-for-opposite-category
source_book: gtm005
source_chapter: "I"
source_section: "2. Contravariance and Opposites"
---

The proof proceeds by induction on the construction of $\Sigma$ from atomic statements.

An atomic statement in the elementary theory of an abstract category is of the form "$f = g \circ h$" (equality of an arrow with a composite). The dual of such a statement is "$f^{\text{op}} = h^{\text{op}} \circ g^{\text{op}}$". By the definition of composition in $C^{\text{op}}$, we have $h^{\text{op}} \circ g^{\text{op}} = (g \circ h)^{\text{op}}$. Thus $f = g \circ h$ in $C$ is equivalent to $f^{\text{op}} = (g \circ h)^{\text{op}} = h^{\text{op}} \circ g^{\text{op}}$ in $C^{\text{op}}$.

For the induction step, suppose the equivalence holds for statements $\Sigma_1$ and $\Sigma_2$. Then it holds for their logical combinations (conjunction, disjunction, negation, implication) and for quantifications over arrows or objects. Since every statement in the elementary theory of an abstract category is built up from atomic statements by these logical operations, the principle follows by induction on the structure of $\Sigma$.

The "in particular" clause follows immediately: take $\Sigma$ to be a sentence (no free variables) and apply the equivalence with $C$ replaced by $C^{\text{op}}$ itself.
