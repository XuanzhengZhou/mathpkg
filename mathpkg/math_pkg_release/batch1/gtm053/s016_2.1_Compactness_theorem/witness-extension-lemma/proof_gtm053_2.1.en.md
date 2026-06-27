---
role: proof
locale: en
of_concept: witness-extension-lemma
source_book: gtm053
source_chapter: "2"
source_section: "2.1"
---

We obtain $\tilde{L}$ by adding $|L| + \aleph_0$ new constant symbols. Introduce new languages $L_i$ and complete sets of $L_i$-sentences $\mathcal{E}_i$ for $i = 0, 1, 2, \ldots$

**Base step.** Let $L_0 = L$. By Lindenbaum's theorem (2.3), there exists $\mathcal{E}_0 \supseteq E$, a complete finitely satisfiable set of $L_0$-sentences.

**Inductive step.** Given a finitely satisfiable $\mathcal{E}_i$ in language $L_i$, introduce the new language

$$L_{i+1} = L_i \cup \{c_Q : Q \text{ a one-variable } L_i\text{-formula}\}$$

and the new set of $L_{i+1}$-sentences

$$\mathcal{E}_i^* = \mathcal{E}_i \cup \{\exists v\,Q(v) \to Q(c_Q) : Q \text{ a one-variable } L_i\text{-formula}\}.$$

*Claim.* $\mathcal{E}_i^*$ is finitely satisfiable.

*Proof of claim.* Given a finite $\mathcal{E}' \subseteq \mathcal{E}_i^*$, let $\mathcal{E}'' = \mathcal{E}' \cap \mathcal{E}_i$ and take a model $\mathbf{A}$ of $\mathcal{E}''$ with domain $A$, which we assume well-ordered. Assign constants to the new symbols $c_Q$ as follows:

$$c_Q^{\mathbf{A}} = \begin{cases} \text{the first element in } Q(\mathbf{A}), & \text{if } Q(\mathbf{A}) \neq \varnothing, \\ \text{the first element in } A, & \text{otherwise.} \end{cases}$$

Then for each Henkin axiom $\exists v\,Q(v) \to Q(c_Q)$ in $\mathcal{E}'$, if $\mathbf{A} \models \exists v\,Q(v)$ then $Q(\mathbf{A}) \neq \varnothing$, so $c_Q^{\mathbf{A}}$ is chosen from $Q(\mathbf{A})$ and $\mathbf{A} \models Q(c_Q)$. If $\mathbf{A} \not\models \exists v\,Q(v)$, the implication holds vacuously. Thus the expanded structure satisfies all sentences in $\mathcal{E}'$, proving the claim.

Now apply Lindenbaum's theorem (2.3) to $\mathcal{E}_i^*$ in language $L_{i+1}$ to obtain a complete finitely satisfiable set $\mathcal{E}_{i+1} \supseteq \mathcal{E}_i^*$ of $L_{i+1}$-sentences.

**Completion.** Set $\tilde{L} = \bigcup_{i=0}^{\infty} L_i$ and $\mathcal{E}_{\infty} = \bigcup_{i=0}^{\infty} \mathcal{E}_i$. Then $|\tilde{L}| = |L| + \aleph_0$ (each stage adds at most $|L| + \aleph_0$ new constants, and there are countably many stages). The set $\mathcal{E}_{\infty}$ is finitely satisfiable (any finite subset lies in some $\mathcal{E}_i$) and has witnesses for every one-variable $\tilde{L}$-formula (each such formula appears at some finite stage).

Finally, apply Lindenbaum's theorem once more to $\mathcal{E}_{\infty}$ in language $\tilde{L}$ to obtain a complete finitely satisfiable $\tilde{\mathcal{E}} \supseteq \mathcal{E}_{\infty}$ (hence $\tilde{\mathcal{E}} \supseteq E$) with witnesses.
