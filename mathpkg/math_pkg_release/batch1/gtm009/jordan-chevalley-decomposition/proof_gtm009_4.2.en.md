---
role: proof
locale: en
of_concept: jordan-chevalley-decomposition
source_book: gtm009
source_chapter: "4"
source_section: "4.2"
---

\textbf{Proof.} Let $a_1, \ldots, a_k$ (with multiplicities $m_1, \ldots, m_k$) be the distinct eigenvalues of $x$ on $V$, so the characteristic polynomial is $\prod (T - a_i)^{m_i}$.

Decompose $V$ into generalized eigenspaces: $V = \bigoplus_{i=1}^k V_i$, where $V_i = \text{Ker}(x - a_i \cdot 1)^{m_i}$. Each $V_i$ is stable under $x$, and on $V_i$, the characteristic polynomial of $x$ is $(T - a_i)^{m_i}$.

Apply the Chinese Remainder Theorem (for the ring $F[T]$) to find a polynomial $p(T)$ satisfying:
$$p(T) \equiv a_i \pmod{(T - a_i)^{m_i}}, \quad p(T) \equiv 0 \pmod{T}.$$
(The last congruence is superfluous if 0 is an eigenvalue; otherwise $T$ is relatively prime to the other moduli.)

Set $q(T) = T - p(T)$. Both $p(T)$ and $q(T)$ have zero constant term (since $p(T) \equiv 0 \pmod{T}$).

Define $x_s = p(x)$, $x_n = q(x)$. Since they are polynomials in $x$, they commute with each other and with all endomorphisms commuting with $x$. They also stabilize all subspaces stabilized by $x$, in particular the $V_i$.

The congruence $p(T) \equiv a_i \pmod{(T - a_i)^{m_i}}$ shows that $x_s - a_i \cdot 1$ is zero on $V_i$, hence $x_s$ acts diagonally on $V_i$ with single eigenvalue $a_i$. Since $x_n = x - x_s$, $x_n$ is nilpotent. Because $p(T)$ and $q(T)$ have no constant term, (c) follows.

For uniqueness, let $x = s + n$ be another such decomposition. Then $x_s - s = n - x_n$. All endomorphisms commute. Sums of commuting semisimple (resp. nilpotent) endomorphisms are again semisimple (resp. nilpotent), whereas only 0 can be both semisimple and nilpotent. This forces $s = x_s$, $n = x_n$.
