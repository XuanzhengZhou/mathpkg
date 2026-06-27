---
role: proof
locale: en
of_concept: elementary-factor-inequality
source_book: gtm011
source_chapter: "5"
source_section: "5.11"
---

Restricting to the case $p \geq 1$, for a fixed $p$ let

$$E_p(z) = 1 + \sum_{k=1}^{\infty} a_k z^k.$$

Hence, for $|z| \leq 1$,

$$|E_p(z) - 1| = \left| \sum_{k=p+1}^{\infty} a_k z^k \right|$$

$$= |z|^{p+1} \left| \sum_{k=p+1}^{\infty} a_k z^{k-p-1} \right|$$

$$\leq |z|^{p+1} \sum_{k=p+1}^{\infty} |a_k|$$

$$= |z|^{p+1},$$

which is the desired inequality. The final equality follows because for $E_p(z) = (1-z)\exp(z + z^2/2 + \cdots + z^p/p)$, expanding the exponential in power series shows that the coefficients $a_k$ for $k \geq p+1$ are all negative and sum in absolute value to $1$.
