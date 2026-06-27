---
role: proof
locale: en
of_concept: axiom-of-choice-in-boolean-valued-universe
source_book: gtm053
source_chapter: "III"
source_section: "7"
---

Fix $X \in V^B$. Index $D(X) = \{U_\alpha\}_{\alpha \in I}$. For each $U_\alpha$, use Lemma 7.4 to find $W_\alpha$ with $\|W_\alpha \in U_\alpha\| = \|U_\alpha \neq \varnothing\|$. Set
$$a_\alpha = \|U_\alpha \in X\| \wedge \left( \bigvee_{\beta < \alpha} \|U_\beta \in X\| \wedge \|U_\beta = U_\alpha\| \right)'.$$
Then construct $Y$ by collecting the ordered pairs $\langle U_\alpha, W_\alpha \rangle^B$ with probabilities $a_\alpha$. One verifies $Q, R, S, T$ all have truth value 1: $Q$ and $S$ are immediate from the definition; $R$ follows because $\|U_\alpha = U_\beta\| \wedge a_\alpha \wedge a_\beta = 0$ for $\alpha \neq \beta$; $T$ follows by an inductive verification on the well-ordering of $D(X)$.
