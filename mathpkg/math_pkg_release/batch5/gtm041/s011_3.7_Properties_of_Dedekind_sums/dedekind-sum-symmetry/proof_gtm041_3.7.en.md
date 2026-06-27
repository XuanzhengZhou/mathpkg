---
role: proof
locale: en
of_concept: dedekind-sum-symmetry
source_book: gtm041
source_chapter: "3"
source_section: "3.7"
---
Parts (a) and (b) follow at once from the formula

$$s(h,k) = \sum_{r=1}^{k-1} \left(\left(\frac{hr}{k}\right)\right) \left(\left(\frac{r}{k}\right)\right)$$

where $((x))$ is the Bernoulli periodic function.

To prove (c) we note that $h^2 + 1 \equiv 0 \pmod{k}$ implies $h \equiv -\bar{h} \pmod{k}$, where $\bar{h}$ is the reciprocal of $h$ modulo $k$. Then from (a) and (b) we obtain

$$s(h, k) = -s(\bar{h}, k) = -s(h, k),$$

hence $s(h, k) = 0$.
