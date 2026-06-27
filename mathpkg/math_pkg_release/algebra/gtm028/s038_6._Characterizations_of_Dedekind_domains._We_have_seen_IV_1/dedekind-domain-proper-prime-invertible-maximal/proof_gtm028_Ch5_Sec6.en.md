---
role: proof
locale: en
of_concept: dedekind-domain-proper-prime-invertible-maximal
source_book: gtm028
source_chapter: "V"
source_section: "6"
---

We first show that every invertible proper prime ideal $\mathfrak{p}$ in $R$ is maximal. We consider an element $a$ of $R$, not in $\mathfrak{p}$, and the ideals $\mathfrak{p} + Ra$, $\mathfrak{p} + Ra^2$. As $R$ is a Dedekind domain, we have

$$\mathfrak{p} + Ra = \prod_{i=1}^n \mathfrak{p}_i, \quad \mathfrak{p} + Ra^2 = \prod_{j=1}^m \mathfrak{q}_j,$$

where the $\mathfrak{p}_i$ and the $\mathfrak{q}_j$ are prime ideals.

Let $\bar{R}$ be the residue class ring $R/\mathfrak{p}$, and $\bar{a}$ be the residue class of $a$ modulo $\mathfrak{p}$. We have

$$\bar{R} \cdot \bar{a} = \prod_{i=1}^n (\mathfrak{p}_i/\mathfrak{p}), \quad \bar{R} \cdot \bar{a}^2 = \prod_{j=1}^m (\mathfrak{q}_j/\mathfrak{p}),$$

where the ideals $\mathfrak{p}_i/\mathfrak{p}$ and $\mathfrak{q}_j/\mathfrak{p}$ are prime. By Lemma 4 these prime ideals are invertible. Thus, since $\bar{R} \cdot \bar{a}^2 = (\bar{R} \cdot \bar{a})^2 = \prod_{i=1}^n (\mathfrak{p}_i/\mathfrak{p})^2$, Lemma 5 shows that the ideals $\mathfrak{q}_j/\mathfrak{p}$ are the ideals $\mathfrak{p}_i/\mathfrak{p}$ each repeated twice. Therefore $m = 2n$, and after reordering $\mathfrak{q}_{2i-1} = \mathfrak{q}_{2i} = \mathfrak{p}_i$. This implies $\mathfrak{p} + Ra = \prod_i \mathfrak{p}_i$ and $\mathfrak{p} + Ra^2 = \prod_i \mathfrak{p}_i^2$, hence $\mathfrak{p} + Ra^2 \subset (\mathfrak{p} + Ra)^2$. Consequently $a^2 \in \mathfrak{p} + Ra^2 \subset \mathfrak{p}^2 + \mathfrak{p}Ra + Ra^2$, and since $a^2$ cancels, we obtain $R = \mathfrak{p} + Ra$; thus $\mathfrak{p}$ is maximal.

Having proved that invertible proper prime ideals are maximal, we now show every proper prime ideal $\mathfrak{p}$ is invertible. Since $R$ is a Dedekind domain, $\mathfrak{p} = \prod_i \mathfrak{p}_i$ where the $\mathfrak{p}_i$ are prime ideals. Since each $\mathfrak{p}_i \supset \mathfrak{p}$, by maximality (or minimality) each $\mathfrak{p}_i$ equals $\mathfrak{p}$, and the product must be a single factor $\mathfrak{p}$, which is invertible by the definition of Dedekind domain.
