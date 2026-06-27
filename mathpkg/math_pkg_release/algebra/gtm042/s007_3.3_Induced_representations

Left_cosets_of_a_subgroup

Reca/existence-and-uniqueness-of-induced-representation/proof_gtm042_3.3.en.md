---
role: proof
locale: en
of_concept: existence-and-uniqueness-of-induced-representation
source_book: gtm042
source_chapter: "3"
source_section: "3.3"
---

Let us first prove the existence of the induced representation $\rho$. In view of example 3 (induction preserves direct sums), we may assume that $\theta$ is irreducible. In this case, $\theta$ is isomorphic to a subrepresentation of the regular representation of $H$, which can be induced to the regular representation of $G$ (cf. example 1). Applying example 4 (induction of stable subspaces), we conclude that $\theta$ itself can be induced.

It remains to prove the uniqueness of $\rho$ up to isomorphism. Let $(V, \rho)$ and $(V', \rho')$ be two representations induced by $(W, \theta)$. Applying Lemma 1 to the injection of $W$ into $V'$, we see that there exists a linear map $F: V \rightarrow V'$ which is the identity on $W$ and satisfies $F \circ \rho_s = \rho_s' \circ F$ for all $s \in G$. Consequently the image of $F$ contains all the $\rho_s' W$, and thus is equal to $V'$. Since $V'$ and $V$ have the same dimension $(G: H) \cdot \dim(W)$, we see that $F$ is an isomorphism, which proves the theorem.
