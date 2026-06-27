---
role: proof
locale: en
of_concept: existence-of-nonstandard-arithmetic
source_book: gtm053
source_chapter: "2"
source_section: "2.13"
---

Let $L_1\mathrm{Ar} = \{+, \cdot, 0, 1\}$ be the language of arithmetic and let $L_1\mathrm{Ar}(c)$ be its expansion by a new constant symbol $c$. Define
$$\mathcal{E} = \operatorname{Th}(\mathbf{N}) \cup \{ \neg c = \bar{n} : n = 0, 1, 2, \ldots \},$$
where $\bar{n}$ denotes the numeral $\underbrace{1 + \cdots + 1}_{n \text{ times}}$ (with $\bar{0} = 0$).

We first show $\mathcal{E}$ is finitely satisfiable. Let $\mathcal{E}_0 \subseteq \mathcal{E}$ be finite. Then $\mathcal{E}_0$ contains only finitely many sentences of the form $\neg c = \bar{n}$, say for $n \in \{n_1, \ldots, n_k\}$. Choose a standard integer $m \in \mathbb{N}$ larger than all $n_j$. Interpret the constant $c$ as $m$ in the standard model $\mathbf{N}$. Then $(\mathbf{N}, m)$ satisfies every sentence in $\operatorname{Th}(\mathbf{N})$ (since $\mathbf{N}$ does) and also satisfies $\neg c = \bar{n}_j$ for each $j$ (since $m \neq n_j$). Hence $(\mathbf{N}, m) \vDash \mathcal{E}_0$.

Since every finite subset of $\mathcal{E}$ is satisfiable, the compactness theorem implies that $\mathcal{E}$ itself has a model $\mathbf{M} = (\mathbf{A}, c^{\mathbf{M}})$. Let $\mathbf{A}^*$ be the reduct of $\mathbf{M}$ to the language $L_1\mathrm{Ar}$.

Then $\mathbf{A}^* \vDash \operatorname{Th}(\mathbf{N})$, so $\mathbf{A}^* \equiv \mathbf{N}$. But the element $c^{\mathbf{M}} \in A^*$ satisfies $c^{\mathbf{M}} \neq \bar{n}^{\mathbf{A}^*}$ for every $n \in \mathbb{N}$, so the map $n \mapsto \bar{n}^{\mathbf{A}^*}$ is not surjective. Hence $\mathbf{A}^*$ is not isomorphic to $\mathbf{N}$, and is therefore a nonstandard arithmetic.
