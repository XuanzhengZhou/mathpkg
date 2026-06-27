---
role: proof
locale: en
of_concept: extremal-set-extension
source_book: gtm054
source_chapter: "V"
source_section: "B"
---

If $U$ is extremal, let $W = V \setminus N(U)$. Clearly $U \subseteq W$, and every component of $\Gamma_U$ is a component of $\Gamma_W$. Hence $\|U\| \leq \|W\|$. Moreover, $N(U) = N(W)$ because any vertex outside $W$ is in $N(U)$ by definition of $W$, and any vertex in $N(U)$ is certainly in $N(W)$ since $U \subseteq W$, giving $N(W) \supseteq N(U)$; conversely $N(W) \subseteq N(U)$ follows from $W = V \setminus N(U)$. Thus $W \cup N(W) = (V \setminus N(U)) \cup N(U) = V$, and

$$\delta(W) = \|W\| - |N(W)| = \|W\| - |N(U)| \geq \|U\| - |N(U)| = \delta(U).$$

Since $U$ is extremal, $\delta(U) = \delta(\Gamma)$ is maximal, so $\delta(W) \geq \delta(U)$ forces $\delta(W) = \delta(\Gamma)$, making $W$ extremal as well.
