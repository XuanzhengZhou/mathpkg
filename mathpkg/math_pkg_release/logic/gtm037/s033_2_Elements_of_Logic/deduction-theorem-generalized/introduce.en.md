---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Generalized Deduction Theorem extends the standard deduction theorem (which handles a single additional hypothesis) to the case of finitely many hypotheses. It states that $\psi$ is provable from $\Gamma$ together with $\varphi_0,\dots,\varphi_m$ if and only if the implication $\varphi_0\wedge\cdots\wedge\varphi_m \rightarrow \psi$ is provable from $\Gamma$ alone. The proof proceeds by induction on $m$, repeatedly applying the ordinary deduction theorem (10.86) and a suitable propositional tautology to collapse the nested implications into a single conjunction. The converse direction is trivial: from the conjunctive implication one immediately recovers each hypothesis.
