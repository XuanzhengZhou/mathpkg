---
role: proof
locale: en
of_concept: frame-determines-basis
source_book: gtm006
source_chapter: "II"
source_section: "3"
---

Let $F_1, \dots, F_{n+2}$ be a frame. Choose non-zero vectors $f_i$ such that $F_i = \langle f_i \rangle$ for $i = 1, \dots, n+1$. Then $\{f_1, \dots, f_{n+1}\}$ is a basis for $V$ (since $F_1, \dots, F_{n+1}$ are not contained in any hyperplane, their representative vectors are linearly independent). Now $F_{n+2}$ is not contained in the hyperplane spanned by any $n$ of $F_1, \dots, F_{n+1}$, so if $f_{n+2}$ is any vector with $F_{n+2} = \langle f_{n+2} \rangle$ and we write $f_{n+2} = \sum_{i=1}^{n+1} x_i f_i$, then each coefficient $x_i$ must be non-zero (otherwise $F_{n+2}$ would lie in the span of the $n$ other basis vectors). Define $e_i = x_i f_i$ for $i = 1, \dots, n+1$. Then $\langle e_i \rangle = \langle f_i \rangle = F_i$, and $e_1 + \cdots + e_{n+1} = \sum x_i f_i = f_{n+2}$, so $\langle e_1 + \cdots + e_{n+1} \rangle = F_{n+2}$. For uniqueness: if $e_i' = \lambda e_i$ for all $i$ (with the same $\lambda \neq 0$), then the frame points are unchanged but the basis vectors are scaled uniformly. Conversely, if two bases $\{e_i\}$ and $\{e_i'\}$ produce the same frame, then $\langle e_i \rangle = \langle e_i' \rangle$ implies $e_i' = \lambda_i e_i$, and $\langle \sum e_i \rangle = \langle \sum e_i' \rangle$ forces all $\lambda_i$ to be equal. $\square$
