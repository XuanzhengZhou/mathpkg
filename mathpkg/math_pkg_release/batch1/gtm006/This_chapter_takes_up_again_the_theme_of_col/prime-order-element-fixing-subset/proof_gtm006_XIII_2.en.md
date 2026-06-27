---
role: proof
locale: en
of_concept: prime-order-element-fixing-subset
source_book: gtm006
source_chapter: "XIII"
source_section: "2"
---

Let $t_1, t_2$ be any two distinct elements of $\mathcal{T}$ and suppose that $t_1$ and $t_2$ lie in different orbits of $\Gamma$. Let $\gamma_i \in \Gamma$, $(i = 1, 2)$, have prime order $p$ and be such that $t_i^{\gamma_i} = t_i$ but $s^{\gamma_i} = s$ for all $s \in \mathcal{S}$, $s \neq t_i$. Then, for any $s \in \mathcal{S}$, $s \neq t_i$, the length of the orbit of $s$ under $\langle \gamma_i \rangle$ is $p$.

Since $\langle \gamma_i \rangle$ is a subgroup of $\Gamma$, any orbit of $\Gamma$ must be a union of orbits of $\langle \gamma_i \rangle$. Putting $i = 1$ we see that, since $t_1$ is the only orbit of length 1 under $\langle \gamma_1 \rangle$ and since $t_2 \neq t_1$, the orbit of $t_2$ under $\Gamma$ is partitioned into disjoint cycles of length $p$ by $\langle \gamma_1 \rangle$, so that:
$$
|t_2^{\Gamma}| \equiv 0 \pmod{p}
$$
whereas:
$$
|t_1^{\Gamma}| \equiv 1 \pmod{p}
$$
(because $\langle \gamma_1 \rangle$ partitions the points of $t_1^{\Gamma}$ into cycles of length $p$, except for $t_1$ itself which is fixed).

However, the same argument with $i = 2$ gives:
$$
|t_1^{\Gamma}| \equiv 0 \pmod{p}, \qquad |t_2^{\Gamma}| \equiv 1 \pmod{p}.
$$

This is a contradiction. Therefore $t_1$ and $t_2$ must lie in the same orbit of $\Gamma$, so $\mathcal{T}$ is contained in a single orbit of $\Gamma$.
