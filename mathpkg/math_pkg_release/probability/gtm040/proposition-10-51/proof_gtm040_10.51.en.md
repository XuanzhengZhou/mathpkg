---
role: proof
locale: en
of_concept: proposition-10-51
source_book: gtm040
source_chapter: "10"
source_section: "51"
---

**Proof:** The process watched starting in $E$ is a Markov chain with transition matrix $P$ and starting distribution $\mu^E$ if $E$ is a finite set in $S$. By Proposition 10-21, $z_v$ exists and has the required values for almost every path in this chain, and in this chain

$$\Pr_{\mu^E}[z_v \in C] = \sum_{i \in E} \mu^E_i \Pr_i[z_v \in C]$$

$$= \sum_{i \in E} \mu^E_i \int_C K(i, x) d\mu(x)$$

$$= \int_C \mu^E K(\cdot, x) d\mu(x).$$

As $E$ increases to $S$, we obtain almost all paths of $\{z_n\}$ in this way. Hence $z_v$ exists and is in $S \cup B_e$ a.e., and, by Definition 10-4,

$$\Pr[z_v \in C] = \lim_{E \uparrow S} \int_C \mu^E K(\cdot, y) d\mu(y).$$

By Lemma

Proposition 10-52: On almost every path,

$$z_u(\omega) = \lim_{n \uparrow u} z_n(\omega)$$

exists in $*S$. On almost every path for which the limit exists, either $u > -\infty$ and $z_n \in S$ or else $u = -\infty$ and $z_u \in B^e$. Moreover, for any Borel set $C$ in $*S$,

$$\Pr[z_u \in C] = \int_C p(x) d\mu^\nu(x),$$

where $\mu^\nu$ is the unique measure on $S \cup B^e$ representing $\nu$.

Proof: Form the reverse process and call its measure $\Pr'$. Its transition matrix restricted to the states of $S$ is the $\nu$-dual of $P$, denoted $\hat{P}$. Form the exit and entrance boundaries of $\hat{P}$ relative to $\hat{\pi} = \nu$-dual $f$ and $\hat{f} = \nu$-dual $\pi$. By Proposition 10-51, the limit

$$z_v = \lim_{n \uparrow v} z_n$$

exists in $\hat{S}^*$ a.e. $[\Pr']$, and either $v$ is finite and $z_v \in S$ or else $v$ is infinite and a.e. $z_v \in \hat{B}_e$. Therefore

$$z_u = \lim_{n \uparrow u} z_n$$

exists in $\hat{S}^*$ a.e. $[\Pr]$, and either $u$ is finite and $z_u \in S$ or else $u$ is infinite and a.e. $z_u \in \hat{B}_e$. Since $\hat{S}^*$ and $*S$ are canonically identified according to Lemma 10-49, the first part of the proposition follows. Moreover, we have

$$\Pr[z_u \in C] = \Pr'[z_v \in C] = \int_C \lim_{E \uparrow S} [\mu^E \hat{K}(\cdot, x)] d\mu^\nu(x),$$

where $\mu^\nu$

Conversely, if we select any probability measure $\mu^\sigma$ on $S \cup B^e$, then Theorem 10-48 yields a unique normalized $P$-superregular measure $\sigma$ represented by $\mu^\sigma$. If $\sigma$ is positive, Theorem 10-9 assures the existence of at least one extended chain with $\sigma$ as its vector of mean times. Any such chain starts in $C$ with probability

$$\int_C p(x) d\mu^\sigma(x).$$

By varying $\mu^\sigma$ we may change the total measure on $\{z_n\}$, even as to whether it is finite or infinite.

We consider two special cases. First, if 0 is in $S$, let

$$\sigma_j = J(0, j) = N_{0j}/(Nf)_0.$$

By the uniqueness of the representation we must have $\mu^\sigma(\{0\}) = 1$, and hence we may represent $\sigma$ (provided it is positive) by an extended chain which has a.e. path starting at 0. The total measure of the process must be

$$\int_{*S} p(x) d\mu^\sigma(x) = p(0) \mu^\sigma(\{0\}) = p(0),$$

and so the interpretation of $\sigma_j$ as the mean number of times in state $j$ shows that

$$\sigma_j = p(0) N_{0j}.$$

As a check, we can compute $p(0)$ directly. We have

$$p(0) = \lim_{E \uparrow S} \frac{h_0^E}{(Nf)_0} = \frac{1}{(Nf)_0},$$

as required.

Second, choose $\sigma = J(x, \cdot)$, where $x$ is in $B^e$. Then $\mu^\sigma(\{x\}) = 1$, and (if $\sigma$ is positive) an extended chain representing $\sigma$ in the sense of Theorem 10-9 must start a.e. at $x$ with total measure $p(x)$. Therefore, $J(x, \cdot)$ may be interpreted as the vector of mean times for any extended chain which is started almost surely at $x$, and, if $p

starting state $x$ according to the starting distribution and then weighting it by the conditional mean of the number of times in $j$ given that the process starts at $x$.

As we noted earlier, there is an asymmetry between $p(x)$ and $q^\nu(y)$ in that one of these quantities depends on $\nu$ and the other does not. This asymmetry is cleared up by a discussion of $h$-processes for $P$; we shall see that $p(x)$ depends on $h$ and that $q^\nu(y)$ does not. The special case we have been considering so far will be seen to be the case $h = 1$.

In discussing the entrance boundary for $P^h$, where $h > 0$ is superregular and normalized, we choose

$$f_i^h = f_i/h_i$$

in analogy with the choice of $\pi^h$. Define $\sigma$ by

$$\sigma_i = \nu_i h_i.$$

Then $\sigma$ is positive, is $P^h$-superregular, and satisfies $\sigma f^h = \nu f = 1$. Direct calculation shows that

$$\sigma\text{-dual} (P^h) = \nu\text{-dual} P = \hat{P}$$

and that

$$\sigma\text{-dual} (f^h) = \nu\text{-dual} f = \hat{\pi}.$$

Therefore the entrance boundary for $P^h$ and $f^h$ is the same as that for $P$ and $f$.

Now let $\{z'_n\}$ be an extended chain representing $P^h$ and $\sigma$ (existence by Theorem 10-9), and take $\pi^h$ and $f^h$ as the functions relative to which the exit and entrance boundaries are formed. The process starts in $*S$ and goes to $S^h* = S^*$. To obtain the starting and final distributions, we need the functions $p$ and $q$. For $p$ we have

$$p^h(x) = \lim_{E \uparrow S} \lim_{j \rightarrow x} \frac{(h^E)_j^h}{(N^h f^h)_j}$$
