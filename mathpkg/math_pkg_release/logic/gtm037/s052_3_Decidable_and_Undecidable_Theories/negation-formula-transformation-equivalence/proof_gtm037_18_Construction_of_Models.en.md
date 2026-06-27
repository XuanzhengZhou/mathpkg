---
role: proof
locale: en
of_concept: negation-formula-transformation-equivalence
source_book: gtm037
source_chapter: "18"
source_section: "Construction of Models"
---

The equivalence $\models \neg\varphi \leftrightarrow \varphi\rightarrow$ is established by induction on the structure of $\varphi$.

- If $\varphi$ is atomic, then $\varphi\rightarrow = \neg\varphi$ by definition, so $\models \neg\varphi \leftrightarrow \neg\varphi$, which trivially holds.
- If $\varphi = \neg\psi$, then $\varphi\rightarrow = \psi$ by definition, and we need to show $\models \neg\neg\psi \leftrightarrow \psi$.
- If $\varphi = \psi \lor \chi$, then $\varphi\rightarrow = \neg\psi \land \neg\chi$ by definition, and we must verify $\models \neg(\psi \lor \chi) \leftrightarrow \neg\psi \land \neg\chi$, which is a propositional tautology.
- If $\varphi = \psi \land \chi$, then $\varphi\rightarrow = \neg\psi \lor \neg\chi$ by definition, and $\models \neg(\psi \land \chi) \leftrightarrow \neg\psi \lor \neg\chi$, again a De Morgan law.
- If $\varphi = \forall\alpha\psi$, then $\varphi\rightarrow = \exists\alpha\neg\psi$ by definition. Now $\models \neg\forall\alpha\psi \leftrightarrow \exists\alpha\neg\psi$ holds because $\neg\forall\alpha\psi$ is logically equivalent to $\exists\alpha\neg\psi$, completing the quantifier case.

Thus $\models \neg\varphi \leftrightarrow \varphi\rightarrow$ for all $\varphi$. $\square$
