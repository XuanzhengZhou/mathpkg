---
role: proof
locale: en
of_concept: dirichlets-first-case-impossibility
source_book: gtm050
source_chapter: "3"
source_section: "3.3"
---

Assume for contradiction that $u^5 \pm v^5 = w^5$ where $u, v, w$ are pairwise relatively prime positive integers and $w$ is divisible by $10$. Since $u$ and $v$ are odd (they are relatively prime to the even number $w$), set $u + v = 2p$ and $u - v = 2q$. Then $u = p + q$, $v = p - q$, and

$$u^5 \pm v^5 = (p + q)^5 \pm (p - q)^5.$$

Expanding and simplifying leads to an expression of the form $P^2 - 5Q^2$ being a fifth power, where $P$ and $Q$ are derived from $p$ and $q$.

The basic idea is to write $P^2 - 5Q^2 = (P + Q\sqrt{5})(P - Q\sqrt{5})$ and attempt to show that $P + Q\sqrt{5}$ must be a fifth power in $\mathbb{Z}[\sqrt{5}]$. However, because Pell's equation $9^2 - 5 \cdot 4^2 = 1$ provides a non-trivial unit $9 + 4\sqrt{5}$ of norm $1$, the element $P + Q\sqrt{5}$ could differ from a fifth power by a unit factor: $P + Q\sqrt{5} = (A + B\sqrt{5})^5 (9 + 4\sqrt{5})^k$ for some integer $k$.

Dirichlet observed that if $P + Q\sqrt{5} = (A + B\sqrt{5})^5$, then expanding shows $Q$ is necessarily divisible by $5$. Thus $5 \mid Q$ is a necessary condition. He then proved, via his lemma, that when $P$ and $Q$ are relatively prime and of opposite parity, this condition is also sufficient: $5 \mid Q$ forces $P + Q\sqrt{5} = (A + B\sqrt{5})^5$.

The proof of this lemma proceeds by noting that any element of $\mathbb{Z}[\sqrt{5}]$ whose norm is a fifth power can be written as $(A + B\sqrt{5})^5 (9 + 4\sqrt{5})^r$ with $0 \leq r \leq 4$. Writing $C + D\sqrt{5} = (A + B\sqrt{5})^5$ and $E + F\sqrt{5} = (9 + 4\sqrt{5})^r$, one has $D \equiv 0 \pmod{5}$ and $Q = CF + DE$. Since $Q \equiv 0 \pmod{5}$, it follows that $CF \equiv 0 \pmod{5}$. But $C \not\equiv 0 \pmod{5}$ (otherwise $P$ and $Q$ would share factor $5$), so $F \equiv 0 \pmod{5}$. By the binomial theorem, $F = r \cdot 9^{r-1} \cdot 4$ plus multiples of $5$, which cannot be divisible by $5$ for $1 \leq r \leq 4$. Hence $r = 0$, establishing $P + Q\sqrt{5} = (A + B\sqrt{5})^5$.

With this lemma, the equation $P^2 - 5Q^2 = \text{fifth power}$ together with the circumstances of the problem (which guarantee $5 \mid Q$ and opposite parity) yields $P + Q\sqrt{5} = (A + B\sqrt{5})^5$. Expanding and comparing coefficients leads to an infinite descent, ultimately showing that the original equation cannot hold. Thus the first case is impossible.
