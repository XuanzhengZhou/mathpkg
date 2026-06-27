---
role: proof
locale: en
of_concept: free-algebra-quotient-in-spk
source_book: gtm037
source_chapter: "24"
source_section: "24"
---

Let $I = \{(\sigma, \tau) : \sigma = \tau \notin \Gamma\}$. For each $(\sigma, \tau) \in I$ there is a structure $\mathfrak{A}_{\sigma\tau} \in K$ such that $\sigma = \tau$ fails to hold in $\mathfrak{A}_{\sigma\tau}$. Hence there is an $x_{\sigma\tau} \in {}^\omega A_{\sigma\tau}$ such that $\sigma^{\mathfrak{A}_{\sigma\tau}}x_{\sigma\tau} \neq \tau^{\mathfrak{A}_{\sigma\tau}}x_{\sigma\tau}$.

By the axiom of choice, let $x \in \prod_{F \in I} A_F$ where $A_F$ is the universe of the structure indexed by $F$. For each $a \in A$ define $g_a \in \prod_{F \in I} A_F$ by setting $g_aF = a$ if $a \in A_F$ and $g_aF = x_F$ otherwise. Let $fa = [g_a]_{\equiv_\Gamma}$. The verification that $f$ is an embedding of $\mathfrak{Fr}_\mathcal{L}/\equiv_\Gamma$ into a product of members of $K$ follows from the construction.
