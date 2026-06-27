---
role: proof
locale: en
of_concept: product-uniformity-topology
source_book: gtm027
source_chapter: "6"
source_section: "Uniform Spaces"
---

# Proof that the Topology of the Product Uniformity is the Product Topology (Theorem 6.10)

**Theorem 6.10.** The topology of the product uniformity is the product topology.

A function $f$ on a uniform space to a product of uniform spaces is uniformly continuous if and only if the composition of $f$ with each projection into a coordinate space is uniformly continuous.

**Proof.** Let $\{(X_a, \mathcal{U}_a) : a \in A\}$ be a family of uniform spaces. The product uniformity on $\prod_{a \in A} X_a$ has as a subbase all sets of the form

$$\{(x,y) : (x_a, y_a) \in U\}$$

where $a \in A$ and $U \in \mathcal{U}_a$. For a fixed point $x = (x_a)_{a \in A}$, the section of such a subbase set is

$$\{y : (x_a, y_a) \in U\} = \{y : y_a \in U[x_a]\}.$$

Thus a subbase for the neighborhood system of $x$ in the product uniformity topology consists of all sets of the form $\{y : y_a \in U[x_a]\}$ for $a \in A$ and $U \in \mathcal{U}_a$. A base for the neighborhood system is then the family of finite intersections of such sets, i.e.,

$$\bigcap_{i=1}^{n} \{y : y_{a_i} \in U_i[x_{a_i}]\} = \prod_{a \in A} T_a$$

where $T_{a_i} = U_i[x_{a_i}]$ and $T_a = X_a$ otherwise. But this is precisely a basic open set in the product topology. Hence the two topologies coincide.

For the second statement: if $f$ is uniformly continuous, then each projection $P_a$ is uniformly continuous (by construction of the product uniformity), so $P_a \circ f$ is uniformly continuous. Conversely, if $P_a \circ f$ is uniformly continuous for each $a$, then for any subbase member $\{(x,y) : (x_a, y_a) \in U\}$ of the product uniformity, its inverse image under $f_2$ is

$$f_2^{-1}[\{(x,y) : (x_a, y_a) \in U\}] = \{(u,v) : (P_a \circ f(u), P_a \circ f(v)) \in U\}$$

which belongs to the uniformity of the domain of $f$ because $P_a \circ f$ is uniformly continuous. Since the inverse image of each subbase member belongs to the domain uniformity, $f$ is uniformly continuous.
