---
role: proof
locale: en
of_concept: deduction-lemma
source_book: gtm053
source_chapter: "II"
source_section: "4"
---

# Proof of the Deduction Lemma

**Lemma 4.5 (Deduction Lemma).** Suppose that $\mathcal{E} \supset \mathrm{Ax}\,L$ contains all logical axioms and is closed under modus ponens, and $P$ is a closed formula. If $\mathcal{E} \cup \{P\} \vdash Q$, then $\mathcal{E} \vdash P \Rightarrow Q$.

*Proof.* We proceed by induction on the length of the deduction of $Q$ from $\mathcal{E} \cup \{P\}$. Let $Q_1, \ldots, Q_n = Q$ be a deduction of $Q$. For each $i \leq n$, we construct a deduction of $P \Rightarrow Q_i$ from $\mathcal{E}$.

For the inductive step, we consider the possible justifications for $Q_i$ appearing in the original deduction:

**(a)** $Q_i$ is a logical axiom or an axiom in $\mathcal{E}$. Then we have the deduction:
$$Q_i, \quad Q_i \Rightarrow (P \Rightarrow Q_i), \quad P \Rightarrow Q_i$$
where the second formula is a tautology (axiom A1: $\phi \Rightarrow (\psi \Rightarrow \phi)$), and the third follows by MP.

**(b)** $Q_i$ is the assumption $P$. Then $P \Rightarrow P$ is a tautology (derivable from the logical axioms A0, A1, A2 as shown in Lemma 4.3). Hence $\mathcal{E} \vdash P \Rightarrow P$.

**(c)** $Q_i$ follows from $Q_j$ and $Q_k = Q_j \Rightarrow Q_i$ by MP, for some $j, k < i$. By the induction hypothesis, we already have deductions of $P \Rightarrow Q_j$ and $P \Rightarrow (Q_j \Rightarrow Q_i)$ from $\mathcal{E}$. We extend these with:
$$(P \Rightarrow (Q_j \Rightarrow Q_i)) \Rightarrow ((P \Rightarrow Q_j) \Rightarrow (P \Rightarrow Q_i))$$
which is an instance of axiom A2: $(\phi \Rightarrow (\psi \Rightarrow \chi)) \Rightarrow ((\phi \Rightarrow \psi) \Rightarrow (\phi \Rightarrow \chi))$. Applying MP twice yields $P \Rightarrow Q_i$.

**(d)** $Q_i$ is $\forall x\, R$ obtained from $R$ by the generalization rule Gen. Since $P$ is closed, $x$ does not occur free in $P$. By the induction hypothesis, $\mathcal{E} \vdash P \Rightarrow R$. Then:
$$\forall x(P \Rightarrow R) \quad \text{(Gen)}$$
$$\forall x(P \Rightarrow R) \Rightarrow (P \Rightarrow \forall x R) \quad \text{(logical quantifier axiom, since } P \text{ is closed)}$$
$$P \Rightarrow \forall x R \quad \text{(MP)}$$

This gives $\mathcal{E} \vdash P \Rightarrow \forall x R = P \Rightarrow Q_i$.

By induction, we obtain a deduction of $P \Rightarrow Q_n = P \Rightarrow Q$ from $\mathcal{E}$. $\square$
