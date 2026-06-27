---
role: proof
locale: en
of_concept: dedekind-sum-power-of-2-congruence
source_book: gtm041
source_chapter: "3"
source_section: "3.7"
---
Since $h$ is odd, we can apply Theorem 3.9, formula (40), with $h$ and $k$ interchanged to obtain

$$12h\,s(k, h) \equiv h - 1 + 4 \sum_{v < h/2} \left[ \frac{2kv}{h} \right] \pmod{8}.$$

Multiplying by $k$,

$$12hk\,s(k, h) \equiv k(h - 1) + 4k \sum_{v < h/2} \left[ \frac{2kv}{h} \right] \pmod{2^{\lambda+3}}.$$

From the reciprocity law (Theorem 3.7) we have

$$12hk\,s(h, k) = h^2 + k^2 + 1 - 3hk - 12hk\,s(k, h).$$

Substituting the congruence for $12hk\,s(k, h)$ and simplifying, noting that $h^2 \equiv 1 \pmod{8}$ since $h$ is odd, we obtain

$$12hk\,s(h, k) \equiv h^2 + k^2 + 1 + 5k - 4k \sum_{v < h/2} \left[ \frac{2kv}{h} \right] \pmod{2^{\lambda+3}}.$$

The simplification uses that $3hk + k(h-1) = 4hk - k \equiv -5k \pmod{2^{\lambda+3}}$ (since $4h \equiv 4 \pmod{8}$ and $2^{\lambda+3}$ divides appropriate multiples).
