---
role: proof
locale: en
of_concept: sigma-congruence-mod-8
source_book: gtm007
source_chapter: "V"
source_section: "§1. Preliminaries"
---

Both $\tau \bmod 8$ and $\sigma$ define homomorphisms $K(S) \to \mathbf{Z}/8\mathbf{Z}$. For the generator $I_+$ (rank 1, signature $(1,0)$), we have $\tau(I_+) = 1$ and $\sigma(I_+) = 1$. For $I_-$ (rank 1, signature $(0,1)$), $\tau(I_-) = -1 \equiv 7 \pmod{8}$ and $\sigma(I_-) \equiv -1 \equiv 7 \pmod{8}$. Since both homomorphisms agree on the generators of $K(S)$, they are equal.

For the second statement: if $E$ is type II, then $\sigma(E) = 0$ (since $x \cdot x$ is always even, the element $u$ with $u \cdot u$ odd does not exist, and the invariant is defined to be $0$). Hence $\tau(E) \equiv 0 \pmod{8}$, and consequently $r(E) \equiv 0 \pmod{2}$ and $d(E) = (-1)^{r(E)/2}$.
