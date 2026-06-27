---
role: proof
locale: en
of_concept: existence-of-extended-chain
source_book: gtm040
source_chapter: "10"
source_section: "11"
---

**Proof of Theorem 10-9.**

**(1) Construction of the extended stochastic process.** Let

$$\bar{P} = P^*_{S \cup \{b\}} \quad \text{and} \quad P = \bar{P}_S.$$

Redefine $\nu$ as being restricted to the domain $S$. Let $\nu^E$ be the balayage potential of $\nu$ on a finite set $E$ with $\mu^E$ the balayage charge. For each $E$ we shall consider a Markov chain with transition matrix $P$ and starting distribution $\mu^E$, and we shall combine these into a single extended stochastic process by choosing a common time scale. For the sake of convenience we assume that $S = \{0, 1, \ldots\}$. Our measure is then defined on the space of bilateral sequences with state space $S \cup \{a\} \cup \{b\}$, where the states $a$ and $b$ are absorbing and the measure of the single path $(b, b, b, \ldots)$ is zero. (Then $s$ and $t$ are defined everywhere except on the one path $(b, b, b, \ldots)$.)

There are two kinds of probability assignments to be made on the basic cylinder sets. First, if $i \in S$, define

$$\Pr[x_n = i \land x_{n+1} = j \land \cdots \land x_{n+m} = k]$$

$$= \Pr_{\mu^E}[y_{t+n} = i \land y_{t+n+1} = j \land \cdots \land y_{t+n+m} = k],$$

where $E = \{i\}$ and where the right side is taken as $0$ for the set of $\omega$ on which $t(\omega) + n < 0$. Second, define

$$\Pr[x_{-n-r} = a \land \cdots \land x_{-n-2} = a \land x_{-n-1} = a$$

$$\land x_{-n} = i \land x_{-n+1} = j \land \cdots \land x_{-n+m} = k]$$

$$= \mu_i \Pr_i[y_1 = j \land \cdots \land y_m = k \land t = n].$$

The effect of these definitions is to fix a time scale with this property: For each path there is a designated state such that the first entry into that state occurs at time $0$. Then for $i \in S$, $\Pr[x_n = i]$ is finite for all $n$. To show that $\{x_n\}$ is an extended stochastic process, we must check that the above definitions on cylinder sets are consistent. That is, we must show typically that

$$\sum_k \Pr[x_n = i \land x_{n+1} = j \land x_{n+2} = k] = \Pr[x_n = i \land x_{n+1} = j],$$

when $i$ and $j$ do not both equal $a$, and that

$$(*) \quad \sum_i \Pr[x_{-n-1} = i \land x_{-n} = j \land x_{-n+1} = k] = \Pr[x_{-n} = j \land x_{-n+1} = k].$$

Now $\mu^F B^E = \mu^E$, since $\mu^F$ and $\mu^E$ are balayage charges (see Section 2). Therefore

$$\Pr_{\mu^F}[q] = \sum_{m \in E} (\mu^E)_m \Pr_m[q] = \Pr_{\mu^E}[q].$$

It follows that

$$\Pr_{\mu^E}[q] = \lim_{F \uparrow S} \Pr_{\mu^F}[q],$$

which is the first of the two alternate identities we need.

Next, we note that $\nu(I - P) = \mu$ by Theorem 5-10. Hence $\mu_i = \lim_{F \uparrow S} \mu^F_i$ by the property of balayage charges that they converge to the product of the given superregular measure and $I - P$. Thus

$$\Pr[x_{-n-2} = a \land x_{-n-1} = a \land x_{-n} = i \land x_{-n+1} = j \land x_{-n+2} = k]$$

$$= \mu_i \Pr_i[y_1 = j \land y_2 = k \land t = n]$$

$$= \lim_{F} \mu^F_i \Pr_i[y_1 = j \land y_2 = k \land t = n]$$

$$= \lim_{F} \Pr_{\mu^F}[y_0 = i \land y_1 = j \land y_2 = k \land t = n],$$

which is our second alternate identity.

Now we are in a position to prove $(*)$. In the proof we shall use the abbreviation

$$Y = \lim_{F \uparrow S} \sum_{m=1}^{\infty} \sum_{i \in S-F} \Pr_{\mu^F}[y_{m-1} = i \land y_m = j \land y_{m+1} = k \land t = m + n].$$

We begin by using our two alternate identities and by performing a direct calculation. Recall that $i$ cannot equal $a$ in the sum defining $(*)$. Thus we are to prove $Y = 0$. Now

$$0 \leq Y \leq \lim_{F} \sum_{m=1}^{\infty} \sum_{i \in S-F} \Pr_{\mu^F}[y_{m-1} = i \land y_m = j]$$

$$= \lim_{F} \sum_{m=1}^{\infty} \sum_{i \in S-F} (\mu^F P^{m-1})_i P_{ij}$$

$$= \lim_{F} \sum_{i \in F} (\mu^F N)_i P_{ij}$$

$$= \lim_{F} \sum_{i \in F} \nu_i^F P_{ij}$$

$$\leq \lim_{F} \sum_{i \in F} \nu_i P_{ij}.$$

Since $\sum_{i} \nu_i P_{ij}$ is convergent, the right side is zero. Hence $Y = 0$. Therefore $\{x_n\}$ is an extended stochastic process.

**(2) Verification of some of the properties of an extended chain.** We must now check that $\{x_n\}$ satisfies the four properties of an extended chain. First we check (2). Consider the special case in which $E$ is the finite set $\{0, 1, 2, \ldots, i\}$. This set has the property that on any path beginning in a state of $E$ the statement $t \geq n$ implies the statement that there is an $m \geq n$ with $y_m \in E$. Therefore

$$\lim_{n} \Pr[x_{-l} \in E \text{ for some } l \geq n]$$

$$= \lim_{n} \sum_{l=n}^{\infty} \Pr[x_{-l} \in E \land x_{-l+1} \notin E \land \cdots \land x_{-n} \notin E]$$

$$= \lim_{n} \sum_{l=n}^{\infty} \Pr_{\mu^E}[y_{t-l} \in E \land \cdots \land y_{t-n} \notin E]$$

$$= \lim_{n} \Pr_{\mu^E}[y_t \in E \land \cdots \land y_{t+n} \notin E] = 0,$$

since for a Markov chain with finite starting distribution the probability of staying outside a finite set forever tends to $0$. This establishes property (2).

Now suppose for the moment that we have proved (3) in the form that for any finite set $E$ the process watched starting in $E$ is a Markov chain with starting distribution $\mu^E$ and transition matrix $P$, and suppose we have identified the given measure $\nu$ as the vector of mean times in the various states. Then (4) follows, since $\nu$ was assumed finite-valued. To prove (1) that the domain of $u_E$ has positive measure, let $j \in E$. Then

$$0 < \nu_j = \nu_j^E = \sum_{i \in E} \mu_i^E N_{ij}.$$

Hence $\mu_i^E > 0$ for some $i \in E$. But $\mu^E$ is the measure of the set on which $E$ is ever entered for the first time. That is, it is the measure of the set where $u_E > -\infty$. Hence (1) holds.

Thus we are to prove that the process watched starting in the finite set $E$ is a Markov chain with starting distribution $\mu^E$ and transition matrix $\bar{P}$, and we are to identify $\nu$. Suppose we have proved this assertion for all finite sets of the form $E = \{0, 1, 2, \ldots, e\}$, and suppose $F$ is an arbitrary finite set. We show first how the assertion follows for $F$. Choose a set $E$ of the special form containing $F$. Then watching the process beginning in $F$ is the same as watching the process watched starting in $E$ beginning in $F$. Thus since the $E$-process is a Markov chain, so is the $F$-process by Theorem 4-9. The starting distribution for the $F$-process is

$$\Pr_{\mu^E}[y_{t_F} = j] = \sum_{i \in S} \mu_i^E \Pr_i[y_{t_F} = j] = \sum_{i \in S} \mu_i^E B_{ij}^F = \mu_j^F.$$

Hence we may assume that $E$ is a set of the form $E = \{0, 1, \ldots, e\}$. Let $\{z_n\}$ be the outcome of watching $\{x_n\}$ starting in $E$.

**(3) Contribution to $\Pr[z_0 = i \land z_1 = j \land z_2 = k]$ from paths with $u > -\infty$.** For paths with $u > -\infty$, we have $u(\omega) = -m$ for some $m \geq 0$. Then since $i \in E$ we must have $t(\omega) \geq m$. Hence we need sum on $n$ only over $n \geq 0$. If $n \geq 0$, then for any $\omega$ for which $y_0, \ldots, y_{m-1}$ are not in $E$, we have that $t(\omega) = m + n$ if and only if $t(\omega_m) = n$. Therefore we may apply Theorem 4-9 to the relevant probability. The contribution is

$$= \sum_{n \geq 0} \sum_{m \geq 0} \Pr_{\mu}[y_0 \in \tilde{E} \land \cdots \land t = m + n]$$

$$= \sum_{n \geq 0} \sum_{m \geq 0} \Pr_{\mu}[y_0 \in \tilde{E} \land \cdots \land y_{m-1} \in \tilde{E} \land y_m = i]$$

$$\times \Pr_i[y_1 = j \land y_2 = k \land t = n].$$

Let $B^{E,m}$ denote the matrix of probabilities of entry to $E$ at time $m$. The above expression is

$$= \sum_{n \geq 0} \sum_{m \geq 0} (\mu B^{E,m})_i \Pr_i[y_1 = j \land y_2 = k \land t = n]$$

$$= \sum_{n \geq 0} (\mu B^{E})_i \Pr_i[y_1 = j \land y_2 = k \land t = n]$$

$$= (\mu B^{E})_i \Pr_i[y_1 = j \land y_2 = k]$$

$$= (\mu B^{E})_i \bar{P}_{ij} \bar{P}_{jk}.$$

Thus the contribution is $(\mu B^{E})_i \bar{P}_{ij} \bar{P}_{jk}$.

**(4) Contribution to $\Pr[z_0 = i \land z_1 = j \land z_2 = k]$ from paths with $u = -\infty$.** We have $u(\omega) = -\infty$ and $t(\omega) = l + m + n$ for some $l \geq 0$, $m \geq 0$, $n \geq 0$, with

$$y_0(\omega) \in \tilde{G} \land \dots \land y_{l-1}(\omega) \in \tilde{G} \land y_l(\omega) = s$$
$$\land y_{l+1}(\omega) \in \tilde{E} \land \dots \land t(\omega) = l + m + n,$$

where $G = \{0, 1, \dots, i\}$. In the presence of the information

$$y_0(\omega) \in \tilde{G} \land \dots \land y_{l-1}(\omega) \in \tilde{G} \land y_l(\omega) = s,$$

it is true that $t(\omega) = l + m + n$ if and only if $t(\omega_l) = m + n$. Theorem 4-9 now applies. The contribution to the probability therefore is

$$= \sum_n \lim_{m} \sum_{s \in \tilde{E}} \lim_{F} \sum_{l \geq 0} \Pr_{\mu^F}[y_0 \in \tilde{G} \land \dots \land y_{l-1} \in \tilde{G} \land y_l = s]$$
$$\times \Pr_s[y_1 \in \tilde{E} \land \dots \land y_{m+2} = k \land t = m + n].$$

Next, we operate on the second factor. In the presence of the information $y_0(\omega) = s \land y_1(\omega) \in \tilde{E} \land \dots \land y_{m-1}(\omega) \in \tilde{E} \land y_m(\omega) = i$, we know by the special form of $E$ that $t(\omega) = m + n$ if and only if $t(\omega_m) = n$. Hence, by Theorem 4-9, we have

$$\Pr_s[y_1 \in \tilde{E} \land \dots \land y_{m+2} = k \land t = m + n]$$

$$= \Pr_s[y_1 \in \tilde{E} \land \dots \land y_{m-1} \in \tilde{E} \land y_m = i] \cdot \bar{P}_{ij} \bar{P}_{jk}.$$

Since $\nu^F \to \nu$ monotonically and since $\mu_s^F \to \mu_s$, we have

$$\lim_{F} \sum_{l \geq 0} \Pr_{\mu^F}[y_0 \in \tilde{G} \land \cdots \land y_{l-1} \in \tilde{G} \land y_l = s] = \mu_s + (\nu P)_s - (\nu^G P)_s$$

$$= \nu_s - (\nu^G P)_s,$$

since $\nu(I - P) = \mu$. Thus the contribution is

$$= \lim_{m} \sum_{s \in \tilde{E}} (\nu - \nu^G P)_s \Pr_s[y_1 \in \tilde{E} \land \cdots \land y_{m-1} \in \tilde{E} \land y_m = i] \bar{P}_{ij} \bar{P}_{jk}.$$

But

$$\Pr_s[y_1 \in \tilde{E} \land \cdots \land y_{m-1} \in \tilde{E} \land y_m = i] = ({}^E P^{m-1} P)_{si}.$$

If

$$P = \begin{pmatrix} T & U \\ R & Q \end{pmatrix},$$

then ${}^E P = \begin{pmatrix} 0 & 0 \\ 0 & Q \end{pmatrix}$

and

$${}^E P^{m-1} P = \begin{pmatrix} 0 & 0 \\ Q^{m-1} R & Q^m \end{pmatrix}.$$

From this representation of ${}^E P^{m-1} P$, we see that the sum $\sum_{s \in \tilde{E}}$ may now be extended over all of $S$, and the contribution is

$$= \lim_{m} [(\nu - \nu^G P)({}^E P^{m-1} P)]_i \bar{P}_{ij} \bar{P}_{jk}.$$

Now $\nu^G P({}^E P^{m-1}) = \nu_E Q^{m-1} R$ where $\nu_E$ denotes the restriction of $\nu$ to $E$ as a row vector. By monotone convergence,

$$\lim_{m} \nu_E Q^{m-1} R = \nu_E R - (\nu_E U + \mu_E) {}^E N_E R.$$

As we noted in Section 2, the balayage potential $\nu^E$ satisfies

$$\nu^E = (\nu_E \quad \nu_E U {}^E N_E).$$

Hence

$$\lim_{m} \nu_E Q^{m-1} R = (\nu - \nu^E)_{\bar{E}} R - \mu_{\bar{E}}^E N_{\bar{E}} R.$$

If we twice use the fact that $\nu$ and $\nu^E$ agree on $E$, we obtain

$$(\nu - \nu^E)_{\bar{E}} R = [(\nu - \nu^E)P]_E = [(\nu - \mu) - (\nu^E - \mu^E)]_E = \mu_{\bar{E}}^E - \mu_E.$$

Thus

$$\lim_{m} \nu_E Q^{m-1} R = \mu_{\bar{E}}^E - (\mu_E + \mu_{\bar{E}}^E N_{\bar{E}} R) = (\mu^E - \mu B^E)_{\bar{E}}.$$

We conclude that the contribution to $\Pr[z_0 = i \land z_1 = j \land z_2 = k]$ from paths with $u = -\infty$ is

$$= (\mu^E - \mu B^E)_{i} \bar{P}_{ij} \bar{P}_{jk}.$$

**(5) Completion of proof.** From steps (3) and (4), adding the contributions from paths with $u > -\infty$ and $u = -\infty$, we find that

$$\Pr[z_0 = i \land z_1 = j \land z_2 = k] = \mu_i^E \bar{P}_{ij} \bar{P}_{jk} \quad \text{for } i \in E.$$

Hence

$$\Pr[z_2 = k \mid z_0 = i \land z_1 = j] = \bar{P}_{jk}$$

if $\Pr[z_0 = i \land z_1 = j] > 0$. That is, $\{z_n\}$ is a Markov chain with matrix $\bar{P}$ and with starting distribution $\mu^E$, where $\mu^E$ is precisely the balayage charge of $\nu$ on $E$. This verifies property (3) for sets $E$ of the special form $\{0, 1, \ldots, e\}$, and by the reduction argument given in part (2), it holds for all finite $E \subseteq S$.

Since $\nu(I - P) = \mu$, and the starting distribution is $\mu^E$, property (4) follows by the identification of $\nu^E$ as the balayage potential of $\nu$ on $E$ and the convergence $\nu^E \uparrow \nu$ as $E \uparrow S$. The expected number of visits to state $j$ is given by $(\mu^E N)_j = \nu_j^E$, which converges to $\nu_j$ as $E \uparrow S$. This completes the proof of Theorem 10-9.
