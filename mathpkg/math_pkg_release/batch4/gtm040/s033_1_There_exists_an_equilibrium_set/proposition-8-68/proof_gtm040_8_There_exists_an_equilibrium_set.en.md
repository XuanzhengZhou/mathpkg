---
role: proof
locale: en
of_concept: proposition-8-68
source_book: gtm040
source_chapter: "8"
source_section: "There exists an equilibrium set"
---

Start the process in a transient state $i$, and let $a$ be the absorption time. Since $i$ is transient,
$$a^r(\omega) = (a+1)^r(\omega_1)$$
so that
$$a^r(\omega) - a^r(\omega_1) = (a+1)^r(\omega_1) - a^r(\omega_1)$$
or
$$(a^r - (a^r)^{(1)})(\omega) = ((a+1)^r - a^r)(\omega_1).$$
By Theorem 4-11 with the random time identically one,
$$M_i[a^r - (a^r)^{(1)}] = \sum_k P_{ik} M_k[(a+1)^r - a^r]$$
$$= \sum_{k \text{ abs.}} R_{ik} M_k[1] + \sum_{k \text{ trans.}} Q_{ik} M_k[(a+1)^r - a^r].$$
For absorbing states $k$, $M_k[1] = 1$. For transient states $k$, expanding $(a+1)^r$ by the binomial theorem gives
$$M_k[(a+1)^r - a^r] = M_k\left[\sum_{m=1}^{r-1} \binom{r}{m} a^m\right] = \sum_{m=1}^{r-1} \binom{r}{m} a_k^{(m)}.$$
Therefore $f = \sum_{m=1}^{r-1} \binom{r}{m} Q a^{(m)} + \mathbf{1}$, and $h = a^{(r)}$ satisfies $z \geq z^{(1)}$ with condition (2) of Theorem 8-67. Hence $h = Nf$, giving the stated formula.
