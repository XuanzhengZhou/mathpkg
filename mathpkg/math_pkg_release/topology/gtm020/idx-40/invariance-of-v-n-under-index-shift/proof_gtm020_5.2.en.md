---
role: proof
locale: en
of_concept: invariance-of-v-n-under-index-shift
source_book: gtm020
source_chapter: "5"
source_section: "5.2"
---

Using (4.8), we have the following relations in $K(X)$:

$$L^{2n+2}(\zeta, p_{n+1})_+ = L^{2n+2}(\zeta, zp_{n+1})_+ = L^{2n+1}(\zeta, zp_n)_+ = L^{2n}(\zeta, p_n)_+ \oplus \zeta.$$

From this we compute:

\begin{align*}
v_{n+1}(\zeta, u) &= L^{2n+2}(\zeta, p_{n+1})_+ \otimes (\eta^n - \eta^{n+1}) + \zeta \otimes \eta^{n+1} \\
&= L^{2n}(\zeta, p_n)_+ \otimes (1 - \eta) + \zeta \otimes (\eta^n - \eta^{n+1}) + \zeta \otimes \eta^{n+1} \\
&= L^{2n}(\zeta, p_n)_+ \otimes (\eta^{n-1} - \eta^n) + \zeta \otimes \eta^n \\
&= v_n(\zeta, u).
\end{align*}

This proves the proposition.
