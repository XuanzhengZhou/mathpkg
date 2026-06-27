---
role: proof
locale: en
of_concept: free-objects-adjointness-equivalence
source_book: gtm026
source_chapter: "2"
source_section: "2.15"
---

**(1) implies (2).** Let $(KF, K\eta)$ be free over $K$ with respect to $U$. Given $f: K \longrightarrow L$ in $\mathcal{K}$, the universal property forces the definition of $fF: KF \longrightarrow LF$ so as to make $\eta: \text{id}_{\mathcal{K}} \longrightarrow FU$ a natural transformation.

The functorial equations, $(f \circ g)F = fF \circ gF$ and $(\text{id}_K)F = \text{id}_{KF}$, are immediate consequences of the universal property.

The first triangle in 2.16 forces us to define $\varepsilon$ by $A\varepsilon = (\text{id}_{AU})^{\#}$.

Of general interest is the formula

$$
\tag{2.19}
f^{\#} = fF \circ A\varepsilon \qquad \text{for all } f: K \longrightarrow AU,
$$

which is seen from the diagram. One verifies that $A\varepsilon \circ f = (fU)^{\#} = fUF \circ B\varepsilon$ for all $f: A \longrightarrow B$ in $\mathcal{A}$, establishing that $\varepsilon$ is natural. The second triangle in 2.16 is established by showing that $\eta F \circ F\varepsilon = (\text{id}_{FU})^{\#}$.

**(2) implies (1).** Let $(\mathcal{A}, \mathcal{K}, U, F, \eta, \varepsilon)$ be an adjointness and let $K$ be an object in $\mathcal{K}$. We wish to show that $(KF, K\eta)$ is free over $K$ with respect to $U$. Let $f: K \longrightarrow AU$ be given. Define $f^{\#}$ as in (2.19):

$$
f^{\#} = fF \circ A\varepsilon.
$$

The diagram then proves that

$$
K\eta \circ f^{\#}U = f.
$$

Suppose also $\psi: KF \longrightarrow A$ satisfies $K\eta \circ \psi U = f$. Then

$$
\psi = (\text{id}_{KF})^{\#} \circ \psi = \cdots = f^{\#},
$$

proving uniqueness. $\square$
