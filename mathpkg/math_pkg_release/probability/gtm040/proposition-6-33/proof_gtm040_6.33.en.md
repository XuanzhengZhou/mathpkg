---
role: proof
locale: en
of_concept: proposition-6-33
source_book: gtm040
source_chapter: "6"
source_section: "33"
---

**Proof:** Let $p'_k = P'_{0k}$ for $k \geq 1$; then $\sum_{k=1}^{\infty} p'_k = 1$. We take $P$ to be a basic example and $s$ to be state 0; the values of $p_i$ and $q_i$ in the basic example are yet to be specified. Define recursively the $q_i$'s by the relations

$$p'_1 = q_1 = \beta_0 - \beta_1$$

and

$$p'_n = p_1 \ldots p_{n-1} q_n = \beta_{n-1} q_n = \beta_{n-1} - \beta_n.$$

In $P$ we have $\Pr[t_1 - t_0 = k] = p'_k$ as required; it remains to be proved that $P$ is recurrent. We have

$$\sum_{k=1}^{n} p'_k = \sum_{k=1}^{n} (\beta_{k-1} - \beta_k) = \beta_0 - \beta_n = 1 - \beta_n,$$

and since $\sum_{k=1}^{\infty} p'_k = 1$, we must have $\lim_n \beta_n = 0$. Hence $P$ is recurrent.

We close this section with two remarks about sums of independent random variables and their relation to recurrence. First, we have seen in Proposition 5

of independent random variables and the second the classical proof using the Renewal Theorem of Section 1-6f. We shall further show that, conversely, the truth of the convergence theorem just when $P$ is the basic example implies the full validity of the Renewal Theorem.

We begin by proving two lemmas needed in both proofs of the convergence theorem; their effect is to formulate noncyclicity in a number-theoretic way.
