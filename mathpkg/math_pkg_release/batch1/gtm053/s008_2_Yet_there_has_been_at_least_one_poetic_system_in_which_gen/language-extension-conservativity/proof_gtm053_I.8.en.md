---
role: proof
locale: en
of_concept: language-extension-conservativity
source_book: gtm053
source_chapter: "I"
source_section: "8"
---

We describe the case $n \geqslant 1$; the case $n = 0$ is analogous and simpler.

**Translation of formulas.** A term $f(t_1, \ldots, t_n)$ is called a simple $f$-term if $f$ does not occur in $t_1, \ldots, t_n$. The translation eliminates $f$ inductively.

**(a)** Let $Q$ be an atomic formula in $L$. If $f$ does not occur in $Q$, $Q$ is its own translation. If $f$ occurs, there exists a simple $f$-term $f(t_1, \ldots, t_n)$ occurring in $Q$. Take the first occurrence, substitute a new variable $x$ in its place to obtain $Q^*$, and construct:

$$Q'_{(1)}: \exists x (P'(x, t_1, \ldots, t_n) \land Q^*(x)).$$

Repeat this procedure on $Q'_{(1)}$ to eliminate further occurrences of $f$. After finitely many steps, we obtain a formula $Q'$ in which $f$ does not occur. This $Q'$ is the translation of $Q$.

**(b)** For non-atomic formulas, the translation is defined inductively in the obvious way: $\text{tr}(\neg Q) = \neg \text{tr}(Q)$, $\text{tr}(Q_1 \land Q_2) = \text{tr}(Q_1) \land \text{tr}(Q_2)$, $\text{tr}(\forall x Q) = \forall x \text{tr}(Q)$, etc.

**Key property:** For any formula $Q$ in $L$, $\mathcal{E} \vdash Q \Leftrightarrow \text{tr}(Q)$. The proof is by induction on the construction of $Q$, using the defining axiom for $f$ and the provability of $\exists! x P'$.

**Normal models.** The proof uses three facts about normal models (where $=$ is interpreted as equality):

1. If a formula $Q'$ is true in every normal model of $\mathcal{E}'$, then $Q'$ is true in every model of $\mathcal{E}'$ (since any model can be quotiented by the equivalence relation interpreting $=$ to obtain a normal model, preserving truth values).

2. The normal models of $\mathcal{E}'$ (in $L'$) coincide with the normal models of $\mathcal{E}$ (in $L$). There is a natural bijection: given a normal model of $\mathcal{E}'$, the condition $\mathcal{E}' \vdash \exists! x P'$ ensures that $P'$ defines a function $M^n \to M$, which serves as the interpretation of $f$.

**Conservativity.** Suppose $Q$ is a formula of $L'$ deducible from $\mathcal{E}$ in $L$. Then $Q$ is true in all normal models of $\mathcal{E}$. By (2), $Q$ is true in all normal models of $\mathcal{E}'$. By the completeness theorem (or directly by (1)), $Q$ is deducible from $\mathcal{E}'$ in $L'$. Thus the set of $L'$-formulas deducible from $\mathcal{E}'$ coincides with the set of $L'$-formulas deducible from $\mathcal{E}$.
