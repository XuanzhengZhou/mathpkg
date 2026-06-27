---
role: proof
locale: en
of_concept: construction-free-monoids
source_book: gtm005
source_chapter: "VII"
source_section: "1"
---

**Proof.** The distributive law $\theta : \coprod_n(a \square b_n) \cong a \square \coprod_n b_n$ holds for each denumerable coproduct $\coprod_n b_n$ of objects $b_n \in B$ because the functors $a \square -$ and $- \square a$ preserve coproducts.

For a given object $a \in B$, define the object $M_a = \coprod_n a^n$, where $a^n$ is the $n$-th power with all parentheses in front. The multiplication $\mu : M_a \square M_a \rightarrow M_a$ is constructed using the distributive law and the coproduct universal property. The composite

$$M_a \square M_a = \left(\coprod_m a^m\right) \square \left(\coprod_n a^n\right) \cong \coprod_{m,n} (a^m \square a^n)$$

maps each summand $a^m \square a^n$ via the canonical isomorphism $a^m \square a^n \cong a^{m+n}$ (from coherence) followed by the coproduct injection $i_{m+n} : a^{m+n} \rightarrow M_a$. A large but routine diagram shows this $\mu$ to be associative, in the sense of the monoid axiom (1). A corresponding unit $\eta_a : e \rightarrow \coprod_n a^n$ is defined to be the injection $i_0 : e = a^0 \rightarrow \coprod_n a^n$ of the coproduct. All told, $\langle \coprod_n a^n, \mu, \eta_a \rangle$ is a monoid in $B$. The injection $\varrho_a = i_1 : a = a^1 \rightarrow \coprod_n a^n$ of the coproduct is an arrow

$$\varrho_a : a \rightarrow U \langle \coprod_n a^n, \mu, \eta_a \rangle$$

to the forgetful functor $U : \mathbf{Mon}_B \rightarrow B$.

This arrow is universal from $a$ to $U$. For let $\langle c, \mu_c, \eta_c \rangle$ be any monoid in $B$ and $f : a \rightarrow c = U(c, \mu_c, \eta_c)$ an arrow in $B$. Then we define an arrow $f' : \coprod_n a^n \rightarrow c$ as the composite on the bottom of the commutative diagram

$$\begin{array}{ccc}
a^n & c^n & \mu_w \\
i_n & j_n & \parallel \\
\coprod_n a^n & \longrightarrow \coprod_n c^n & \longrightarrow c
\end{array}$$

constructed as follows. First, take $w$ to be the word of length $n$ with all parentheses in front, so that $w_B = b^n$, by definition of $b^n$; then $\mu_w : c^n \rightarrow c$ is the $n$-fold product defined in the general associative law (6), $i_n$ and $j_n$ are coproduct injections, and the dotted arrows on the bottom are constructed, by universality of the coproducts, so as to make the indicated squares commute (for all $n$). A routine large diagram will prove that $f'$ is a morphism of monoids; by construction $f' \circ \varrho_a = f$. The uniqueness of $f'$ follows from the universal property of the coproduct. Thus $\varrho_a$ is universal, establishing the left adjoint to $U$.
