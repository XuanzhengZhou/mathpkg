---
role: proof
locale: en
of_concept: boolean-valued-model-of-zf
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

The proof proceeds by verifying that the sequence of structures $\langle V_{\alpha}^{(B)} \mid \alpha \in On \rangle$ satisfies conditions 1-5 specified in Section 9 (see Remark following Definition 9.2):

1. $V_{\alpha}^{(B)} \subseteq V_{\beta}^{(B)}$ for $\alpha \leq \beta$ (obvious from the definition).
2. $V_{\alpha}^{(B)} = \bigcup_{\xi < \alpha} V_{\xi}^{(B)}$ for limit $\alpha$ (Theorem 13.2).
3. $V_{\alpha}^{(B)}$ satisfies the Axiom of Extensionality (Theorem 13.9).
4. (Comprehension/Separation) For any formula $\varphi(x, a_1, \ldots, a_n)$ and parameters $a_1, \ldots, a_n \in V_{\alpha}^{(B)}$, the set $\{x \in V_{\alpha}^{(B)} \mid \varphi(x, a_1, \ldots, a_n)\}$ exists in $V_{\alpha+1}^{(B)}$.

   Let $b: V_{\alpha}^{(B)} \to B$ be defined by $b(a) = [\![\varphi(a, a_1, \ldots, a_n)]\!]_{\alpha}$ for $a \in V_{\alpha}^{(B)}$. Then $b \in V_{\alpha+1}^{(B)}$ and for each $a \in V_{\alpha}^{(B)}$:
   $$[\![a \in b]\!] = \sum_{a' \in V_{\alpha}^{(B)}} [\![\varphi(a', a_1, \ldots, a_n)]\!]_{\alpha} \cdot [\![a' = a]\!]$$
   $$\leq [\![\varphi(a, a_1, \ldots, a_n)]\!]_{\alpha}$$
   by the equality axioms, while $[\![a \in b]\!] \geq [\![\varphi(a, a_1, \ldots, a_n)]\!]_{\alpha}$ by Theorem 13.4(3).

5. The remaining conditions about bounded quantifiers in $V_{\alpha+1}^{(B)}$ are satisfied by the construction.

By Theorem 9.26, since $\langle V_{\alpha}^{(B)} \mid \alpha \in On \rangle$ satisfies these conditions, $V^{(B)} = \bigcup_{\alpha \in On} V_{\alpha}^{(B)}$ is a $B$-valued model of $ZF$, i.e., $[\![\varphi]\!] = 1$ for every axiom $\varphi$ of $ZF$.
