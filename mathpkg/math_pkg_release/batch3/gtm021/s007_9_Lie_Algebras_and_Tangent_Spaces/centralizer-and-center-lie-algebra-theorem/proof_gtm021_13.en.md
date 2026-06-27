---
role: proof
locale: en
of_concept: centralizer-and-center-lie-algebra-theorem
source_book: gtm021
source_chapter: "13"
source_section: "Correspondence Between Groups and Lie Algebras"
---
(a) Proposition 10.6 shows that equality holds when $G = \operatorname{GL}(n, K)$, $\mathfrak{g} = \mathfrak{gl}(n, K)$. In general, embed $G$ as a closed subgroup of some $\operatorname{GL}(n, K)$ (Theorem 8.6). Then
$$C_G(x) = G \cap C_{\operatorname{GL}(n, K)}(x),$$
while
$$\mathfrak{c}_{\mathfrak{g}}(x) = \mathfrak{g} \cap \mathfrak{c}_{\mathfrak{gl}(n, K)}(x).$$
Since Theorem 12.5 (on intersections) holds in characteristic 0, we obtain
$$\mathcal{L}(C_G(x)) = \mathcal{L}(G \cap C_{\operatorname{GL}(n, K)}(x)) = \mathfrak{g} \cap \mathfrak{c}_{\mathfrak{gl}(n, K)}(x) = \mathfrak{c}_{\mathfrak{g}}(x).$$

(b) Since $Z(G) \subset \operatorname{Ker} \operatorname{Ad}$ always holds (if $x \in Z(G)$, then $\operatorname{Int} x = \operatorname{id}$, so $\operatorname{Ad} x = \operatorname{id}$), we have $\mathfrak{z}(\mathfrak{g}) \subset \mathcal{L}(\operatorname{Ker} \operatorname{Ad})$.

Separability of morphisms (char 0) implies $\mathcal{L}(\operatorname{Ker} \operatorname{Ad}) = \operatorname{Ker} d(\operatorname{Ad}) = \operatorname{Ker} \operatorname{ad} = \mathfrak{z}(\mathfrak{g})$. So $\mathcal{L}(\operatorname{Ker} \operatorname{Ad}) = \mathfrak{z}(\mathfrak{g})$.

Now $Z(G) \subset \operatorname{Ker} \operatorname{Ad}$ and $\mathcal{L}(Z(G)) \subset \mathfrak{z}(\mathfrak{g})$ (since $\operatorname{ad} X = 0$ for $X \in \mathcal{L}(Z(G))$ by differentiating the condition $xy = yx$). But also $\mathfrak{z}(\mathfrak{g}) = \mathcal{L}(\operatorname{Ker} \operatorname{Ad})$, and $Z(G)^\circ$ and $(\operatorname{Ker} \operatorname{Ad})^\circ$ have the same Lie algebra $\mathfrak{z}(\mathfrak{g})$, so by Theorem 13.1 they coincide. Since $Z(G)$ and $\operatorname{Ker} \operatorname{Ad}$ differ at most by a finite group (they have the same identity component), and in characteristic 0 one can argue that the equality $Z(G) = \operatorname{Ker} \operatorname{Ad}$ holds.

More precisely: $Z(G)$ is the kernel of the morphism $G \to \operatorname{Aut}(\mathfrak{g})$ given by $\operatorname{Ad}$, and since $\operatorname{char} K = 0$, separability ensures the scheme-theoretic kernel equals the group-theoretic kernel, which is $Z(G)$.
