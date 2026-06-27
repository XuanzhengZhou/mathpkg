---
role: proof
locale: en
of_concept: decomposition-of-nilpotent-group-into-p-groups
source_book: gtm016
source_chapter: "0.2"
source_section: "0.2.2"
---

For each prime $p$, let $G_p = \{g \in G \mid g^{p^f} = e \text{ for some } f\}$. Since $G$ is nilpotent, each $G_p$ is a subgroup. Each $G_p$ has order a power of $p$. Elements from distinct $G_p$ commute, so the map $f(g_1,\ldots,g_n) = \prod g_i$ is a homomorphism from $\prod G_{p_i}$ to $G$. It is injective since the orders of the $G_{p_i}$ are pairwise coprime, and surjective by order comparison using $|G| = \prod p_i^{e_i}$.
