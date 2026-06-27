---
role: proof
locale: en
of_concept: theorem-6
source_book: gtm077
source_chapter: "I"
source_section: "2"
---

# Proof of Theorem 6: Cancellation Law for Congruences

**Theorem.** If $ca \equiv cb \pmod{n}$, then

$$a \equiv b \pmod{\frac{n}{d}}, \quad \text{where} \quad (c, n) = d,$$

and conversely.

*Proof.* ($\Rightarrow$) The hypothesis $ca \equiv cb \pmod{n}$ means $n \mid c(a - b)$. Let $d = (c, n)$ and write

$$n = d n_1, \qquad c = d c_1, \qquad \text{where} \quad (c_1, n_1) = 1.$$

The condition $n \mid c(a - b)$ becomes $d n_1 \mid d c_1 (a - b)$, which after cancelling the factor $d$ yields

$$n_1 \mid c_1 (a - b).$$

Since $(c_1, n_1) = 1$, it follows from the coprimality property (Theorem 4, Part 3) that $n_1 \mid (a - b)$. Hence

$$a \equiv b \pmod{n_1} = \pmod{\frac{n}{d}}.$$

($\Leftarrow$) Conversely, if $a \equiv b \pmod{n/d}$, then $n/d \mid a - b$. Since $c = d c_1$, we multiply by $d$: $n \mid d(a - b)$. And since $d(a - b) = d c_1 (a - b) / c_1$ — wait, more directly: $n \mid d(a - b)$. Then $c(a - b) = d c_1 (a - b)$ is a multiple of $n$ because $n = d n_1$ and $n_1 \mid a - b$, so $c(a - b) = d c_1 \cdot (n_1 k) = (d n_1) c_1 k = n \cdot (c_1 k)$. Thus $ca \equiv cb \pmod{n}$. $\square$

**Special case.** If $(c, n) = 1$, then $ca \equiv cb \pmod{n}$ implies $a \equiv b \pmod{n}$. In other words, when $c$ is coprime to the modulus, we may cancel it from both sides of a congruence without changing the modulus.

**Example.** From $5 \cdot 4 \equiv 5 \cdot 1 \pmod{15}$, we cannot conclude $4 \equiv 1 \pmod{15}$. Since $(5, 15) = 5$, we can only conclude $4 \equiv 1 \pmod{3}$, which is indeed true.
