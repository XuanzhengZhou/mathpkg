---
role: proof
locale: en
of_concept: theorem-9-15
source_book: gtm040
source_chapter: "9"
source_section: "1. Potentials"
---

By Proposition 9-12, if $\lim_n \sum_k N_{ik}^{(n)} f_k$ exists, then
$$\lim_n \sum_k [N_{ik}^{(n)} - N_{0k}^{(n)}] f_k = \sum_k {}_0 N_{ik} f_k$$
or
$$\left( \lim_n \sum_k N_{ik}^{(n)} f_k \right) - \left( \lim_n \sum_k N_{0k}^{(n)} f_k \right) = ({}_0 N f)_i.$$
Hence $\lim_n \sum_k N_{ik}^{(n)} f_k$ exists for all $i$, and $f$ is a charge.

(1) Therefore $g_i - g_0 = ({}_0 N f)_i$ and $g = {}_0 N f + g_0 \mathbf{1}$ follows.

(2) From the proof of Proposition 9-13 we have $(I-P){}_0 N f = f$ (since $\alpha f = 0$). Multiplying (1) by $I-P$ gives $(I-P)g = f$, since $(I-P)\mathbf{1} = 0$.

(3) By (2) we have $g = Pg + f$, so by induction $g = P^n g + (I + P + \cdots + P^{n-1})f$. Since $g$ is finite-valued and $(I + \cdots + P^{n-1})f \to g$, we must have $P^n g \to 0$.

(4) Since $f$ has support in $E$, ${}_E N f = 0$ because ${}_E N_{ij} = 0$ when $j \in E$. By the balayage theorem, $B^E({}_0 N f) = {}_0 N f$, so $B^E g = g$.

(5) $f = (I-P)g = (I-P)(B^E g) = [(I-P)B^E]g$
$$= \begin{pmatrix} I - P^E & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} g_E \\ g_{\tilde{E}} \end{pmatrix} = \begin{pmatrix} (I - P^E)g_E \\ 0 \end{pmatrix},$$
using Proposition 6-17. Hence $f_E = (I - P^E)g_E$.
