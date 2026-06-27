---
role: proof
locale: en
of_concept: positive-intersection-subsequence-lemma
source_book: gtm036
source_chapter: "17"
source_section: "17.9"
---
It is sufficient to prove that there is an integer $s$ and a positive number $d$ such that $m(A_s \cap A_k) \geq d$ for infinitely many integers $k$. Application of the diagonal process, beginning with the subsequence of all such $A_k$, then yields the desired subsequence.

Let $B_n = \bigcup \{A_k : k = 1, \cdots, n\}$; then $\{m(B_n)\}$ is a bounded non-decreasing sequence of numbers. Let $a = \lim m(B_n)$; then there is a positive integer $r$ such that $a - m(B_r) < e/2$. Hence for any integer $k$ greater than $r$, there is an integer $s$ such that $1 \leq s \leq r$ and $m(A_s \cap A_k) \geq e/2r$. For otherwise $m(B_k) \leq m(B_r) + m\left(\bigcup \{A_t : t = r+1, \cdots, k\}\right)$ and, since for each $t > r$ and $s \leq r$ we would have $m(A_s \cap A_t) < e/2r$, the additivity of $m$ would imply $m(A_t \setminus B_r) = m(A_t) - m(A_t \cap B_r) \geq e - r \cdot (e/2r) = e/2$, leading to $m(B_k) \geq m(B_r) + (k-r) \cdot e/2$, contradicting the boundedness of $\{m(B_n)\}$ as $k \to \infty$.
