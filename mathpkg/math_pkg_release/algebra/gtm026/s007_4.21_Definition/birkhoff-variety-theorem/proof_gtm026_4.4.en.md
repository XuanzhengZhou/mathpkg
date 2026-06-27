---
role: proof
locale: en
of_concept: birkhoff-variety-theorem
source_book: gtm026
source_chapter: "4"
source_section: "4"
---

**Proof of Birkhoff Variety Theorem (4.22).** Let $\mathcal{A}$ be a class of $(\Omega, E)$-algebras closed under products, subalgebras, and quotients. Let $E$ be the set of all equations $\{e_1, e_2\} \subset \mathcal{V}\Omega$ such that for every algebra $(X, \delta)$ in $\mathcal{A}$ and every function $r: \mathcal{V} \longrightarrow X$ it is the case that $r^\#$ identifies $e_1$ and $e_2$. Trivially, all algebras in $\mathcal{A}$ satisfy $E$.

Let $(X, \delta)$ be an arbitrary $(\Omega, E)$-algebra. We will show that $(X, \delta)$ is a quotient of a subalgebra of a product of elements of $\mathcal{A}$. If $\mathbf{T}$ is the algebraic theory of $(\Omega, E)$ as in 4.1, the structure map of $(X, \delta)$ is an $\Omega$-homomorphism onto, so it suffices to show that $XT$ is isomorphic to a subalgebra of a product of elements of $\mathcal{A}$.

To do this we show that $XT$ admits enough homomorphisms to elements of $\mathcal{A}$ to separate points, that is:

**(4.23)** If $[p] \neq [q] \in XT$ then there exists an algebra $(A, \gamma)$ in $\mathcal{A}$ and a map $r: X \longrightarrow A$ such that $[p]r^\# \neq [q]r^\#$.

To prove 4.23, let $X_n = \{x_1, \ldots, x_n\}$ be the finite set of all variables in $[p]$ and $[q]$. Since $[p]r^\# = \langle p', s^\# \rangle$, the proof of 4.23 is complete.

For each pair $(t, u)$ of distinct elements of $XT$, choose $A_{t, u}$ in $\mathcal{A}$ and a homomorphism $r_{t, u}: XT \longrightarrow A_{t, u}$ which maps $t$ and $u$ to different values. Let $A$ be the product algebra of $(A_{t, u} : t \neq u \in XT)$ and define a single homomorphism $r: XT \longrightarrow A$ by $([p]r)_{t, u} = [p]r_{t, u}$. By construction, $r$ is injective.

The proof is complete by the following standard fact:

**(4.24)** If $f: (X, \delta) \longrightarrow (Y, \gamma)$ is an injective $\Omega$-homomorphism then its image $Xf \subset Y$ is a subalgebra of $(Y, \gamma)$ and the map $g: X \longrightarrow Xf$, $xg = xf$ is an isomorphism.

Thus $XT$ is isomorphic to a subalgebra of a product of algebras from $\mathcal{A}$, and since $\mathcal{A}$ is closed under products and subalgebras, $XT \in \mathcal{A}$. As $(X, \delta)$ is a quotient of $XT$, closure under quotients yields $(X, \delta) \in \mathcal{A}$, establishing that $\mathcal{A}$ is exactly the class of $(\Omega, E)$-algebras. $\square$
