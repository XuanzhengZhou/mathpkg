---
role: proof
locale: en
of_concept: "pure-state-characterization-via-gns-irreducibility"
source_book: gtm039
source_chapter: "1"
source_section: "1.6"
---
If $f$ is pure and $E \in \pi(A)'$ is a projection with $E \neq 0,1$, then $E\xi \neq 0$ and $E^\perp\xi \neq 0$ (otherwise $\pi(A)\xi$ density fails). Set $t = \|E\xi\|^2 \in (0,1)$. Define $g_1(x) = t^{-1}(\pi(x)E\xi,E\xi)$ and $g_2(x) = (1-t)^{-1}(\pi(x)E^\perp\xi,E^\perp\xi)$. Both are states and $f = tg_1 + (1-t)g_2$, contradicting purity. Conversely, if $\pi$ is irreducible and $f = tg_1 + (1-t)g_2$, then $g_i \leqslant t^{-1}f$, giving vector states by a Radon–Nikodym argument, forcing $g_1 = g_2 = f$. $\square$
