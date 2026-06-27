---
role: proof
locale: en
of_concept: lemma-5-11
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. We may restrict our attention to the case where $p \geq 1$. For a fixed $p$ let

$$E_p(z) = 1 + \sum_{k=1}^{\infty} a_k

Hence, for $|z| \leq 1$,

$$|E_p(z) - 1| = \sum_{k=p+1}^{\infty} a_k z^k$$

$$= |z|^{p+1} \sum_{k=p+1}^{\infty} a_k z^{k-p-1}$$

$$\leq |z|^{p+1} \sum_{k=p+1}^{\infty} |a_k|$$

$$= |z|^{p+1}$$

which is the desired inequality.

Before solving the general problem of finding a function with prescribed zeros, the problem for the case where $G = \mathbb{C}$ will be solved. This is done for several reasons. In a later chapter on entire functions the specific information obtained when $G$ is the whole plane is needed. Moreover, the proof of the general case, although similar to the proof for $\mathbb{C}$, tends to obscure the rather simple idea behind the proof.
