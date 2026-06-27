---
role: proof
locale: en
of_concept: torsion-composition-formula
source_book: gtm010
source_chapter: "22"
source_section: "22"
---

Using the mapping cylinder construction and (20.3) (excision property of torsion):
tau(gf) = (gf)_* tau(M_{gf}, K)
= g_* f_* [tau(M_f, K) + i_*^{-1} tau(M_g \cup_{f} M_f, M_f)] where i: K -> M_f
= g_* tau(f) + g_* tau(M_g, L) (since f = p i and 1_L = p j imply f_* i_*^{-1} j_* = 1)
= g_* tau(f) + tau(g).
