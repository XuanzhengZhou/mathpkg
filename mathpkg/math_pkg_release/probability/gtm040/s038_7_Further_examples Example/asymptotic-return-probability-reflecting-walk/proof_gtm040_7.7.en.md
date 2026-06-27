---
role: proof
locale: en
of_concept: asymptotic-return-probability-reflecting-walk
source_book: gtm040
source_chapter: "7"
source_section: "7. Further examples"
---

Apply Stirling's formula $n! \sim \sqrt{2\pi n} \, (n/e)^n$ to the binomial coefficient:

$$\binom{2n-2}{n-1} = \frac{(2n-2)!}{(n-1)!(n-1)!} \sim \frac{\sqrt{2\pi(2n-2)} (2n-2)^{2n-2} e^{-(2n-2)}}{2\pi(n-1) (n-1)^{2n-2} e^{-2(n-1)}} \sim \frac{4^{n-1}}{\sqrt{\pi(n-1)}}.$$

Multiplying by $(2n)^r$, the Catalan factor $\frac{1}{n}$, and $(pq)^n$:

$$(2n)^r \cdot \frac{1}{n} \cdot \binom{2n-2}{n-1} (pq)^n \sim (2n)^r \cdot \frac{1}{n} \cdot \frac{4^{n-1}}{\sqrt{\pi(n-1)}} (pq)^n.$$

For large $n$, $n-1 \sim n$, and $4^{n-1} = 4^n / 4$. Absorbing constants into $c$:

$$\sim c \cdot (4pq)^n \cdot 2^r n^r \cdot n^{-1} \cdot n^{-1/2} = c' (4pq)^n \cdot n^{r-3/2},$$

where $c$ and $c'$ are positive constants.
