---
role: proof
locale: en
of_concept: lemma-downward-ls-weak-second-order
source_book: gtm037
source_chapter: "30"
source_section: "5"
---

The proof is an extension of Lemma 19.16 and the proof of the downward Lowenheim--Skolem theorem 19.17. Let $\mathfrak{B}$ be an $\mathcal{L}$-structure. We construct an increasing sequence $D_0 \subseteq D_1 \subseteq \cdots$ of subsets of $B$ as follows. Let $D_0$ be any countable subset of $B$.

Given $D_m$, we define $D_{m+1}$ by adding Skolem witnesses for all existential formulas (both first-order and weak second-order) satisfied in $\mathfrak{B}$ with parameters from $D_m$. For each tuple $(G, \varphi, k, l, x, y) \in J_m$:

- If $\mathfrak{B} \models \exists v_k \varphi[x; y]$ (first-order existential), add a witness $a \in B$ such that $\mathfrak{B} \models \varphi[x_a^k; y]$, represented as the closure $\mathcal{C}\{a : \mathfrak{B} \models \varphi[x_a^k; y]\}$.

- If $\mathfrak{B} \models \exists F_i \varphi[x; y]$ (weak second-order existential over finite subsets), add a finite subset $H \subseteq B$ such that $\mathfrak{B} \models \varphi[x; y_H^l]$, represented as the closure $\mathcal{C}\{H : \mathfrak{B} \models \varphi[x; y_H^l]\}$.

The crucial point is that $H$ is a finite set, so its elements are finitely many individuals added to $D_{m+1}$. Thus the cardinality of $D_{m+1}$ remains at most $\max(|D_m|, \aleph_0)$. The construction ensures that equality (5) from the proof of 19.17 still holds for the weak second-order formulas, where $y_j = 0$ whenever $F_j$ does not occur in $\varphi$.

Let $\mathfrak{A}$ be the substructure of $\mathfrak{B}$ with universe $D = \bigcup_{m \in \omega} D_m$. Then $|A| \leq \max(|D_0|, \aleph_0) \cdot \aleph_0 = \aleph_0$, and by the usual Tarski--Vaught argument extended with the finite-subset witnesses, $\mathfrak{A} \preccurlyeq \mathfrak{B}$ in weak second-order logic. Hence the downward Lowenheim--Skolem theorem holds: every structure has a countable elementary substructure in weak second-order logic.
