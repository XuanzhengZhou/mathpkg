role: proof
locale: en
of_concept: quantifier-elimination-to-basic-formulas
source_book: gtm037
source_chapter: "13"
source_section: "3"
---

The assertion is obvious for atomic formulas, and the induction steps involving $\neg$, $\lor$, $\land$ are trivial. As in the proof of Lemma 13.4 it is hence sufficient to prove the lemma for $\varphi$ of the form $\exists\alpha\psi$, with $\psi$ a conjunction of basic formulas and their negations.

Now the following equivalences hold in $\mathfrak{A}$:

$$
\neg(\sigma = \tau) \leftrightarrow \sigma < \tau \lor \tau < \sigma
$$
$$
\neg(\sigma < \tau) \leftrightarrow \tau = \sigma \lor \tau < \sigma
$$
$$
\neg(\sigma \equiv_{m} \tau) \leftrightarrow \sigma + 1 \equiv_{m} \tau \lor \cdots \lor \sigma + (m - 1) \equiv_{m} \tau.
$$

Therefore we may actually assume that $\psi$ is a conjunction of basic formulas (without negations). As in the proof of Lemma 13.4, we may assume that each conjunct actually involves $\alpha$. Now if $\sigma$ is a term involving $\alpha$, then there is a term $\tau$ not involving $\alpha$ and an $m \in \mathbb{Z}$ such that

$$\sigma = m\alpha + \tau$$

holds in $\mathfrak{A}$. It follows that formulas of the forms $\sigma = \tau$, $\sigma < \tau$, and $\sigma \equiv_m \tau$ can be rewritten so that all occurrences of the quantified variable $\alpha$ appear in a normalized linear form.

Now for $p > 0$ the following pairs of formulas are equivalent in $\mathfrak{A}$:

$$\sigma = \tau \quad \text{and} \quad p\sigma = p\tau;$$
$$\sigma < \tau \quad \text{and} \quad p\sigma < p\tau;$$
$$\sigma \equiv_m \tau \quad \text{and} \quad p\sigma \equiv_{mp} p\tau.$$

It follows that we may assume all coefficients of $\alpha$ in the conjuncts are equal and greater than $1$. Thus the formula $\exists\alpha\psi$ becomes of the form

$$\exists\alpha\bigl(p\alpha = \xi_0 \land \cdots \land p\alpha = \xi_{i-1} \land p\alpha < \xi_i \land \cdots \land p\alpha < \xi_{j-1} \land$$
$$\xi_j < p\alpha \land \cdots \land \xi_{k-1} < p\alpha \land p\alpha \equiv_{q_k} \xi_k \land \cdots \land p\alpha \equiv_{q_{l-1}} \xi_{l-1}\bigr)$$

where $0 \leq i \leq j \leq k \leq l$, $l > 0$, $p > 1$, $q_0, \ldots, q_{l-1} > 1$, and $\xi_0, \ldots, \xi_{l-1}$ do not involve $\alpha$. This in turn is clearly equivalent to

$$\exists\alpha\bigl(\alpha = \xi_0 \land \cdots \land \alpha = \xi_{i-1} \land \alpha < \xi_i \land \cdots \land \alpha < \xi_{j-1} \land \xi_j < \alpha$$
$$\land \cdots \land \xi_{k-1} < \alpha \land \alpha \equiv_p 0 \land \alpha \equiv_{q_k} \xi_k \land \cdots \land \alpha \equiv_{q_{l-1}} \xi_{l-1}\bigr).$$

In the case where equality conjuncts are present ($i > 0$), the existential quantifier can be eliminated by substituting one of the $\xi$'s for $\alpha$ and checking consistency. In the remaining cases, the existential formula can be expressed as a quantifier-free combination of formulas involving the $\xi$'s using the order and congruence relations, by analyzing the possible residues of $\alpha$ modulo suitable moduli. If $i = 0$ and $j = 0$ (no upper bounds) or if the system of inequalities admits a solution, the quantifier elimination proceeds by solving the system of congruences via the Chinese remainder theorem and checking satisfiability of the resulting linear inequalities. In all cases an equivalent quantifier-free formula can be effectively constructed.
