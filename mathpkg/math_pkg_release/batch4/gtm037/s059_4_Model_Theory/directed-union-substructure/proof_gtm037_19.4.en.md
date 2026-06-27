---
role: proof
locale: en
of_concept: directed-union-substructure
source_book: gtm037
source_chapter: "19"
source_section: "4. Model Theory"
---

**Proof.** This follows directly from the definition of $\bigcup K$. For any $\mathcal{A} \in K$, the universe of $\mathcal{A}$ is contained in the universe of $\bigcup K$, and for any operation symbol $O$ and $a_0, \ldots, a_{m-1} \in A$, we have

$$
O^{\bigcup K}(a_0, \ldots, a_{m-1}) = O^{\mathcal{A}}(a_0, \ldots, a_{m-1})
$$

since $\mathcal{A}$ itself is a member of $K$ containing all the arguments. Similarly, for any relation symbol $R$,

$$
R^{\mathcal{A}} \subseteq \bigcup_{\mathcal{B} \in K} R^{\mathcal{B}} = R^{\bigcup K}.
$$

Thus $\mathcal{A} \subseteq \bigcup K$. $\square$
