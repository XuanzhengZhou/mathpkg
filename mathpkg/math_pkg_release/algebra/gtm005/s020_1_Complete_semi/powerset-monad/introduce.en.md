---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The power set monad $\langle \mathcal{P}, \eta, \mu \rangle$ on the category $\mathbf{Set}$ of sets is defined by the covariant power set functor $\mathcal{P}$, the singleton natural transformation $\eta_X(x) = \{x\}$, and the union natural transformation $\mu_X$ that collapses a set of sets into their union. This monad, introduced by Ernest Manes in his thesis, is a fundamental example illustrating the monad concept. Its algebras are precisely the complete semi-lattices: the structure map $h : \mathcal{P}X \to X$ of a $\mathcal{P}$-algebra defines a partial order $x \leq y$ iff $h\{x,y\} = y$, with suprema given by $hS$ for any subset $S \subset X$.
