---
role: proof
locale: en
of_concept: convergence-theorem-noncyclic-recurrent-chains
source_book: gtm040
source_chapter: "6"
source_section: "4"
---

**First Proof.**

Every recurrent chain is either ergodic or null. Taking $\pi$ to be a vector with 1 in the $i$th entry and zeros elsewhere, we see that the existence of $\lim P^n$ follows from the other assertions of the theorem.

**Ergodic case.** Let $P$ be ergodic and let $A = 1lpha$ be the Cesaro limit of the powers of $P$. We have $lpha P^n = lpha$ for every $n$ (regularity). Let $eta = \pi$ (any initial distribution) and $\gamma = lpha$ in Lemma 6-37. Then
$$\lim_{n 	o \infty} \|(\pi - lpha)P^n\| = 0,$$
which means $\pi P^n 	o lpha$ componentwise, independent of $\pi$. Taking $\pi = e_i$ (the $i$th unit vector), we obtain $P_{ij}^{(n)} 	o lpha_j$ for all $i, j$, so $\lim_n P^n = 1lpha$.

**Null case.** Suppose $P$ is null and the assertion is false. Then by Corollary 1-64, for some probability vector $\pi$, there exists an increasing sequence $\{n_k\}$ of positive integers and a non-zero row vector $ho$ such that
$$\lim_k (\pi P^{n_k})_i = ho_i \quad 	ext{for every state } i.$$

Clearly $ho_i \geq 0$. Summing on $i$, by Fatou's Theorem we obtain
$$ho 1 = \sum_i ho_i = \sum_i \lim_k (\pi P^{n_k})_i \leq \liminf_k \sum_i (\pi P^{n_k})_i = 1.$$

Applying Lemma 6-37 with $eta = \pi$ and $\gamma = \pi P$, we see that
$$\lim_k (\pi P^{n_k+1})_i = ho_i \quad 	ext{for each } i.$$

By Fatou's Theorem again,
$$ho P = (\lim_k \pi P^{n_k}) P \leq \liminf_k \pi P^{n_k+1} = ho.$$

Hence $ho$ is a non-negative superregular vector with finite total mass ($ho 1 \leq 1 < \infty$). By Proposition 6-4, $ho$ must be regular, and since $ho 
eq 0$, this implies that $P$ has a non-zero regular measure with finite total mass. But this contradicts Theorem 6-9, which states that a null chain has no non-zero finite regular measure. Therefore the assumption is false and $\lim P^n = 0$.

**Second Proof (using Renewal Theorem).**

We first prove convergence for the $i$th diagonal entry. Set $f_n = ar{F}_{ii}^{(n)}$, $u_n = (P^n)_{ii}$, and
$$\mu = \sum_n n f_n = \sum_n n ar{F}_{ii}^{(n)} = \sum_n n \Pr_i[ar{t}_i = n] = M_i[ar{t}_i] = ar{M}_{ii}.$$

Lemmas 6-34 and 6-35 establish all the hypotheses of Theorem 1-67 (the Renewal Theorem) except for $\sum_n f_n = 1$, which follows from recurrence:
$$\sum_n f_n = \sum_n ar{F}_{ii}^{(n)} = ar{H}_{ii} = 1.$$

Therefore $u_n 	o 1/\mu$ if $\mu < \infty$ (ergodic) or $u_n 	o 0$ if $\mu = \infty$ (null). The value of the limit for diagonal entries follows from Proposition 6-25 which relates $ar{M}_{ii} = 1/lpha_i$.

For off-diagonal entries, let $i$ and $j$ be distinct states. Define a row vector $eta$ and a sequence of column vectors $\{g^{(n)}\}$ by
$$eta_m = ar{F}_{ij}^{(m)}, \qquad g^{(n)}_m = egin{cases} (P^{n-m})_{jj} & 	ext{if } n \geq m \ 0 & 	ext{if } n < m. \end{cases}$$

Then $\lim_n g^{(n)}_m = L_{jj}$ exists since diagonal convergence is already proved. By Lemma 6-34,
$$(P^n)_{ij} = \sum_{m=1}^n eta_m (P^{n-m})_{jj} = \sum_{m=1}^\infty eta_m g^{(n)}_m = eta g^{(n)}.$$

Since $eta 1 = \sum_m ar{F}_{ij}^{(m)} = ar{H}_{ij} = 1$ (by recurrence and irreducibility in the communicating class) and $|g^{(n)}_m| \leq 1$, the Dominated Convergence Theorem applies, yielding
$$\lim_n (P^n)_{ij} = \lim_n eta g^{(n)} = eta (\lim_n g^{(n)}) = eta (1 L_{jj}) = L_{jj}.$$
