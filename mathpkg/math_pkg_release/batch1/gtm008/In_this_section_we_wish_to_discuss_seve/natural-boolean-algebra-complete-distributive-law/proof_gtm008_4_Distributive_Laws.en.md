---
role: proof
locale: en
of_concept: natural-boolean-algebra-complete-distributive-law
source_book: gtm008
source_chapter: "4"
source_section: "Distributive Laws"
---

If $b_{ij} \subseteq A$ for $i \in I$ and $j \in J$ then
$$b \in \bigcap_{i \in I} \bigcup_{j \in J} b_{ij} \leftrightarrow (\forall i \in I)(\exists j \in J)[b \in b_{ij}]$$
$$\leftrightarrow (\exists f \in J^I)(\forall i \in I)[b \in b_{i,f(i)}]$$
$$\leftrightarrow b \in \bigcup_{f \in J^I} \bigcap_{i \in I} b_{i,f(i)}.$$
Thus $\bigcap_{i \in I} \bigcup_{j \in J} b_{ij} = \bigcup_{f \in J^I} \bigcap_{i \in I} b_{i,f(i)}$, which is precisely the $(\alpha,\beta)$-distributive law for all $\alpha$ and $\beta$. Hence $\mathcal{P}(A)$ satisfies the complete distributive law.
