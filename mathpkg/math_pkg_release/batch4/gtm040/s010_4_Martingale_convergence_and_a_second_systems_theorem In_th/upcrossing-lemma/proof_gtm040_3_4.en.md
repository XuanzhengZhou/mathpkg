---
role: proof
locale: en
of_concept: upcrossing-lemma
source_book: gtm040
source_chapter: "3"
source_section: "4"
---

Consider first the special case $f_k \geq 0$ and $r = 0$. Let $s > 0$. Define $f_k$ for $k = 0, \ldots, n$. An upcrossing of $[0, s]$ occurs between times $n - k$ and $n$ if $f_{n-k}(\omega) = 0$, $0 < f_{n-k+m}(\omega) < s$ for $0 < m < k$, and $f_n(\omega) \geq s$.

Let $\beta(\omega)$ be the number of such upcrossings. Consider the total increase contributed by these upcrossings. For each upcrossing, the process starts at or below $0$ and ends at or above $s$, contributing at least $s$ to the final value. Moreover, the submartingale property and non-negativity ensure that intermediate excursions do not reduce this contribution. Summing over all upcrossings yields

$$s \cdot \beta(\omega) \leq f_n(\omega)$$

for each $\omega$. Taking expectations,

$$s \cdot M[\beta] \leq M[f_n]$$

so that

$$M[\beta] \leq \frac{M[f_n]}{s}.$$

Thus the special case is proved.

For a general sequence $\{f_n\}$ and general $r$, consider the function $(f_k - r)^+$, which is the supremum of the zero function and the function $f_k - r$. It is readily verified that constant functions are martingales and that the difference of a submartingale and a martingale is a submartingale. Thus $(f_k - r, \mathcal{R}_k)$ is a submartingale and by Lemma 3-9 $((f_k - r)^+, \mathcal{R}_k)$ is a submartingale. Applying the special case proved above to $(f_k - r)^+$ and upcrossings of $[0, s - r]$, we find

$$(s - r) \cdot M[\beta] \leq M[(f_n - r)^+] \leq M[|f_n - r|] \leq M[|f_n| + |r|] = M[|f_n|] + |r|.$$

This completes the proof of the Upcrossing Lemma.
