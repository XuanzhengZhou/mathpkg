---
role: proof
locale: en
of_concept: theorem-9
source_book: gtm026
source_chapter: "1"
source_section: "2.18"
---

(1) implies (2). Let $(KF, K\eta)$ be free over $K$ with respect to $U$. Given $f: K \longrightarrow L$ in $\mathcal{K}$, the universal property forces the definition of

2. Free Objects

$fF:KF \longrightarrow LF$ so as to make $\eta: \text{id}_{\mathcal{K}} \longrightarrow FU$ a natural transformation:

The functorial equations, $(f.g)F = fF.gF$ and $(\text{id}_K)F = \text{id}_{KF}$, are immediate consequences of the universal property. The first triangle in 2.16 forces us to define $\varepsilon$ by $A\varepsilon = (\text{id}_{AU})^{\#}$:

Of general interest, is the formula

(2.19) For all $f:K \longrightarrow AU, f^{\#} = fF.A\varepsilon$, which is seen from

Finally, look at the two diagrams:

The first shows that $A\varepsilon.f = (fU)^{\#} = fUF.B\varepsilon$ for all $f:A \longrightarrow B$ in $\mathcal{A}$, that is, that $\varepsilon$ is natural; the second establishes the second triangle in 2.16 by showing that $\eta F.F\varepsilon = (\text{id}_{FU})^{\#}$.

(2) implies (1). Let $(\mathcal{A}, \mathcal{K}, U, F, \eta, \varepsilon)$ be an adjointness and let $K$ be an object in $\mathcal{K}$. We wish to show that $(KF, K\eta)$ is free over $K$ with respect to $U$. Let $f:K \longrightarrow AU$ be given. We expect that $f^{\#}$ will be defined as in (2.19), so define $f^{\#}$ that way. The diagram

proves that $K\eta.f^{\#} = f$. Suppose also, $\psi: KF \longrightarrow A$ satisfies $K\eta.\psi U = f$. Then

proves that $\psi = f^{\#}$. $\square$

With the help of 2.17 we see that the dual of 2.18 reads as follows:
