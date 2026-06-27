---
role: proof
locale: en
of_concept: theorem-4-9
source_book: gtm040
source_chapter: "4"
source_section: "9"
---

**Proof:** We shall prove the theorem for any statement $r$ measurable with respect to $\mathcal{T

this is so because $r$ is the denumerable union of statements

$$x_t = c_t \wedge \cdots \wedge x_{t+N} = c_{t+N},$$

and we may take $\hat{r}$ to be the same union over the statements

$$x_n = c_t \wedge \cdots \wedge x_{n+N} = c_{t+N}.$$

In this notation the statement $r'$ is the union of the statements

$$x_0 = c_t \wedge \cdots \wedge x_N = c_{t+N},$$

and we have that $\omega$ is in the truth set of $\hat{r}$ if and only if $\omega_n$ is in the truth set of $r'$. Hence

$$\Pr_{\pi}[r \mid q \wedge x_n = i \wedge t = n] = \Pr_{\pi}[r \wedge t = n \mid q \wedge x_n = i \wedge t = n]$$

$$= \Pr_{\pi}[\hat{r} \wedge t = n \mid q \wedge x_n = i \wedge t = n]$$

$$= \Pr_{\pi}[\hat{r} \mid (q \wedge t = n) \wedge x_n = i]$$

$$= \Pr_{\pi}[\hat{r} \mid x_n = i]$$

$$= \Pr_i[r']$$

the last two equalities following from Lemma 4-7.

An equivalent way of stating the first equality of the conclusion of the preceding theorem is

$$\Pr_{\pi}[q \wedge r \mid x_t = i] = \Pr_{\pi}[q \mid x_t = i] \Pr_{\pi}[r \mid x_t = i].$$

This is the form in which the theorem asserts that if the present is known, then the past and future are independent.

5. Systems theorems for Markov chains

As immediate consequences of the strong Markov property, we can prove two systems theorems for Markov chains. The first states that if $p$ is a statement depending on outcomes only beyond some random time $t$, then one may compute $\Pr_{\pi}[p]$ as if the chain were started with

PROOF: By (1) we have

$$\Pr_{\pi}[p] = \sum_{k} \Pr_{\pi}[\omega \in P \land x_t = k]$$

$$= \sum_{k} \Pr_{\pi}[\omega_t \in P' \land x_t = k]$$

$$= \sum_{k} \Pr_{\pi}[x_t = k] \Pr_{\pi}[\omega_t \in P' \mid x_t = k]$$

$$= \sum_{k} \Pr_{\pi}[x_t = k] \Pr_k[p']$$ by Theorem 4-9.

Theorem 4-10, which is a result about probabilities of statements, can also be thought of as a result about means of characteristic functions. Then Theorem 4-11 to follow becomes a straightforward generalization to arbitrary functions.

Theorem 4-11: Let $\{x_n\}$ be a Markov chain, and let $f$ be a random variable satisfying

(1) $$\Pr_{\pi}[f \neq 0 \land t = \infty] = 0,$$ and

(2) there exists a random variable $f'$ such that if $t(\omega) < \infty$, then $f(\omega) = f'(\omega_t)$.

Then

$$M_{\pi}[f] = \sum_{k} \Pr_{\pi}[x_t = k] M_k[f'].$$

PROOF: If $f$ assumes negative values, we may prove the result for $f^+$ and $f^-$ separately. We therefore assume $f \geq 0$. Let $p_{j^{(m)}}$ be the statement $j/2^m \leq f < (j+1)/2^m$, for $1 \leq j < m \cdot 2^m$, let $p_{0^{(m)}}$ be the statement $0 < f < 1/2^m$, and let $p_{m2^{(m)}}$ be the statement $m \leq f$. Define statements $p_{j^{(m)}}'$ similarly for $f'$. Then $p_{j^{(m)}}$ and $p_{j^{(m)}}'$ satisfy the hypotheses of Theorem 4-10, so that
