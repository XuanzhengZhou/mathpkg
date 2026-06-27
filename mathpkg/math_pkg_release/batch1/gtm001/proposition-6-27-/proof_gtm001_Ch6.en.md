---
role: proof
locale: en
of_concept: proposition-6-27-
source_book: gtm001
source_chapter: "6"
source_section: ""
---

** If $A - B \neq 0$ then by Proposition 6.26

$$(\exists x \in A - B)[(A - B) \cap (R^{-1}) \land \{x\} = 0]$$

then

$$A \cap (R^{-1}) \land \{x\} \subseteq B$$

Since $x \in A$ it follows from hypothesis that $x \in B$. But this contradicts the fact that $x \in A - B$.

Therefore $A - B = 0$ that is $A \subseteq B$. Since by hypothesis $B \subseteq A$ we conclude that $A = B$.

**Remark.** Proposition 6.27 is an induction principle. To prove that $(\forall x \in A)\varphi(x)$, we consider

$$B = \{x \in A | \varphi(x)\}.$$

If for any $R$ that is a well-founded well ordering on $A$ we can prove

$$(\forall x \in A)[A \cap (R^{-1}) \land \{x\} \subseteq B \rightarrow x \in B]$$

it then follows that $A = B$, i.e. $(\forall x \in A)\varphi(x)$.

Later it will be shown that Propositions 6.26 and
