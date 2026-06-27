---
role: proof
locale: en
of_concept: compactness-theorem
source_book: gtm053
source_chapter: "X"
source_section: "2"
---

# Proof of Compactness Theorem (First-Order Logic)

**Theorem 2.1 (Compactness Theorem).** Let $E$ be a finitely satisfiable set of $L$-sentences. Then $E$ is satisfiable; moreover, $E$ has a model of cardinality less than or equal to $|L| + \aleph_0$.

*Proof.* There are several proofs of this theorem, each using the Axiom of Choice. We present the proof via Gödel's Completeness Theorem and the Henkin construction.

**Step 1: Consistency (Lemma 2.2).** $E$ is consistent. Suppose $E \vdash P$. Then $E^0 \vdash P$ for some finite $E^0 \subseteq E$, since only finitely many formulas are involved in the proof. In particular, if $E$ were inconsistent, already its finite subset $E^0$ would be. But then $E^0$ could not be satisfiable, contradicting the assumption that $E$ is finitely satisfiable. Hence $E$ is consistent.

**Step 2: Completion (Lindenbaum's Theorem 2.3).** $E$ can be completed; that is, there exists a complete finitely satisfiable set of $L$-sentences $E^\sharp$ such that $E \subseteq E^\sharp$. Using the Axiom of Choice (Zorn's Lemma), let

$$S = \{E' : E \subseteq E' \text{ is a finitely satisfiable set of } L\text{-sentences}\}.$$

$S$ satisfies the hypothesis of Zorn's Lemma, so it contains a maximal element $E^\sharp$. This $E^\sharp$ is complete: if there were a sentence $S$ with $S \notin E^\sharp$ and $\neg S \notin E^\sharp$, then by maximality neither $\{S\} \cup E^\sharp$ nor $\{\neg S\} \cup E^\sharp$ would be finitely satisfiable, leading to a contradiction.

**Step 3: Adding witnesses (Lemma 2.6).** For some extension $\tilde{L} \supseteq L$ of the language, with $|\tilde{L}| = |L| + \aleph_0$, there exists an extension $\tilde{\mathcal{E}} \supseteq \mathcal{E}$ of $\mathcal{E}$ to a complete finitely satisfiable set of $\tilde{L}$-sentences with witnesses.

Construct $\tilde{L}$ by adding $|L| + \aleph_0$ new constant symbols. Define an increasing chain of languages $L_i$ and complete sets $\mathcal{E}_i$ of $L_i$-sentences for $i = 0, 1, \ldots$:

- $L_0 = L$, and $\mathcal{E}_0 \supseteq \mathcal{E}$ is a complete set of $L_0$-sentences (by Lindenbaum's Theorem).
- Given $\mathcal{E}_i$ in $L_i$, define
  $$L_{i+1} = L_i \cup \{c_Q : Q \text{ a one-variable } L_i\text{-formula}\}$$
  and
  $$\mathcal{E}_i^* = \mathcal{E}_i \cup \{(\exists v\, Q(v) \to Q(c_Q)) : Q \text{ a one-variable } L_i\text{-formula}\}.$$

One shows $\mathcal{E}_i^*$ is finitely satisfiable. Then by Lindenbaum's Theorem extend to a complete set $\mathcal{E}_{i+1}$ in $L_{i+1}$. Set $\tilde{L} = \bigcup_i L_i$ and $\tilde{\mathcal{E}} = \bigcup_i \mathcal{E}_i$.

**Step 4: Canonical Model.** Construct a model $\mathbf{A}$ of $\tilde{\mathcal{E}}$ as follows. The domain $A$ consists of equivalence classes $[\tau]$ of constant terms $\tau$ of $\tilde{L}$, where $\tau_1 \sim \tau_2$ iff $(\tau_1 = \tau_2) \in \tilde{\mathcal{E}}$. For a relation symbol $p$ of arity $n$, define

$$\mathbf{A} \models p([\tau_1], \ldots, [\tau_n]) \iff p(\tau_1, \ldots, \tau_n) \in \tilde{\mathcal{E}}.$$

For a function symbol $f$ of arity $m$, define $f^{\mathbf{A}}([\tau_1], \ldots, [\tau_m]) = [\tau]$ where $f(\tau_1, \ldots, \tau_m) = \tau \in \tilde{\mathcal{E}}$. For a constant symbol $c$, $c^{\mathbf{A}} = [c]$.

By induction on formula complexity, $\mathbf{A} \models Q([\tau_1], \ldots, [\tau_n])$ iff $Q(\tau_1, \ldots, \tau_n) \in \tilde{\mathcal{E}}$. Hence $\mathbf{A}$ is a model of $\tilde{\mathcal{E}}$, and its reduct to $L$ is a model of $E$. The cardinality bound $|A| \leq |L| + \aleph_0$ follows since the number of constant terms of $\tilde{L}$ is $|\tilde{L}| = |L| + \aleph_0$. $\square$

*Alternative proofs.* The theorem can also be proved via ultraproducts (see Loś's Theorem 2.10) and via the method of diagrams (Section 3.2).
