---
role: proof
locale: en
of_concept: invariant-subspace-quotient-correspondence
source_book: gtm031
source_chapter: "III"
source_section: "3"
---

**Forward direction.** Let $\mathfrak{U}$ be invariant relative to $\Omega$ with $\mathfrak{R} \supseteq \mathfrak{U} \supseteq \mathfrak{S}$. Set $\bar{\mathfrak{U}} = \mathfrak{U}/\mathfrak{S}$, a subspace of $\bar{\mathfrak{R}} = \mathfrak{R}/\mathfrak{S}$. For any $\bar{u} \in \bar{\mathfrak{U}}$, we have $\bar{u} = u + \mathfrak{S}$ with $u \in \mathfrak{U}$. For any $A \in \Omega$, the induced transformation $\bar{A}$ on $\bar{\mathfrak{R}}$ satisfies $\bar{u}\bar{A} = \overline{uA}$. Since $\mathfrak{U}$ is invariant under $A$, $uA \in \mathfrak{U}$, hence $\overline{uA} \in \bar{\mathfrak{U}}$. Thus $\bar{\mathfrak{U}}$ is invariant relative to $\bar{\Omega}$.

**Converse direction.** Let $\bar{\mathfrak{U}}$ be a subspace of $\bar{\mathfrak{R}}$ invariant relative to $\bar{\Omega}$. Define $\mathfrak{U}$ to be the totality of vectors contained in the cosets that belong to $\bar{\mathfrak{U}}$. If $u_1, u_2 \in \mathfrak{U}$, then $\bar{u}_1 = u_1 + \mathfrak{S}$ and $\bar{u}_2 = u_2 + \mathfrak{S}$ lie in $\bar{\mathfrak{U}}$. Hence $\bar{u}_1 + \bar{u}_2 = (u_1 + u_2) + \mathfrak{S} \in \bar{\mathfrak{U}}$, so $u_1 + u_2 \in \mathfrak{U}$. Similarly, for any scalar $\alpha$, $\alpha \bar{u}_1 = \alpha u_1 + \mathfrak{S} \in \bar{\mathfrak{U}}$ implies $\alpha u_1 \in \mathfrak{U}$. Thus $\mathfrak{U}$ is a subspace of $\mathfrak{R}$ containing $\mathfrak{S}$.

To see that $\mathfrak{U}$ is invariant under $A \in \Omega$: for $u \in \mathfrak{U}$, $\bar{u} = u + \mathfrak{S} \in \bar{\mathfrak{U}}$. By invariance of $\bar{\mathfrak{U}}$ under $\bar{A}$, $\bar{u}\bar{A} = \overline{uA} \in \bar{\mathfrak{U}}$, which means $uA \in \mathfrak{U}$. Hence $\mathfrak{U}$ is invariant relative to $\Omega$, and clearly $\bar{\mathfrak{U}} = \mathfrak{U}/\mathfrak{S}$.
