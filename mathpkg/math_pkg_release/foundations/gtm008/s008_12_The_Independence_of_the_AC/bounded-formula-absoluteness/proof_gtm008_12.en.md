---
role: proof
locale: en
of_concept: bounded-formula-absoluteness
source_book: gtm008
source_chapter: "12"
source_section: "The Independence of the AC"
---

A bounded formula (also called $\Delta_0$ formula) is one in which all quantifiers are bounded: $(\forall x \in y)$ or $(\exists x \in y)$. 

The absoluteness of bounded formulas for transitive models is a standard result: if $M$ is a transitive class and $\varphi(x_1, \ldots, x_n)$ is a bounded formula, then for all $a_1, \ldots, a_n \in M$,

$$
\varphi^M(a_1, \ldots, a_n) \leftrightarrow \varphi(a_1, \ldots, a_n).
$$

This is proved by induction on the complexity of $\varphi$. For atomic formulas the result holds by the definition of relativization. For propositional connectives the induction step is trivial. For bounded quantifiers: if $\varphi$ is $(\exists x \in y)\psi(x, y, \ldots)$, then $\varphi^M(a_1, \ldots)$ means $(\exists x \in M)(x \in a_1 \land \psi^M(x, a_1, \ldots))$. Since $a_1 \subseteq M$ (by transitivity of $M$), this is equivalent to $(\exists x \in a_1)\psi(x, a_1, \ldots)$ by the induction hypothesis.

In the context of Boolean-valued models and forcing, bounded formula absoluteness ensures that certain basic set-theoretic properties (like "$f$ is a function", "$\alpha$ is an ordinal", etc.) are preserved when moving between ground models and generic extensions.
