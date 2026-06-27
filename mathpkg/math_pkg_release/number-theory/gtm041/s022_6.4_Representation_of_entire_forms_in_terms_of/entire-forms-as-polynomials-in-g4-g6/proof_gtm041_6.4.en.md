---
role: proof
locale: en
of_concept: entire-forms-as-polynomials-in-g4-g6
source_book: gtm041
source_chapter: "6"
source_section: "6.4"
---
If $k$ is odd, $k < 0$ or $k = 2$ the sum is empty and $f$ is $0$. If $k = 0$, $f$ is constant and the sum consists of only one term, $c_{0,0}$. If $k = 4, 6, 8$ or $10$ then each of the respective quotients $f/G_4$, $f/G_6$, $f/G_4^2$ and $f/(G_4 G_6)$ is an entire form of weight $0$ and hence is constant. This proves (8) for $k < 12$ or $k$ odd.

To prove the result for even $k \geq 12$ we use induction on $k$. Assume the theorem has been proved for all entire forms of weight $<k$. By Theorem 6.3, $f$ can be written as a sum of terms $G_{k-12r} \Delta^r$. Since $\Delta$ is itself a polynomial in $G_4$ and $G_6$ and each $G_{k-12r}$ is either an Eisenstein series (expressible as polynomial in $G_4$ and $G_6$) or has weight less than $k$, the induction hypothesis applies and the result follows.
