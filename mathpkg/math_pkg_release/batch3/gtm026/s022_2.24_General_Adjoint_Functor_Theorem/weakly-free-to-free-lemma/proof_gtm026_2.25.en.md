---
role: proof
locale: en
of_concept: weakly-free-to-free-lemma
source_book: gtm026
source_chapter: "2"
source_section: "2.25"
---

Since $iU$ is the collective equalizer of $\{xU : x \in C\}$ and $\eta'.(\text{id}_{F'})U = \eta'$, we have $\text{id}_{F'} \in C$. Hence $\text{id}_{F'}U \in \{xU : x \in C\}$. Since $iU$ equalizes all pairs from this set, we have $(iU)(\text{id}_{F'}U) = (iU)(xU)$ for any $x \in C$, which means $iU = (iU)(xU)$. In particular, because $\eta'.xU = \eta'$ for all $x \in C$, we obtain $\eta'.iU = \eta'.xU.iU = \eta'.iU$ (trivially). More importantly, since $U$ preserves equalizers and the collective equalizer $iU$ equalizes all $xU$, there exists a unique morphism $\eta: K \longrightarrow FU$ such that $\eta.iU = \eta'$.

We claim that $(F, \eta)$ is free over $K$ with respect to $U$. To prove the universal property, let $f: K \longrightarrow AU$ be given. Since $(F', \eta')$ is weakly free, there exists $\psi: F' \longrightarrow A$ with $\eta'.\psi U = f$. But we need a morphism from $F$, not $F'$. Define $\psi' = i.\psi$. Then $\eta.\psi' U = \eta.iU.\psi U = \eta'.\psi U = f$, giving existence.

For uniqueness, suppose $\psi, \psi': F \longrightarrow A$ are two $\mathcal{A}$-morphisms such that $\eta.\psi U = \eta.\psi' U$. Form $j = \text{eq}(\psi, \psi')$ in $\mathcal{A}$ so that $j U = \text{eq}(\psi U, \psi' U)$ in $\mathcal{K}$ (since $U$ preserves equalizers of pairs). Because $\eta.\psi U = \eta.\psi' U$, there exists unique $f$ with $f.j U = \eta$. Since $(F', \eta')$ is weakly free, there exists $\Gamma: F' \longrightarrow E$ (where $E$ is the domain of $j$) with $\eta'.\Gamma U = f$. Set $x: F' \longrightarrow F' = \Gamma.j.i$. Reading off the diagram, we see that $\eta'.xU = \eta.iU = \eta'$, so $x \in C$. As $\text{id}_{F'} \in C$, the collective equalizer property gives $i.x = i$, that is $i.\Gamma.j.i = \text{id}_{F}.i$. Since $i$ is an equalizer (hence a monomorphism), we can cancel it on the right to obtain $i.\Gamma.j = \text{id}_{F}$. It follows that $\psi = i.\Gamma.j.\psi = i.\Gamma.j.\psi' = \psi'$. Therefore the mediating morphism is unique, and $(F, \eta)$ is free over $K$ with respect to $U$.
