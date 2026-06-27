---
role: proof
locale: en
of_concept: proposition-8-19
source_book: gtm040
source_chapter: "8"
source_section: "19"
---

**Proof:** The fact that $g = B^E g$ is immediate from Lemma 8-17. Hence $g_E$ determines $g$. Since $g = B^E g$, we have $f_E = (I - P^E)g_E$ by conclusion (3) of Proposition 8-16. Finally $g_E = N_E f_E$ either by

Proof: Since

$$\alpha \begin{pmatrix} I - P^E & 0 \\ 0 & 0 \end{pmatrix} = (\alpha_E (I - P^E) \quad 0)$$

is finite-valued, each column of $N \begin{pmatrix} I - P^E & 0 \\ 0 & 0 \end{pmatrix}$ is a potential with support in $E$. Thus by Proposition 8-19,

$$N \begin{pmatrix} I - P^E & 0 \\ 0 & 0 \end{pmatrix} = B^E N \begin{pmatrix} I - P^E & 0 \\ 0 & 0 \end{pmatrix}$$

$$= B^E \begin{pmatrix} N_E (I - P^E) & 0 \\ N_3 (I - P^E) & 0 \end{pmatrix}$$ with $N = \begin{pmatrix} N_E & N_2 \\ N_3 & N_4 \end{pmatrix}$

$$= B^E \begin{pmatrix} I & 0 \\ N_3 (I - P^E) & 0 \end{pmatrix}$$ by Lemma 8-18

$$= B^E.$$

Corollary 8-21: For any set $E$, $\lim_n P^n B^E = 0.$

Proof: Apply Proposition 8-20 and Corollary 8-9.

Finally we work toward a proof that a non-negative superregular function dominated by a potential is a potential, a result we state as Proposition 8-25.

Lemma 8-22: If $E$ is a finite set and if $h$ is non-negative superregular, then $B^E h$ is a pure potential of finite support.

Proof: $B^E h$ is a finite linear combination of columns of $B^E$ and is therefore by Proposition 8-20 a potential with support in the finite set $E$. Since $h$ is non-negative superregular, $B^E h$ is non-negative superregular by conclusion (3) of Proposition 8-16. Hence, $B^

Lemma 8-22 and conclusion (4) of Proposition 8-16. If $i$ is in $E_n$, then $h_i^{(n)} = h_i$, so that $\lim h^{(n)} = h$.

If $g$ is a potential with charge $f$, then the total charge of $g$ (or $f$) is defined to be $\alpha f$ (see Section 7-5).

Lemma 8-24: If $N\bar{f} \leq Nf$ with $\bar{f} \geq 0$ and $\alpha f$ finite, then

$$0 \leq \alpha \bar{f} \leq \alpha f < \infty.$$

Proof: By the dual of Proposition 8-23, we may find a sequence of finite measures $\pi^{(n)}$ such that $\alpha$ is the monotone limit of $\pi^{(n)}N$. Since $N\bar{f} \leq Nf$, we have $\pi^{(n)}(N\bar{f}) \leq \pi^{(n)}(Nf)$ and

$$\lim_n \pi^{(n)}(N\bar{f}) \leq \lim_n \pi^{(n)}(Nf).$$

Since $\bar{f} \geq 0,$

$$\pi^{(n)}(N\bar{f}) = (\pi^{(n)}N)\bar{f},$$

and

$$\lim_n \pi^{(n)}(N\bar{f}) = (\lim_n \pi^{(n)}N)\bar{f} = \alpha \bar{f}$$

by monotone convergence with $\bar{f}$ as the measure. And since $\pi^{(n)}Nf^+ \leq \alpha f^+ < \infty$ and $\pi^{(n)}Nf^- \leq \alpha f^- < \infty,$

$$\pi^{(n)}(Nf) = \pi^{(n)}Nf^+ - \pi^{(n)}Nf^-.$$

Hence

$$\lim_n \pi^{(n)}(Nf) = \alpha f^+ - \alpha f^- = \alpha f$$
