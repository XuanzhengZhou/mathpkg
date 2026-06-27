---
role: proof
locale: en
of_concept: frobenius-group-order-2n-properties
source_book: gtm006
source_chapter: "XIV"
source_section: "2, 8 (Appendix)"
---
**Proof of Result 14.2.** Let $\Lambda$ be a Frobenius permutation group of order $2n$ on a set $\mathcal{S}$ of $n$ points, where $n$ is odd.

**(i)** Let $a, b$ be distinct points of $\mathcal{S}$. Define $\alpha_a$ as an element of order $2$ in $\Lambda$. Since $\Lambda$ is a Frobenius group, any non-identity element fixes at most one point. Thus $\alpha_a$ fixes exactly one point. By analyzing the action, the orbit structure implies that the point interchanged with $a$ by $\alpha_a$ has $n - 1$ distinct images $a^{\alpha_a c}$ as $c$ varies over $\mathcal{S} \setminus \{a\}$. One of these must be $b$, which proves (i).

**(ii)** Let $\alpha_a$ be an element of order $2$ in $\Lambda'$, let $\mathcal{T}$ be the orbit of $\Lambda'$ containing $a$, and let $|\mathcal{T}| = t$. Since $\alpha_a$ fixes only one point of $\mathcal{T}$, $t$ is odd. Furthermore, since $\Lambda' \subseteq \Lambda_a$ and $|\Lambda_a| = 2 \geq |\Lambda'|$, the order of $\Lambda'$ is $2t$. Since $\Lambda'$ is a subgroup of the Frobenius group $\Lambda$, only the identity of $\Lambda'$ fixes $2$ points of $\mathcal{T}$, so $\Lambda'$ is a Frobenius group on $\mathcal{T}$.

The argument used at the beginning of the proof establishes a one-to-one correspondence between the elements of order $2$ in $\Lambda'$ and the points of $\mathcal{T}$. Thus $r = t$ and $|\Lambda'| = 2t = 2r$. $\square$
