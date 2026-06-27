---
role: proof
locale: en
of_concept: lemma-10-10
source_book: gtm040
source_chapter: "10"
source_section: "10"
---

**Proof:**

$$\Pr[x_{v_E-2} = i \wedge x_{v_E-1} = j \wedge x_{v_E} = k]$$

$$= \sum_n \Pr[x_n = i \wedge x_{n+1} = j \wedge x_{n+2} = k$$

$$\wedge \{x_n\} \text{ not in } E \text{ after time } (n+

Definition 10-11: Let $\{x_n\}$ be an extended chain defined on $\Omega$ with measure $\mu$. Set

$$\Pr'[\omega \in A] = \Pr[\omega' \in A]$$

for all sets $A$ for which the right side is defined. The extended stochastic process on $\Omega$ defined by the measure $\Pr'$ is called the reverse of the extended chain.

Proposition 10-12: If $\{x_n\}$ is an extended chain with transition matrix $P$, then its reverse is also an extended chain and its transition matrix $\hat{P}$ satisfies

$$\hat{P}_{ji} = \nu_i P_{ij}/\nu_j$$

for all states $i$ and $j$ in $S$.

Proof: From the definition of $\omega'$, we see that

$$\hat{u}_E(\omega) = -v_E(\omega').$$

Hence

$$\Pr'[\omega \in \text{domain } \hat{u}_E] = \Pr[\omega \in \text{domain } v_E] = \Pr[\omega \in \text{domain } u_E] > 0$$

and (1) holds. Since the chain watched starting in $E$ is in the finite set $E$ infinitely often with probability 0 (second half of Proposition 10-6),

$$0 = \Pr[v_E = +\infty] = \Pr'[\hat{u}_E = -\infty].$$

Thus (2) holds.

Next, we show that the reverse process watched starting in $E$ is a Markov chain with transition matrix $\hat{P}$. We shall compute only a typical conditional probability: Let $k \in E$ and first suppose $i \neq b$. Since

$$\Pr'[x_{\hat{u}_E} = k \land x_{\hat{u}_E+1} = j \land x_{\hat{u}_E+2} = i]$$

$$= \Pr[x_{v_E-2} = i \land x_{v_E-1} = j \land x_{v_E} = k]$$

$$= \nu_i P_{ij} P_{jk} e_k^E$$

by Lemma 1

Since we know $b$ is absorbing, we may assume $j \neq b$. Then this probability is

$$\Pr'[x_{\hat{u}_E} = k \land x_{\hat{u}_E + 1} = j] - \Pr'[x_{\hat{u}_E} = k \land x_{\hat{u}_E + 1} = j \land x_{\hat{u}_E + 2} \in S]$$

$$= \nu_j P_{jk} e_k^E - \sum_{i \in S} \nu_i P_{ij} P_{jk} e_k^E.$$

Hence if $\Pr'[x_{\hat{u}_E} = k \land x_{\hat{u}_E + 1} = j] > 0$, then

$$\Pr'[x_{\hat{u}_E + 2} = b \mid x_{\hat{u}_E} = k \land x_{\hat{u}_E + 1} = j] = (\nu_j - \sum_{i \in S} \nu_i P_{ij}) / \nu_j.$$

(Notice this probability is non-negative because $\nu$ is $P_S$-superregular.) Therefore the reverse process watched starting in $E$ is a Markov chain.

The total starting measure is finite for the reverse process watched starting in $E$ because

$$\sum_i \Pr'[x_{\hat{u}_E} = i] = \sum_i \Pr[x_{v_E} = i]$$

$$= \sum_i \nu_i e_i^E \text{ by Lemma 10-10}$$

$$< \infty$$

by (4) for the given process and by the finiteness of the set $E$. Hence (3) holds.

Finally we prove (4) for the reverse process. The same argument as in Proposition 6-12 shows that

$$\hat{N}_{ji} = \nu_i N_{ij} / \nu_j.$$

Hence $P$ is transient and (4) holds by Proposition 10-6.

3. Martin exit boundary

We now define the Martin exit boundary of a transient chain with respect to a given starting distribution. With this boundary we shall be able to

conventions about what to do when $\pi N$ has some zero entries. These conventions we shall discuss at the end of this section, and except when stated otherwise we shall assume that $\pi N$ is everywhere positive. Let $S$ be the state space of $P$.

Since $N_{\pi j} = (\pi N)_j$ has been assumed positive, we may define

$$K(i,j) = N_{ij}/N_{\pi j}.$$

The notation $K(\cdot,j)$ will mean $K(i,j)$ considered as a function of the first variable with $j$ fixed. Then for each $j$, $K(\cdot,j)$ is a non-negative finite-valued superregular function with $\pi K(\cdot,j) = 1$. It is regular everywhere except at $j$, where it is strictly superregular.

For fixed $i$ the function $K(i,\cdot)$ is bounded, since

$$K(i,j) = \frac{N_{ij}}{N_{\pi j}} = \frac{1}{N_{\pi i}} \left( \frac{N_{\pi i} N_{ij}}{N_{\pi j}} \right) = \frac{1}{N_{\pi i}} \hat{N}_{ji} \leq \frac{1}{N_{\pi i}} \hat{N}_{ii} = \frac{N_{ii}}{N_{\pi i}},$$

where carets denote duality with respect to $\pi N$.

The real-valued functions $d_i(j,j')$ defined on $S \times S$ by

$$d_i(j,j') = |K(i,j) - K(i,j')|$$

have the property that $\{K(i,j_n)\}$ is a Cauchy sequence for all $i$ in $S$ if and only if $\lim_{m,n \to \infty} d_i(j_m,j_n) = 0$ for all $i$. According to the bound we just computed for $K(i,j)$, we may lump the functions $d_i$ into the single finite-valued function $d$ defined by

$$d(j,j') = \sum_{i \in S} w_i N_{\pi i} |K(i,j) - K(i,j')|,$$

where the $w_i$ are positive weights such that $\sum w_i N_{

PROOF: If $\{j_n\}$ is Cauchy, then certainly $\{w_i N_{\pi i} K(i, j_n)\}$ is Cauchy. Since $w_i N_{\pi i} > 0$, $\{K(i, j_n)\}$ is Cauchy.

Conversely, let $\{K(i, j_n)\}$ be Cauchy for all $i$, and let $\epsilon > 0$ be given. Choose a finite set of states $E$ such that

$$\sum_{k \in S - E} w_k N_{kk} < \epsilon/2,$$

and choose $M$ sufficiently large that

$$|K(i, j_m) - K(i, j_n)| < \frac{\epsilon}{2 \sum w_k N_{kk}}$$

for $i \in E$ and for all $n, m \geq M$. Then $d(j_m, j_n) < \epsilon$.

We define $S^*$ to be the Cauchy completion of the metric space $(S, d)$, and we let $B = S^* - S$. The set $B$ is the Martin exit boundary for the chain $P$ started with distribution $\pi$.

The set $B$ is not necessarily a boundary in the topological sense, since there are examples in which it is not a closed set in $S^*$, but the abuse of notation will not disturb us.

From Proposition 10-13 we see that $K(i, \cdot)$ is a uniformly continuous function on $S$. Hence it extends uniquely to a continuous function on $S^*$. We shall use the same notation $K(i, \cdot)$ for the function on $S^*$, but will normally denote points of $B = S^* - S$ by $x$ or $y$.

The characterization of Cauchy sequences given in Proposition 10-13 shows that the nature of the space $S^*$ does not depend upon the choice of the weights $w_i$. That is, the Cauchy completions of $S$ corresponding to two different choices of weights are homeomorphic.

Since $K(i, \cdot)$ is continuous on $S^*$, it follows that the extension of $d$ to $S^*$ is simply

$$d(x,

Thus by a diagonal process we may choose a subsequence $\{x_{n_k}\}$ such that $\{K(i, x_{n_k})\}$ is Cauchy for all $i$. Then $\{x_{n_k}\}$ is Cauchy in $S^*$. Since $S^*$ is complete, $\{x_{n_k}\}$ is convergent.

The sets in the smallest Borel field containing the open sets of $S^*$ are called Borel sets. The boundary $B$ is a Borel set, since it is the complement of a countable set. Finite measures defined on the Borel sets are called Borel measures.

We conclude this section by agreeing on what conventions we shall adopt in case $\pi N$ has some zero entries. If $S$ is the set of all states, let

$$W = \{i \in S \mid (\pi N)_i > 0\}.$$

The special nature of $W$ implies that $P_W = P^W$, and by Lemma 8-18 we see that the fundamental matrix for $P_W$ is $N_W$. Thus if we agree that boundary theory for $P$ and $\pi$ is to be interpreted as boundary theory for $P_W$ and $\pi_W$, we find that for $i$ and $j$ in $W$

$$K(i, j) = N_{ij}/N_{\pi j},$$

and $K(i, j)$ is not defined otherwise. Hence the metric is

$$d(j, j') = \sum_{i \in W} w_i N_{\pi i} |K(i, j) - K(i, j')|$$

for $j$ and $j'$ in $W$. Boundary theory is then done relative to the Cauchy completion of $(W, d)$.

4. Convergence to the boundary

We continue to assume that $P$ is a Markov chain with all states transient and that $\pi$ is a starting distribution with $\pi N > 0$. Let $\bar{P}$ denote the enlarged chain obtained from $P$ by adding the absorbing state $b$.

The main theorem of this section will be that with probability one every path $\omega$ has the property that either $x_n(\omega)$ converges in $

Proof: Form the process watched starting in the finite set $E$. The claim is that for $n \geq 0$, $\{g(x_{u_E} + n)\}$ is a non-negative supermartingale. It satisfies the supermartingale inequality because $g$ is non-negative superregular. Thus, to show that the means are finite, it is sufficient to consider $M[g(x_{u_E})]$. We have

$$M[g(x_{u_E})] = \mu^E g = \mu^E Nf = \nu^E f \leq \nu f < \infty,$$

since $f$ is non-negative and $\nu^E \leq \nu$. Hence $\{g(x_{u_E} + n)\}$ is a non-negative supermartingale.

If $0 \leq r < s$, then Proposition 3-11 applied to $-g$ (or Proposition 8-79) shows that the mean number of downcrossings of $[r, s]$ by $\{g(x_{u_E} + j)\}$ up to time $n$ is bounded by $s/(s - r)$ independently of $n$ and of $E$. Let $n \to \infty$ and then let $E$ increase so that $u_E$ approaches $u$. The mean number of downcrossings of $[r, s]$ remains bounded, and by monotone convergence the mean number of downcrossings after time $u$ is finite. By the argument in the proof of Theorem 3-12, $g(x_n)$ converges a.e. as $n$ decreases to $u$. It can be shown that the limit is finite a.e., but this fact will not be needed.

Lemma 10-17: Let $G$ be a Borel field of subsets of a set $\Omega$, let $S^*$ be a compact metric space, and for each $n$ let $f_n: \Omega \to S^*$ be a function with the property that $f_n^{-1}(E)$ is in $G$ for all Borel sets $E$. If $f_n(\omega) \to f(\omega)$ for all $\omega$, then $f^{-1}(E)$ is in $

PROOF: First we prove the measurability. The set where $x_v$ is defined is the countable union of the sets $\{v = 1\}, \{v = 2\}, \ldots$ and the set $\{v = \infty \wedge x_n(\omega)\}$ converges. All of these except possibly the last are certainly in $\mathcal{G}$. The last set is

$$A = \{\omega \mid v(\omega) = \infty \wedge \lim_{n} \sup_{i} K(i, x_n(\omega)) = \lim_{n} \inf_{i} K(i, x_n(\omega)) \text{ for all } i\}$$

and is therefore in $\mathcal{G}$. Now the intersection of $\{v = n\}$ with the inverse image under $x_v$ of a Borel set $E$ is certainly in $\mathcal{G}$. Therefore to complete the proof of the measurability part of the theorem it is sufficient to prove that the intersection of the set $A$ defined above with $x_v^{-1}(E)$ is in $\mathcal{G}$ for every Borel set $E$. In Lemma 10-17 let $\Omega$ be the set $A$ and let the field be the class of sets $A \cap G$, where $G \in \mathcal{G}$. Since $A \cap x_n^{-1}(E)$ is in the field for all $E$, the lemma applies and gives the result immediately.

Next we are to prove the almost-everywhere statement. Form the extended chain associated with $\pi$ and $P$, as described in Section 2 after Corollary 10-7. All statements about this extended chain after time $n \geq 0$ have the same probabilities as the corresponding statements about $P$, and the vector $\nu$ of mean times in the various states is $\pi N$. It is therefore sufficient to show in the extended chain the convergence of $K(i, x_n)$ for all $i$.

Let $\{\hat{x}_n\}$ be the reverse of this extended chain. Since

$$K(i, j) = \hat{N}_{ji}/N_{\pi i},$$

it suffices to show for each $i$ that in the reverse process $\hat{N}_{x_n

Corollary 10-19: $\Pr_i[x_v \in S^*] = 1$.

Proof: As in the proof of Theorem 10-18, form the extended chain associated with $P$ and $\pi$. By Theorem 10-18 almost every path in the process $P$ (started according to $\pi$) satisfies $x_v \in S^*$. Hence the same is true of the extended chain, and hence it is true of those paths in the extended chain which pass through $i$. On any path $\omega$ which passes through $i$, $x_v(\omega) \in S^*$ if and only if $x_v(\omega_{u_{i}}) \in S^*$. Therefore by Definition 10-4, the extended chain watched starting in $\{i\}$ satisfies

$$\Pr_{\mu^{(i)}}[x_v \in S^*] = \mu_i^{(i)}$$

On the other hand,

$$\Pr_{\mu^{(i)}}[x_v \in S^*] = \mu_i^{(i)} \Pr_i[x_v \in S^*]$$

Since $\mu_i^{(i)} \neq 0$, we must have $\Pr_i[x_v \in S^*] = 1$.

It is to be emphasized that $S^*$ has been constructed for the fixed starting distribution $\pi$ and that Corollary 10-19 is not the same as Theorem 10-18 restated for the case where $\pi$ assigns measure one to the state $i$: The boundaries for different starting distributions may be different.

5. Poisson–Martin Representation Theorem

The notation $P, \pi, K(i, x), S^*, \mathcal{F}$, and $\mathcal{G}$ of Sections 3 and 4 is still in force. We shall use $\Pr$ to mean $\Pr_\pi$.

We recall that $\pi K(\cdot, j) = 1$ for all $j$ in $S$. If $j_n \rightarrow x$ in $S^*$, then $K(\cdot, j_n) \rightarrow K(\cdot, x)$ and, for all $n$, $\pi K(\cdot, j_n) = 1

Proof: It is clearly non-negative and is finite-valued because $K(i, \cdot)$ is bounded. By Fubini's Theorem,

$$\pi h = \sum_{i} \int_{S^*} \pi_i K(i, x) d\nu(x) = \int_{S^*} \left[ \sum_{i} \pi_i K(i, x) \right] d\nu(x) \leq \int_{S^*} d\nu(x) = 1$$

and

$$(Ph)_i = \sum_{j} \int_{S^*} P_{ij} K(j, x) d\nu(x) = \int_{S^*} \left[ \sum_{j} P_{ij} K(j, x) \right] d\nu(x)$$

$$\leq \int_{S^*} K(i, x) d\nu(x) = h_i.$$

Thus Borel measures on $S^*$ give rise to $\pi$-integrable non-negative superregular functions $h$. Our goal in this section will be to prove conversely that every non-negative (finite-valued) superregular function $h$ arises as the integral over $S^*$ of $K(i, x)$ with respect to some measure. We postpone the uniqueness question to Sections 6 and 7.

Throughout the remainder of this chapter we shall use "superregular" to mean "finite-valued superregular."

Harmonic measure $\mu$ is defined on the Borel sets $E$ of $S^*$ by

$$\mu(E) = \Pr[x_v \in E].$$

By Theorem 10-18 the definition of $\mu$ makes sense and $\mu(S^*) = 1$. The complete additivity of $\mu$ is a consequence of the complete additivity of Pr. Thus $\mu$ is a Borel measure. The proposition to follow gives a formula for $\Pr[i[x_v \in E]]$ in terms of harmonic measure.

Proposition 10-21: For every Borel set $E$ of $S^*$,

$$\Pr[i[x_v \in E] = \int_E K(i, x) d\mu(x).$$

Proof: Let $E

For Borel sets $E$ of $S^*$ define measures by

$$\mu_{in}(E) = \Pr_i[x_{v_n} \in E],$$
$$\mu_i(E) = \Pr_i[x_v \in E],$$
$$\mu_{\pi n}(E) = \Pr_\pi[x_{v_n} \in E],$$

and

$$\mu_\pi(E) = \Pr_\pi[x_v \in E] = \mu(E).$$

What we have just shown is that

$$\mu_{in}(E) = \int_E K(i, x) d\mu_{\pi n}(x).$$

Now if $f \geq 0$ is a Borel measurable function on $S^*$, the claim is that

$$\int_{S^*} f(x) d\mu_{in}(x) = \int_\Omega f(x_{v_n}(\omega)) d\Pr_i(\omega).$$

The result for characteristic functions is just the definition of $\mu_{in}$, and for general $f \geq 0$ it follows from the result for simple functions by monotone convergence. Then the result holds for continuous $f \geq 0$ and hence for all continuous $f$. Similarly for continuous $f$,

$$\int_{S^*} f(x) d\mu_i(x) = \int_\Omega f(x_v(\omega)) d\Pr_i(\omega),$$

where we set $x_v(\omega) = 0$ when $v$ is not defined.

As $n \to \infty$, $x_{v_n}(\omega) \to x_v(\omega)$ a.e. $[\Pr_i]$ by Corollary 10-19. When $f$ is continuous, $f(x_{v_n}(\omega)) \to f(x_v(\omega))$ a.e. $[\Pr_i]$. Since continuous functions are bounded, we have

$$\lim_n \int_\Omega f(x_{v_n}(\omega)) d\Pr_i(\omega) = \int_\Omega f(x_v(\omega)) d\Pr_i(\omega)$$

by dominated convergence. Hence

$$\lim_n \int_{S^*} f(x) d\mu_{in}(x) = \int_{S^*} f

for all continuous $f$. Therefore

$$\mu_i(E) = \int_E K(i, x) d\mu_\pi(x).$$

Corollary 10-22: $\int_{S^*} K(i, x) d\mu(x) = 1$ for all $i \in S$.

Proof: Since $\Pr_i[x_v \in S^*] = 1$ by Corollary 10-19, the result follows from Proposition 10-21.

The corollary we have just proved is the representation theorem as it applies to the column vector which is identically one. We shall be able to get the general case by applying the corollary to a suitable modification of the $h$-process introduced in Chapter 8. We now re-define the $h$-process in such a way that we allow $h$ to have some entries equal to zero.

Definition 10-23: If $h \geq 0$ is a finite-valued $P$-superregular function such that $\pi h = 1$, then $h$-process is defined to be the Markov chain with state space $S$ and with the measure $\Pr^h$ defined by

$$\Pr^h[x_0 = c \wedge x_1 = d \wedge x_2 = e \wedge \dots \wedge x_{n-1} = i \wedge x_n = j]$$

$$= \pi_c P_{cd} P_{de} \dots P_{ij} h_j.$$

We readily check that the $h$-process is indeed a Markov chain. If we define $S^h$ by

$$S^h = \{i \in S \mid h_i > 0\},$$

then the transition matrix $P^h$ of the $h$-process satisfies

$$P_{ij}^h = \begin{cases} \frac{P_{ij} h_j}{h_i} & \text{for } i \text{ and } j \text{ in } S^h, \\ 0 & \text{for } i \in S^h \text{ and } j \in S - S^h \end{cases}$$

and the starting vector $\pi^h$ satisfies

$$\pi_i^h = \

Lemma 10-24: If $h \geq 0$ is a $P$-superregular function and if $h_i = 0$ and $h_j > 0$, then $N_{ij} = 0$. If, in addition, $\pi h = 1$, then $(\pi^h N^h)_j = h_j(\pi N)_j$, and $(\pi^h N^h)_j > 0$ if and only if $j$ is in $S^h$. For $i$ and $j$ in $S^h$,

$$K^h(i,j) = K(i,j)/h_i.$$

Proof: If $h_i = 0$ and $h_j > 0$, then for every $n$

$$h_i \geq \sum_k P_{ik}^{(n)}h_k \geq P_{ij}^{(n)}h_j$$

and hence $P_{ij}^{(n)} = 0$. Therefore $N_{ij} = \sum_n P_{ij}^{(n)} = 0$. Consequently,

$$(\pi^h N^h)_j = \sum_{i \in S^h} \pi_i h_i \left( \frac{N_{ij} h_j}{h_i} \right) = h_j \sum_{i \in S^h} \pi_i N_{ij} = h_j \sum_{i \in S^h} \pi_i N_{ij} = h_j(\pi N)_j.$$

By assumption $\pi$ is a vector such that $\pi N$ is strictly positive. Therefore $(\pi^h N^h)_j = 0$ if and only if $h_j = 0$.

Finally, according to the convention at the end of Section 3 and the calculation just completed, $K^h(i,j)$ is defined if $i$ and $j$ are in $S^h$. We have

$$K^h(i,j) = N_{ij}^h / (\pi^h N^h)_j = \frac{N_{ij} h_j/h_i}{h_j(\pi N)_j} = K(i,j)/h_i.$$

Since the $h$-process has the property that $(\pi^h N^h)_j$ is positive exactly when $j

It follows from Lemma 10-25 that $S^h$ can be canonically identified with a compact subset of $S^*$. Thus by continuity, $K^h(i, x) = K(i, x)/h_i$ for all $i$ in $S^h$ and $x$ in $S^h^*$. Harmonic measure for the $h$-process will be denoted $\mu^h$. We can consider it to be defined on $S^*$ (as well as on $S^h^*$) if we set

$$\mu^h(E) = \mu^h(E \cap S^h^*)$$

for Borel sets $E$ in $S^*$.

We are finally in a position to state and prove the existence half of the Markov chain analog of the Poisson–Martin Representation Theorem.

Theorem 10-26: If $h \geq 0$ is a finite-valued $P$-superregular function such that $\pi h = 1$, then

$$h_i = \int_{S^*} K(i, x) d\mu^h(x).$$

Proof: Applying Corollary 10-22 to the $h$-process, we have

$$\int_{S^h^*} K^h(i, x) d\mu^h(x) = 1$$

for $i$ in $S^h$. That is, for $i$ in $S^h$

$$h_i = \int_{S^h^*} K(i, x) d\mu^h(x) = \int_{S^*} K(i, x) d\mu^h(x).$$

Now if $i \in S - S^h$, $N_{ij} = 0$ for all $j \in S^h$ by Lemma 10-24. Thus $K(i, j) = 0$ for such $i$ and $j$. Since $K(i, x)$ is continuous on $S^h^*$, $K(i, x) = 0$ for $i \in S - S^h$ and $x \in S^h^*$. Therefore for such $i$,

$$h_i = 0 = \int_{S^

is to define the set $B_e$ of extreme points of the boundary and the subset $\bar{S} = S \cup B_e$ of $S^*$. In Section 7 we shall see that $\mu^h$ has all its mass on $\bar{S}$ and that $\mu^h$ is the unique measure with all its mass on $\bar{S}$ for which the representation in Theorem 10-26 holds.

There are three kinds of behavior of points of the boundary that we shall want to exclude:

(1) $x$ has the property that $\pi K(\cdot, x) < 1$.
(2) $x$ has the property that $K(\cdot, x)$ is not regular.
(3) $x$ has the property that $K(\cdot, x)$ is regular but is a nontrivial convex combination of other non-negative regular functions.

The first two of these possibilities are the topic of the two lemmas to follow. The third possibility will require more of our attention, and we discuss it beginning with Definition 10-29 and Lemma 10-30.

We recall that $\pi K(\cdot, x) \leq 1$ for all $x$ in $S^*$.
