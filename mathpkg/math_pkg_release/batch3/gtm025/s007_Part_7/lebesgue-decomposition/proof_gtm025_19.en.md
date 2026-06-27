---
role: proof
locale: en
of_concept: lebesgue-decomposition
source_book: gtm025
source_chapter: ""
source_section: "19"
---

Apply 19.24 to $\nu \ll \mu+\nu$ to obtain $f_0$ with $\int f d\nu = \int f f_0 d(\mu+\nu)$. Show $0 \leq f_0 \leq 1$. Let $B = \{x: f_0(x) = 1\}$, $\nu_1(A) = \nu(A \cap B')$, $\nu_2(A) = \nu(A \cap B)$. Then $\nu_2 \perp \mu$ since $\mu(B) = 0$ (set $f = \xi_B$). And $\nu_1 \ll \mu$ because on sets where $\mu = 0$, the integral identity forces $\nu_1 = 0$.
