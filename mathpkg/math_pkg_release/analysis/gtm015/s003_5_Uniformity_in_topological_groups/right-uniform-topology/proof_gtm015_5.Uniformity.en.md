---
role: proof
locale: en
of_concept: right-uniform-topology
source_book: gtm015
source_chapter: "5"
source_section: "Uniformity in topological groups"
---

# Proof of Right uniform topology coincides with given topology

Let $G$ be a topological group and let $(G, \mathcal{U}_r)$ be its right uniform structure. Write $G'$ for the group $G$ equipped with the opposite multiplication, as in (5.15). The right uniformity of $G$ is by definition the left uniformity of $G'$.

By (5.10), the topology derived from the left uniformity of any topological group coincides with its given topology. Applying this to $G'$, the topology derived from $\mathcal{U}_r$ coincides with the given topology on $G'$, which is the same as the given topology on $G$.

Moreover, for any entourage $V_r \in \mathcal{U}_r$, the neighborhood of a point $x$ is

$$V_r(x) = \{y : (x, y) \in V_r\} = \{y : yx^{-1} \in V\} = \{y : y \in Vx\} = Vx.$$

Thus the right-uniform neighborhoods of $x$ are precisely the right translates $Vx$ of neighborhoods $V$ of $e$.
