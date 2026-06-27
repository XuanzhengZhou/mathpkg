---
role: proof
locale: en
of_concept: birkhoff-variety-theorem
source_book: gtm037
source_chapter: "24"
source_section: "24"
---

($\Rightarrow$) If $K$ is a variety, then $K = \operatorname{Mod} \Gamma$ for some set $\Gamma$ of equations. By earlier results (24.2 and 24.9), equations are preserved under $\mathbf{H}$, $\mathbf{S}$, and $\mathbf{P}$, so $\mathbf{HSP}K \subseteq K$. The reverse inclusion is trivial since $K \subseteq \mathbf{HSP}K$.

($\Leftarrow$) Assume $K = \mathbf{HSP}K$. By 24.11, $K$ is closed under $\mathbf{H}$, $\mathbf{S}$, and $\mathbf{P}$, and hence also under $\mathbf{Up}$. Let $\Gamma = \{\sigma = \tau : \sigma = \tau \text{ holds in every member of } K\}$. We claim $K = \operatorname{Mod} \Gamma$. Each member of $K$ is trivially a model of $\Gamma$. Now let $\mathfrak{A}$ be a model of $\Gamma$. By 24.21, it suffices to take any finitely generated substructure $\mathfrak{B}$ of $\mathfrak{A}$ and show $\mathfrak{B} \in K$.

Choose $x \in {}^\omega B$ so that $\operatorname{Rng} x$ generates $\mathfrak{B}$. Then for every $b \in B$ there is a term $\sigma$ such that $\sigma^{\mathfrak{B}}x = b$. Since $\mathfrak{A} \models \Gamma$, also $\mathfrak{B} \models \Gamma$. By Lemma 24.20, $\mathfrak{Fr}_\mathcal{L}/\equiv_\Gamma \in \mathbf{SPK}$. Using the homomorphism from the free algebra onto $\mathfrak{B}$ that factors through $\equiv_\Gamma$, we obtain $\mathfrak{B} \in \mathbf{HSPK} = K$.
