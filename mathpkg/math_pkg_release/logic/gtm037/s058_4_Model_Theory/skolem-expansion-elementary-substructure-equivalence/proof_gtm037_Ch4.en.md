---
role: proof
locale: en
of_concept: skolem-expansion-elementary-substructure-equivalence
source_book: gtm037
source_chapter: "4"
source_section: "Model Theory"
---

The implication $(ii) \Rightarrow (i)$ is trivial. Now assume $(i)$. We shall apply Theorem 19.16 (the Tarski–Vaught criterion) in order to prove $(ii)$. To this end, assume that $x \in {}^\omega A$ and $B \models \exists v_i \varphi[x]$. Then, since $B$ is a model of the Skolem set of $L'$ over $L$, we have

$$B \models \varphi(v_0, \ldots, v_{i-1}, \sigma)[x],$$

where $\sigma$ is the term

$$S_j^j_{\exists v_i \varphi} \alpha_0 \cdots \alpha_{m-1},$$

with $m = |\mathrm{Fv} \exists v_i \varphi|$, and $\alpha_0, \ldots, \alpha_{m-1}$ are the free variables of $\exists v_i \varphi$ taken in order. Since $A \subseteq B$, the interpretation of $\sigma$ in $B$ at $x$ coincides with its interpretation in $A$ at $x$, and thus $A \models \varphi(v_0, \ldots, v_{i-1}, \sigma)[x]$. Hence the condition of Theorem 19.16 is satisfied, yielding $A \preceq B$.
