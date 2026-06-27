---
role: proof
locale: en
of_concept: carlitz-hadamard-determinant-bound
source_book: gtm059
source_chapter: "3"
source_section: "7"
---

Let $D_p = \det(a_{ij})$ be the Maillet determinant where $a_{ij} = R_{ij}^+ - R_{ij}^-$ for $i,j = 1,\dots,\frac{p-1}{2}$. As noted in the proof of Theorem 7.1, each entry satisfies $|a_{ij}| \leq p$.

Hadamard's inequality states that for any $n \times n$ matrix $A = (a_{ij})$,

$$|\det A| \leq \prod_{i=1}^{n} \left( \sum_{j=1}^{n} |a_{ij}|^2 \right)^{1/2}.$$

Apply this with $n = \frac{p-1}{2}$. For each row $i$, the squared Euclidean length is

$$\sum_{j=1}^{(p-1)/2} |a_{ij}|^2 \leq \frac{p-1}{2} \cdot p^2.$$

Therefore

$$|D_p| \leq \prod_{i=1}^{(p-1)/2} \left( \frac{p-1}{2} \cdot p^2 \right)^{1/2} = \left( p \cdot \sqrt{\frac{p-1}{2}} \right)^{(p-1)/2}.$$

Rewriting,

$$|D_p| \leq p^{(p-1)/2} \cdot \left( \frac{p-1}{2} \right)^{(p-1)/4}.$$

Since $D_p = \pm p^{(p-3)/2} \cdot h^-$ (up to a power of $2$) by Theorem 7.1, we obtain

$$h^- \leq \frac{|D_p|}{p^{(p-3)/2}} \leq p \cdot \left( \frac{p-1}{2} \right)^{(p-1)/4},$$

which is the Carlitz bound. The factor $p^{(p-1)/2} / p^{(p-3)/2} = p$ accounts for the scaling between the determinant and the class number.

Carlitz pointed out that Hadamard's inequality thus directly bounds the class number. Montgomery and Mozgovoy [M-M] later proved the sharper two-sided estimate stated in the theorem, confirming that the Hadamard exponent is essentially optimal.
