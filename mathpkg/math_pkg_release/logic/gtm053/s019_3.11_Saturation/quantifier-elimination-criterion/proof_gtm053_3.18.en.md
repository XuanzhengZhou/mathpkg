---
role: proof
locale: en
of_concept: quantifier-elimination-criterion
source_book: gtm053
source_chapter: "3"
source_section: "3.18"
---

**(ii) $\Rightarrow$ (i):** Assuming (ii), every $n$-type is equivalent to a quantifier-free $n$-type. Hence $\text{qftp}(\bar{a}) = \text{qftp}(\bar{b})$ implies $\text{tp}(\bar{a}) = \text{tp}(\bar{b})$, and by the Proposition on saturated types and automorphisms, there exists $\pi \in \text{Aut}(\mathbf{A})$ with $\pi(\bar{a}) = \bar{b}$.

**(i) $\Rightarrow$ (ii):** We prove the converse. Let $Q(\bar{x})$ be an $L$-formula with $n$ free variables. Consider the set

$$\Phi(\bar{x}) := \{\theta(\bar{x}) : \theta \text{ is quantifier-free and } T \vdash Q(\bar{x}) \to \theta(\bar{x})\}.$$

We claim that $T \vdash \Phi(\bar{x}) \to Q(\bar{x})$. If not, by compactness there exists a model $\mathbf{A}$ of $T$ (which we may take to be saturated by passing to a saturated elementary extension) and a tuple $\bar{a}$ in $\mathbf{A}$ such that $\mathbf{A} \vDash \Phi(\bar{a})$ but $\mathbf{A} \vDash \neg Q(\bar{a})$.

Now consider the quantifier-free type $\text{qftp}(\bar{a})$. Since $\mathbf{A} \vDash \neg Q(\bar{a})$, the formula $\neg Q(\bar{x})$ is consistent with the quantifier-free consequences of $Q$. By a compactness argument, there exists a tuple $\bar{b}$ in some elementary extension (which we may absorb into the saturated model) such that $\text{qftp}(\bar{b}) = \text{qftp}(\bar{a})$ and $\mathbf{A} \vDash Q(\bar{b})$.

By condition (i), since $\text{qftp}(\bar{a}) = \text{qftp}(\bar{b})$, there exists $\pi \in \text{Aut}(\mathbf{A})$ with $\pi(\bar{a}) = \bar{b}$. But automorphisms preserve all formulas, not just quantifier-free ones, so $\mathbf{A} \vDash Q(\bar{a})$ iff $\mathbf{A} \vDash Q(\bar{b})$, a contradiction.

Therefore $T \vdash \Phi(\bar{x}) \leftrightarrow Q(\bar{x})$. Since $\Phi$ is a (possibly infinite) set of quantifier-free formulas, by compactness there is a finite subset whose conjunction is equivalent to $Q$ modulo $T$, yielding a quantifier-free equivalent of $Q$.
