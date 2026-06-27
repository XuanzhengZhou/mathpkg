---
role: proof
locale: en
of_concept: schwarz-inequality-for-cc
source_book: gtm012
source_chapter: "4. Hilbert Spaces and Fourier Series"
source_section: "§1. An inner product in ℂ, and the space L²"
---

# Proof of Schwarz inequality for the space of continuous periodic functions

**Lemma 1.1.** If $u, v \in \mathcal{C}$, then

$$|(u, v)| \leq \|u\| \|v\|.$$

*Proof.* If $v = 0$ then

$$(u, v) = (u, 0v) = 0(u, v) = 0,$$

and the inequality is true. Suppose $v \neq 0$. Note that for any complex number $a$,

$$0 \leq (u - av, u - av) = (u, u) - (av, u) - (u, av) + (av, av)$$

$$= \|u\|^2 - a(v, u) - a^*(u, v) + |a|^2 \|v\|^2$$

$$= \|u\|^2 - a(u, v)^* - a^*(u, v) + |a|^2 \|v\|^2,$$

using the property $(v, u) = (u, v)^*$. Now take

$$a = \frac{(u, v)}{\|v\|^2}.$$

Then $a^* = (u, v)^* / \|v\|^2$, and $|a|^2 = |(u, v)|^2 / \|v\|^4$. Substituting,

$$0 \leq \|u\|^2 - \frac{(u, v)(u, v)^*}{\|v\|^2} - \frac{(u, v)^*(u, v)}{\|v\|^2} + \frac{|(u, v)|^2}{\|v\|^4} \|v\|^2$$

$$= \|u\|^2 - \frac{2|(u, v)|^2}{\|v\|^2} + \frac{|(u, v)|^2}{\|v\|^2}$$

$$= \|u\|^2 - \frac{|(u, v)|^2}{\|v\|^2}.$$

Therefore $|(u, v)|^2 \leq \|u\|^2 \|v\|^2$, and taking square roots gives $|(u, v)| \leq \|u\| \|v\|$. ∎
