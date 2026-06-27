---
role: proof
locale: en
of_concept: lemma-6-36
source_book: gtm040
source_chapter: "6"
source_section: "36"
---

**Proof:** Form the process $P^*$ of Proposition 6-32. We shall first show that for any two states $i$ and $j$ there is a state $k$ which it is possible to reach from both $i$ and $j$; for this purpose it is sufficient to show that from state 0 it is possible to reach all sufficiently large states, since $P^*$ represents sums of independent random variables. Now the set of states which can be reached from

is zero or one and is independent of $\pi$. If

$$\Pr_{\pi}[x_n = s \text{ for infinitely many } n \in E] = 0$$

and

$$\Pr_{\pi}[x_n = s \text{ for infinitely many } n \in F] = 0,$$

then

$$\Pr_{\pi}[x_n = s \text{ infinitely often}] = 0,$$

in contradiction to the recurrence of $P$.

The following lemma uses the notation $\|\beta\| = \sum_i |\beta_i|$.
