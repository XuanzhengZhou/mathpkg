---
role: proof
locale: en
of_concept: theorem-23-18-u-1-u-n-v-b-u-1-u-n-v-b
source_book: gtm008
source_chapter: "3"
source_section: "3 A consequence of"
---
(By induction on the number of logical symbols in $\varphi$.) We consider only the case of a quantifier.

Let $\varphi(u_1, \ldots, u_n) = (\forall x) \psi(x, u_1, \ldots, u_n)$ where $u_1, \ldots, u_n \in V^{(B)}$. Let $b = [\varphi(u_1, \ldots, u_n)]^{V^{(B)}}$ and let $v$ be any member of $V^{(B)}$. Claim:

$$b \leq [\psi(v, u_1, \ldots, u_n)]^{V^{(B)}}.$$

Suppose not: Then

$$p \cdot [\psi(v, u_1, \ldots, u_n)]^{V^{(B)}} = 0 \quad \text{for some } p, 0 < p \leq b.$$

By Collorary 23.17, there exists a $u \in V^{(B)}$ such that $p \cdot [u = v] > 0$. Then

$$0 = p \cdot [

Remark. Under the assumption of Theorem 23.20, every regular open class in $P$ can be represented by $\sum \{A \mid x \in a\}$ where $a$ is a set and each $A \mid x$ is a basic open class. These are of the form $[p]$ for some $p \in P$ and hence they are determined by sets $p \in P$. Therefore, if $\tilde{B}$ is the Boolean algebra of regular open classes in $P$, each element of $\tilde{B}$ can be represented by a set. Thus we may assume that $\tilde{B}$ is a class of sets and hence is of type $B$ as discussed in the beginning of this section.
