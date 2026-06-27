---
role: proof
locale: en
of_concept: equational-deduction-properties
source_book: gtm037
source_chapter: "24"
source_section: "Preservation and Characterization Theorems"
---

(i) is obvious from 24.17(ii) and 24.17(iii). For (ii): assume $\Gamma \vdash_{\text{eq}} \sigma = \tau$. We also have $\Gamma \vdash_{\text{eq}} \tau = \tau$ by (i), so $\Gamma \vdash_{\text{eq}} \tau = \sigma$ by 24.17(iv). (iii) clearly follows from (ii) and 24.17(iv). To prove (iv), let $\alpha_0, \ldots, \alpha_{m-1}$ be distinct variables not occurring in any of the terms. Then by repeated use of 24.17(iii) and the definition of equational deduction, the congruence property follows.
