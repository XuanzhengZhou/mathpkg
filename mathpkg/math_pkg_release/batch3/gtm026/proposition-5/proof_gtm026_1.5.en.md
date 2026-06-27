---
role: proof
locale: en
of_concept: proposition-5
source_book: gtm026
source_chapter: "1"
source_section: "5.13"
---

If $\varnothing$ is a $\mathbf{T}$-algebra, the existence of $\xi: \varnothing T \longrightarrow \varnothing$ guarantees $\varnothing T = \varnothing$. Conversely, if $\varnothing T = \varnothing$, $\varnothing = (\varnothing T, \varnothing \mu)$ is a $\mathbf{T}$-algebra. Assume $\varnothing T \neq \varnothing$ and let $\omega \in nT$ be constant. Since $\varnothing$ is not a $\mathbf{T}$-algebra, $\operatorname{ar}(\tilde{\omega}) = 0$. By 5.11, $\operatorname{ar}(\omega) = 0$.

It is possible to be constant without being true. Let $\Omega_1 = \{u\}, \Omega_n = \varnothing$ for $n \neq 1$ and let $E$ have the single equation $\{v_1 u, v_2 u\}$. Then an $(\Omega, E)$-algebra is $(X, \delta)$ where $\delta: X \longrightarrow X$ is constant. $\varnothing$ is an $(\Omega

only if the supremum of $x$ and $y$ is $y$ i.e., $x + y = y$. It is easy to check that these passages are mutually inverse in such a way that semilattice homomorphisms are just $\Omega$-homomorphisms. More generally, let $M$ be a fixed infinite cardinal. An $M$-complete semilattice is a semilattice $(X, \leqslant)$ for which every subset of $X$ of cardinal less than $M$ has a supremum. The $M$-complete homomorphisms are required to preserve all $n$-ary suprema for $n < M$. Finitely complete semilattices are $\aleph_0$-complete semilattices. A complete semilattice is a semilattice $(X, \leqslant)$ in which every subset of $X$ has a supremum; the homomorphisms preserve all suprema. The Boolean $\sigma$-rings used in measure theory are, in part, $\aleph_1$-complete semilattices. In a complete lattice every subset $A$ has an infimum also, namely $\operatorname{Inf}(A) = \operatorname{Sup}(x:x \leqslant a$ for all $a \in A)$. If $X$ is the set of all open subsets of the real numbers (in the usual topology) and $\leqslant$ is inclusion, then $(X, \leqslant)$ is a complete semilattice where suprema are ordinary unions, but the infimum of a family of open sets is the interior of the set-theoretic intersection. The inclusion map of $(X, \leqslant)$ into the complete semilattice of all subsets of the real numbers is a complete semilattice homomorphism which does not preserve the infimum of the countable family $[(-1/n, 1/n):n = 1, 2, 3, \ldots]$. It is because of the homomorphisms that we distinguish between complete semilattices and complete lattices.

It is easy to check that if $(\Omega, E)$ describes semilattices as above, there is a bijective correspondence between $\Omega$-terms in $X$ and finite subsets of $X$ (note that the words of 4

z, that is $x \leqslant z$. Let $A$ be a subset of $X$. For all $a \in A$, $\sup\{a, \sup(A)\} = \sup(\{a\} \cup A) = \sup(A)$ proving that $\sup(A)$ is an upper bound of $A$. If $x$ is another upper bound of $A$ then $\sup\{\sup(A), x\} = \sup(A \cup \{x\}) = \sup(\cup(\{a, x\}: a \in A)) = \sup\{\sup\{a, x\}: a \in A\} \sup\{\sup\{x\}\} = x$, so $\sup(A) \leqslant x$. This completes the verification that $\mathbf{T}$-algebras are coextensive with complete semilattices.

To deal with $M$-complete semilattices it seems natural to “truncate” $\mathbf{T}$ at $M$ by defining $XT_M = \{A \subset X: A \text{ has cardinal} < M\}$. Is $T_M$ a subtheory of $\mathbf{T}$ in the sense of 3.20? Since every singleton subset is in $XT_M$ the condition on $\eta$ is true. There is a problem, however, with staying closed under composition. Given $\alpha: A \longrightarrow BT$ and $\beta: B \longrightarrow CT$ then $(\alpha \circ \beta)_a = \cup\{b\beta: b \in a\alpha\}$. If $\alpha$ factors through $BT_M$ (i.e., $a\alpha$ has cardinal $< M$) and $\beta$ factors through $CT_M$ (i.e., each $b\beta$ has cardinal $< M$) we would hope that $(\alpha \circ \beta)_a$ also has cardinal $< M$. A moment’s thought shows that this condition amounts to a rewording of the definition (see the primer on set theory at the end of this section) of a regular cardinal. We formalize with:

(5.16) $M$ is a regular cardinal if and only if $T_M$ is a subtheory of $\mathbf{T}$, where $\mathbf

We turn now to the proof that the complete atomic Boolean algebras may be identified with the algebras over the double power-set theory of 3.19. Unlike the situation of 5.15, we do not know how to interpret the structure map. So let us begin by seeing in what sense an element $A \in XT$ looks like a syntactic formula in $X$. It actually is. First, we record what most readers already know (and the rest should check for themselves): any Boolean ring $(X, +, 0, \text{jux}, 1)$ is a lattice with binary infima $x \wedge y = xy$, binary suprema $x \vee y = x + y + xy$ and unique complements (that is, for all $x$ there is unique $x'$ with $x \wedge x' = 0$ and $x \vee x' = 1$) namely $x' = x + 1$. According to the definition of $\eta$ in 3.19 the element $x \in X$ is the “variable” $\text{prin}(x) \in XT$. For $A \subset X$, $\cap(\text{prin}(x):x \in A) = \{B \subset X:A \subset B\}$. Since $(\text{prin}(x))' = \{B \subset X:x \notin B\}$, we have $\cap((\text{prin}(x))':x \notin A) = \{B \subset X:B \subset A\}$. It follows at once that $A$ is the syntactic formula:

$$A = \bigcup_{A \in A} \cap \left\{ \text{prin}(x):x \in A \right\} \cup \left\{ ((\text{prin}(x))':x \notin A \right\}$$

This immediately forces us to define
