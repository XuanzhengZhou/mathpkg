---
role: proof
locale: en
of_concept: uniqueness-of-inverse
source_book: gtm028
source_chapter: "I"
source_section: "1"
---

Suppose $a \in G$ has inverses $a'$ and $a''$. That is, $a'a = aa' = e$ and $a''a = aa'' = e$. Then

$$a'' = a''e = a''(aa') = (a''a)a' = ea' = a'.$$

The first equality uses that $e$ is the identity. The second equality uses that $a'$ is an inverse of $a$, so $aa' = e$. The third equality uses associativity. The fourth uses that $a''$ is an inverse of $a$, so $a''a = e$. The last uses that $e$ is the identity. Thus $a'' = a'$, and the inverse is unique.
