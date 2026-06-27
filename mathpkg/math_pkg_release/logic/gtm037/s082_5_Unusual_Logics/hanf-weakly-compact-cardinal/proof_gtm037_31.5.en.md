---
role: proof
locale: en
of_concept: hanf-weakly-compact-cardinal
source_book: gtm037
source_chapter: "31"
source_section: "5"
---

Assume the hypothesis holds but the conclusion fails. By 31.10 and 31.11, $m$ is weakly inaccessible but not a power of $2$. We take a language $L$ with nonlogical constants $<$, $F$ (ternary), $G$ (ternary), $H$ (4-ary), $P$, $Q$, $R$ (unary). Let $\Gamma$ be the following set of sentences of $L_{mm}$:

(1) $<$ is a well-ordering;
(2) $\exists v_0 \varphi_\alpha$ (for each $\alpha < m$);
(3) $\forall v_0 \forall v_1 \forall v_2 \forall v_3 (Fv_0 v_1 v_2 \land Fv_0 v_1 v_3 \rightarrow v_2 = v_3)$;
(4) $\forall v_0 \exists v_1 [v_1 < v_0 \land \forall v_2 \forall v_3 (Fv_0 v_2 v_3 \rightarrow v_2 < v_1 \land v_3 < v_0)]$;
(5) $\forall v_0 \forall v_1 [Pv_0 \land v_1 < v_0 \rightarrow \exists v_2 \exists v_3 (Fv_0 v_2 v_3 \land v_1 < v_3)]$;
(6) $\forall v_0 \forall v_1 \forall v_2 \forall v_3 [(Gv_0 v_1 v_2 \land Gv_0 v_1 v_3 \rightarrow v_2 = v_3) \land (Gv_0 v_2 v_1 \land Gv_0 v_3 v_1 \rightarrow v_2 = v_3)]$;
(7) $\forall v_0 [Qv_0 \rightarrow \exists v_1 \forall v_2 \forall v_3 (Gv_0 v_2 v_3 \rightarrow v_2 < v_1)]$;
(8) $\forall v_0 [Qv_0 \rightarrow \forall v_2 \exists v_3 Gv_0 v_2 v_3]$;
(9) $\forall v_0 [v_0 \neq 0 \rightarrow Pv_0 \lor Qv_0]$;
(10) sentences ensuring $H$ encodes a surjection witnessing each cardinal in $Q$ is a power of $2$.

From sentences (2), it follows that $m \subseteq \alpha + 1$ hence $m \leq \alpha + 1$ and actually $m \leq \alpha$ since $m$ is an infinite cardinal. Thus $m \in \alpha + 1$. We shall obtain a contradiction by showing that each uncountable infinite cardinal $n \in \alpha + 1$ is accessible, i.e., is either singular or else satisfies $n \leq 2^p$ for some $p < n$. By (9) we have $n \in P^{\mathfrak{A}}$ or $n \in Q^{\mathfrak{A}}$.

Case 1. $n \in P^{\mathfrak{A}}$. Let $f = \{(\beta, \gamma) : (n, \beta, \gamma) \in F^{\mathfrak{A}}\}$. Thus by (3), $f$ is a function. By (4) we can choose $\delta < n$ such that $f$ maps a subset of $\delta$ into $n$. By (5), $\bigcup \operatorname{Rng} f = n$. Thus $n$ is singular.

Case 2. $n \in Q^{\mathfrak{A}}$. By (7), choose $\beta < n$ such that $\delta < \beta$ whenever $(n, \gamma, \delta) \in G^{\mathfrak{A}}$. Now for each $\gamma < n$ let $f\gamma = \{\delta : (n, \gamma, \delta) \in G^{\mathfrak{A}}\}$. Thus $f\gamma \subseteq \beta$. And by (6), $f$ is one-one. Hence $f: n \rightarrow \mathcal{P}(\beta)$, as desired.

Since $m$ is strongly inaccessible, we have reached a contradiction. Thus $\Gamma$ has no model.

Now let $\Delta$ be a subset of $\Gamma$ of power $< m$. Let $\beta$ be the supremum of all ordinals $\alpha < m$ such that $\exists v_0\varphi_\alpha \in \Delta$. We now build up a model $\mathfrak{A}$ of $\Delta$ with universe $A = \beta + 1$ and with the natural ordering of $\beta + 1$ as the interpretation of $<$. Thus (1), (2), and (8) automatically hold. The relations $P^{\mathfrak{A}}$, $Q^{\mathfrak{A}}$, $F^{\mathfrak{A}}$, $G^{\mathfrak{A}}$, $H^{\mathfrak{A}}$ are defined appropriately to satisfy the remaining sentences in $\Delta$.
