---
role: proof
locale: en
of_concept: varieties-neighborhood-coincidence
source_book: gtm044
source_chapter: "III"
source_section: "1"
---

# Proof of Varieties Coinciding in a Neighborhood are Equal

**Theorem 3.1.** Let $V_1$ and $V_2$ be varieties in $\mathbb{P}^n(\mathbb{C})$ or in $\mathbb{C}^n$, each of whose irreducible components contains a given point $P$; if there is an open neighborhood $U$ of $\mathbb{P}^n(\mathbb{C})$ or $\mathbb{C}^n$ about $P$ such that $V_1 \cap U = V_2 \cap U$, then $V_1 = V_2$.

*Proof.* If $V_1$ and $V_2$ are both irreducible, then the theorem follows at once from Theorem 2.11 of Chapter IV (which states that two irreducible varieties which agree on a nonempty open subset are identical). In the general case, decompose $V_1$ and $V_2$ into their irreducible components:

$$V_1 = \bigcup_{\alpha} W_{1,\alpha}, \qquad V_2 = \bigcup_{\beta} W_{2,\beta}.$$

By hypothesis, each irreducible component of $V_1$ contains $P$. Fix a component $W_{1,\alpha}$ of $V_1$. Since $P \in W_{1,\alpha}$ and $P \in U$, the intersection $W_{1,\alpha} \cap U$ is a nonempty open subset of the irreducible variety $W_{1,\alpha}$. From $V_1 \cap U = V_2 \cap U$, we have

$$W_{1,\alpha} \cap U \subset V_1 \cap U = V_2 \cap U = \bigcup_{\beta} (W_{2,\beta} \cap U).$$

Since $W_{1,\alpha}$ is irreducible and $W_{1,\alpha} \cap U$ is dense in $W_{1,\alpha}$, the irreducibility of $W_{1,\alpha}$ implies that $W_{1,\alpha} \cap U \subset W_{2,\beta} \cap U$ for some $\beta$, and hence (by density of $W_{1,\alpha} \cap U$ in $W_{1,\alpha}$) we obtain $W_{1,\alpha} \subset W_{2,\beta}$. By symmetry, each irreducible component of $V_2$ is contained in some irreducible component of $V_1$. Therefore $V_1 = V_2$. $\square$
