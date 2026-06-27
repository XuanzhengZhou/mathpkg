---
role: proof
locale: en
of_concept: internal-direct-product-of-subgroups
source_book: gtm030
source_chapter: "2"
source_section: "14"
---

Condition (2) implies that for each $\alpha$, every element of $\mathfrak{G}_{\alpha}'$ commutes with every element of $\mathfrak{G}_{\beta}'$ for $\beta \neq \alpha$, since $\mathfrak{G}_{\alpha}'$ and $\mathfrak{G}_{\beta}'$ are invariant subgroups intersecting trivially. Condition (1) guarantees that every $g \in \mathfrak{G}$ can be expressed as a finite product $g = g_{\alpha_1} \cdots g_{\alpha_n}$ with $g_{\alpha_i} \in \mathfrak{G}_{\alpha_i}'$ and distinct indices $\alpha_i$. The mapping

$$\varphi: \prod_{\alpha \in J} \mathfrak{G}_{\alpha}' \to \mathfrak{G}$$

defined by $\varphi((\cdots, g_{\alpha}, \cdots)) = \prod_{\alpha} g_{\alpha}$ (a finite product since only finitely many $g_{\alpha} \neq 1$) is a homomorphism because elements from distinct factors commute. It is surjective by condition (1). Injectivity follows from condition (2): if $\prod_{\alpha} g_{\alpha} = 1$, then each $g_{\alpha} = 1$, for otherwise some $g_{\alpha}$ would be a non-identity element in $\mathfrak{G}_{\alpha}' \cap \prod_{\beta \neq \alpha} \mathfrak{G}_{\beta}'$.
