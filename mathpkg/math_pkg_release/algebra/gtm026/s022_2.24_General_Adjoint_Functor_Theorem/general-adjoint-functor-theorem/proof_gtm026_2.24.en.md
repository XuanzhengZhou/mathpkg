---
role: proof
locale: en
of_concept: general-adjoint-functor-theorem
source_book: gtm026
source_chapter: "2"
source_section: "2.24"
---

We have already observed the necessity of these conditions, so we concentrate on the sufficiency. $U$ preserves all small limits because $\mathcal{A}$ has all small limits and because of the construction used to prove 1.22. Fix $K$ in $\mathcal{K}$. Our object is to produce a free $\mathcal{A}$-object $(F, \eta)$ over $K$ with respect to $U$. First, we will construct a weakly free $\mathcal{A}$-object over $K$ with respect to $U$, this being a pair $(F', \eta')$ such that $\eta': K \longrightarrow F'U$ in $\mathcal{K}$ and given any pair $(A, f)$ with $f: K \longrightarrow AU$ there exists $\psi: F' \longrightarrow A$ in $\mathcal{A}$ with $\eta'.\psi U = f$.

Let $\mathcal{S}_K$ be a solution set at $K$. Let $P$ be the product in $\mathcal{A}$ of all $S$ with $(S, s) \in \mathcal{S}_K$. Let $p_s: P \longrightarrow S$ be the $s$-th projection. Since $U$ preserves products, $PU$ is a product with projections $p_s U$. By the universal property of products in $\mathcal{K}$, there exists unique $\eta': K \longrightarrow PU$ such that $\eta'.p_s U = s$ for all $(S, s) \in \mathcal{S}_K$. If $(A, f)$ is an arbitrary pair then, by the definition of $\mathcal{S}_K$, there exists $(S, s) \in \mathcal{S}_K$ and $\Gamma: S \longrightarrow A$ in $\mathcal{A}$ with $s.\Gamma U = f$. Setting $\psi: F' \longrightarrow A = p_s.\Gamma$, we have $\eta'.\psi U = f$ as desired.

The second step invokes Lemma 2.25. Let $C = \{F' \xrightarrow{x} F': \eta'.xU = \eta'\}$. Form the collective equalizer $i: F \longrightarrow F'$ of $C$, which is preserved by $U$. Setting $\eta = \eta'.iU$ yields the desired free object. The proof that $(F, \eta)$ satisfies the universal property: If $\eta.\psi U = \eta.\psi' U$, then $\psi = \psi'$. Form $j = \text{eq}(\psi, \psi')$ in $\mathcal{A}$ so that $jU = \text{eq}(\psi U, \psi' U)$ in $\mathcal{K}$. Since $\eta.\psi U = \eta.\psi' U$, there exists unique $f$ with $f.jU = \eta$. Since $(F', \eta')$ is weakly free, there exists $\Gamma: F' \longrightarrow E$ with $\eta'.\Gamma U = f$. Set $x: F' \longrightarrow F' = \Gamma.j.i$. Then $\eta'.xU = \eta.iU = \eta'$, so $x \in C$. As $\text{id}_{F'} \in C$, $i.x = i$, that is $i.\Gamma.j.i = \text{id}_{F}.i$. Since $i$ is a monomorphism, $i.\Gamma.j = \text{id}_{F}$. It follows that $\psi = i.\Gamma.j.\psi = i.\Gamma.j.\psi' = \psi'$.
