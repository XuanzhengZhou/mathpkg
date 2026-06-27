---
role: proof
locale: en
of_concept: for-every-p-0-in-p-there-exists-a-mathcalp-generic-set-g-such-that-p-0-in-g
source_book: gtm001
source_chapter: "17"
source_section: ""
---

Since $M$ is countable, we can enumerate all dense subsets of $P$ in $M$, say $D_1, D_2, \ldots$. We then define $p_{n+1}$ by introduction on $n$ such that

$$p_{n+1} \in D_{n+1} \land p_{n+1} \leq p_n.$$

Let $G = \{q \in P | (\exists n)[p_n \leq q]\}$. It is then obvious that $G$ is $\mathcal{P}$-generic. $\square$

Remark. We now introduce a ramified language, $\mathcal{L}(M, \mathbf{G})$, to give a notation for each member of the universe $M[G]$ which we are going to construct, that is, we first give the names of sets and later we will construct them. The symbols of $\mathcal{L}(M, \mathbf{G})$ are the following.

Variables: $x_0, x_1, \ldots, x_n, \ldots (n \in \omega)$.
Symbols for special objects: $\mathbf{k}$ for every $k \in M$.
A symbol for a special set $P$: $\mathbf{P}$.
A symbol for a set $G$ which will be defined: $\mathbf{G}$.
A relation symbol: $\in$.
Propositional connectives: $\neg, \land, \lor$.
Quantifiers: $\exists^\alpha (\

(3) If $\varphi$ and $\psi$ are limited formulas, then $(\neg \varphi), (\varphi \lor \psi)$, and $(\varphi \land \psi)$ are limited formulas.

(4) If $\varphi$ is a limited formula, then $(\exists^\alpha x_i \varphi)$ is a limited formula.

(5) If $\varphi(x_i)$ is a limited formula without free variables other than $x_i$ such that $g(\varphi(x_i)) < g(^\alpha)$, then $(\hat{x}_i^\alpha \varphi(x_i))$ is a constant term. This constant term is called an abstraction term.

(6) Limited formulas and terms are only those obtained by a finite number of applications of (1)-(5).
