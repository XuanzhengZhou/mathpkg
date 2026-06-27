---
role: proof
locale: en
of_concept: maximum-principle-markov-potential-theory
source_book: gtm040
source_chapter: "8"
source_section: "4"
---

For the first statement:
$$h_i = \sum_{j \in E} B^E_{ij} h_j \leq \sum_{j \in E} B^E_{ij} \left( \sup_{j \in E} h_j \right) \leq \sup_{j \in E} h_j.$$

For the second statement, suppose that $h$ assumes its maximum on $\tilde{E}$, that $^E P$ is absorbing, and that the states of $\tilde{E}$ communicate in $^E P$. Let $i$ be a state where the maximum is assumed, and let $k$ be any state of $E$ that can be reached in $^E P$ from $\tilde{E}$. Since the transient states of $^E P$ communicate, we have $B^E_{ik} > 0$. Moreover,

$$h_i = B^E_{ik} h_k + \sum_{j \neq k} B^E_{ij} h_j$$
$$\leq B^E_{ik} h_k + h_i \sum_{j \neq k} B^E_{ij} \quad \text{since } h_j \leq h_i$$
$$= B^E_{ik} h_k + h_i (1 - B^E_{ik}) \quad \text{since } B^E\mathbf{1} = \mathbf{1}$$
$$= h_i - B^E_{ik} (h_i - h_k).$$

Therefore, $h_i = h_k$ for all such $k$. Then for any $m \in \tilde{E}$, $B^E_{mj} > 0$ precisely for those $j$ that can be reached from $\tilde{E}$ in $^E P$, so $h_m = h_i = h_k$.
