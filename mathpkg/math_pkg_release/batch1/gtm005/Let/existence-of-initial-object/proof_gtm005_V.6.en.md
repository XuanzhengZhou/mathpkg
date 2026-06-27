---
role: proof
locale: en
of_concept: existence-of-initial-object
source_book: gtm005
source_chapter: "V"
source_section: "6. Freyd's Adjoint Functor Theorem"
---

**Proof.** Necessity is immediate: if $D$ has an initial object $k$, then $\{k\}$ indexed by the one-point set satisfies the solution set condition.

For sufficiency, assume $D$ is small-complete with small hom-sets and satisfies the solution set condition. Let $w = \prod_i k_i$ be the product in $D$ of the objects $k_i$ from the solution set, with projections $p_i : w \rightarrow k_i$. For each object $d \in D$, the solution set condition gives an arrow $k_i \rightarrow d$ for some $i$, and composing with $p_i$ yields an arrow $w \rightarrow d$. Thus $w$ admits at least one arrow to every object of $D$.

Let $e : v \rightarrow w$ be the equalizer of all endomorphisms of $w$ (this equalizer exists because the set of endomorphisms of $w$ is small and $D$ is small-complete). We claim $v$ is initial. For any $d \in D$, there exists at least one arrow $f : w \rightarrow d$, so $f \circ e : v \rightarrow d$ shows $v$ admits an arrow to $d$.

It remains to prove uniqueness. Suppose $f, g : v \rightarrow d$ are two arrows. Form their equalizer $e_1 : u \rightarrow v$:

$$\xymatrix{
u \ar[r]^{e_1} & v \ar@<0.5ex>[r]^{f} \ar@<-0.5ex>[r]_{g} & d
}$$

Since $w$ admits an arrow to every object, there is an arrow $s : w \rightarrow u$, so the composite $e e_1 s$ is an endomorphism of $w$. But $e$ equalizes all endomorphisms of $w$, so

$$e e_1 s e = 1_w e = e 1_v.$$

Since $e$ is an equalizer, it is monic; cancelling $e$ on the left yields $e_1 s e = 1_v$. Thus the equalizer $e_1$ of $f$ and $g$ has a right inverse. Since $e_1$ is monic (as an equalizer), it is an isomorphism. Hence $f = g$. Therefore $v$ admits exactly one arrow to each object $d \in D$, so $v$ is initial. $\square$
