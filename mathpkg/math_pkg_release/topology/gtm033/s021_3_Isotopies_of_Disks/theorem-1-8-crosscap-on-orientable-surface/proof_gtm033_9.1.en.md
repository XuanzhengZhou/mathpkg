---
role: proof
locale: en
of_concept: crosscap-on-orientable-surface
source_book: gtm033
source_chapter: "9"
source_section: "1"
---

# Proof of Theorem 1.8 (Crosscap on an Orientable Surface)

Let $M$ be an orientable surface of genus $p$. Attaching a crosscap to $M$ yields a nonorientable surface of genus $2p + 1$.

**Proof.** This is clear if $p = 0$: attaching a crosscap to $S^2$ yields $\mathbb{R}P^2$, a nonorientable surface of genus $1 = 2 \cdot 0 + 1$.

If $p > 0$, consider $M$ as the connected sum of $p$ tori:

$$M \approx T^2 \# T^2 \# \cdots \# T^2 \quad (p \text{ times}).$$

Then $M \# P$ (attaching a crosscap to $M$) is the same as $P$ with $p$ handles attached. By Theorem 1.7, each handle attachment to a nonorientable surface adds $2$ to the genus. Starting from $P$ (genus $1$) and attaching $p$ handles, we obtain a nonorientable surface of genus $1 + 2p = 2p + 1$. $\square$
