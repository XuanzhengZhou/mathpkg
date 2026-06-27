---
role: proof
locale: en
of_concept: unique-reading-lemma
source_book: gtm053
source_chapter: "II"
source_section: "1"
---

Using induction on the length of the expression $E$, we describe an informal algorithm for syntactic analysis, which uniquely determines which alternative holds.

(a) If there are no parentheses in $E$, then $E$ is either a constant term, a variable term, or neither a term nor a formula.

(b) If $E$ contains parentheses, but there is no parentheses bijection between the left and right parentheses, then $E$ is neither a term nor a formula.

(c) Suppose $E$ contains parentheses with a parentheses bijection. Then either $E$ is uniquely represented in one of the nine forms
$$f(E_0) \quad (\text{where } f \text{ is an operation}),$$
$$p(E_0) \quad (\text{where } p \text{ is a relation}),$$
$$(E_1) \Leftrightarrow (E_2),\quad (E_1) \Rightarrow (E_2),\quad (E_1) \vee (E_2),\quad (E_1) \wedge (E_2),$$
$$\neg(E_3),\quad \forall x(E_3),\quad \exists x(E_3),$$
or else $E$ is neither a term nor a formula.

For uniqueness: if $E_0$ is known to be the concatenation of a finite number of terms, then this representation is unique. Either $E_0$ can be uniquely represented in one of the forms $xE_0'$, $cE_0'$, $f(E_0''')E_0'$ (where $x$ is a variable, $c$ is a constant, and $f$ is an operation whose parentheses correspond under the unique parentheses bijection in $E_0$), or else $E_0$ cannot be represented in the form $tE_0'$ where $t$ is a term. In the cases $E_0 = xE_0'$ or $E_0 = cE_0'$, this is obviously the only way to break off a term from the left. In the case $E_0 = f(E_0''')E_0'$, the question reduces to whether $E_0''$ is a concatenation of $\deg(f)$ terms. By induction on the length of $E_0$, we may assume that either $E_0''$ is not such a concatenation, or else it is uniquely representable as a concatenation of terms. The lemma is proved.
