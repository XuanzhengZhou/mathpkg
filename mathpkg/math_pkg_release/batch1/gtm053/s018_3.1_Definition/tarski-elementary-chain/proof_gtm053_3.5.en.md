---
role: proof
locale: en
of_concept: tarski-elementary-chain
source_book: gtm053
source_chapter: "3"
source_section: "3.5"
---

We prove by induction on the complexity of $L$-formulas $P(\bar{x})$ that for all $\alpha < \delta \leq \kappa$ and all $\bar{a} \in A_\alpha$,

$$A_\alpha \models P(\bar{a}) \iff A_\delta \models P(\bar{a}).$$

**Atomic formulas.** Since each $A_\alpha \subseteq A_{\alpha+1}$ and the limit $A_\delta$ is defined as the union with predicates and functions interpreted by union, the truth of atomic formulas is preserved through the chain by construction.

**Boolean connectives.** If the claim holds for $P$ and $Q$, it holds trivially for $\neg P$, $P \land Q$, $P \lor Q$, etc.

**Existential quantifier.** Suppose the claim holds for $P(\bar{x}, y)$. We prove it for $\exists y\, P(\bar{x}, y)$.

($\Rightarrow$): If $A_\alpha \models \exists y\, P(\bar{a}, y)$, then there exists $b \in A_\alpha$ such that $A_\alpha \models P(\bar{a}, b)$. Since $A_\alpha \preceq A_{\alpha+1}$, we have $A_{\alpha+1} \models P(\bar{a}, b)$, and by the induction hypothesis (applied repeatedly through the chain), $A_\delta \models P(\bar{a}, b)$. Hence $A_\delta \models \exists y\, P(\bar{a}, y)$.

($\Leftarrow$): If $A_\delta \models \exists y\, P(\bar{a}, y)$, then there exists $b \in A_\delta$ such that $A_\delta \models P(\bar{a}, b)$. Since $A_\delta = \bigcup_{\beta < \delta} A_\beta$, there exists $\beta < \delta$ with $b \in A_\beta$. We may assume $\alpha < \beta$ (otherwise take $\beta = \alpha$). By the induction hypothesis, $A_\beta \models P(\bar{a}, b)$. Hence $A_\beta \models \exists y\, P(\bar{a}, y)$. Since $A_\alpha \preceq A_\beta$, we have $A_\alpha \models \exists y\, P(\bar{a}, y)$.

**Universal quantifier** follows from the existential case via $\forall y\, P \equiv \neg \exists y\, \neg P$.

Thus $A_\alpha \preceq A_\delta$ for all $\alpha < \delta \leq \kappa$, as required.
