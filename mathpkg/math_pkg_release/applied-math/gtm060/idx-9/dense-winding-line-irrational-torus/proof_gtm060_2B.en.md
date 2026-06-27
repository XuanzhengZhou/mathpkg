---
role: proof
locale: en
of_concept: dense-winding-line-irrational-torus
source_book: gtm060
source_chapter: "2"
source_section: "B"
---

Clearly, $\text{div } \mathbf{f} = \frac{\partial \alpha_1}{\partial \varphi_1} + \frac{\partial \alpha_2}{\partial \varphi_2} = 0$. By Liouville's theorem, the flow $g^t$ preserves the volume $d\varphi_1 \, d\varphi_2$. By Poincaré's recurrence theorem, for any neighborhood $U$ on the torus, there exists a point whose orbit returns to $U$.

The orbit of any point under $g^t$ is $\{(\varphi_1 + \alpha_1 t, \varphi_2 + \alpha_2 t) \bmod 2\pi\}$. The set of return times forms a subgroup of $\mathbb{R}$. Since $\alpha_1/\alpha_2$ is irrational, this subgroup is not discrete (otherwise the trajectory would be periodic). A non-discrete subgroup of $\mathbb{R}$ is dense. Therefore, the orbit is dense in the torus.
