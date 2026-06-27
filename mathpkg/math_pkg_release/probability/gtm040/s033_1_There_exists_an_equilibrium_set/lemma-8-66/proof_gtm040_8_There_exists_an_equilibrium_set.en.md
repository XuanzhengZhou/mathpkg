---
role: proof
locale: en
of_concept: lemma-8-66
source_book: gtm040
source_chapter: "8"
source_section: "There exists an equilibrium set"
---

Note that ${}_m({}_{m+1} z) = {}_m z$. Applying Lemma 8-65 to ${}_{m+1} z$, we find that
$${}_{m+1} z - {}_{m+1} z^{(1)} \geq {}_m z - {}_m z^{(1)}.$$
Taking expectations $M_i[\cdot]$ preserves the inequality, so ${}_{m+1} f_i \geq {}_m f_i$. Since $\lim_m ({}_m z - {}_m z^{(1)}) = z - z^{(1)}$ almost everywhere, the dominated convergence theorem (or monotone convergence, since the differences are nonnegative by Lemma 8-65) gives $\lim_m {}_m f = f$.
