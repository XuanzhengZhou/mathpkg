---
role: proof
locale: en
of_concept: consistency-family-downward-closure
source_book: gtm037
source_chapter: "31"
source_section: "5"
---

The following lemma is proved just like 18.7. Let $S' = \{\Gamma : \Gamma \subseteq \Delta \text{ for some } \Delta \in S\}$. We verify each condition.

For (C0): If $\Gamma \in S'$, then $\Gamma \subseteq \Delta$ for some $\Delta \in S$. Since $\Delta$ is countable (as $S$ consists of countable sets), $\Gamma$ is also countable.

For (C3'): Suppose $\bigwedge_{i<\omega}\varphi_i \in \Gamma \in S'$. Then $\Gamma \subseteq \Delta$ for some $\Delta \in S$, so $\bigwedge_{i<\omega}\varphi_i \in \Delta$. Since $S$ satisfies (C3'), $\Delta \cup \{\varphi_i\} \in S$ for each $i$. But $\Gamma \cup \{\varphi_i\} \subseteq \Delta \cup \{\varphi_i\}$, hence $\Gamma \cup \{\varphi_i\} \in S'$.

For (C4'): Suppose $\bigvee_{i<\omega}\varphi_i \in \Gamma \in S'$. Then $\bigvee_{i<\omega}\varphi_i \in \Delta$ for some $\Delta \in S$. Since $S$ satisfies (C4'), there exists $i$ such that $\Delta \cup \{\varphi_i\} \in S$. Then $\Gamma \cup \{\varphi_i\} \subseteq \Delta \cup \{\varphi_i\}$, so $\Gamma \cup \{\varphi_i\} \in S'$.

The remaining conditions (C1)-(C9) are verified similarly as in Lemma 18.7.
