---
role: proof
locale: en
of_concept: explicit-reciprocity-law-theorem-1.1
source_book: gtm059
source_chapter: "9"
source_section: "1. Statement of the Reciprocity Laws"
---

By the formalism of the norm residue symbol, we know that

$$
1 = (N_1^* K_2) (N_1^* K_1) (N_1^* K_0).
$$

Hence $[N_1^* u_i] = u_i$ by the Lubin-Tate theory, establishing the first assertion. For the second assertion, we choose $t = \pi_0$ so that $[\pi^{n+1}] = u_0$. Then

$$
\langle u_i, u_j \rangle_n = \pi^* t - t.
$$

Since $(N_1^* K_2)(N_1^* K_1)(N_1^* K_0)$ satisfies the Lubin-Tate relations, we obtain

$$
\langle u_i, u_j \rangle_n = (N_1^* u_i) t - t = (N_1^{n+1}(u_i) - 1) \cdot t.
$$

The factor $\frac{1}{p^2}$ appears from the normalization of the symbol, yielding the stated formula

$$
\langle u_i, u_j \rangle_n = \left[ \frac{1}{p^2} \left( N_1^{n+1}(u_i) - 1 \right) \right]_u.
$$
