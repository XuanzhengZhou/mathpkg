---
role: proof
locale: en
of_concept: proposition-8-15
source_book: gtm040
source_chapter: "8"
source_section: "15"
---

**Proof:** First suppose that $h > 0$. Form the $h$-process; then $h^* = 1$. Since $(B^E

(2) $\bar{h}$ is the pointwise infimum of all non-negative superregular functions which dominate $h$ on $E$.

(3) If $\bar{f} = (I - P)\bar{h}$, then

$$\bar{f}_E = (I - P^E)h_E \geq 0$$

and

$$\bar{f}_E = 0.$$

Therefore, $\bar{h}$ is regular on $\tilde{E}$ and is superregular everywhere.

(4) If $E \subset F$, then $B^Eh \leq B^Fh$.

Proof: Statement (1) follows from Proposition 8-15 and the fact that $B^E_{ij} = \delta_{ij}$ for $i$ in $E$. For (2) let $x$ be a non-negative superregular function such that $x_E \geq h_E$. Since the $\tilde{E}$ columns of $B^E$ are zero,

$$x \geq B^Ex \geq B^Eh = \bar{h},$$

and (2) holds provided we show in (3) that $\bar{h}$ is superregular. For (3), since $P\bar{h} \leq Ph \leq h$ is finite-valued,

$$\bar{f} = (I - P)(B^Eh) = [(I - P)B^E]h = \begin{pmatrix} I - P^E & 0 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} h_E \\ h_E \end{pmatrix}.$$

But $h_E$ is $P^E$-superregular by the dual of Lemma 6-7, and (3) follows. Finally for (4), if $E \subset F$, then by conclusion (6) of Proposition 5-8,

$$B^Eh = B^F(B^Eh) \leq B^Fh.$$

We now prove two lemmas and a proposition which conclude that a charge and its potential may both be computed from a knowledge of the values of the potential on the support. The first lemma is interesting in itself because of its game interpretation, which we shall discuss after proving the result.

Lemma

But $f_j$ is the difference of the total number of times the process is in $j$ and the number of times it is in $j$ before reaching $E$. Hence

$$M_i[f_j] = N_{ij} - E N_{ij},$$

and the first equation follows. To get the second equation we multiply through by $f$; associativity in $B^E N f$ holds because $B^E N |f|$ is finite-valued.

In the game interpretation of potentials, $f_j$ is a payment received each time the process is in state $j$, and $g$ is the expected total gain if the process is started in $i$. The second equation of Lemma 8-17 states that $g$ is the expected gain when and after $E$ is entered plus the expected gain before $E$ is entered. If all the payments are non-negative, then it is obvious from this interpretation that $g \geq B^E g$. If the support of $f$ is in $E$, then all non-zero payments occur in $E$, and the expected gain before reaching $E$ is zero. Hence, as we shall see formally in Proposition 8-19, $g = B^E g$.
