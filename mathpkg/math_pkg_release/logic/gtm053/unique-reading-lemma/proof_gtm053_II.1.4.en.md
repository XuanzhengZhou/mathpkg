---
role: proof
locale: en
of_concept: unique-reading-lemma
source_book: gtm053
source_chapter: "II"
source_section: "1.4"
---

Using induction on the length of the expression $E$, we describe an informal algorithm for syntactic analysis, which uniquely determines which alternative holds.

(a) If there are no parentheses in $E$, then $E$ is either a constant term, a variable term, or neither a term nor a formula.

(b) If $E$ contains parentheses, but there is no parentheses bijection between the left and right parentheses, then $E$ is neither a term nor a formula.

(c) Suppose $E$ contains parentheses with a parentheses bijection. Then either $E$ is uniquely represented in one of the nine forms

$$f(E_0) \quad (\text{where } f \text{ is an operation}),$$
$$p(E_0) \quad (\text{where } p \text{ is a relation}),$$
$$(E_1) \Leftrightarrow (E_2),\; (E_1) \Rightarrow (E_2),\; (E_1) \vee (E_2),\; (E_1) \wedge (E_2),$$
$$\neg(E_3),\; \forall x(E_3),\; \exists x(E_3),$$

or else $E$ is neither a term nor a formula. Here the representation is unique: in the first two cases $E_0$ is uniquely determined by $E$, and in the remaining cases $(E_1, E_2)$ or $(E_3)$ are uniquely determined. This follows from Lemma 1.2 on the uniqueness of the parentheses bijection and from the fact that the first symbol of $E$ uniquely determines which of the nine forms applies.

In addition, in the course of the proof we show that if an expression is the concatenation of a finite sequence of terms, then it is uniquely representable as such a concatenation. The proof uses induction on the length of $E_0$ to show that the decomposition of $E_0$ into a concatenation of terms is unique.
