---
role: proof
locale: en
of_concept: dimension-theorem-sum-and-intersection
source_book: gtm049
source_chapter: "I"
source_section: "1.4"
---

Part (1) is an immediate consequence of Theorem 1. To prove part (2), we may suppose, using Theorem 1, Corollary 1, that $\{a_1, \ldots, a_r\}$ is a basis of $M \cap N$, $\{a_1, \ldots, a_r, b_1, \ldots, b_s\}$ is a basis of $M$ and that $\{a_1, \ldots, a_r, c_1, \ldots, c_t\}$ is a basis of $N$. It is clear that $M + N$ is spanned by $a_1, \ldots, a_r, b_1, \ldots, b_s, c_1, \ldots, c_t$ and it only remains to prove that these vectors are linearly independent.

Suppose that

$$x_1 a_1 + \cdots + x_r a_r + y_1 b_1 + \cdots + y_s b_s + z_1 c_1 + \cdots + z_t c_t = 0,$$

where the $x_i$'s, $y_i$'s and $z_i$'s are in $F$. Then $\sum x_i a_i + \sum y_i b_i = -\sum z_i c_i$ lies in $M \cap N$ and thus can be expressed as a linear combination of $a_1, \ldots, a_r$. Since $b_1, \ldots, b_s$ are linearly independent from the $a_i$'s, we deduce $y_i = 0$ for all $i$. Similarly $z_i = 0$ for all $i$, and then $x_i = 0$ for all $i$. Hence $\dim(M+N) = r+s+t$, $\dim(M \cap N) = r$, $\dim M = r+s$, $\dim N = r+t$, and the formula follows.
