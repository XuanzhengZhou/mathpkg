---
role: proof
locale: en
of_concept: factor-algebra-prime-power-decomposition
source_book: gtm023
source_chapter: "12"
source_section: "4. The structure of factor algebras"
---

The relation (12.19) is an immediate consequence of Proposition I, and formulae (12.16) and (12.17). To show that $\bar{e}_i$ is an identity in $I_i$, note that $\bar{e}_i \in I_i$ and for any $\bar{q} \in I_i$, since $I_i \cdot I_j = 0$ for $i \neq j$, we have $\bar{e}_i \bar{q} = \bar{e}_i \bar{q} = \bar{q}$ (as $\sum_j \bar{e}_j = \bar{1}$ and $\bar{e}_j \bar{q} = 0$ for $j \neq i$).

Now let $\bar{q}$ be an arbitrary element of $\Gamma(\bar{t})$ and let $q = \sum_k \alpha_k t^k$ be any representative. Writing

$$\bar{q} = \alpha_0(\bar{e}_1 + \cdots + \bar{e}_r) + \sum_{k=1}^{m} \alpha_k (\bar{t}_1 + \cdots + \bar{t}_r)^k.$$

But $\bar{t}_i \bar{t}_j \in I_i \cap I_j = 0$ for $i \neq j$, so

$$(\bar{t}_1 + \cdots + \bar{t}_r)^k = \bar{t}_1^k + \cdots + \bar{t}_r^k.$$

It follows that

$$\bar{q} = \sum_{k=0}^{r} \alpha_k (\bar{t}_1^k + \cdots + \bar{t}_r^k) = \sum_{i=1}^{r} q(\bar{t}_i) \quad (\bar{t}_i^0 = \bar{e}_i).$$

Finally, let $I$ be any ideal in $\Gamma(\bar{t})$. Then clearly $I \cap I_i = \bar{e}_i I$, and so the decomposition $I = \sum_{i=1}^{r} I \cap I_i$ is an immediate consequence of (12.20).
