---
role: proof
locale: en
of_concept: mathcal-emptyset-exists-a7
source_book: gtm054
source_chapter: "6"
source_section: "Section 21"
---

Let $m = \min\{\rho(x): x \in V_1\}$, and let $U \subseteq V_1$. Since any edge incident with a vertex in $U$ is also incident with a vertex in $N(U)$, one has

$$m|U| \leq \sum_{x_1 \in U} \rho(x_1) \leq \sum_{x_2 \in N(U)} \rho(x_2) \leq m|N(U)|,$$

the last inequality in A8 holding since $\rho(x_2) \leq m$ for all $x_2 \in V_2$. Since $\mathcal{E} \neq \emptyset$, $\rho(x_2) > 0$ for some $x_2 \in V_2$. Hence $m >
