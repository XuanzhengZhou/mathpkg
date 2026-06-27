---
role: proof
locale: en
of_concept: k-set-non-recursiveness
source_book: gtm037
source_chapter: "6"
source_section: "6.3"
---

Obviously $K \in \Sigma_1$, so $K$ is recursively enumerable. Suppose $K$ is recursive. Then so is $\omega \setminus K$, so by 6.2(v) there is an $e \in \omega$ such that $\omega \setminus K = \operatorname{Dmn} \varphi_e^1$. Then

$$e \in K \quad \text{iff} \quad e \in \operatorname{Dmn} \varphi_e^1 \quad \text{by the definition of } K,$$
$$e \notin K \quad \text{iff} \quad e \in \operatorname{Dmn} \varphi_e^1 \quad \text{by the choice of } e,$$

contradiction.
