---
role: proof
locale: en
of_concept: markov-chain-conditional-independence-from-past
source_book: gtm040
source_chapter: "4"
source_section: "4"
---

Write

$$q = \bigvee_m (x_0 = c_0^{(m)} \land \cdots \land x_{n-1} = c_{n-1}^{(m)} \land x_n = c_n^{(m)}).$$

Set

$$q^* = \bigvee_m (x_0 = c_0^{(m)} \land \cdots \land x_{n-1} = c_{n-1}^{(m)}),$$

where the disjunction is taken over just those $m$ such that $c_n^{(m)} = i$. Then

$$(q^* \land x_n = i) \equiv (q \land x_n = i)$$

and $q^*$ is a statement relative to $\mathcal{F}_{n-1}$.

In the special case where $r$ is relative to $\mathcal{T}_n \cap \mathcal{F}$, we may write

$$r = \bigvee_m (x_n = c_n^{(m)} \land \cdots \land x_N = c_N^{(m)}) \quad (N \text{ fixed})$$

and define

$$r^* = \bigvee_m (x_{n+1} = c_{n+1}^{(m)} \land \cdots \land x_N = c_N^{(m)})$$

with the second disjunction taken over only those $m$ such that $c_n^{(m)} = i$. Then

$$\Pr_\pi[r \mid q \land x_n = i] = \Pr_\pi[r^* \mid q^* \land x_n = i].$$

Now $q^*$ is relative to $\mathcal{F}_{n-1}$ and $r^*$ is relative to $\mathcal{T}_{n+1} \cap \mathcal{F}$, so Lemma 4-6 applies, yielding

$$\Pr_\pi[r^* \mid q^* \land x_n = i] = \Pr_\pi[r^* \mid x_n = i] = \Pr_i[r'].$$

For a general $r$ relative to $\mathcal{T}_n$, the class $\mathcal{T}_n \cap \mathcal{F}$ is a field that generates $\mathcal{T}_n$ as the smallest augmented Borel field containing it. By Theorem 1-19 (uniqueness of extension of a probability measure), a probability measure on $\mathcal{T}_n$ is completely determined by its values on $\mathcal{T}_n \cap \mathcal{F}$. Since the equality holds for all $r \in \mathcal{T}_n \cap \mathcal{F}$, the uniqueness of the extension implies the equality holds for all $r$ relative to $\mathcal{T}_n$.
