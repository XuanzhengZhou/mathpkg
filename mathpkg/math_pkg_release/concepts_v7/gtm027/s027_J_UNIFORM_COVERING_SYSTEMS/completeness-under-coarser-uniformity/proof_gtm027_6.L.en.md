---
role: proof
locale: en
of_concept: completeness-under-coarser-uniformity
source_book: gtm027
source_chapter: "6"
source_section: "L"
---

# Proof of Completeness Inheritance Under Coarser Uniformities

Let $\mathfrak{U}$ and $\mathfrak{V}$ be uniformities for $X$ such that $\mathfrak{V} \subset \mathfrak{U}$. Suppose $(X, \mathfrak{U})$ is complete and the topology of $\mathfrak{V}$ is identical with that of $\mathfrak{U}$.

Let $\{x_\alpha, \alpha \in D\}$ be a Cauchy net relative to $\mathfrak{V}$. Since $\mathfrak{V} \subset \mathfrak{U}$, this net is also Cauchy relative to $\mathfrak{U}$. By completeness of $(X, \mathfrak{U})$, there exists $x \in X$ such that $x_\alpha \to x$ in the topology of $\mathfrak{U}$. Since the topologies coincide, $x_\alpha \to x$ in the topology of $\mathfrak{V}$. It remains to show that the net converges to $x$ relative to the uniformity $\mathfrak{V}$.

Take any $V \in \mathfrak{V}$. By the uniform space axioms, there exists a symmetric $W \in \mathfrak{V}$ with $W \circ W \subset V$. Since $x_\alpha \to x$ in the topology of $\mathfrak{V}$, there exists $\alpha_0$ such that $x_\alpha \in W[x]$ for all $\alpha \geq \alpha_0$. Since the net is Cauchy relative to $\mathfrak{V}$, there exists $\alpha_1$ such that $(x_\alpha, x_\beta) \in W$ for all $\alpha, \beta \geq \alpha_1$. Choose $\alpha_2$ with $\alpha_2 \geq \alpha_0, \alpha_1$. Then for any $\alpha \geq \alpha_2$, we have $(x_\alpha, x) \in W \circ W \subset V$. Therefore $x_\alpha \to x$ relative to $\mathfrak{V}$, and $(X, \mathfrak{V})$ is complete.

Hence a completely regular space is topologically complete iff it is complete relative to the largest uniformity whose topology is $\mathfrak{J}$.
