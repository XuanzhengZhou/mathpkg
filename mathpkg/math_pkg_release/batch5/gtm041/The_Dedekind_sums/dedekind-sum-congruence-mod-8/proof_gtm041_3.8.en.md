---
role: proof
locale: en
of_concept: dedekind-sum-congruence-mod-8
source_book: gtm041
source_chapter: "3"
source_section: "3.8"
---

Starting from the reciprocity law in the form (36):
$$12k\,s(h,k) = 2h(k-1)(k-2h) - (k-1)(k-2) + 4\sum_{r=1}^{k-1} \left[\frac{hr}{k}\right]\left(\left[\frac{hr}{k}\right] + 1\right).$$

One analyzes the last sum modulo $8$. Note that
$$\sum_{r=1}^{k-1} \left[\frac{hr}{k}\right]\left(\left[\frac{hr}{k}\right] + 1\right) \equiv 2\sum_{r < k/2} \left[\frac{2hr}{k}\right] - \sum_{r=1}^{k-1} \left[\frac{hr}{k}\right] \pmod{2}.$$

The next-to-last term simplifies via the sawtooth function:
\begin{align*}
-4\sum_{r=1}^{k-1} \left[\frac{hr}{k}\right] &= 4\sum_{r=1}^{k-1} \left(\left(\frac{hr}{k}\right)\right) - 4\sum_{r=1}^{k-1} \frac{hr}{k} + 2\sum_{r=1}^{k-1} 1 \\
&= 0 - 2h(k-1) + 2(k-1) = (k-1)(2-2h).
\end{align*}

Combining:
$$(k-1)(k-2h) + (k-1)(2-2h) = (k-1)(k+2) - 4h(k-1),$$
which proves the general congruence (39).

When $k$ is odd, we have $4h(k-1) \equiv 0 \pmod{8}$ because $k-1$ is even. Moreover,
$$(k-1)(k+2) = k^2 + k - 2 \equiv 1 + k - 2 = k - 1 \pmod{8},$$
since $k^2 \equiv 1 \pmod{8}$ for odd $k$. Hence (39) simplifies to (40). $\square$
