---
role: proof
locale: en
of_concept: homomorphism-preserves-trace-reject
source_book: gtm013
source_chapter: "1"
source_section: "8"
---

For the trace: for each $h \in \mathrm{Hom}_R(U, M)$ with $U \in \mathcal{U}$, we have $f \circ h \in \mathrm{Hom}_R(U, N)$ and $f(\mathrm{Im}\, h) = \mathrm{Im}(f \circ h)$. Summing over all such $h$ yields $f(\mathrm{Tr}_M(\mathcal{U})) \leq \mathrm{Tr}_N(\mathcal{U})$.

For the reject: if $x \in \mathrm{Rej}_M(\mathcal{U})$ and $h \in \mathrm{Hom}_R(N, U)$ with $U \in \mathcal{U}$, then $h \circ f \in \mathrm{Hom}_R(M, U)$, so $h(f(x)) = (h \circ f)(x) = 0$. Thus $f(x) \in \mathrm{Ker}\, h$ for all such $h$, yielding $f(x) \in \mathrm{Rej}_N(\mathcal{U})$. This proves $f(\mathrm{Rej}_M(\mathcal{U})) \leq \mathrm{Rej}_N(\mathcal{U})$.
