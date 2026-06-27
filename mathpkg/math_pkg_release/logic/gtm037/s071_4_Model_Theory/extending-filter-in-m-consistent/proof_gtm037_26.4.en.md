---
role: proof
locale: en
of_concept: extending-filter-in-m-consistent
source_book: gtm037
source_chapter: "26"
source_section: "4"
---

The proof proceeds by transfinite recursion on $\alpha < m$. Define sequences $\langle H_\alpha : \alpha < m \rangle$ (subsets of $F$) and $\langle E_\alpha : \alpha < m \rangle$ (filters over $n$) inductively. At stage $\alpha$, suppose $H_\beta$ and $E_\beta$ have been defined for all $\beta < \alpha$ with $H_\beta \subseteq F$, $E_\beta \supseteq D$, and $(F \setminus \bigcup_{\beta<\alpha} H_\beta, G, E_\alpha)$ is $m$-consistent over $n$.

Consider $\Gamma_\alpha$. Either adding $\Gamma_\alpha$ to the current filter preserves $m$-consistency, or adding $n \setminus \Gamma_\alpha$ does. Choose whichever works; if neither works, then condition (iv) of Definition 26.33 would be violated. The hypothesis $n^{\partial} \leq m$ ensures that the cardinality constraints remain satisfied throughout the induction. After $m$ steps, set $F' = F \setminus \bigcup_{\alpha < m} H_\alpha$ and $D' = E_m$. By construction, $|F \setminus F'| \leq m$ and each $\Gamma_\alpha$ is decided by $D'$.
