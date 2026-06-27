---
role: proof
locale: en
of_concept: finitary-theory-equational-presentation
source_book: gtm026
source_chapter: "4"
source_section: "4"
---

**Proof of Theorem 4.25.** Define $\Omega_n = \{n\} \times V_n T$ where $V_n$ is as defined in 4.18. Let $\Omega = \bigcup_n \Omega_n$ be the operator domain. For each $\omega \in \Omega_n$, written as $\omega = (n, \bar{\omega})$ with $\bar{\omega} \in V_n T$, define an operation on a $T$-algebra $(X, \xi)$ by:

$$\delta_\omega = X\hat{\omega} \cdot \xi$$

where $\hat{\omega}: X^n \longrightarrow XT$ is the map corresponding to $\bar{\omega}$ under the finitary property.

The proof proceeds by establishing three lemmas:

**(4.26)** For any $T$-homomorphism $f: (X, \xi) \longrightarrow (Y, \theta)$, the diagram commutes: $(r \cdot f)T = rT \cdot fT$.

**(4.27) Products:** If $(X_i, \xi_i)$ is a family of $T$-algebras, then the product set $X = \prod X_i$ admits a unique $T$-algebra structure $\xi$ making all projections $T$-homomorphisms, and this coincides with the cartesian product algebra structure. The proof uses the principle that two functions into a product are equal if and only if they are equal followed by each projection.

**(4.28) Subalgebras:** Let $(X, \xi)$ be a $T$-algebra and $A \subset X$ with inclusion $i: A \hookrightarrow X$. $A$ is a $T$-subalgebra if there exists $\xi_0: AT \longrightarrow A$ such that $iT \cdot \xi = \xi_0 \cdot i$. An $\Omega$-subalgebra of a $T$-algebra is a $T$-subalgebra: for $\bar{a} \in AT$ there exists $r: V_n \longrightarrow A$ and $\omega \in V_n T$ with $\langle \omega, rT \rangle = \bar{a}$, and closure under $\Omega$-operations ensures $\langle \bar{a}, iT \cdot \xi \rangle \in A$.

**(4.29)** If $H: \mathbf{Set} \longrightarrow \mathbf{Set}$ is any functor and $f: X \longrightarrow Y$ is surjective, then $fH: XH \longrightarrow YH$ is also surjective (by the axiom of choice).

To complete the proof, let $\mathcal{A}$ be the class of all $\Omega$-algebras arising from $T$-algebras via the construction above. We show $\mathcal{A}$ is closed under products (4.27), subalgebras (4.28), and quotients (using 4.29 and the axiom of choice to construct the required $T$-algebra structure on a quotient). By Birkhoff's Variety Theorem (4.22), there exists a set $E$ of equations such that $\mathcal{A}$ equals the class of all $(\Omega, E)$-algebras. $\square$
