---
role: proof
locale: en
of_concept: balayage-properties-b-e-h
source_book: gtm040
source_chapter: "8"
source_section: "1"
---

(1) Follows from Proposition 8-15 and the fact that $B^E_{ij} = \delta_{ij}$ for $i$ in $E$.

(2) Let $x$ be a non-negative superregular function such that $x_E \geq h_E$. Since the $\tilde{E}$ columns of $B^E$ are zero, $x \geq B^E x \geq B^E h = \bar{h}$, and (2) holds provided we show in (3) that $\bar{h}$ is superregular.

(3) Since $P\bar{h} \leq Ph \leq h$ is finite-valued,
$$\bar{f} = (I - P)(B^E h) = [(I - P)B^E]h = \begin{pmatrix} I - P^E & 0 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} h_E \\ h_{\tilde{E}} \end{pmatrix}.$$
But $h_E$ is $P^E$-superregular by the dual of Lemma 6-7, and (3) follows.

(4) If $E \subset F$, then by conclusion (6) of Proposition 5-8,
$$B^E h = B^F(B^E h) \leq B^F h.$$
