---
role: proof
locale: en
of_concept: gauss-three-triangular-numbers
source_book: gtm007
source_chapter: "IV"
source_section: "§3. Quadratic forms over Q"
---

Apply the three-square theorem to $8n+3$. Since $8n+3 \equiv 3 \pmod{8}$, it is not of the form $4^a(8b-1)$. Hence there exist integers $x_1, x_2, x_3$ with
$$
x_1^2 + x_2^2 + x_3^2 = 8n + 3.
$$
Reducing modulo $8$: the squares mod $8$ are $0, 1, 4$. To obtain $3 \pmod{8}$ as a sum of three squares, the only possibility is $1+1+1 \equiv 3 \pmod{8}$. Hence each $x_i^2 \equiv 1 \pmod{8}$, forcing each $x_i$ odd: $x_i = 2m_i + 1$. Then
$$
(2m_i+1)^2 = 4m_i(m_i+1) + 1.
$$
Substituting,
$$
\sum_{i=1}^3 (4m_i(m_i+1) + 1) = 8n + 3 \implies 4\sum m_i(m_i+1) = 8n \implies \sum rac{m_i(m_i+1)}{2} = n.
$$
