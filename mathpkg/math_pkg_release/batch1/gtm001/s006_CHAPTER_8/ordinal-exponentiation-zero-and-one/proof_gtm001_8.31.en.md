---
role: proof
locale: en
of_concept: ordinal-exponentiation-zero-and-one
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (1) From Definition 8.30, $0^0 = 1$.

(2) If $\beta \geq 1$, then $\beta \in K_{\mathrm{II}}$ or $(\exists \delta)[\beta = \delta + 1]$. If $\beta \in K_{\mathrm{II}}$, then by Definition 8.30, $0^\beta = 0$. If $\beta = \delta + 1$, then $0^\beta = 0^{\delta+1} = 0^\delta \cdot 0 = 0$.

(3) (By transfinite induction). For $\beta = 0$: $1^0 = 1$. If $1^\beta = 1$, then $1^{\beta+1} = 1^\beta \cdot 1 = 1^\beta = 1$. If $\beta \in K_{\mathrm{II}}$ and $1^\gamma = 1$ for $\gamma < \beta$, then $1^\beta = \bigcup_{\gamma < \beta} 1^\gamma = 1$.
