---
role: proof
locale: en
of_concept: lemma-2-G-tilde-a-G
source_book: gtm008
source_chapter: "11"
source_section: "11 The Independence of V = L and the CH"
---

**Proof of Lemma 2.** Take any $\langle p_1, p_2 \rangle \in P$ such that $p_1 \subseteq \tilde{a}(G)$ and $p_2 \subseteq \omega - \tilde{a}(G)$. We need to show $\langle p_1, p_2 \rangle \in G$.

Since $\tilde{a}(G) = \{ n \in \omega \mid (\exists p_1', p_2')\,[n \in p_1' \wedge \langle p_1', p_2' \rangle \in G] \}$, for each $n \in p_1$ there exists $q^n = \langle q_1^n, q_2^n \rangle \in G$ with $n \in q_1^n$. By genericity and finiteness of $p_1$, there exists $r \in G$ such that $r \leq q^n$ for all $n \in p_1$, so $r = \langle r_1, r_2 \rangle$ with $p_1 \subseteq r_1$. Take $q = \langle r_1, 0 \rangle$; then $q \leq r$ implies $q \in G$ by upward closure, and $p_1 \subseteq q_1$.

Now let $p_2 = \{m_1, \ldots, m_l\}$ and define

$$S = \bigcup_{i=1}^{l} [\langle m_i, 0 \rangle] \cup [\langle 0, p_2 \rangle],$$

where $[p]$ denotes the set of conditions below $p$. Then $S$ is dense: for any condition $t = \langle t_1, t_2 \rangle$, if some $m_i \notin t_2$ we can extend to include $m_i$ in the first coordinate, and otherwise if $p_2 \subseteq t_2$ we can extend to include $0$; in all cases we find an extension in $S$. Hence $S \cap G \neq \varnothing$.

Let $q' \in S \cap G$. Since $p_2 \subseteq \omega - \tilde{a}(G)$, we have $q_1' \cap p_2 = \varnothing$ where $q' = \langle q_1', q_2' \rangle$. Therefore $q' \leq \langle 0, p_2 \rangle$.

Since $q, q' \in G$, there exists $r \in G$ with $r \leq q$ and $r \leq q'$. Because $q \leq \langle p_1, 0 \rangle$ and $q' \leq \langle 0, p_2 \rangle$, we have $r \leq \langle p_1, p_2 \rangle$. Hence $\langle p_1, p_2 \rangle \in G$ by the upward closure of $G$.

Therefore $\tilde{G}(\tilde{a}(G)) \subseteq G$. $\square$
