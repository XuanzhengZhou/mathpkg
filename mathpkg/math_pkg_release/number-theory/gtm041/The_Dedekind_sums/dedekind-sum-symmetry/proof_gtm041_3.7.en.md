---
role: proof
locale: en
of_concept: dedekind-sum-symmetry
source_book: gtm041
source_chapter: "3"
source_section: "3.7"
---

Parts (a) and (b) follow at once from the expression of $s(h,k)$ in terms of the function $((x))$:
$$s(h,k) = \sum_{r \bmod k} \left(\left(\frac{r}{k}\right)\right) \left(\left(\frac{hr}{k}\right)\right).$$

Since $((x))$ is periodic with period $1$ and odd, the stated congruences for $h$ translate directly into the corresponding equalities or sign changes for $s(h,k)$.

To prove (c), note that $h^2 + 1 \equiv 0 \pmod{k}$ implies $h \equiv -\bar{h} \pmod{k}$, where $\bar{h}$ is the reciprocal of $h$ modulo $k$. Applying (a) and (b) yields $s(h,k) = -s(h,k)$, hence $s(h,k) = 0$.
