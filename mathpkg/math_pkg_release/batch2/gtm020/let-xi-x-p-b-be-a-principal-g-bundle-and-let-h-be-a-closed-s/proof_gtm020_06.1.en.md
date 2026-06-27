---
locale: en
of_concept: let-xi-x-p-b-be-a-principal-g-bundle-and-let-h-be-a-closed-s
role: proof
source_book: gtm020
source_chapter: 6. Change of Structure Group
source_section: '1'
---

Let $h: X \bmod H \rightarrow X_{G \bmod H}$ be defined by the relation $h(xH) = (x, eH)G$. For $v \in H$, we have $h(xH) = h(xvH) = (xv, eH)G = (xv, v^{-1}eH)G = (x, eH)G$, and $h$ is a well-defined function. Since $X \bmod H$ has the quotient topology, $h$ is continuous. For each $u \in G$, we have $(x, uH)G = (xu, eH)G$, and $h$ is surjective. For $h(xH) = h(x'H)$, we have $(

Finally, we prove that $h^{-1}$ is continuous. The functions $g_1: X \times G \rightarrow X$ and $g_2: X \times (G \bmod H) \rightarrow X \bmod H$ given by the relations $g_1(x, u) = xu$ and $g_2(x, uH) = xuH$ are continuous. Since $g_2(x, uH) = g_2(xv, v^{-1}uH)$, the map $g_2$ induces a map $(X \times (G \bmod H)) \bmod G \rightarrow X \bmod H$ which is $h^{-1}$. This proves the theorem.
