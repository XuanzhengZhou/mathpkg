---
role: proof
locale: en
of_concept: induction-on-commuting-products
source_book: gtm030
source_chapter: "1"
source_section: "4"
---

The proof is by induction on $n$. For $n = 1$, the statement $a_1 b = b a_1$ is given. Assume the statement holds for $n-1$, i.e., $a_1 \cdots a_{n-1} b = b a_1 \cdots a_{n-1}$. Then

$$a_1 \cdots a_{n-1} a_n b = a_1 \cdots a_{n-1} (a_n b) = a_1 \cdots a_{n-1} (b a_n)$$

since $a_n b = b a_n$ by hypothesis. By the associative law,

$$(a_1 \cdots a_{n-1} b) a_n.$$

Applying the induction hypothesis, this equals $(b a_1 \cdots a_{n-1}) a_n = b a_1 \cdots a_{n-1} a_n$, completing the induction.
