---
role: proof
locale: en
of_concept: kolmogorovs-extension-theorem-r-t
source_book: gtm095
source_chapter: "2"
source_section: "5"
---

# Proof of Kolmogorov's Theorem on the Extension of Measures on $(R^T, \mathcal{B}(R^T))$

Let the set $\hat{B} \in \mathcal{B}(R^T)$. By Theorem 3 of Sect. 2 there is an at most countable set $S = \{s_1, s_2, \ldots\} \subseteq T$ such that $\hat{B} = \{x : (x_{s_1}, x_{s_2}, \ldots) \in B\}$, where $B \in \mathcal{B}(R^S)$, $R^S = R_{s_1} \times R_{s_2} \times \cdots$. In other words, $\hat{B} = \mathcal{I}_S(B)$ is a cylinder set with base $B \in \mathcal{B}(R^S)$.

We can define a set function $P$ on such cylinder sets by putting

$$P(\mathcal{I}_S(B)) = P_S(B), \tag{22}$$

where $P_S$ is the probability measure whose existence is guaranteed by Theorem 3. We claim that $P$ is in fact the measure whose existence is asserted in the theorem. To establish this we first verify that the definition (22) is consistent, i.e., that it leads to a unique value of $P(\hat{B})$ for all possible representations of $\hat{B}$; and second, that this set function is countably additive.

Let $\hat{B} = \mathcal{I}_{S_1}(B_1)$ and $\hat{B} = \mathcal{I}_{S_2}(B_2)$. It is clear that then $\hat{B} = \mathcal{I}_{S_1 \cup S_2}(B_3)$ with some $B_3 \in \mathcal{B}(R^{S_1 \cup S_2})$; therefore it is enough to show that if $S \subseteq S'$ and $B \in \mathcal{B}(R^S)$, then $P_{S'}(B') = P_S(B)$, where

$$B' = \{(x_{s_1}', x_{s_2}', \ldots) : (x_{s_1}, x_{s_2}, \ldots) \in B\}$$

with $S' = \{s_1, s_2, \ldots, s_n, \ldots\}$ an extension of $S$. But this follows immediately from the consistency condition (20) and the construction of Theorem 3. Hence the definition (22) is consistent.

The countable additivity of $P$ on the cylinder sets follows from the countable additivity of the measures $P_S$ on the corresponding spaces $(R^S, \mathcal{B}(R^S))$ (guaranteed by Theorem 3) and from the fact that any countable collection of cylinder sets can be embedded into a single $S$ by taking the union of their supporting index sets.

Thus $P$ is a well-defined, countably additive probability measure on the cylinder sets, and by Carathéodory's theorem it extends uniquely to a probability measure on $\mathcal{B}(R^T)$.

**Remark.** If we consider ordered sets $\tau = (t_1, \ldots, t_n)$ of different indices (so that the collections $(a, b)$ and $(b, a)$ consisting of the same points are treated as different), then in order to have Theorem 4 hold we have to adjoin to (20) a further consistency condition:

$$P_{(t_1, \ldots, t_n)}(A_{t_1} \times \cdots \times A_{t_n}) = P_{(t_1, \ldots, t_n)}(A_{t_{i_1}} \times \cdots \times A_{t_{i_n}}), \tag{23}$$

where $(i_1, \ldots, i_n)$ is an arbitrary permutation of $(1, \ldots, n)$ and $A_{t_i} \in \mathcal{B}(R_{t_i})$. The necessity of this condition for the existence of the probability measure $P$ follows from (21) (with $P_{[t_1, \ldots, t_n]}(B)$ replaced by $P_{(t_1, \ldots, t_n)}(B))$.
