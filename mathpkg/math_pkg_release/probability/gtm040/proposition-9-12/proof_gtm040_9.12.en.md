---
role: proof
locale: en
of_concept: proposition-9-12
source_book: gtm040
source_chapter: "9"
source_section: "12"
---

**Proof:** Let

$$S_k^{(n)} = \left[ \left(N_{00}^{(n)} - N_{k0}^{(n)}\right) \frac{\alpha_i}{\alpha_0} + \left(N_{ki}^{(n)} - N_{0i}^{(n)}\right) \right].$$

Since $\mu 1 = 0$, we have

$$\sum_k \mu_k \left[ N_{ki}^{

Proposition 9-13: If $\alpha f = 0$, then $f$ is a charge if and only if
$$\lim_{n} [P^n(0Nf)]$$
exists and is finite-valued. If $f$ is a charge, then its potential $g$ satisfies
$$g = 0Nf - \lim_{n} [P^n(0Nf)].$$

Proof: We have
$$\left(P^0N\right)_{ij} = \sum_{k} P_{ik} 0N_{kj} = \begin{cases} 0 & \text{if } j = 0 \text{ since } 0N_{k0} = 0 \\ 0\bar{N}_{0j} = \frac{\alpha_j}{\alpha_0} & \text{if } i = 0 \text{ and } j \neq 0 \\ 0N_{ij} - \delta_{ij} & \text{if } i \neq 0 \text{ and } j \neq 0 \end{cases}$$
$$\left((I - P)^0N\right)_{ij} = \begin{cases} 0 & \text{if } j = 0 \\ -\alpha_j/\alpha_0 & \text{if } i = 0 \text{ and } j \neq 0 \\ \delta_{ij} & \text{if } i \neq 0 \text{ and } j \neq 0. \end{cases}$$

By Lemma 9-11, $0Nf$ is finite-valued, and hence associativity holds in the triple product $(I - P)^0Nf$. We find
$$\left((I - P)^0Nf\right)_i = \begin{cases} \sum_{j \neq 0} \delta_{ij}f_j = f_i & \text{for } i \neq 0 \\ \sum_{j \neq 0} \left(-\frac{\alpha_j}{\alpha_0}\right)f_j = \frac{1}{\alpha_0} \left(\alpha_0f_0\right) = f_0 & \text{for } i = 0. \end{cases}$$

number of times that the process is in state $j$ before $F$, counting from the time when $E$ is first entered. This mean is the difference of the number of times in $j$ before $F$ and the number of times in $j$ before $E$, since $F$ cannot be entered unless $E$ is entered.

Theorem 9-15: If $f$ is a function with $\alpha f = 0$ and if

$$\lim [(I + P + \cdots + P^{n-1})f]_0$$

exists and is finite for some state 0, then $f$ is a charge. If $g$ is its potential, then

(1) $g = 0Nf + g_01$.
(2) $f = (I - P)g$.
(3) $P^n g \rightarrow 0$.
(4) $B^E g = g$ if the support is contained in $E$.
(5) $f_E = (I - P^E)g_E$ if the support is contained in $E$.

Proof: By Proposition 9-12, if $\lim_n \sum_k N_{ik}^{(n)}f_k$ exists, then

$$\lim_n \sum_k [N_{ik}^{(n)} - N_{0k}^{(n)}]f_k = \sum_n 0N_{ik}f_k$$

or

$$\left( \lim_n \sum_k N_{ik}^{(n)}f_k \right) - \left( \lim_n \sum_k N_{0k}^{(n)}f_k \right) = (0Nf)_i.$$

Hence $\lim_n \sum_k N_{ik}^{(n)}f_k$ exists, and $f$ is a charge.

(1) Therefore $g_i - g_0 = (0Nf)_i$ and (1) follows.
(2) From the proof of Proposition 9-13 we have $(I - P)0Nf = f$, since $\alpha f = 0$. Thus if we multiply (1) by $I - P$, we get (2).
(3) By (2) we have $g = Pg + f$, and, since $P^k f$ is finite-

Since $f$ has support in $E$, $E N f = 0$ because $E N_{ij} = 0$ when $j \in E$.

(5) $f = (I - P) g = (I - P)(B^E g) = [(I - P) B^E] g$
$$= \begin{pmatrix} I - P^E & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} g_E \\ g_E \end{pmatrix} \text{ by Proposition 6-17}$$
$$= \begin{pmatrix} (I - P^E) g_E \\ 0 \end{pmatrix}.$$

We note from conclusion (2) that a potential uniquely determines its charge.
