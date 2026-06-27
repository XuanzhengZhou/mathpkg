---
role: proof
locale: en
of_concept: z-matrix-fundamental-properties
source_book: gtm040
source_chapter: "9"
source_section: "5. Strong ergodic chains"
---

For (1) we have

$$\text{dual } Z = \text{dual}\left( \sum_{n=0}^{\infty} (P - A)^n \right) = \sum_{n=0}^{\infty} [\text{dual} (P - A)]^n = \sum_{n=0}^{\infty} (\hat{P} - A)^n = \hat{Z}.$$

Hence in conclusions (2) through (5) the second result is always the dual of the first, and we need verify only the first. Conclusion (5) comes from Proposition 9-75.

For (2), we have

$$Z1 = [A - G(I - A)]1$$

since by Proposition 9-73 all terms are finite-valued,

$$= A1 - G1 + GA1 = 1 - G1 + G1 = 1.$$

For (3),

$$Z(I - P) = [A - G(I - A)](I - P)$$
$$= A(I - P) - G(I - A)(I - P)$$
$$= 0 - G(I - P - A + AP)$$
$$= -G + GP + GA - GAP$$
$$= -G + GP + GA - GA$$
$$= -G(I - P)$$
$$= I - A \quad \text{by Corollary 9-51}.$$

Conclusion (4) follows directly from (2) and (3).
