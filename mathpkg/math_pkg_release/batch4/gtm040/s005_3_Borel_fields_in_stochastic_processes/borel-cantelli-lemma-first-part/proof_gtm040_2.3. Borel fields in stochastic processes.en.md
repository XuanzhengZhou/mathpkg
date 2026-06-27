---
role: proof
locale: en
of_concept: borel-cantelli-lemma-first-part
source_book: gtm040
source_chapter: "2"
source_section: "3. Borel fields in stochastic processes"
---

Let $q_n$ be the statement that all of $p_n, p_{n+1}, \ldots$ are false. Let $\epsilon > 0$. Choose $N$ large enough so that $\sum_{n=N}^{\infty} \Pr[p_n] < \epsilon$. Then
$$1 - \Pr[q_N] = \Pr[\text{at least one of } p_N, p_{N+1}, \ldots \text{ occurs}] = \Pr[p_N \vee p_{N+1} \vee \cdots].$$
By Proposition 1-18 (countable subadditivity) the right side is
$$\leq \sum_{n=N}^{\infty} \Pr[p_n] < \epsilon.$$
Hence,
$$\Pr[\text{finitely many } p_n \text{ are true}] = \Pr\left[\bigvee_{n=1}^{\infty} q_n\right] \geq \Pr[q_N] > 1 - \epsilon.$$
Since this holds for every $\epsilon > 0$, the probability must be 1.
