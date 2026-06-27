---
role: proof
locale: en
of_concept: inversion-uniform-isomorphism
source_book: gtm015
source_chapter: "5"
source_section: "Uniformity in topological groups"
---

# Proof of Inversion induces isomorphism of left and right uniformities

Let $G$ be a topological group and let $J: G \rightarrow G$ be the inversion mapping, $Jx = x^{-1}$. Denote by $\mathcal{U}_s$ and $\mathcal{U}_r$ the left and right uniformities of $G$, respectively.

We claim that the mapping $(x, y) \mapsto (Jx, Jy)$ on $G \times G$ transforms $\mathcal{U}_s$ into $\mathcal{U}_r$.

For any entourage $V_s \in \mathcal{U}_s$, defined by $V_s = \{(x, y) : x^{-1}y \in V\}$ with $V$ a neighborhood of $e$, we have

$$(Jx, Jy) = (x^{-1}, y^{-1}).$$

Now $(x^{-1}, y^{-1}) \in V_r$ means $x^{-1}(y^{-1})^{-1} = x^{-1}y \in V$, which is exactly the condition $(x, y) \in V_s$. Thus

$$(J \times J)(V_s) = V_r.$$

Conversely, $(J \times J)(V_r) = V_s$. Since $J \times J$ is a self-inverse bijection of $G \times G$, it follows that $(J \times J)(\mathcal{U}_s) = \mathcal{U}_r$ and $(J \times J)(\mathcal{U}_r) = \mathcal{U}_s$.

Thus $J \times J$ is a bijective mapping on $G \times G$ that transforms $\mathcal{U}_s$ into $\mathcal{U}_r$. Equivalently, $J$ is a uniformly continuous mapping of $(G, \mathcal{U}_s)$ onto $(G, \mathcal{U}_r)$, with uniformly continuous inverse. Hence $J$ induces an isomorphism between the two uniform structures.
