---
role: proof
locale: en
of_concept: domain-minus-zero-set
source_book: gtm038
source_chapter: "I"
source_section: "5. Expansion in Reinhardt Domains"
---
**Proof.** 1. $E$ is closed, therefore $\mathbb{C}^n - E$ is open, and hence $G' = G \cap (\mathbb{C}^n - E)$ is also open. Moreover, $E$ contains no interior points.

2. Write the points $\mathfrak{z} \in \mathbb{C}^n$ in the form $\mathfrak{z} = (z_1, \mathfrak{z}^*)$ with $\mathfrak{z}^* \in \mathbb{C}^{n-1}$. Let $\mathfrak{z}_0 = (z_1^{(0)}, \mathfrak{z}^{*(0)}) \in G$ and let $U'_\varepsilon(\mathfrak{z}_0) = U_\varepsilon(z_1^{(0)}) \times U'_\varepsilon(\mathfrak{z}^{*(0)})$ be an $\varepsilon$-neighborhood. We show $U'_\varepsilon - E$ is connected. Let $\mathfrak{z}_1 = (z_1^{(1)}, \mathfrak{z}^{*(1)})$ and $\mathfrak{z}_2 = (z_1^{(2)}, \mathfrak{z}^{*(2)})$ be two points in $U'_\varepsilon - E$. Define $\mathfrak{z}_3 := (z_1^{(2)}, \mathfrak{z}^{*(1)})$. Clearly $\mathfrak{z}_3 \in U'_\varepsilon - E$. $U_\varepsilon(z_1^{(0)})$ is an open disk in the $z_1$-plane, and $U_\varepsilon(z_1^{(0)}) - \{0\}$ is connected. Hence there is a path joining $z_1^{(1)}$ and $z_1^{(2)}$ within $U_\varepsilon(z_1^{(0)}) - \{0\}$, and also a path joining $\mathfrak{z}^{*(1)}$ and $\mathfrak{z}^{*(2)}$ in $U'_\varepsilon(\mathfrak{z}^{*(0)})$. These combine to join $\mathfrak{z}_1$ to $\mathfrak{z}_2$ within $U'_\varepsilon - E$.

For the connectedness of $G'$: given $\mathfrak{z}', \mathfrak{z}'' \in G'$, join them by a path in $G$, cover it with finitely many neighborhoods as above, and construct a path within $G'$ using the local connectivity established above. $\square$
