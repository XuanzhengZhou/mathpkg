---
role: proof
locale: en
of_concept: lemma-8-66
source_book: gtm040
source_chapter: "8"
source_section: "66"
---

**Proof:** We note that $m(m+1 z) = m z$. Applying Lemma 8-65 to $m+1 z$, we find that $m+1 z - m+1 z^{(1)} \geq m z - m z^{(1)}$. Then $m+1 f_i \geq m f_i$. Since $\lim_{m} (m z - m z^{(1)}) = z - z^{(1)}$ a.e., $\lim_m

(2) The extended chain is absorbing and $z(\omega) = 0$ for every path $\omega$ which begins in the absorbing state.

Proof: For each $m$, $mz$ is bounded. If one of the conditions applies to $z$, then it applies to $mz$ because $0 \leq mz \leq z$. Hence by Lemma 8-64,

$$mh = Nmf.$$

By Lemma 8-66, $mf$ increases to $f$, and by monotone convergence $mh$ increases to $h$. Therefore $h = Nf$ by the Monotone Convergence Theorem.

We now apply Theorem 8-67 in four special cases.

First let $P$ be an absorbing chain with fundamental matrix $N$. We define $a_i^{(r)} = M_i[a(\omega)^r]$, where $a(\omega)$ is the absorption time defined in Chapter 5. The column vector $a^{(r)}$ is indexed by the transient states of $P$.

Proposition 8-68: If $P$ is an absorbing chain, then

$$a^{(r)} = \sum_{m=1}^{r-1} \binom{r}{m} NQa^{(m)} + N1.$$

Proof: Start the process in a transient state $i$, and let $a$ be the absorption time. Since $i$ is transient,

$$a^r(\omega) = (a + 1)^r(\omega_1)$$

so that

$$a^r(\omega) - a^r(\omega_1) = (a + 1)^r(\omega_1) - a^r(\omega_1)$$

or

$$(a^r - (a^r)^{(1)})(\omega) = ((a + 1)^r - a^r)(\omega_1).$$

By Theorem 4-11 with the random time identically one,

$$M_i[a^r - (a^r)^{(1)}] = \sum_k P_{ik}M_k[(a + 1)^r - a^r]$$

$$= \sum_{k \text{ abs.}} R_{ik}M_k[1] + \sum

satisfies $z \geq z^{(1)}$, and condition (2) of the theorem holds for $z$. As we have just shown,

$$f = \sum_{m=1}^{r-1} \binom{r}{m} Qa^{(m)} + 1,$$

and we also have $h = a^{(r)}$. Hence $h = Nf$ by the theorem.
