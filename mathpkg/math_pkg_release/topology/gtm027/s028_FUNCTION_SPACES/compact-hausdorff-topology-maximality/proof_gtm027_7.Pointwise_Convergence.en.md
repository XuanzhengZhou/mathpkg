---
role: proof
locale: en
of_concept: compact-hausdorff-topology-maximality
source_book: gtm027
source_chapter: "7"
source_section: "Pointwise Convergence"
---

# Proof of Maximality of Compact Hausdorff Topologies

**Proposition.** Let $F$ be a set equipped with two topologies $\mathfrak{j}$ and $\varphi$ such that $\varphi \subset \mathfrak{j}$ (i.e., $\mathfrak{j}$ is finer than $\varphi$). If $(F, \mathfrak{j})$ is compact and $(F, \varphi)$ is Hausdorff, then $\mathfrak{j} = \varphi$.

*Proof.* Consider the identity map

\[
i : (F, \mathfrak{j}) \to (F, \varphi), \qquad i(f) = f.
\]

Since $\varphi \subset \mathfrak{j}$, every $\varphi$-open set is also $\mathfrak{j}$-open; thus the inverse image under $i$ of any $\varphi$-open set is $\mathfrak{j}$-open. Hence $i$ is continuous.

The map $i$ is bijective (it is the identity on the underlying set $F$). The domain $(F, \mathfrak{j})$ is compact by hypothesis, and the codomain $(F, \varphi)$ is Hausdorff by hypothesis. It is a fundamental result in general topology that a continuous bijection from a compact space onto a Hausdorff space is a homeomorphism (see Theorems 5.6 and 5.8). Therefore $i$ is a homeomorphism, which means that the topologies coincide:

\[
\mathfrak{j} = \varphi.
\]

*Application to function spaces.* Let $\wp$ be the topology of pointwise convergence on a family $F$ of functions on $X$ to a Hausdorff space $Y$. Then $(F, \wp)$ is Hausdorff (because $Y$ is Hausdorff and pointwise limits are unique). If $\mathfrak{j}$ is any topology on $F$ that is finer than $\wp$ (i.e., $\wp \subset \mathfrak{j}$) and for which $(F, \mathfrak{j})$ is compact, then the Proposition yields $\mathfrak{j} = \wp$. Thus a compact Hausdorff topology on $F$ that contains the pointwise topology cannot be strictly larger than the pointwise topology. This maximality property is a key observation motivating the study of the compact-open topology, which is genuinely larger than the pointwise topology but at the cost of compactness. $\square$