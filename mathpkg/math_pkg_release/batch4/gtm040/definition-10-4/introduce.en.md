---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Let $E$ be a subset of $S$ and define

$$y_n(\omega) = x_{(n+u_E(\omega))}(\omega)$$

for all $n \geq 0$ and for all $\omega$ such that $u_E(\omega) > -\infty$. Let $\bar{\Omega}$ be the ordinary sequence space with state space $S \cup \{b\}$ with the measure of each

Definition 10-5: An extended stochastic process $\{x_n\}$ is an extended chain with transition matrix $P$ if the following conditions hold for each finite subset $E$ of $S$:

(1) The domain of $u_E$ has positive measure.

(2) $\Pr[u_E = -\infty] = 0$.

(3) The process watched starting in $E$ is a Markov chain with transition matrix $P$ and finite starting measure (but not necessarily a probability measure).

(4) For all $j \in S$, $\nu_j < \infty$.

Note that the transition matrix $P$ of an extended chain necessarily satisfies $P1 = 1$. The state space of $P$ never needs to be any bigger than $S \cup \{b\}$, but as we shall see shortly it must contain $S$. If $b$ is in the state space, it clearly must be an absorbing state.

From the definition of the process watched starting in $E$, we see that the total starting measure for the process is equal to the measure of the set of paths on which there is a first entry to $E$. That is, it is the measure of the set where $u_E > -\infty$. By conditions (1) and (2), this measure is positive. Hence the process watched starting in $E$ has a starting measure which is not identically zero.

Applying this observation to the one-point set $\{j\}$, we see that $j$ must be included in the state space of $P$.

Let $\{x_n\}$ be an extended stochastic process satisfying (1), (2), and (3). We shall derive as Proposition 10-6 a necessary and sufficient condition for (4) to hold. Let $E$ be a finite set of $S$. We introduce the abbreviations

$$\mu_i^{E,m} = \Pr[u_E = m \wedge x_m = i]$$

and

$$\mu^E = \sum_m \mu^{E,m}.$$

Then $\mu^E$ is the starting measure of the process watched starting in $E$ and is a finite measure with support in $E$ by (3). Our remarks above showed that $\mu^E$ is not identically zero.

Since the process watched starting in $E$ is a Markov

Proposition 10-6: Let $\{x_n\}$ be an extended stochastic process satisfying conditions (1), (2), and (3) for an extended chain. Then for $j \in E$,

$$\nu_j = (\mu^E N)_j.$$

Moreover, the process is an extended chain if and only if $P$ is the transition matrix of a transient chain whose transient states are $S$ and which may have $b$ as an absorbing state.
