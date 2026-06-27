---
role: proof
locale: en
of_concept: c-matrix-z-representation
source_book: gtm040
source_chapter: "9"
source_section: "5. Strong ergodic chains"
---

The second assertion follows from the first, since $C = M D^{-1}$. For the first we have

$$Z_{ij} - \alpha_j = \lim_n \sum_{m=0}^{n} (P^m - A)_{ij}$$
$$= \lim_n \left[N_{ij}^{(n)} - (n + 1)\alpha_j\right]$$

and similarly

$$Z_{jj} - \alpha_j = \lim_n \left[N_{jj}^{(n)} - (n + 1)\alpha_j\right].$$

Hence

$$Z_{jj} - Z_{ij} = \lim_n \left[N_{jj}^{(n)} - N_{ij}^{(n)}\right] = C_{ij}.$$

Thus $C_{ij} = (Z_{\mathrm{dg}})_{jj} - Z_{ij}$, which in matrix form is $C = E Z_{\mathrm{dg}} - Z$.
