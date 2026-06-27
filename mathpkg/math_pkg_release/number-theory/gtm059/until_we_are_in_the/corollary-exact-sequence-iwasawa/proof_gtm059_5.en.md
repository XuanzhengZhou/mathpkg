---
role: proof
locale: en
of_concept: corollary-exact-sequence-iwasawa
source_book: gtm059
source_chapter: "5"
source_section: "Iwasawa Theory and Ideal Class Groups"
---

From the proof of Theorem 4.1, we have $G = G_n \cdot I$ as a semidirect product with $G_n \cap I = \{1\}$. The inertia group $I$ surjects onto $\Gamma = \operatorname{Gal}(K_\infty/K)$ since the ramified prime is totally ramified. The kernel of $I \to \Gamma$ is the wild inertia subgroup, which is a finite $p$-group.

Thus we obtain the exact sequence

$$
1 \to G_n \to G \to \Gamma \to 1
$$

(where the third map may have a finite kernel corresponding to the wild inertia, which can be absorbed into $G_n$ after passing to a sufficiently high layer). The action of $\Gamma$ on $G_n$ via conjugation in $G$ gives $G_n$ the structure of a module over the completed group ring $\Lambda = \mathbb{Z}_p[[\Gamma]]$.
