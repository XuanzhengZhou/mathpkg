---
role: proof
locale: en
of_concept: krull-schmidt-theorem
source_book: gtm030
source_chapter: "2"
source_section: "13"
---

Suppose that we have already obtained a pairing of $\mathfrak{H}_1, \mathfrak{H}_2, \cdots, \mathfrak{H}_{r-1}$ respectively with $\mathfrak{G}_1, \mathfrak{G}_2, \cdots, \mathfrak{G}_{r-1}$ in such a way that $\mathfrak{G}_i \cong \mathfrak{H}_i$, $i = 1, 2, \cdots, r-1$, and (36) holds for $k \leq r-1$. (At the start we have $r = 1$.) Consider the intermediate decomposition

$$\mathfrak{G} = \mathfrak{H}_1 \times \mathfrak{H}_2 \times \cdots \times \mathfrak{H}_{r-1} \times \mathfrak{G}_r \times \cdots \times \mathfrak{G}_s.$$

Let $\lambda_1, \lambda_2, \cdots, \lambda_s$ be the projections determined by this decomposition and let $\eta_1, \eta_2, \cdots, \eta_t$ be the projections determined by the second decomposition (35). Evidently we have

$$\lambda_r = \left( \sum_{1}^{t} \eta_j \right) \lambda_r = \sum_{1}^{t} \eta_j \lambda_r.$$

For any $x$ in $\mathfrak{G}$, $x\eta_j \in \mathfrak{H}_j$. Let $\bar{\mathfrak{H}}_r = \mathfrak{H}_r \lambda_r$ and $\bar{\mathfrak{H}}_j = \mathfrak{H}_j \lambda_r$ for $j \neq r$. Since $\lambda_r$ maps $\mathfrak{H}_r$ isomorphically onto $\bar{\mathfrak{H}}_r \neq 1$, and $\eta_r$ is an isomorphism of $\mathfrak{H}_r$ onto $\mathfrak{H}_r$, we have that $\lambda_r$ is an isomorphism of $\mathfrak{H}_r$ onto $\bar{\mathfrak{H}}_r$.

Now $\lambda_r$ maps every element of $\mathfrak{H}_1 \times \cdots \times \mathfrak{H}_{r-1} \times \mathfrak{H}_{r+1} \times \cdots \times \mathfrak{H}_s$ onto $1$. Hence, since $\lambda_r$ induces an isomorphism of $\mathfrak{H}_r$,

$$\mathfrak{H}_r \cap (\mathfrak{H}_1 \cdots \mathfrak{H}_{r-1} \mathfrak{H}_{r+1} \cdots \mathfrak{H}_s) = 1.$$

Consider $\mathfrak{G}' \equiv \mathfrak{H}_1 \cdots \mathfrak{H}_r \mathfrak{G}_{r+1} \cdots \mathfrak{G}_s$. By the induction hypothesis and the fact that $\mathfrak{H}_r$ intersects the product of the other factors trivially, we obtain

$$\mathfrak{G}' = \mathfrak{H}_1 \times \cdots \times \mathfrak{H}_r \times \mathfrak{G}_{r+1} \times \cdots \times \mathfrak{G}_s.$$

If $x = x_1 x_2 \cdots x_s$ with $x_i \in \mathfrak{H}_i$ for $i \leq r-1$, $x_j \in \mathfrak{G}_j$ for $j \geq r$, then the mapping

$$\theta: x_1 x_2 \cdots x_s \rightarrow x_1 \cdots x_{r-1}(x_r \eta_r) x_{r+1} \cdots x_s$$

is a normal $M$-endomorphism of $\mathfrak{G}$. Since $\mathfrak{H}_r$ is indecomposable and $\eta_r$ is an isomorphism on it, applying the results of Fitting's lemma and its corollaries, we conclude that $\mathfrak{G}_r \cong \mathfrak{H}_r$ and the pairing can be extended. By induction, $s = t$ and the theorem follows.
