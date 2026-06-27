---
role: proof
locale: en
of_concept: proposition-11-3
source_book: gtm040
source_chapter: "11"
source_section: "3"
---

**Proof:** Using as a set of alternatives the time when the $Q^\nu$-process is last in $E$, we have for, $j \in E$,

$$\theta^E_j = \sum_{n=0}^{\infty} (Q^\nu)_{0j}^{(n)} \Pr_j^\nu[\text{process leaves } E \text{ immediately and never returns}]$$

$$= N^v_{0j} \left[ 1 - \sum_{k \in E} \left( Q^v_{jk} + \sum_{c,d \in E} Q^v_{jc} E N^v_{cd} Q^v_{dk} \right) \right].$$

Now $N^v_{0j} = \nu_j + \delta_{0j}$, and therefore

$$N^v_{0j} Q^v_{jk} = \nu_k P_{kj}$$

and

$$N^v_{0j} Q^v_{jc} E N^v_{cd} Q^v_{dk} = \nu_k P_{kd} E N^v_{dc} P_{cj}.$$

for all states, not just those in $S^\nu \cup \{0\}$. Substitution and use of Lemma 6-6 give

$$\theta^E_j = \nu_j + \delta_{0j} - \sum_{k \in E} \nu_k P^E_{kj}.$$

In general, $\theta^E$ has total measure less than one, since the $Q^\nu$ process either may fail to reach $E$ or may return to it infinitely often. If $E$ is finite and $0 \in E$, neither of these alternatives has positive probability and thus $\theta^

Proposition 11-5: If $\nu$ satisfies (1), (2), and (3) and if $\{E_k\}$ is an increasing sequence of finite sets of states with union $S$, then the measures $\theta^{E_k}$ converge to $\beta^\nu$ weak-star on $*S$.

3. Harmonic measure for normal chains

We come now to the first convergence theorem. We shall prove that if $P$ is a normal chain, then the measures $\lambda^E$ converge weak-star to a measure $\beta$ which will play the role of an entrance distribution for $P$. This result agrees with the statement in Section 1.

Lemma 11-6: If $P$ is normal, then the row vector $\nu = G_0$. satisfies conditions (1), (2), and (3). Also, for any finite set $E$ containing 0,

$$\nu_E(I - P^E) = \lambda^E_E - \delta_0.$$

Proof: We know that $G_{0j} \geq 0$ and $G_{00} = 0$. Hence (1) and (2) hold. Condition (3) follows by multiplying the definition of $G_0$. through on the right by $P$ and applying Fatou's Theorem.

Form the $K$-matrix of Definition 9-80 with respect to the distinguished state 0. By Lemma 9-81, $K_{0j} = G_{0j}$. Hence the formula for $\nu_E(I - P^E)$ is the 0th row of the formula of Corollary 9-86.

Harmonic measure $\beta$ for a normal chain $P$ is defined to be the measure $\beta = \beta^\nu$ of Proposition 11-2 for $\nu = G_0$. The justification for a name independent of 0 is contained in the following theorem.

Theorem 11-7: If $\{E_k\}$ is an increasing sequence of finite sets with union $S$, then the measures $\lambda^{E_k}$ converge weak-star to $\beta$ on $*S$. The measure $\beta$ is independent of the distinguished state 0. Also
