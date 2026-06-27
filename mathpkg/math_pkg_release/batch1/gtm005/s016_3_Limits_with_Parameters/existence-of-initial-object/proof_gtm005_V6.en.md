---
role: proof
locale: en
of_concept: existence-of-initial-object
source_book: gtm005
source_chapter: "V"
source_section: "6. Freyd's Adjoint Functor Theorem"
---

**Necessity.** If $D$ has an initial object $k$, take the one-point set $I = \{*\}$ and the family consisting of $k$ alone. Then for every $d \in D$, the unique arrow $k \rightarrow d$ satisfies the condition.

**Sufficiency.** Assume $D$ is small-complete with small hom-sets and satisfies the solution set condition. Form the product $w = \prod_{i \in I} k_i$, which exists since $D$ is small-complete. Let $e : v \rightarrow w$ be the equalizer of all endomorphisms of $w$ — that is, $e$ equalizes the (possibly large) family of all arrows $f : w \rightarrow w$ in $D$.

Now we claim $v$ is an initial object. Let $d$ be any object of $D$. By the solution set condition, there exists $i \in I$ and an arrow $k_i \rightarrow d$. Compose with the product projection $w \rightarrow k_i$ to obtain an arrow $w \rightarrow d$. This provides at least one arrow $v \rightarrow d$, as follows: take the composite $v \stackrel{e}{\rightarrow} w \rightarrow d$, giving an arrow $v \rightarrow d$.

To show uniqueness, suppose $f, g : v \rightarrow d$ are two arrows. Form their equalizer $e_1 : u \rightarrow v$. As $w$ is the product, there is an arrow $s : w \rightarrow u$ (by the solution set condition constructing an arrow from each factor $k_i$ into $u$). Then $e e_1 s : w \rightarrow w$ is an endomorphism of $w$, so it must be equalized by $e$, giving $e e_1 s e = e$. Since $e$ is an equalizer (hence monic), cancel to get $e_1 s e = 1_v$. Thus the equalizer $e_1$ has a right inverse; being monic (as any equalizer), it is an isomorphism. Therefore $f = g$, proving there is exactly one arrow $v \rightarrow d$. Hence $v$ is initial.
