---
role: proof
locale: en
of_concept: quantifier-elimination-criterion
source_book: gtm053
source_chapter: "X"
source_section: "3"
---

# Proof of Quantifier Elimination Criterion (via Automorphisms)

**Proposition 3.18.** Given a saturated $L$-structure $\mathbf{A}$ and two $n$-tuples $\bar{a}$ and $\bar{b}$ in $\mathbf{A}$,

$$\operatorname{tp}(\bar{a}) = \operatorname{tp}(\bar{b}) \quad \text{iff there exists } \pi \in \operatorname{Aut}(\mathbf{A}) \text{ such that } \pi : \bar{a} \mapsto \bar{b}.$$

*Proof.* The right-to-left implication is trivial: automorphisms preserve all first-order formulas, hence types. For the left-to-right implication, assume $\operatorname{tp}(\bar{a}) = \operatorname{tp}(\bar{b})$. Extend the language $L$ by $n$ new constant symbols, interpreting them as $\bar{a}$ in the first expansion and as $\bar{b}$ in the second. We obtain two expansions $\mathbf{A}_{\bar{a}}$ and $\mathbf{A}_{\bar{b}}$ of $\mathbf{A}$ to the extended language. Both remain saturated (saturation is preserved under adding finitely many constants). Since $\operatorname{tp}(\bar{a}) = \operatorname{tp}(\bar{b})$, the two expansions satisfy the same $L(\bar{c})$-sentences; i.e., $\operatorname{Th}(\mathbf{A}_{\bar{a}}) = \operatorname{Th}(\mathbf{A}_{\bar{b}})$. By the uniqueness part of Theorem 3.11(ii), two saturated models of the same complete theory and of the same cardinality are isomorphic. Hence there exists an isomorphism $\pi : \mathbf{A}_{\bar{a}} \to \mathbf{A}_{\bar{b}}$. As an $L$-automorphism of $\mathbf{A}$, $\pi$ sends $\bar{a}$ to $\bar{b}$. $\square$

---

**Theorem 3.18 (Quantifier Elimination Criterion).** Given a saturated model $\mathbf{A}$ of a complete theory $T$, the following two conditions are equivalent:

(i) For any two $n$-tuples $\bar{a}$ and $\bar{b}$ in $\mathbf{A}$,

$$\operatorname{qftp}(\bar{a}) = \operatorname{qftp}(\bar{b}) \iff \text{there exists } \pi \in \operatorname{Aut}(\mathbf{A}) \text{ such that } \pi : \bar{a} \mapsto \bar{b}.$$

(ii) Any $L$-formula with $n$ free variables is equivalent (modulo $T$) to a quantifier-free $L$-formula.

*Proof.* (ii) $\Rightarrow$ (i): Assume every formula is equivalent to a quantifier-free one. Then $\operatorname{qftp}(\bar{a}) = \operatorname{qftp}(\bar{b})$ implies $\operatorname{tp}(\bar{a}) = \operatorname{tp}(\bar{b})$. By the Proposition above, there exists $\pi \in \operatorname{Aut}(\mathbf{A})$ with $\pi(\bar{a}) = \bar{b}$.

(i) $\Rightarrow$ (ii): Let $Q(\bar{x})$ be an $L$-formula with $n$ free variables. Consider the set

$$\Gamma(\bar{x}) = \{\theta(\bar{x}) : \theta \text{ is quantifier-free and } T \models \forall \bar{x}(Q(\bar{x}) \to \theta(\bar{x}))\}.$$

We claim that $\Gamma(\bar{x})$ entails $Q(\bar{x})$ modulo $T$; that is, if $\bar{a}$ satisfies $\Gamma(\bar{x})$ in some model of $T$, then it satisfies $Q(\bar{x})$. By compactness, this would imply that some finite subset of $\Gamma$ (hence a single quantifier-free formula) is equivalent to $Q(\bar{x})$.

Suppose for contradiction that there exists a model $\mathbf{M} \models T$ and a tuple $\bar{a} \in M^n$ such that $\mathbf{M} \models \Gamma(\bar{a})$ but $\mathbf{M} \not\models Q(\bar{a})$. Pass to a sufficiently saturated elementary extension $\mathbf{A} \succeq \mathbf{M}$ in which all relevant types are realized.

Since $\mathbf{A} \models \Gamma(\bar{a})$ and $\mathbf{A} \models \neg Q(\bar{a})$, we can consider the quantifier-free type $\operatorname{qftp}(\bar{a})$. By a standard compactness argument, there exists a tuple $\bar{b} \in A^n$ such that $\mathbf{A} \models Q(\bar{b})$ and $\operatorname{qftp}(\bar{b}) = \operatorname{qftp}(\bar{a})$. (If not, the quantifier-free type of $\bar{a}$ together with $Q(\bar{x})$ would be inconsistent, implying $Q$ is equivalent to the negation of a quantifier-free formula.)

Now $\operatorname{qftp}(\bar{a}) = \operatorname{qftp}(\bar{b})$ but one satisfies $Q$ and the other $\neg Q$. By condition (i), there exists $\pi \in \operatorname{Aut}(\mathbf{A})$ with $\pi(\bar{a}) = \bar{b}$. But automorphisms preserve all formulas, so $\mathbf{A} \models Q(\bar{a}) \iff \mathbf{A} \models Q(\bar{b})$, contradicting the assumption.

Thus $\Gamma(\bar{x})$ entails $Q(\bar{x})$ modulo $T$, proving that $Q(\bar{x})$ is equivalent to a quantifier-free formula. $\square$
