---
role: proof
locale: en
of_concept: proposition-10-8
source_book: gtm040
source_chapter: "10"
source_section: "8"
---

**Proof:** We have

$$\nu^E P_S = \mu^E N P_S = \mu^E (N - I) = \nu^E - \mu^E.$$

Along any increasing sequence of sets $E_n$ with union $S$, $\nu^E$ increases to $\nu$. Hence by monotone convergence

$$\nu P_S = \nu - \lim_n \mu^{E_n}.$$

This equality implies that

$$\nu P_S = \nu - \lim_{E \uparrow S} \mu^E$$

and proves (1) and (2). To prove (3) we need only

non-negative finite-valued measure defined on the transient states and superregular for the restriction of $P^*$ to the transient states. Let $S$ be the support of $\nu$, and suppose $S$ has at least two elements. Then there is an extended chain $\{x_n\}$ having $P^*_{S \cup \{b\}}$ as transition matrix and having $\nu$ as its vector of mean times in the states of $S$. Furthermore, if

$$\nu_S = \mu N + \rho$$

is the unique decomposition of $\nu_S$ with $\rho$ regular for $P^*_S$, then $\mu N$ is contributed by the paths $\omega$ with $\mathbf{u}(\omega) > -\infty$ and $\rho$ is contributed by the paths with $\mathbf{u}(\omega) = -\infty$.

To conclude this section we shall define what we mean by the reverse of an extended stochastic process, and we shall prove that the reverse of an extended chain is an extended chain. The transition matrix of the reverse, at least when restricted to $S$, will turn out to be the $\nu$-dual of the transition matrix, restricted to $S$, of the original process. We need the following lemma, whose proof uses the calculation preceding Proposition 10-6.
