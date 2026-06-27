---
role: proof
locale: en
of_concept: theorem-13-9
source_book: gtm008
source_chapter: "12"
source_section: "12 The Independence of the AC

In order to prove the independen"
---
Let $u, v \in V_{\alpha}^{(B)}$. Then

$$[\![(\forall x)[x \in u \leftrightarrow x \in v]\!]_{\alpha} = \prod_{x \in V_{\alpha}^{(B)

Proof. Let $a_1, \ldots, a_n \in V_{\alpha}^{(B)}$ and define $b: V_{\alpha}^{(B)} \rightarrow B$ by
$$b(a) = \llbracket \varphi(a, a_1, \ldots, a_n) \rrbracket_{\alpha} \quad \text{for} \quad a \in V_{\alpha}^{(B)}.$$
Then $b \in V_{\alpha+1}^{(B)}$ and
$$\llbracket a \in b \rrbracket = \sum_{a' \in V_{\alpha}^{(B)}} \llbracket \varphi(a', a_1, \ldots, a_n) \rrbracket_{\alpha} \cdot \llbracket a' = a \rrbracket$$
$$\leq \llbracket \varphi(a, a_1, \ldots, a_n) \rrbracket_{\alpha} \quad \text{by the Axioms of Equality}.$$
On the other hand, for $a \in V_{\alpha}^{(B)}$
$$\llbracket a \in b \rrbracket \geq \llbracket \varphi(a, a_1, \ldots, a_n) \rrbracket_{\alpha}$$
by Theorem 13.4(3).

Remark. Since the conditions of §9 are satisfied by $\langle V_{\alpha}^{(B)} | \alpha \in On \rangle$, we have, by Theorem 9.26, the following result:
