---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.2"
proof_technique: algorithmic-diagonalization
locale: en
content_hash: ""
written_against: ""
---
The proof is an algorithm using elementary row and column operations:

1. If $A = 0$, done. Otherwise, permute rows and columns to place an entry $a_1$ of minimal "size" at position $(1,1)$.

2. If $a_1$ divides every entry in the first row and column, use column/row operations to clear the first row and column, producing a block diagonal matrix with $a_1$ in position $(1,1)$.

3. If $a_1$ does not divide some entry $b$ in the first row (or column), use the Euclidean algorithm: write $b = a_1q + r$ with $r \neq 0$ and smaller than $a_1$. Perform column operations to replace $b$ by $r$, then swap to bring $r$ to position $(1,1)$, obtaining a strictly smaller entry.

4. Since the original $a_1$ has only finitely many distinct proper divisors (as $R$ is a UFD), this process terminates, yielding a matrix with $d_1$ at $(1,1)$ and zeros elsewhere in the first row and column. Apply induction to the $(n-1) \times (m-1)$ submatrix.

5. The divisibility condition $d_1 \mid d_2 \mid \cdots \mid d_r$ holds because otherwise an elementary operation could produce a smaller entry. Uniqueness of the ideal chain follows from the structure theorem for finitely generated modules over a PID (Theorem IV.6.12).
