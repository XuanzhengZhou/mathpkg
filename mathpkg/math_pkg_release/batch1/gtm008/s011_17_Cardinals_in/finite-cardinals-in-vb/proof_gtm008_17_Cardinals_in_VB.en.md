---
role: proof
locale: en
of_concept: finite-cardinals-in-vb
source_book: gtm008
source_chapter: "17"
source_section: "Cardinals in V^{(B)}"
---

We have to show that

$$[\neg (\exists f)(\exists \beta < \check{\alpha})[f: \beta \rightarrow \check{\alpha} \land \mathcal{W}(f) = \check{\alpha}]] = 1$$

i.e.,

$$(\forall f \in V^{(B)}) (\forall \beta < \alpha) [\llbracket f: \check{\beta} \rightarrow \check{\alpha} \rrbracket \land \llbracket \mathcal{W}(f) = \check{\alpha} \rrbracket = 0].$$

Now let us assume that $\alpha \leq \omega$. Since $\beta < \alpha$,

$$b = \llbracket f: \check{\beta} \rightarrow \check{\alpha} \rrbracket \land \llbracket \mathcal{W}(f) = \check{\alpha} \rrbracket \leq \prod_{\eta < \beta + 1} \sum_{\xi < \beta} \llbracket f(\check{\xi}) = \check{\eta} \rrbracket$$

$$= \sum_{\varphi \in {}^{\beta}(\beta + 1)} \prod_{\eta < \beta + 1} \llbracket f(\varphi(\eta)) = \check{\eta} \rrbracket$$

by the $(\beta + 1, \beta)$-DL (see Definition 4.1) which holds for every $B$ since $\beta$ is finite.

Therefore

$$0 < b \cdot \prod_{\eta < \beta + 1} \llbracket f(\varphi(\eta)) = \check{\eta} \rrbracket \text{ for some } \varphi: \beta + 1 \rightarrow \beta.$$

There must exist $n, m < \beta + 1$ such that $n \neq m \land \varphi(n) = \varphi(m)$. Then

$$0 < b \cdot \llbracket f(\varphi(n)) = \check{n} \rrbracket \cdot \llbracket f(\varphi(m)) = \check{m} \rrbracket$$

$$\leq b \cdot \llbracket \check{n} = \check{m} \rrbracket \quad \text{since } b \leq \llbracket f(\varphi(n)) = f(\varphi(m)) \rrbracket$$

$$= 0 \quad \text{since } n \neq m.$$

This is a contradiction.
