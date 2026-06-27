---
role: proof
locale: en
of_concept: dirichlet-lemma-p2-minus-5q2-fifth-power
source_book: gtm050
source_chapter: "3"
source_section: "3.2"
---

**Proof (sketch).** The solution of Pell's equation $9^2 - 5 \cdot 4^2 = 1$ shows that the fundamental unit in $\mathbb{Z}[\sqrt{5}]$ is $9 + 4\sqrt{5}$. In general, if $P^2 - 5Q^2$ is a fifth power, then by the theory of quadratic forms one can write $P + Q\sqrt{5} = (A + B\sqrt{5})^5 (9 + 4\sqrt{5})^r$ for some integer $r$ with $0 \leq r \leq 4$, up to sign.

It must be shown that $r = 0$ under the given conditions. Let $C + D\sqrt{5} = (A + B\sqrt{5})^5$ and $E + F\sqrt{5} = (9 + 4\sqrt{5})^r$. Since $Q = 5A^4B + 50A^2B^3 + 25B^5$ in the expansion of $(A+B\sqrt{5})^5$, we have $5 \mid D$. The condition $5 \mid Q$ together with $Q = CF + DE$ implies $CF \equiv 0 \pmod{5}$. But $C \not\equiv 0 \pmod{5}$ (otherwise $P$ and $Q$ would share the factor 5). Hence $F \equiv 0 \pmod{5}$.

If $r \geq 1$, the binomial expansion gives $F = r \cdot 9^{r-1} \cdot 4$ plus terms divisible by 5. Since this can never be divisible by 5 for $1 \leq r \leq 4$, the condition $F \equiv 0 \pmod{5}$ forces $r = 0$. Therefore $P + Q\sqrt{5} = (A + B\sqrt{5})^5$. $\square$
