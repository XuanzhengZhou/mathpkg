---
role: proof
locale: en
of_concept: lemma-4-6
source_book: gtm040
source_chapter: "4"
source_section: "6"
---

Proof: Write

$$q = \bigvee_m (x_0 = c_0^{(m)} \wedge \cdots \wedge x_{n-1} = c_{n-1}^{(m)} \wedge x_n = c_n^{(m)}).$$

If we set $q^* = \bigvee_m (x_0 = c_0^{(m)} \wedge \cdots \wedge x_{n-1} = c_{n-1}^{(m)})$, where the disjunction is taken over just those $m$ such that $c_n^{(m)} = i$, then

$$(q^* \wedge x_n = i) \equiv (q \wedge x_n = i)$$

and $q^*$ is a statement relative to $\mathcal{F}_{n-1}$. In the special case where $r$ is relative to $\mathcal{T}_n \cap \mathcal{F}$, we may write

$$r = \bigvee_m (x_n = c_n^{(m)} \wedge \cdots \wedge x_N = c_N^{(m)}) \quad (N \text{ fixed})$$

and

$$r^* = \bigvee_m (x_{n+1} = c_{n-1} \wedge \cdots \wedge x_N = c_N^{(m)})$$

with the second disjunction taken over only those $m$ such that $c_n^{(m)} = i$. Then

$$\Pr_\pi[r \mid q \wedge x_n = i] = \Pr_\pi[r^* \mid q^* \wedge x_n = i],$$

$$

$t(\omega) = n$. We do not define $\omega_t$ if $t(\omega) = \infty$. Similarly the outcome function $x_t$ is defined to be $x_n(\omega)$ if $t(\omega) = n$, and it is not defined for $t(\omega) = \infty$.
