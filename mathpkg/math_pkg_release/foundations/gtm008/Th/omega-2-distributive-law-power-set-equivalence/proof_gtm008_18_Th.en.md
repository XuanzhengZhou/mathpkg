---
role: proof
locale: en
of_concept: omega-2-distributive-law-power-set-equivalence
source_book: gtm008
source_chapter: "18"
source_section: "Model Theoretic Consequences of the Distributive Laws"
---

**Forward direction.** Assume that $B$ satisfies the $(\omega, 2)$-DL. We need only show that $[\mathcal{P}(\check{\omega}) \subseteq \mathcal{P}(\omega)^{\vee}] = 1$ (the reverse inclusion holds by Theorem 18.1). Let $t \in B^{\mathcal{L}(\check{\omega})}$ be such that $[t \subseteq \check{\omega}] = 1$. Define:
$$
b_{n1} = [\check{n} \in t], \qquad b_{n0} = [\check{n} \notin t] \quad \text{for } n \in \omega.
$$
Then $(\forall n \in \omega)[b_{n1} = -b_{n0}]$, and by the $(\omega, 2)$-DL:
$$
1 = \prod_{n < \omega} (b_{n0} + b_{n1}) = \sum_{s \in 2^{\omega}} \prod_{n \in \omega} b_{n, s(n)}.
$$
This proves that $[\mathcal{P}(\check{\omega}) \subseteq \mathcal{P}(\omega)^{\vee}] = 1$, so $[\mathcal{P}(\omega)^{\vee} = \mathcal{P}(\check{\omega})] = 1$.

**Converse direction.** Assume $[\mathcal{P}(\check{\omega}) = \mathcal{P}(\omega)^{\vee}] = 1$, and let $\{b_{ni} \mid n \in \omega \land i \in 2\} \subseteq B$. By Theorem 18.4 we can assume that $(\forall n \in \omega)[b_{n0} = -b_{n1}]$. Define $u \in V^{(B)}$ by:
$$
\mathcal{D}(u) = \mathcal{D}(\check{\omega}) \land (\forall n \in \omega)[u(\check{n}) = b_{n1}].
$$
Then $[u \subseteq \check{\omega}] = 1$, i.e. $[u \in \mathcal{P}(\check{\omega})] = 1$, and by assumption $[u \in \mathcal{P}(\omega)^{\vee}] = 1$. Hence:
$$
1 = [[u \in \mathcal{P}(\omega)^{\vee}]] = \sum_{s \in 2^{\mathcal{D}(\check{\omega})}} [[u = s]]
= \sum_{s \in 2^{\mathcal{D}(\check{\omega})}} \prod_{n \in \omega} ([\check{n} \in u] \iff s(\check{n}))
= \sum_{s \in 2^{\omega}} \prod_{n \in \omega} b_{n, s(n)}.
$$
Since also $1 = \prod_{n \in \omega} (b_{n0} + b_{n1})$, this verifies the $(\omega, 2)$-DL condition.
