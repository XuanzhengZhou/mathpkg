---
role: proof
locale: en
of_concept: lebesgue-density-theorem
source_book: gtm002
source_chapter: "3"
source_section: "3. Lebesgue Measure in r-Space"
---

It is sufficient to show that $E - \phi(E)$ is a nullset, since $\phi(E) - E \subset E' - \phi(E')$ and $E'$ (the complement of $E$) is measurable. We may also assume that $E$ is bounded. Furthermore,

$$
E - \phi(E) = \bigcup_{\varepsilon > 0} A_{\varepsilon},
$$

where

$$
A_{\varepsilon} = \left\{ x \in E : \liminf_{h \to 0} \frac{m(E \cap [x - h, x + h])}{2h} < 1 - \varepsilon \right\}.
$$

Hence it is sufficient to show that $A_{\varepsilon}$ is a nullset for every $\varepsilon > 0$. Put $A = A_{\varepsilon}$ and suppose for contradiction that $m^*(A) > 0$.

If $m^*(A) > 0$, there exists a bounded open set $G$ containing $A$ such that

$$
m(G) < \frac{m^*(A)}{1 - \varepsilon}.
$$

Let $\mathcal{E}$ denote the class of all closed intervals $I$ such that $I \subset G$ and

$$
m(E \cap I) \leq (1 - \varepsilon) |I|.
$$

Observe that:
1. $\mathcal{E}$ includes arbitrarily short intervals about each point of $A$, and
2. For any disjoint sequence $\{I_n\}$ of members of $\mathcal{E}$, we have

$$
m^*\left(A \cap \bigcup I_n\right) \leq \sum m(E \cap I_n) \leq (1 - \varepsilon) \sum |I_n|.
$$

One then uses a Vitali-type covering argument to select a disjoint sequence of intervals from $\mathcal{E}$ that covers $A$ up to a nullset. This yields

$$
m^*(A) \leq (1 - \varepsilon) \, m(G) < m^*(A),
$$

a contradiction. Therefore $m^*(A) = 0$, proving the theorem.
