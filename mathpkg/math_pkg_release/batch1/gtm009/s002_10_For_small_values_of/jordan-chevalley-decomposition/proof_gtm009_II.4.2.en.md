---
role: proof
locale: en
of_concept: jordan-chevalley-decomposition
source_book: gtm009
source_chapter: "II"
source_section: "4.2"
---
Let $a_1, \ldots, a_k$ be the distinct eigenvalues of $x$ with multiplicities $m_1, \ldots, m_k$. Decompose $V = \bigoplus_{i=1}^k V_i$ where $V_i = \operatorname{Ker}((x - a_i \cdot 1)^{m_i})$ are the generalized eigenspaces. On $V_i$, $x$ has characteristic polynomial $(T - a_i)^{m_i}$.

Apply the Chinese Remainder Theorem for the ring $F[T]$ to find a polynomial $p(T)$ satisfying $p(T) \equiv a_i \pmod{(T - a_i)^{m_i}}$ for all $i$, and $p(T) \equiv 0 \pmod{T}$. Set $q(T) = T - p(T)$. Define $x_s = p(x)$ and $x_n = q(x)$.

Since $x_s$ and $x_n$ are polynomials in $x$, they commute with each other and with every endomorphism commuting with $x$. They also stabilize all subspaces stabilized by $x$. The congruences show that $x_s$ acts as $a_i \cdot 1$ on $V_i$, so $x_s$ is semisimple (diagonal with eigenvalue $a_i$ on each $V_i$). Then $x_n = x - x_s$ is nilpotent because on each $V_i$, $x - a_i \cdot 1$ is nilpotent.

For uniqueness: if $x = s + n$ is another decomposition, then $x_s - s = n - x_n$. All four endomorphisms commute pairwise. A sum of commuting semisimple (resp. nilpotent) endomorphisms is semisimple (resp. nilpotent), while only $0$ can be both. Hence $s = x_s$ and $n = x_n$.
