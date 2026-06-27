---
role: proof
locale: en
of_concept: theorem-13-5-1
source_book: gtm008
source_chapter: "12"
source_section: "12 The Independence of the AC

In order to prove the independen"
---
(By induction on $\alpha$).

1. If rank $(u) < \alpha$, rank $(u') < \alpha$, and rank $(v) \leq \alpha$, then
$$[\![u = u']\!] \cdot [[u \in v]] = \sum_{y \in \mathcal{D}(v)} v(y) \cdot [[y = u]] \cdot [[u = u']]$$
$$\leq \sum_{y \in \mathcal{D}(v)} v(y) \cdot [[y = u']] \quad \text{by the induction hypothesis for 3}$$
$$= [[u' \in v]].$$

2. If rank $(u) < \alpha$, rank $(v) \leq \alpha$, and rank $(v') \leq \alpha$, then for $y \in \mathcal{D}(v)$
$$[\![u = y]\!] \cdot v(y) \cdot [[v = v']] \leq [[u = y]] \cdot v(y)(v(y) \Rightarrow [[y \in v']])$$
$$\leq [[u = y]] [[y \in v']]$$
$$\

Remark. Therefore $V^{(B)} = \langle V^{(B)}, \bar{=}, \bar{\in} \rangle$ is a B-valued structure for the language $\mathcal{L}_0$. Even more, $V^{(B)}$ is a B-valued model of $ZF$ i.e. $V^{(B)}$ satisfies each axiom of $ZF$. Here a formula $\varphi$ of the language $\mathcal{L}_0$ is satisfied by $V^{(B)}$ iff $[\varphi] = 1$ interpreting $\in$ (of $\mathcal{L}_0$) by $\bar{\in}$. We shall not give a direct proof of this statement but use the results of §9.
