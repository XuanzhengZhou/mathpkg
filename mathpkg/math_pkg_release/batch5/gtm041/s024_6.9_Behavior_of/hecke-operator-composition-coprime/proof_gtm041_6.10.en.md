---
role: proof
locale: en
of_concept: hecke-operator-composition-coprime
source_book: gtm041
source_chapter: "6"
source_section: "6.10"
---

If $f \in M_k$ we have

$$(T_n f)(\tau) = \frac{1}{n} \sum_{\substack{a \geq 1,\; ad = n \\ 0 \leq b < d}} a^k f(A\tau),$$

where $A = \begin{pmatrix} a & b \\ 0 & d \end{pmatrix}$. Applying $T_m$ to each member we have

$$\{T_m(T_n(f))\}(\tau) = \frac{1}{m} \sum_{\substack{\alpha \geq 1,\; \alpha \delta = m \\ 0 \leq \beta < \delta}} \alpha^k \frac{1}{n} \sum_{\substack{a \geq 1,\; ad = n \\ 0 \leq b < d}} a^k f(BA\tau),$$

where $B = \begin{pmatrix} \alpha & \beta \\ 0 & \delta \end{pmatrix}$. The product $C = BA$ has the form

$$C = \begin{pmatrix} \alpha a & \alpha b + \beta d \\ 0 & \delta d \end{pmatrix}.$$

Since $(m,n)=1$, the linear combination $\alpha b + \beta d$ runs through a complete residue system mod $d\delta$ as $b$ and $\beta$ run through complete residue systems mod $d$ and $\delta$, respectively. Therefore the matrix $C$ runs through a complete set of non-equivalent elements of $\Gamma(mn)$ and we see that (27) implies (26).
