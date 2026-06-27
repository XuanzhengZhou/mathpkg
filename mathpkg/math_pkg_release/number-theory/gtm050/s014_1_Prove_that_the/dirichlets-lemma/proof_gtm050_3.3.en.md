---
role: proof
locale: en
of_concept: dirichlets-lemma
source_book: gtm050
source_chapter: "3"
source_section: "3.3"
---

Given that $P^2 - 5Q^2$ is a fifth power, one can use the fact that any element of $\mathbb{Z}[\sqrt{5}]$ whose norm is a fifth power can be written in the form $(A + B\sqrt{5})^5 (9 + 4\sqrt{5})^r$ for some integers $A, B$ and $0 \leq r \leq 4$. Write this as

$$P + Q\sqrt{5} = (A + B\sqrt{5})^5 (9 + 4\sqrt{5})^r.$$

Let $C + D\sqrt{5} = (A + B\sqrt{5})^5$ and $E + F\sqrt{5} = (9 + 4\sqrt{5})^r$. Expanding $(A + B\sqrt{5})^5$ shows that $D \equiv 0 \pmod{5}$. Since $Q = CF + DE$ and $Q \equiv 0 \pmod{5}$ by hypothesis, it follows that $CF \equiv 0 \pmod{5}$ (because $DE \equiv 0$). Now $C \not\equiv 0 \pmod{5}$, for if $C \equiv 0 \pmod{5}$ then both $P$ and $Q$ would be divisible by $5$, contradicting relative primality. Therefore $F \equiv 0 \pmod{5}$.

If $r \geq 1$, then by the binomial theorem applied to $(9 + 4\sqrt{5})^r$, one obtains $F = r \cdot 9^{r-1} \cdot 4$ plus terms each divisible by $5$. Since $9^{r-1} \cdot 4$ is not divisible by $5$, $F$ can be divisible by $5$ only if $r$ is a multiple of $5$. But $0 \leq r \leq 4$, so $r = 0$ is the only possibility. Thus $P + Q\sqrt{5} = (A + B\sqrt{5})^5$ as claimed.
