---
role: proof
locale: en
of_concept: markov-chain-one-step-conditional-independence
source_book: gtm040
source_chapter: "4"
source_section: "4"
---

Since $r$ is relative to $\mathcal{T}_{n+1} \cap \mathcal{F}$, it can be expressed as a finite disjunction of disjoint elementary statements of the form $x_{n+1} = c_{n+1} \land \cdots \land x_m = c_m$. By Lemma 4-4, it suffices to prove the result for such elementary statements.

**Case 1:** $r$ is of the form $x_{n+1} = c_{n+1}$. Because $q$ is relative to $\mathcal{F}_{n-1}$, it depends only on outcomes $x_0, \ldots, x_{n-1}$. By the definition of a Markov chain, the conditional distribution of $x_{n+1}$ given $x_n = i$ is independent of the history before time $n$, so

$$\Pr_{\pi}[r \mid q \land x_n = i] = \Pr_{\pi}[x_{n+1} = c_{n+1} \mid x_n = i] = \Pr_i[x_1 = c_{n+1}] = \Pr_i[r'].$$

**Case 2:** $r$ is of the form $x_{n+1} = c_{n+1} \land \cdots \land x_m = c_m$, $m > n$. We factor the conditional probability:

$$\Pr_{\pi}[r \mid q \land x_n = i] = \Pr_{\pi}[x_{n+1} = c_{n+1} \mid q \land x_n = i] \times \cdots \times \Pr_{\pi}[x_m = c_m \mid q \land x_n = i \land \cdots \land x_{m-1} = c_{m-1}].$$

The general factor on the right is

$$\Pr_{\pi}[x_{n+k+1} = c_{n+k+1} \mid q \land x_n = i \land \cdots \land x_{n+k} = c_{n+k}].$$

First, suppose that none of these factors is zero. Then we may apply Case 1 with $n + k$ in place of $n$ and $q \land x_n = i \land \cdots \land x_{n+k-1} = c_{n+k-1}$ in place of $q$. The $q$'s drop out of the conditions, and the product of the new conditional probabilities is $\Pr_{\pi}[r \mid x_n = i]$.

Next, suppose that at least one of the factors is zero; let the first such factor from the left be

$$\Pr_{\pi}[x_{n+k+1} = c_{n+k+1} \mid q \land x_n = i \land \cdots \land x_{n+k} = c_{n+k}] = 0.$$

If $k = 0$, then by Case 1 we have $0 = \Pr_{\pi}[x_{n+1} = c_{n+1} \mid x_n = i] = \Pr_i[x_1 = c_{n+1}] = \Pr_i[r']$. If $k > 0$, then by the same reasoning applied inductively, $\Pr_i[r'] = 0$ as well. In either case $\Pr_{\pi}[r \mid x_n = i] = 0 = \Pr_i[r']$, completing the proof.
