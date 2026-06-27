---
role: proof
locale: en
of_concept: corollary-8-69
source_book: gtm040
source_chapter: "8"
source_section: "69"
---

**Proof:** By Proposition 8-68,

$$a^{(r)} = N \sum_{m=1}^{r-1} \binom{r}{m} Qa^{(m)} + N1,$$

even if both sides are infinite. Hence

$$a^{(r)} \leq (2^r - 2)NQa^{(r-1)} + N1 \quad \text{since } a^{(m)} \leq a^{(r-1)}$$

$$= (2^r - 2)(N - I)a^{(r-1)} + N1 \quad \text{since } N - I = NQ$$

$$\leq (2^r - 2)Na^{(r-1)} + N1$$

$$\leq (2^r - 1)Na^{(r-1)} \quad \text{since } 1 \leq a^{(r-1)}.$$

For the other inequality,

$$a^{(r)} \geq NQa^{(r-1)}$$

$$= Na^{(r-1)} - a^{(r-1)}$$

$$\geq Na^{(r-1)} - a^{(r)} \quad \text{since } a^{(r-1)} \leq a^{(r)}.$$

Hence $Na^{(r-1)} \leq 2a^{(r)}$.

As a second example, let $P$ be a transient chain, and for any two transient states $i$ and $j$ define

$$W_{

We note that $W$ is finite-valued; similarly one shows that $M_i[n_j^r] < \infty$ for $r > 2$.

Next let $E$ be an equilibrium set and let $z$ be the time at which the process is in $E$ for the last time (or 0 if $E$ is never reached). Set $v^E = M_i[z]$. Then

$$z - z^{(1)} = \begin{cases} 1 & \text{if } E \text{ is ever reached after time 0} \\ 0 & \text{otherwise.} \end{cases}$$

Hence $M_i[z - z^{(1)}] = \bar{h}_i^E$, the probability that, from $i$, $E$ is reached after time 0. The random variable $z$ satisfies condition (1) of the theorem. Hence

$$v^E = N\bar{h}^E.$$

Finally, let $E$ be an equilibrium set and let $j$ be any state. Let $z_j$ be the number of times in $j$ before $E$ is left for the last time (or 0 if $E$ is never reached). Define

$$N_{ij}^E = M_i[z_j].$$

Then $z_j$ satisfies condition (1) of the theorem, and we have

$$z - z^{(1)} = \begin{cases} 1 & \text{if } x_0(\omega) = j \text{ and } E \text{ is ever reached} \\ 0 & \text{otherwise.} \end{cases}$$

Hence

$$M_i[z - z^{(1)}] = \delta_{ij}h_j^E,$$

and

$$N_{ij}^E = N\{\delta_{ij}h_j^E\} = N_{ij}h_j^E.$$

9. General denumerable stochastic processes

We shall show that any denumerable stochastic process can be represented within a transient Markov chain in such a manner that potential theory applied to the chain yields corresponding results for the stochastic process.

Throughout this section we shall deal with a probability space $\Omega$ with measure $\mu$, and a fixed sequence $\{\mathcal{R}_i\

all ordered pairs $\langle U, n \rangle$, where $U \in \mathcal{R}_n$ and $\mu(U) > 0$, and whose transition probabilities are

$$P_{\langle U, n \rangle, \langle V, m \rangle} = \begin{cases} \frac{\mu(V)}{\mu(U)} & \text{if } m = n + 1 \text{ and } V \subset U \\ 0 & \text{otherwise.} \end{cases}$$

The chain is started in the state $\langle \Omega, 0 \rangle$, which will be called state 0.
