---
role: proof
locale: en
of_concept: local-symbol-properties
source_book: gtm059
source_chapter: "Local Class Field Theory"
source_section: "54. The Reciprocity Law"
---

The properties of the Kummer pairing follow from the definition and the properties of the reciprocity automorphism $r_a$.

**Property 1 (Biadditivity).** For the additivity in the first argument, let $x_1, x_2 \in A(\mathfrak{m}_0)$ with $[\pi^n]_A(t_1) = x_1$ and $[\pi^n]_A(t_2) = x_2$. Then $[\pi^n]_A(t_1 +_A t_2) = x_1 +_A x_2$, so
$$\langle x_1 +_A x_2, a \rangle = r_a(t_1 +_A t_2) -_A (t_1 +_A t_2) = (r_a(t_1) -_A t_1) +_A (r_a(t_2) -_A t_2) = \langle x_1, a \rangle +_A \langle x_2, a \rangle.$$
The multiplicativity in the second argument follows from $r_{a_1 a_2} = r_{a_1} r_{a_2}$ and the fact that $r_a$ acts as an endomorphism of the formal group $A$, so
$$\langle x, a_1 a_2 \rangle = r_{a_1 a_2}(t) -_A t = r_{a_1}(r_{a_2}(t)) -_A t = (r_{a_1}(r_{a_2}(t)) -_A r_{a_2}(t)) +_A (r_{a_2}(t) -_A t).$$
Since $[\pi^n]_A(r_{a_2}(t)) = r_{a_2}([\pi^n]_A(t)) = r_{a_2}(x) = x$ when $x \in A[\pi^{k}]$ for appropriate $k$, the first term is $\langle x, a_1 \rangle$ and the second is $\langle x, a_2 \rangle$.

**Property 2 (Kernel).** If $x = [\pi^n]_A(y)$ for some $y \in A(\mathfrak{m}_0)$, then one may take $t = y$ in the definition, giving $\langle x, a \rangle = r_a(y) -_A y$. Since $r_a$ acts trivially on $A(\mathfrak{m}_0)$ modulo higher ramification (by the definition of the reciprocity map on the totally ramified part), the pairing vanishes. Conversely, the non-degeneracy follows from the fact that the reciprocity map gives an isomorphism $K^{*} / K^{* \pi^n} \cong \mathrm{Gal}(K_0/K)$ and the structure of $A[\pi^n]$ as a free $\mathcal{O}_K/\pi^n \mathcal{O}_K$-module of rank $1$.

**Property 3 (Compatibility).** This is immediate from the definition of the symbol.

**Property 4 (Functoriality).** For an isogeny of Lubin-Tate formal groups, the corresponding Kummer pairings are compatible via the induced maps on torsion points and the transfer map on the multiplicative group. This follows from the functoriality of the Lubin-Tate construction.
