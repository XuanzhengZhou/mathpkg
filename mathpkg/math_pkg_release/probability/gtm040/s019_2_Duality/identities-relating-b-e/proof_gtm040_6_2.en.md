---
role: proof
locale: en
of_concept: identities-relating-b-e
source_book: gtm040
source_chapter: "6"
source_section: "2. Duality"
---

Set $N = \sum Q^n$. For the first identity we have

$$(I - P)B^E = \begin{pmatrix} I - T & -U \\ -R & I - Q \end{pmatrix} \begin{pmatrix} I & 0 \\ NR & 0 \end{pmatrix} = \begin{pmatrix} I - (T + UNR) & 0 \\ -R + (I - Q)NR & 0 \end{pmatrix}$$

$$= \begin{pmatrix} I - P^E & 0 \\ 0 & 0 \end{pmatrix},$$

since $(I - Q)N = I$ and $P^E = T + U N R$ by Lemma 6-6.

For the second identity, we have

$${}^E N = \begin{pmatrix} 0 & 0 \\ 0 & N \end{pmatrix}$$

and hence

$$B^E N^{(n)} = N^{(n)} + {}^E N(P^{n+1} - I).$$
