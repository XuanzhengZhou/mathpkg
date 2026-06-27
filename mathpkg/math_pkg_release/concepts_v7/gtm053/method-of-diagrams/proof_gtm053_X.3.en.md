---
role: proof
locale: en
of_concept: method-of-diagrams
source_book: gtm053
source_chapter: "X"
source_section: "3"
---

# Proof of Method of Diagrams

**Theorem (Method of Diagrams).** For an $L$-structure $\mathbf{A}$, let $L_A = L \cup \{c_a : a \in A\}$ be the expansion of the language and let $\mathbf{A}_A$ be the natural expansion of $\mathbf{A}$ to $L_A$ assigning to $c_a$ the element $a$. Define the *diagram* of $\mathbf{A}$:

$$\mathrm{Diag}(\mathbf{A}) = \{S : \text{atomic or negation of atomic } L_A\text{-sentence such that } \mathbf{A}_A \models S\}$$

and the *complete diagram*:

$$\mathrm{CDiag}(\mathbf{A}) = \{S : L_A\text{-sentence such that } \mathbf{A}_A \models S\}.$$

For an $L$-structure $\mathbf{B}$,

(i) there exists an expansion $\mathbf{B}_A$ to $L_A$ such that $\mathbf{B}_A \models \mathrm{Diag}(\mathbf{A})$ iff $\mathbf{A} \subseteq \mathbf{B}$ (i.e., $\mathbf{A}$ embeds into $\mathbf{B}$).

(ii) there exists an expansion $\mathbf{B}_A$ to $L_A$ such that $\mathbf{B}_A \models \mathrm{CDiag}(\mathbf{A})$ iff $\mathbf{A} \preceq \mathbf{B}$ (i.e., $\mathbf{A}$ is an elementary substructure of $\mathbf{B}$).

*Proof.* (i) By definition, the map $a \mapsto c_a^{\mathbf{B}_A}$ is an embedding iff $\mathbf{B}_A \models \mathrm{Diag}(\mathbf{A})$. Indeed, an embedding preserves all atomic formulas and their negations. The sentences in $\mathrm{Diag}(\mathbf{A})$ are exactly the atomic and negated-atomic facts true in $\mathbf{A}_A$. The assignment $a \mapsto c_a^{\mathbf{B}_A}$ satisfies these sentences precisely when it is an embedding of $\mathbf{A}$ into $\mathbf{B}$.

(ii) Similarly, the map $a \mapsto c_a^{\mathbf{B}_A}$ is an elementary embedding (i.e., $\mathbf{A} \preceq \mathbf{B}$) iff $\mathbf{B}_A \models \mathrm{CDiag}(\mathbf{A})$. The complete diagram contains all $L_A$-sentences true in $\mathbf{A}_A$, so satisfying it means that $\mathbf{B}_A$ is elementarily equivalent to $\mathbf{A}_A$ under the interpretation $c_a \mapsto a$, which is exactly the definition of $\mathbf{A} \preceq \mathbf{B}$. $\square$

**Corollary.** Given an $L$-structure $\mathbf{A}$ and an $L$-theory $T$, $T \cup \mathrm{Diag}(\mathbf{A})$ is consistent iff $\mathbf{A}$ embeds into a model of $T$; $T \cup \mathrm{CDiag}(\mathbf{A})$ is consistent iff $\mathbf{A}$ elementarily embeds into a model of $T$.
