---
role: proof
locale: en
of_concept: duality-principle
source_book: gtm005
source_chapter: "II"
source_section: "2"
---

The proof proceeds by induction on the construction of a statement $\Sigma$ in the elementary theory of an abstract category. The elementary theory has atomic formulas of the following types: equality of objects $a = b$, equality of arrows $f = g$, domain assignment $\operatorname{dom}(f) = a$, codomain assignment $\operatorname{cod}(f) = b$, and composition $h = g \circ f$.

**Base case (atomic formulas).** For each atomic formula, the dual statement is obtained by the following translation:
- $f: a \to b$ dualizes to $f^{\text{op}}: b \to a$;
- $h = g \circ f$ dualizes to $h^{\text{op}} = f^{\text{op}} \circ g^{\text{op}}$ (since $(g \circ f)^{\text{op}} = f^{\text{op}} \circ g^{\text{op}}$ by the definition of composition in $C^{\text{op}}$);
- Equality of objects is unchanged.

By the definition of the opposite category, an atomic formula holds for arrows $f, g, \ldots$ in $C$ if and only if its dual holds for $f^{\text{op}}, g^{\text{op}}, \ldots$ in $C^{\text{op}}$. For instance, $h = g \circ f$ in $C$ means precisely that $(g \circ f)^{\text{op}} = h^{\text{op}}$ in $C^{\text{op}}$, and by definition $(g \circ f)^{\text{op}} = f^{\text{op}} \circ g^{\text{op}}$, so $f^{\text{op}} \circ g^{\text{op}} = h^{\text{op}}$ in $C^{\text{op}}$, which is the dual of the original atomic formula.

**Inductive step.** Compound statements are built from atomic formulas using the usual logical connectives: negation ($\neg$), conjunction ($\land$), disjunction ($\lor$), implication ($\Rightarrow$), universal quantification ($\forall$), and existential quantification ($\exists$). The dual $\Sigma^*$ of a compound statement is obtained by dualizing each atomic subformula while leaving the logical structure unchanged:
- $(\neg \Sigma)^* = \neg (\Sigma^*)$;
- $(\Sigma_1 \land \Sigma_2)^* = \Sigma_1^* \land \Sigma_2^*$;
- $(\forall x.\,\Sigma)^* = \forall x.\,(\Sigma^*)$;
- and analogously for the other connectives and quantifiers.

Assume by induction hypothesis that for each proper subformula $\Phi$ of $\Sigma$, we have $\Phi$ holds in $C$ if and only if $\Phi^*$ holds in $C^{\text{op}}$. Then the truth value of $\Sigma$ in $C$ is determined by the truth values of its subformulas via the usual truth tables of the logical connectives. Since duality leaves the logical structure unchanged and the induction hypothesis gives the equivalence for each subformula, the equivalence extends to $\Sigma$: $\Sigma$ is true in $C$ if and only if $\Sigma^*$ is true in $C^{\text{op}}$.

Thus, by induction on formula complexity, every statement $\Sigma$ in the elementary theory of an abstract category satisfies the duality principle. The special case where $\Sigma$ is a sentence (no free variables) yields: $\Sigma$ is true in $C^{\text{op}}$ if and only if $\Sigma^*$ is true in $C$.
