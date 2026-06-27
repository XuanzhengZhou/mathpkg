---
role: proof
locale: en
of_concept: product-theorem-for-torsion
source_book: gtm010
source_chapter: "23"
source_section: "23"
---

For (a), the proof uses the sum theorem and induction on cell structure. If the result holds for Q simple-homotopy equivalent to P, it holds for P. Build P cell by cell; for a top n-cell attached via phi: partial I^n -> P^{n-1}, express P = M_phi \cup I^n. The sum theorem decomposes tau(K x P, K_0 x P) into contributions from K x M_phi and K x I^n. For the mapping cylinder piece, use the fact that M_phi -> point so chi(M_phi) = chi(point) = 1; for the ball piece, chi(I^n) = (-1)^n and tau(K x I^n, K_0 x I^n) = (-1)^n tau(K, K_0). Summing over all cells gives chi(P) tau(K, K_0).
