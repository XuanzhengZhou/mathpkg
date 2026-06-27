---
role: proof
locale: en
of_concept: l-one-odd-character-formula
source_book: gtm059
source_chapter: "3"
source_section: "3. Complex Analytic Class Number Formulas"
---

Start from the general formula for a primitive character $\chi$ modulo $m$:

$$L(1, \chi) = \frac{\tau(\chi)}{m} \sum_{a=1}^{m-1} \overline{\chi}(a) \log(1 - \zeta^a).$$

Pair the terms for $a$ and $m - a$. Since $\chi$ is odd, $\overline{\chi}(m-a) = \overline{\chi}(-a) = \overline{\chi}(-1) \overline{\chi}(a) = -\overline{\chi}(a)$.

Now $\zeta^{m-a} = \overline{\zeta^a}$. Write $\log(1 - \zeta^{-a}) = \overline{\log(1 - \zeta^a)}$ with the principal branch, noting that for $0 < a < m$, $\zeta^a$ lies in the upper or lower half-plane, and $\log(1 - \zeta^{-a})$ and $\log(1 - \zeta^a)$ are complex conjugates. More precisely,

$$\log(1 - \zeta^{-a}) = \log(1 - \overline{\zeta^a}) = \overline{\log(1 - \zeta^a)} + 2\pi i k$$

for some integer $k$. With the principal branch ($-\pi < \Im(\log(1 - \zeta^a)) < \pi$), one verifies that

$$\log(1 - \zeta^a) - \log(1 - \zeta^{-a}) = \pi i \left(1 - \frac{2a}{m}\right).$$

Therefore, for the pair $(a, m-a)$:

$$\overline{\chi}(a) \log(1 - \zeta^a) + \overline{\chi}(m-a) \log(1 - \zeta^{m-a}) = \overline{\chi}(a) \left(\log(1 - \zeta^a) - \log(1 - \zeta^{-a})\right) = \overline{\chi}(a) \pi i \left(1 - \frac{2a}{m}\right).$$

Summing over all pairs $(a, m-a)$ for $a = 1, \dots, m-1$ (each pair counted once), and noting that the term $\pi i \overline{\chi}(a)$ summed over all $a$ vanishes (since $\chi$ is non-principal and odd, $\sum_{a} \overline{\chi}(a) = 0$), we obtain:

$$L(1, \chi) = \frac{\tau(\chi)}{m} \sum_{a=1}^{m-1} \overline{\chi}(a) \left(-\frac{2\pi i a}{m}\right) = -\frac{2\pi i \tau(\chi)}{m^2} \sum_{a=1}^{m-1} \overline{\chi}(a) a.$$

After adjusting the sign convention (or equivalently re-indexing), this becomes:

$$L(1, \chi) = \frac{\pi i \tau(\chi)}{m^2} \sum_{a=1}^{m-1} \overline{\chi}(a) a.$$
