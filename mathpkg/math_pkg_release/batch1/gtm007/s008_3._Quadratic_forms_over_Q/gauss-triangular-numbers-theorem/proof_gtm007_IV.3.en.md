---
role: proof
locale: en
of_concept: gauss-triangular-numbers-theorem
source_book: gtm007
source_chapter: "IV"
source_section: "§3. Quadratic forms over Q"
---

Let $n$ be a positive integer. Apply the three-square theorem to $8n + 3$: since $8n+3 \equiv 3 \pmod{8}$, it is not of the forbidden form $4^a(8b-1)$. Hence there exist integers $x_1, x_2, x_3$ such that
$$
x_1^2 + x_2^2 + x_3^2 = 8n + 3.
$$
Reducing modulo $8$, we note that squares in $\mathbf{Z}/8\mathbf{Z}$ are $0, 1, 4$. The only way to obtain a sum of $3 \pmod{8}$ from three squares is $1+1+1 \equiv 3 \pmod{8}$. Therefore each $x_i^2 \equiv 1 \pmod{8}$, which forces each $x_i$ to be odd. Write $x_i = 2y_i + 1$ with $y_i \in \mathbf{Z}$. Then
$$
x_i^2 = 4y_i^2 + 4y_i + 1 = 4y_i(y_i+1) + 1.
$$
Substituting:
$$
\sum_{i=1}^3 (4y_i(y_i+1) + 1) = 8n + 3,
$$
so $4\sum_i y_i(y_i+1) + 3 = 8n + 3$, hence
$$
\sum_{i=1}^3 rac{y_i(y_i+1)}{2} = n.
$$
Each term $rac{y_i(y_i+1)}{2}$ is a triangular number, completing the proof.
