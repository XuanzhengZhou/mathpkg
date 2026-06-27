---
role: proof
locale: en
of_concept: free-algebra-quotient-in-spk
source_book: gtm037
source_chapter: "24"
source_section: "4"
---

Let $I = \{(\sigma, \tau) : \sigma = \tau \notin \Gamma\}$, i.e., the set of pairs of terms whose equality does not follow from $\Gamma$ (and hence does not hold in every member of $K$). Then for each $(\sigma, \tau) \in I$ there is a structure $\mathfrak{A}_{\sigma\tau} \in K$ such that $\sigma = \tau$ fails to hold in $\mathfrak{A}_{\sigma\tau}$; hence, further, there is an $x_{\sigma\tau} \in {}^\omega A_{\sigma\tau}$ such that $\sigma^{\mathfrak{A}_{\sigma\tau}} x_{\sigma\tau} \neq \tau^{\mathfrak{A}_{\sigma\tau}} x_{\sigma\tau}$.

By the axiom of choice let $x \in \prod_{F \in I} A_F$, where $A_F$ denotes the universe of the structure indexed by $F = (\sigma, \tau)$. For each $a \in A = \bigcup_{F \in I} A_F$, define $g_a \in \prod_{F \in I} A_F$ by

$$g_a F = a \quad \text{if } a \in A_F,$$
$$g_a F = x_F \quad \text{otherwise},$$

and let $f a = [g_a]_\mathfrak{T}$ where $\mathfrak{T}$ is the appropriate ultrafilter or equivalence relation.

The map $f$ embeds $\mathfrak{Fr}_\mathcal{L} / {\equiv_\Gamma}$ into a product of substructures of members of $K$, establishing $\mathfrak{Fr}_\mathcal{L} / {\equiv_\Gamma} \in \mathbf{SPK}$. The desired properties of $f$ are easily checked. $\square$
