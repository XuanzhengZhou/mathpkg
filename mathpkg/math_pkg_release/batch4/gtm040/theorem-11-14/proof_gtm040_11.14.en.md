---
role: proof
locale: en
of_concept: theorem-11-14
source_book: gtm040
source_chapter: "11"
source_section: "14"
---

**Proof:** Apply Theorem

Under the hypotheses of Theorem 11-15, the number $\beta(X)$ for any Borel subset $X$ of $B$ may be interpreted as the probability that the process is near this part of the boundary in the long run. For example, if $x$ is at a positive distance from other boundary points, then any sufficiently small neighborhood $E$ of $x$ will have a continuous characteristic function. By Theorem 11-14,

$$\lim_{n} \Pr_i[x_n \in E] = \sum_{j \in E} P_{ij}^{(n)} \rightarrow \beta(x).$$

Let us see what our results say for a noncyclic ergodic chain $P$. Such a chain is necessarily normal, and $\alpha$ may be chosen to have total measure one. If this choice is made, then $G(I - P) = 1\alpha - I$ by Corollary 9-51. Comparison with Theorem 11-7 shows that $\alpha = \beta$. Thus the harmonic measure is concentrated entirely on $S$, in contrast with Proposition 11-15. The measure $\beta$ is a generalization to all normal chains of the measure $\alpha$ for noncyclic ergodic chains. Thus our results generalize to all normal chains results known for ergodic chains. For example, the representation

$$G_{ij} = \int_{S \cup B^e} {}^i N(x, j) d\beta(x)$$

is a generalization of the identity $G_{ij} = \sum_k \alpha_k {}^i N_{kj}$, which holds for noncyclic ergodic chains. (Theorem 9-26 gives

$$G_{ij} = {}^i \nu_j = \lim \sum P_{mk}^{(n)} {}^i N_{kj},$$

and Proposition 1-57 yields $G_{ij} = \sum \alpha_k {}^i N_{kj}$.) As a second example, $(P^n h)_i$ converges to $\alpha h$ for any bounded function $h$ if $P$ is noncyclic ergodic (Lemma 9-52). This result is generalized in Theorem 11-13, but in this

is of totally finite deviation. Dually $f = (I - P)h$ is the deviation of $h$, and $h$ is of totally finite deviation if $\alpha f$ is finite.

Theorem 11-16: If $\nu$ is a non-negative row vector whose deviation $\mu$ is totally finite, then $\mu 1 \leq 0$ and there is a probability measure $\pi$ on $B^e$ such that

$$\nu_j = \nu_0(\alpha_j/\alpha_0) + (\mu^0 N)_j - (\mu 1) \int_{B^e} 0 N(x,j) d\pi(x).$$

If $\mu 1 \neq 0$, then the probability measure $\pi$ is uniquely determined.

Proof: We know that

$$N_{ij} = 0 N_{ij} + \delta_{0j}.$$

If we put $\bar{\mu} = \nu(I - Q)$, we have $\bar{\mu}_i = \mu_i + \nu_0 P_{0i}$ by direct calculation. We therefore get

$$(\bar{\mu} N)_j = (\mu^0 N)_j + (\mu 1) \delta_{0j} + \nu_0^0 \bar{N}_{0j}$$

$$= (\mu^0 N)_j + (\mu 1) \delta_{0j} + \nu_0(\alpha_j/\alpha_0).$$

From Proposition 8-7 applied to the chain $Q$, we see that $\nu = \bar{\mu} N + \rho$, where $\rho$ is regular and non-negative. The calculation of $\bar{\mu} N$ yields

$$\rho_j = \nu_j - (\bar{\mu} N)_j = \begin{cases} -(\mu 1) & \text{if } j = 0 \\ \nu_j - \nu_0(\alpha_j/\alpha_0) - (\mu^0 N)_j & \text{if } j \neq 0. \end{cases}$$

Since $\rho_0 \geq 0, \mu 1 \leq 0$. If $\mu 1 = 0$, then $\rho$ is a $Q$-regular measure $\geq

We define the exit boundary of $P$ to be the entrance boundary of $\hat{P}$. That is, $S^* = *\hat{S}$ and $B_e = \hat{B}^e$. We obtain a dual for Theorem 11-16.

Theorem 11-17: If $h$ is a non-negative column vector whose deviation $f$ is totally finite, then $\alpha f \leq 0$ and there is a probability measure $\pi$ on $B_e$ such that

$$h_i = h_0 + (^0 Nf)_i - \frac{\alpha f}{\alpha_i} \int_{B_e} ^0 \hat{N}(x, i) d\pi(x).$$

If $\alpha f \neq 0$, then the probability measure $\pi$ is uniquely determined.

We turn to results connected with potential theory. We first apply Theorem 11-17 to give elementary continuous functions a characterization which is valid for all recurrent chains, normal or not.

Proposition 11-18: If $h$ is an elementary continuous function, then

(1) $(I - P)h = f$ has finite support.
(2) $h = c1 + ^0 Nf$ for some $c$.
(3) $\alpha f = 0$.
(4) $B^E h = h$ for any set $E$ containing the support of $f$.

Conversely, if (1) and (2) hold, then $h$ is an elementary continuous function.

Proof: $(I - P)B^E$ is equal to $I - P^E$ for states in $E$ and is 0 otherwise. Hence $\alpha[(I - P)B^E] = 0$ and (1) and (3) hold for columns of $B^E$. Since an elementary continuous function is a finite linear combination of such functions for finite sets $E$, (1) and (3) follow. In particular, any column of $B^E$ is of totally finite deviation and Theorem 11-17 applies. The representation in that theorem establishes (2) for columns of $B^E$, and the general result follows by linearity.

We shall complete the proof by showing that (2) implies (4) and that

Proposition 11-19: If $P$ is normal, then a function $h$ of finite deviation is $T$-continuous if and only if $h = c1 + g$ for a $T$-continuous potential $g$. If the representation holds, then

$$c = \int_{*S} h(x)d\beta(x).$$

Proof: If $(I - P)h = f$ and if $h$ is $T$-continuous, then

$$(I + P + \cdots + P^n)f = (I - P^{n+1})h \rightarrow h - c1$$

by Theorem 11-13. If $h$ is of finite deviation, then $f$ is a charge and the limit $h - c1$ is a potential. This potential is $T$-continuous, since 1 is. (Notice that 1 is the 0th column of $B^{(0)}$.) The converse is clear.

Corollary 11-20: If $P$ is normal and if $g$ is a $T$-continuous potential, then

$$\int_{*S} g(x)d\beta(x) = 0.$$

Proof: Potentials are of finite deviation by definition. Applying Proposition 11-19 and using the fact that 1 is not a potential (since its charge would have to be zero), we see that $c = 0$.

Corollary 11-20 is a recurrent analog of the statement for transient boundary theory that potentials tend to zero along almost all paths of the process.

Corollary 11-21: If $P$ is normal and if $h$ is a $T$-continuous function whose deviation $f$ is totally finite, then $\alpha f = 0$ and $h = c1 + 0Nf$.

Proof: By Proposition 11-19, $h$ differs from the potential $g$ of $f$ by a constant. But $g = g_01 + 0Nf$ by Theorem 9-15.

Our final proposition enables us to give an interpretation to $\theta^E$ for certain infinite sets provided we have an interpretation for finite sets.

Proposition 11-22

As an application of Proposition 11-22, suppose $P$ is normal and we choose $\nu_j = G_{0j}$. Then $\theta^E = \lambda^E$ for finite sets containing 0, and $\theta^E$ is thus a limit of $\lambda^E$-measures for any set with $\theta^E = 1$, whether or not $\lambda^E$ exists for the infinite set $E$. The condition that $\theta^E = 1$ means that the transient chain $Q^v$ leaves $E$ with probability one; this condition is exactly the statement that $E$ be an equilibrium set for $Q^v$. For such a set $E$ and for any reference state $i \in E$, we have

$$[G_E(I - P^E)]_i = \theta^E_E - \delta_i.$$

by Proposition 11-3. Since, for two different reference states $i$ in $E$, we have $\theta^E$ as the limit of the same sequence $\lambda^E_k$ (by Proposition 11-22), we may write $G_E(I - P^E) = 1\theta^E_E - I$. Then

$$(\theta^E_E G_E)(I - P^E) = 0$$

and hence $\theta^E_E G_E = k\alpha$ for some constant $k$. If we form the $K$-matrix relative to state 0, then Lemma 9-81 gives

$$G_{ij} = K_{ij} + (G_{i0} - C_{i0})(\alpha_j/\alpha_0).$$

Consequently, $\theta^E_E K_E = k'\alpha$, provided

$$\sum_{i \in E} \theta_i G_{i0} < \infty \quad \text{and} \quad \sum_{i \in E} \theta_i C_{i0} < \infty.$$
