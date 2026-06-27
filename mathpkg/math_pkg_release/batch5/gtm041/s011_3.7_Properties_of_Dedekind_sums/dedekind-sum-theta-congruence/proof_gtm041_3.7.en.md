---
role: proof
locale: en
of_concept: dedekind-sum-theta-congruence
source_book: gtm041
source_chapter: "3"
source_section: "3.7"
---
The reciprocity law (Theorem 3.7) gives

$$12hks(h,k) \equiv h^2 + k^2 + 1 - 3hk \pmod{\theta k}$$

where $\theta = (3,k)$.

For part (a), we analyze the congruence modulo 3. If $3 \mid k$, then $3 \nmid h$ (since $(h,k)=1$), and the reciprocity law implies $12ks(h,k) \equiv -h \not\equiv 0 \pmod{3}$. If $3 \nmid k$, then $3 \mid (k-1)(k+1)$, which gives $12ks(h,k) \equiv 0 \pmod{3}$. Hence $12ks(h,k) \equiv 0 \pmod{3}$ if and only if $3 \nmid k$.

For part (b), the reciprocity law gives

$$12ks(h,k) \equiv \frac{h^2 + k^2 + 1 - 3hk}{h} \pmod{\theta k}.$$

Since $hk \equiv 0 \pmod{\theta k}$ and $k^2 \equiv 0 \pmod{\theta k}$, we obtain

$$12ks(h,k) \equiv h^2 + 1 \pmod{\theta k}.$$

The final equivalence follows by combining part (b) with Theorem 3.6(c): Theorem 3.6(c) gives $h^2+1 \equiv 0 \pmod{k} \implies s(h,k)=0$, while part (b) gives $s(h,k)=0 \implies h^2+1 \equiv 0 \pmod{k}$ (since $\theta \mid k$, the congruence modulo $\theta k$ implies the same modulo $k$).
