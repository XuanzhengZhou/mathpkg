---
role: proof
locale: en
of_concept: logarithmic-potential-cauchy-transform-summability
source_book: gtm035
source_chapter: "2"
source_section: "2.4"
---

# Proof of Summability Lemma

**Lemma 2.4.** Let $\mu$ be a measure of compact support contained in $\mathbb{C}$. Then the functions

$$\int \left| \log \left| \frac{1}{z - \zeta} \right| \right| d|\mu|(\zeta) \quad \text{and} \quad \int \left| \frac{1}{\zeta - z} \right| d|\mu|(\zeta)$$

are summable with respect to $dx\,dy$ over compact sets in $\mathbb{C}$. Consequently, these functions are finite almost everywhere with respect to $dx\,dy$, and the logarithmic potential $\mu^*$ and the Cauchy transform $\hat{\mu}$ are defined almost everywhere.

## Proof

Since $1/r \geq |\log r|$ for small $r > 0$, it suffices to consider the second integral.

Fix $R > 0$ with $\operatorname{supp} |\mu| \subset \{z : |z| < R\}$. Then

$$\begin{aligned}
\int_{|z| \leq R} \left\{ \int \left| \frac{1}{\zeta - z} \right| d|\mu|(\zeta) \right\} dx\,dy
&= \int d|\mu|(\zeta) \int_{|z| \leq R} \frac{dx\,dy}{|z - \zeta|}.
\end{aligned}$$

For $\zeta \in \operatorname{supp} |\mu|$ and $|z| \leq R$, we have $|z - \zeta| \leq 2R$. The inner integral can be estimated by converting to polar coordinates centered at $\zeta$:

$$\int_{|z| \leq R} \frac{dx\,dy}{|z - \zeta|} \leq \int_{|w| \leq 2R} \frac{dx\,dy}{|w|} = \int_0^{2R} \int_0^{2\pi} \frac{1}{r} \cdot r \, d\theta\,dr = 2\pi \cdot 2R = 4\pi R.$$

Thus

$$\int_{|z| \leq R} \left\{ \int \left| \frac{1}{\zeta - z} \right| d|\mu|(\zeta) \right\} dx\,dy \leq 4\pi R \, |\mu|(\mathbb{C}) < \infty.$$

Hence the function $z \mapsto \int |\zeta - z|^{-1} d|\mu|(\zeta)$ is summable over $|z| \leq R$, and by the remark about $1/r \geq |\log r|$, the logarithmic potential is also summable. The finiteness almost everywhere follows from the summability. $\square$
