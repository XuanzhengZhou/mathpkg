---
role: proof
locale: en
of_concept: sigma-ring-monotone-equivalence
source_book: gtm018
source_chapter: "I"
source_section: "6"
---

(1) A $\sigma$-ring is a monotone class. Let $S$ be a $\sigma$-ring and let $\{E_n\}$ be a monotone sequence of sets in $S$. If $\{E_n\}$ is increasing, then $\lim_n E_n = \bigcup_{n=1}^{\infty} E_n$. Since $S$ is closed under countable unions, $\bigcup_{n=1}^{\infty} E_n \in S$, hence $\lim_n E_n \in S$. If $\{E_n\}$ is decreasing, then $\lim_n E_n = \bigcap_{n=1}^{\infty} E_n$. The identity

$$\bigcap_{n=1}^{\infty} E_n = E_1 - \bigcup_{n=1}^{\infty} (E_1 - E_n)$$

shows that $\lim_n E_n \in S$ since $S$ is closed under differences and countable unions. Therefore $S$ is a monotone class.

(2) A monotone ring is a $\sigma$-ring. Let $M$ be a monotone ring and let $E_i \in M$ for $i = 1, 2, \dots$. Since $M$ is a ring,

$$\bigcup_{i=1}^{n} E_i \in M, \quad n = 1, 2, \dots.$$

The sequence $\{\bigcup_{i=1}^{n} E_i\}_{n=1}^{\infty}$ is increasing, and its union is $\bigcup_{i=1}^{\infty} E_i$. Since $M$ is a monotone class, the limit of this increasing sequence belongs to $M$:

$$\bigcup_{i=1}^{\infty} E_i = \lim_n \bigcup_{i=1}^{n} E_i \in M.$$

Thus $M$ is closed under the formation of countable unions, and since it is already a ring, it is a $\sigma$-ring.
