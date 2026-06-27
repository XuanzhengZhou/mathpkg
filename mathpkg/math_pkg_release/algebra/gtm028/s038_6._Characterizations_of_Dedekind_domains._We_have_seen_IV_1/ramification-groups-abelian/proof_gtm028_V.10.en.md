---
role: proof
locale: en
of_concept: ramification-groups-abelian
source_book: gtm028
source_chapter: "V"
source_section: "10"
---

For $n \geq 1$, let $u$ be a uniformizing element of $R'_{\mathfrak{P}}$ (an element of $\mathfrak{P} \setminus \mathfrak{P}^2$). For $s \in G_{V_n}$, by definition $s(u) \equiv u \pmod{\mathfrak{P}^{n+1}}$, so $s(u) = u + y_s u^{n+1}$ for some $y_s \in R'$. Define the map $\varphi_n: G_{V_n} \to R'/\mathfrak{P}$ by $\varphi_n(s) = \bar{y}_s$ (the residue class of $y_s$ modulo $\mathfrak{P}$).

For $s, t \in G_{V_n}$, one computes that $st(u) = u + (y_s + y_t) u^{n+1} + \text{terms in } \mathfrak{P}^{n+2}$. Hence $\bar{y}_{st} \equiv \bar{y}_s + \bar{y}_t \pmod{\mathfrak{P}}$, proving that $\varphi_n(st) = \varphi_n(s) + \varphi_n(t)$. Thus $\varphi_n$ is a group homomorphism from $G_{V_n}$ into the additive group of $R'/\mathfrak{P}$.

The kernel of $\varphi_n$ consists of those $s$ with $y_s \equiv 0 \pmod{\mathfrak{P}}$, i.e., $s(u) \equiv u \pmod{\mathfrak{P}^{n+2}}$, which is exactly $G_{V_{n+1}}$. Therefore $G_{V_n}/G_{V_{n+1}}$ is isomorphic to a subgroup of $R'/\mathfrak{P}$. Since the additive group of any field is abelian, the quotient is abelian. If the residue field extension is separable of characteristic $p$, then $R'/\mathfrak{P}$ is an elementary abelian $p$-group, and so is the quotient.
