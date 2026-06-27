---
role: proof
locale: en
of_concept: theorem-18-2
source_book: gtm008
source_chapter: "18"
source_section: "18 Model Theoretic Consequences of the Distributive Laws

There"
---
Assume that $B$ satisfies the $(\omega, 2)$-DL. We need only show that $[\mathcal{P}(\check{\omega}) \subseteq \mathcal{P}(\omega)^{\vee}] = 1$. Therefore let $t \in B^{\mathcal{L}(\check{\omega})}$ such that $[t \subseteq \check{\omega}] = 1$. Define $b_{n1} = [\check{n} \in t]$, $b_{n0} = [\check{n} \notin t]$ for $n \in \omega$. Then $(\forall n \in \omega)[b_{n1} = -b_{n0}]$,

$$1 = \prod_{n < \omega} (b_{n0} + b_{n1}) = \sum_{s \in 2^{\omega}} \prod_{n \in \omega} b_{n,s(n)} \quad \text

This proves that $[\mathcal{P}(\check{\omega}) \subseteq \mathcal{P}(\omega)^{\vee}] = 1$. Consequently $[\mathcal{P}(\omega)^{\vee} = \mathcal{P}(\check{\omega})] = 1$. To prove the converse, assume that $[\mathcal{P}(\check{\omega}) = \mathcal{P}(\omega)^{\vee}] = 1$, and let

$$\{b_{ni} \mid n \in \omega \wedge i \in 2\} \subseteq B.$$

By Theorem 18.4 (below) we can assume that

$$(\forall n \in \omega)[b_{n0} = -b_{n1}].$$

Define $u \in V^{(B)}$ by

$$\mathcal{D}(u) = \mathcal{D}(\check{\omega}) \wedge (\forall n \in \omega)[u(\check{n}) = b_{n1}].$$

Then

$$[\uparrow u \subseteq \check{\omega}] = 1,$$

i.e.

$$[\uparrow u \in \mathcal{P}(\check{\omega})] = 1$$

and by assumption

$$[\uparrow u \in \mathcal{P}(\omega)^{\vee}] = 1.$$

$$1 = [[u \in \mathcal{P}(\omega)^{\vee}]] = \sum_{s \in 2\mathcal{D}(\check{\omega})} [[u = s]]$$

by 1 above

$$= \sum_{s \in 2\mathcal{D}(\check{\omega})} \prod_{n \in \omega} ([\check{n} \in u] \iff s(\check{n}))$$

$$= \sum_{s \in 2\omega} \prod_{n \in \omega} b_{n,s(n)}.$$

Since also $1 = \prod_{n \in \omega} (b_{n0} + b_{n1})$, this completes the proof.

Remark.

1. In the same way as we proved Theorem 18.2 we can prove the following:

B satisfies the $(\alpha, 2)$-DL if
