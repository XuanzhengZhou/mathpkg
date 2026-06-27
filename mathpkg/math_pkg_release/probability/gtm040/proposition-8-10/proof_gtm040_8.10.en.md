---
role: proof
locale: en
of_concept: proposition-8-10
source_book: gtm040
source_chapter: "8"
source_section: "10"
---

**Proof:** The dual of $N_{ij} \leq N_{jj}$ is $N_{ij} \leq (N_{ii}/\alpha_i)\alpha_j$. If $\alpha_i \geq kN_{ii}$, then

$$|g_i| \leq \sum_j N_{ij}|f_j| \leq \frac{N_{ii}}{\alpha_i} \sum_j \alpha_j|f_j| \leq \frac{1}{k} \sum_j \alpha_j|f_j|.$$

Thus $g$ is bounded. Now suppose $\lim_i N_{ij} = 0$. By Proposition 8-6 we may assume that $g$ is a pure potential. Define a sequence of functions $h_j^{(i)} = N_{ij}/\alpha_j$ and a measure $\mu_j = \alpha_j f_j$. Then $\mu$ is a finite measure, and

$$h_j^{(i)} \leq \frac{N_{jj}}{\alpha_j} \leq \frac{1}{k}$$

is bounded independently of $i$ and $j$. Hence, by dominated convergence,

$$\lim_i g_i = \lim_i \sum_j h_j^{(i)}\mu_j = \sum_j (\lim_i N_{ij})f_j = 0.$$

Both conditions of Proposition 8-10 hold for the basic example with $\alpha$ chosen as $\beta$. However, only the first condition holds for the reverse of the basic example (see Section 6). In Section 7 we shall see an example where both conditions fail.

**2. The $h$-process and some applications**

Duality is a transformation which interchanges the roles of row and column vectors. Our purpose now is to describe a

Definition 8-12: The $h$-process transformation is a transformation defined on square matrices $Y$, row vectors $\pi$, and column vectors $f$ by

$$Y^* = UYU^{-1}$$

$$\pi^* = \pi U^{-1}$$

$$f^* = Uf.$$

The $h$-process transformation yields results similar to those with duality. If $P$ is a transient chain, then $P^*$ also is transient. Moreover, powers of $P$ transform to the $P^*$ process the same way that $P$ does, and the fundamental matrix for $P^*$ is $N^*$. Sums and products are preserved in their given order; and equalities, inequalities, and limits are preserved entry-by-entry. Any superregular function (or signed measure) for $P$ transforms into a superregular function (or signed measure) for $P^*$.

If $\alpha$ is the distinguished superregular measure for $P$, we select $\alpha^*$ as the distinguished superregular measure for $P^*$. Then $\alpha^*f^* = \alpha f$ and $N^*f^* = (Nf)^*$. Hence if $f$ is a right charge with potential $g$ in $P$, then $f^*$ is a right charge for $P^*$ with potential $g^*$.

If we decompose $P$ as

$$P = \begin{pmatrix} E & \tilde{E} \\ \tilde{E} & \begin{pmatrix} T & U \\ R & Q \end{pmatrix}, \end{pmatrix}$$

then

$$B^E = \begin{pmatrix} I & 0 \\ (\sum Q^n)R & 0 \end{pmatrix}.$$

From this decomposition we see that $(B^E)^*$ is the $B^E$-matrix of the $P^*$-chain because $Q$ and $R$ transform into $Q^*$ and $R^*$, because products are preserved, and because $I^* = I$.

We shall now give some applications of the $h$-process.

Definition 8-13: The support of a charge is the set on which the charge is not 0; the support

in the enlarged chain. Moreover,

$$\left(Nf\right)_i = \sum_j N_{ij} \bar{P}_{ja} = B_{ia}.$$

Thus $r_i = 1 - B_{ia}$ is the probability that the $P$-process, started at $i$, continues indefinitely. The enlarged chain is absorbing if and only if $1 = Nf$.
