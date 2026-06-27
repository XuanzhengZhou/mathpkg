---
role: proof
locale: en
of_concept: simple-homotopy-equivalence-characterization
source_book: gtm010
source_chapter: "5"
source_section: "5"
---

(a) $\Rightarrow$ (b): By the definition of a simple-homotopy equivalence, there is a formal deformation
$$K = K_0 \rightarrow K_1 \rightarrow \ldots \rightarrow K_q = L$$
such that $f$ is homotopic to any deformation associated with this formal deformation. Let $g = g_{q-1} \cdots g_1 g_0$ be such a deformation, where $g_i: K_i \rightarrow K_{i+1}$. For all $i$, $M_{g_i}$ collapses to $\operatorname{dom} g_i = K_i$. Thus
$$M_g \wedge M_{g_0} \cup \ldots \cup M_{g_{q-1}} \text{ rel } K_0$$ by (5.7), and this in turn collapses to $K_0 = K$.

(b) $\Rightarrow$ (c): Suppose that $g$ is a cellular approximation to $f$ such that $M_g \wedge K$ rel $K$ and that $g'$ is any cellular approximation to $f$. Then, by (5.5), $M_g' \wedge M_g \wedge K$ rel $K$.

(c) $\Rightarrow$ (a): Let $g$ be any cellular approximation to $f$. Then $M_g$ collapses to $K$ rel $K$. Reversing the steps in (a) $\Rightarrow$ (b) yields a formal deformation from $K$ to $L$ whose associated deformation is homotopic to $g$, hence to $f$.
