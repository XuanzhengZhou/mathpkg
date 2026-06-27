---
role: proof
locale: en
of_concept: v-b-is-btilde-valued-elementary-substructure
source_book: gtm008
source_chapter: "23"
source_section: "3"
---

(By induction on the number of logical symbols in $\varphi$.) We consider only the case of a quantifier.

Let $\varphi(u_1, \ldots, u_n) = (\forall x) \psi(x, u_1, \ldots, u_n)$ where $u_1, \ldots, u_n \in V^{(B)}$. Let $b = [\varphi(u_1, \ldots, u_n)]^{V^{(B)}}$ and let $v$ be any member of $V^{(\tilde{B})}$. Claim:

$$b \leq [\psi(v, u_1, \ldots, u_n)]^{V^{(\tilde{B})}}.$$

Suppose not: Then

$$p \cdot [\psi(v, u_1, \ldots, u_n)]^{V^{(\tilde{B})}} = 0 \quad \text{for some } p, 0 < p \leq b.$$

By Corollary 23.17, there exists a $u \in V^{(B)}$ such that $p \cdot [u = v] > 0$. Then

$$0 = p \cdot [\psi(v, u_1, \ldots, u_n)]^{V^{(\tilde{B})}} \geq p \cdot [u = v] \cdot [\psi(u, u_1, \ldots, u_n)]^{V^{(B)}},$$

contradicting the induction hypothesis. Therefore $b \leq [\psi(v, u_1, \ldots, u_n)]^{V^{(\tilde{B})}}$ for all $v \in V^{(\tilde{B})}$, so $b \leq [\varphi(u_1, \ldots, u_n)]^{V^{(\tilde{B})}}$. The reverse inequality is proved similarly.
