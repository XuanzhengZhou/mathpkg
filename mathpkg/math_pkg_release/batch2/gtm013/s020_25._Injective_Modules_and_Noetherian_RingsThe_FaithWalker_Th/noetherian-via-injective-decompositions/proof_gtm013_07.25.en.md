---
role: proof
locale: en
of_concept: noetherian-via-injective-decompositions
source_book: gtm013
source_chapter: "7"
source_section: "25. Injective Modules and Noetherian Rings—The Faith–Walker Theorems"
---

(a) $\Rightarrow$ (b). Let $E$ be an injective left $R$-module. [The detailed argument that every injective over a left noetherian ring decomposes into indecomposables is partially truncated in the source. The standard proof uses Zorn's Lemma on the family of sets of independent indecomposable submodules, using the fact that over a noetherian ring every injective is a direct sum of indecomposable injectives.]

(b) $\Rightarrow$ (c). This follows from Proposition 25.5.

(c) $\Rightarrow$ (d). This is trivial.

(d) $\Rightarrow$ (a). Let $S$ be an irredundant set of representatives of the simple left $R$-modules (see (18.16)); then

$$C_0 = \bigoplus_{T \in S} E(T)$$

is the minimal cogenerator for ${}_R\mathbf{M}$. Let

$$E = E(C_0^{(\mathbb{N})}).$$

Then by hypothesis there is a decomposition

$$E = \bigoplus_A E_\alpha$$

that complements maximal direct summands. For each of the simple modules $T \in S$, let

$$A(T) = \{\alpha \in A \mid E_\alpha \cong E(T)\}.$$

Now for each $n > 0$, the injective submodule $E(T)^{(n)}$ is isomorphic to a direct summand of $E$. So by (12.2)

$$\operatorname{card}(A(T)) \geq n,$$

and hence $A(T)$ is infinite. Let

$$B = \bigcup_{T \in S} A(T).$$

Then it is clear that $C_0^{(\mathbb{N})}$ is isomorphic to a direct summand of the direct summand $\bigoplus_B E_\beta$ of $E$. Therefore $C_0^{(\mathbb{N})}$ is injective, and by (25.3) $R$ is left noetherian.
