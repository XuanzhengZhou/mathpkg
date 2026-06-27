---
role: proof
locale: en
of_concept: standard-transitive-model-implies-lk-subset
source_book: gtm008
source_chapter: "7"
source_section: "Relative Constructibility"
---
We prove by induction that $A_\alpha \in M$. Clearly $A_0 = 0 \in M$. If $A_\alpha \in M$ then $\bar{K}_\alpha = A_\alpha \cap K \in M$, hence $A_\alpha = \langle A_\alpha, \bar{K}_\alpha \rangle \in M$. By Theorem 7.10, $Df(A_\alpha)$ is absolute with respect to $M$. Therefore $A_{\alpha+1} \subseteq M$. But $A$ a set implies that $Df(A)$ is a set. Therefore $Df(A_\alpha) \in M$, i.e.,

$$A_{\alpha+1} = Df(A_\alpha) \in M.$$

For limit $\lambda$, $A_\lambda = \bigcup_{\alpha < \lambda} A_\alpha \in M$ by the induction hypothesis and the fact that $M$ is a model of ZF. Thus by transfinite induction, $A_\alpha \in M$ for all $\alpha$, and consequently $L_K = \bigcup_{\alpha \in On} A_\alpha \subseteq M$.
