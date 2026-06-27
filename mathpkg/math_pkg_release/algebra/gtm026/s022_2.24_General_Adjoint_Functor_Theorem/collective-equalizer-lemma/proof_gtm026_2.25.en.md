---
role: proof
locale: en
of_concept: collective-equalizer-lemma
source_book: gtm026
source_chapter: "2"
source_section: "2.25"
---

Define $\eta = \eta'.iU: K \longrightarrow FU$. We must show that $(F, \eta)$ satisfies the universal property: given any $f: K \longrightarrow AU$ there exists unique $\psi: F \longrightarrow A$ with $\eta.\psi U = f$.

Since $(F', \eta')$ is weakly free, there exists $\phi: F' \longrightarrow A$ with $\eta'.\phi U = f$. Set $\psi = i.\phi$. Then $\eta.\psi U = \eta'.iU.(i.\phi)U = \eta'.iU.iU.\phi U = \eta'.\phi U = f$, since $\eta'.iU.xU = \eta'.iU$ for any $x \in C$ and $\text{id}_{F'} \in C$.

For uniqueness, suppose $\eta.\psi U = \eta.\psi' U$ for $\psi, \psi': F \longrightarrow A$. We must show $\psi = \psi'$. Form $j = \text{eq}(\psi, \psi')$ in $\mathcal{A}$ so that $jU = \text{eq}(\psi U, \psi' U)$ in $\mathcal{K}$ (since $U$ preserves equalizers). Since $\eta.\psi U = \eta.\psi' U$, there exists unique $f: K \longrightarrow EU$ with $f.jU = \eta$ (where $E$ is the domain of $j$). Since $(F', \eta')$ is weakly free, there exists $\Gamma: F' \longrightarrow E$ with $\eta'.\Gamma U = f$. Set $x = \Gamma.j.i: F' \longrightarrow F'$. Then $\eta'.xU = \eta'.\Gamma U.jU.iU = f.jU.iU = \eta.iU = \eta'.iU.iU = \eta'$ (since $\text{id}_{F'} \in C$). Thus $x \in C$.

Now $i.x = i.\Gamma.j.i$. Since $i$ is the collective equalizer of $C$ and $\text{id}_{F'} \in C$, we have $i.\text{id}_{F'} = i = i.x$. So $i = i.\Gamma.j.i$. Since $i$ is an equalizer, it is a monomorphism; canceling $i$ on the right gives $\text{id}_F = i.\Gamma.j$. Then $\psi = \text{id}_F.\psi = i.\Gamma.j.\psi = i.\Gamma.j.\psi' = \psi'$.
