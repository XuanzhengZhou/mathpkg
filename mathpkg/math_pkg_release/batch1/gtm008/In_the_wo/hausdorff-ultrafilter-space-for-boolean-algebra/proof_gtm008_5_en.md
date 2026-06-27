---
role: proof
locale: en
of_concept: hausdorff-ultrafilter-space-for-boolean-algebra
source_book: gtm008
source_chapter: "5"
source_section: "Partial Order Structures and Topological Spaces"
---

**Proof.** Suppose not. Then there would exist distinct $F_1, F_2 \in \mathcal{F}$ such that

$$(\forall p_1 \in F_1)(\forall p_2 \in F_2)(\exists F \in \mathcal{F})[p_1 \in F \land p_2 \in F].$$

Then $(\exists r \in F)[r \leq p_1 \land r \leq p_2]$, i.e., $p_1p_2 \neq 0$.

Define $G = \{p \in P \mid (\exists p_1 \in F_1)(\exists p_2 \in F_2)[p_1p_2 \leq p]\}$. We show $G$ is a filter for $\mathcal{P}$. If $p, q \in G$, then

$$(\exists p_1, q_1 \in F_1)(\exists p_2, q_2 \in F_2)[p_1p_2 \leq p \land q_1q_2 \leq q].$$

Since $F_1$ and $F_2$ are filters, $p_1q_1 \in F_1$ and $p_2q_2 \in F_2$. Furthermore $p_1q_1p_2q_2 \leq pq$, so $pq \in G$. Thus for each $p, q \in G$ there is an $r \in G$, namely $pq$, such that $r \leq p$ and $r \leq q$. Clearly $G$ is upward hereditary.

Since $G$ is a filter, $F_1 \subseteq G$ and $F_2 \subseteq G$, and $F_1$ and $F_2$ are distinct ultrafilters, we have a contradiction. Therefore $\langle \mathcal{F}, \mathcal{T} \rangle$ is Hausdorff. $\square$
