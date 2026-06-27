---
role: proof
locale: en
of_concept: iwasawa-invariants-equality
source_book: gtm059
source_chapter: "16"
source_section: "The Galois Group as Module over the Iwasawa Algebra"
---

From the structure theorem for finitely generated modules over the Iwasawa algebra $\Lambda = \mathbb{Z}_p[[T]]$, we know that the Galois group decomposes as
$$G = A^r \times G_{\text{tor}}$$
where $A$ is the Iwasawa algebra, $r$ is the $\Lambda$-rank, and $G_{\text{tor}}$ is the $\Lambda$-torsion submodule.

On the other hand, considering the rank function on the base field $K_\infty$, one has the relation
$$r_A(K_\infty) = r_B^{\,p}$$
relating the $\Lambda$-rank and the $\mathbb{Z}_p$-ranks of the extensions involved.

By Theorem 5.2, the Galois group of the maximal abelian unramified $p$-extension satisfies
$$\text{Gal}(G_A/K_\infty) \cong \mathbb{Z}_p^{\,p+1}$$
as a $\mathbb{Z}_p$-module, where $G_A$ denotes the maximal abelian $p$-extension of $K_\infty$.

From the structure theorem, one sees easily that this compatibility of ranks is possible only if $t = r_B$, where $t$ is the number of $\Lambda$-torsion components in the decomposition of $G$. This completes the proof.

The above theorem gives a sample of Iwasawa's results [W 12]. It is possible to vary some of the hypotheses to obtain variants. For instance, one need not assume the full Leopoldt conjecture in Theorem 5.2; it suffices to assume that the defect in that conjecture is bounded as a function of $m$. For the problem of $K_\infty$-extensions, this can be proved easily; see for instance Greenberg [Gr 4].
