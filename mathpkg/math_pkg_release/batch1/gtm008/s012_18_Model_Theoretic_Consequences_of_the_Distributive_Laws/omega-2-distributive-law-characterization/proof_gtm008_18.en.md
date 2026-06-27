---
role: proof
locale: en
of_concept: omega-2-distributive-law-characterization
source_book: gtm008
source_chapter: "18"
source_section: "18. Model Theoretic Consequences of the Distributive Laws"
---

**Forward direction.** Assume that $B$ satisfies the $(\omega, 2)$-DL. By Theorem 18.1 we already have $[\mathcal{P}(\omega)^{\vee} \subseteq \mathcal{P}(\check{\omega})] = 1$. We need only show that $[\mathcal{P}(\check{\omega}) \subseteq \mathcal{P}(\omega)^{\vee}] = 1$. Let $t \in B^{\mathcal{L}(\check{\omega})}$ such that $[t \subseteq \check{\omega}] = 1$. Define

$$b_{n1} = [\check{n} \in t], \quad b_{n0} = [\check{n} \notin t] \quad \text{for } n \in \omega.$$

Then $(\forall n \in \omega)[b_{n1} = -b_{n0}]$, and

$$1 = \prod_{n < \omega} (b_{n0} + b_{n1}) = \sum_{s \in 2^{\omega}} \prod_{n \in \omega} b_{n,s(n)}$$

by the $(\omega, 2)$-DL. This proves that $[\mathcal{P}(\check{\omega}) \subseteq \mathcal{P}(\omega)^{\vee}] = 1$. Consequently $[\mathcal{P}(\omega)^{\vee} = \mathcal{P}(\check{\omega})] = 1$.

**Converse direction.** Assume that $[\mathcal{P}(\check{\omega}) = \mathcal{P}(\omega)^{\vee}] = 1$, and let

$$\{b_{ni} \mid n \in \omega \wedge i \in 2\} \subseteq B.$$

By Theorem 18.4 (below) we can assume that

$$(\forall n \in \omega)[b_{n0} = -b_{n1}].$$

Define $u \in V^{(B)}$ by

$$\mathcal{D}(u) = \mathcal{D}(\check{\omega}) \wedge (\forall n \in \omega)[u(\check{n}) = b_{n1}].$$

Then

$$[\uparrow u \subseteq \check{\omega}] = 1,$$

i.e. $[\uparrow u \in \mathcal{P}(\check{\omega})] = 1$, and by assumption

$$[\uparrow u \in \mathcal{P}(\omega)^{\vee}] = 1.$$

Hence

$$1 = [[u \in \mathcal{P}(\omega)^{\vee}]] = \sum_{s \in 2^{\mathcal{D}(\check{\omega})}} [[u = s]]
= \sum_{s \in 2^{\mathcal{D}(\check{\omega})}} \prod_{n \in \omega} ([\check{n} \in u] \iff s(\check{n}))
= \sum_{s \in 2^{\omega}} \prod_{n \in \omega} b_{n,s(n)}.$$

Since also $1 = \prod_{n \in \omega} (b_{n0} + b_{n1})$, this completes the proof.
