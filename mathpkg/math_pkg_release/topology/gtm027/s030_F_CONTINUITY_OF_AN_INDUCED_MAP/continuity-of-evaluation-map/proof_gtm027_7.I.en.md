---
role: proof
locale: en
of_concept: continuity-of-evaluation-map
source_book: gtm027
source_chapter: "7"
source_section: "I"
---

# Proof of Continuity of the Evaluation Map

Let $(X, \mathcal{U})$ and $(Y, \mathcal{V})$ be uniform spaces. Let $F$ be a family of functions from $X$ to $Y$, and let $G$ be a family of functions from $F$ to $Y$ endowed with the uniformity of uniform convergence on members of a family $\alpha$ of subsets of $F$. The evaluation map $E : X \to G$ is defined by

$$E(x)(f) = f(x), \qquad x \in X, \; f \in F.$$

We prove that $E$ is continuous if each member of $\alpha$ is equicontinuous.

Take $x_0 \in X$ and a basic entourage for the uniformity on $G$. Such an entourage is determined by a set $A \in \alpha$ and $V \in \mathcal{V}$:

$$W(A, V) = \{(g_1, g_2) \in G \times G : (g_1(f), g_2(f)) \in V \text{ for all } f \in A\}.$$

We need a neighborhood $U$ of $x_0$ in $X$ such that $E(U) \times E(U) \subseteq W(A, V)$, i.e., for all $x_1, x_2 \in U$ and all $f \in A$,

$$(E(x_1)(f), E(x_2)(f)) = (f(x_1), f(x_2)) \in V.$$

Since $A \in \alpha$ is equicontinuous, $A$ is equicontinuous at $x_0$. Choose a symmetric $V_0 \in \mathcal{V}$ with $V_0 \circ V_0 \subseteq V$. By equicontinuity of $A$ at $x_0$, there exists a neighborhood $U$ of $x_0$ (depending on $V_0$ and $A$) such that for all $f \in A$ and $x \in U$,

$$(f(x_0), f(x)) \in V_0.$$

Then for any $x_1, x_2 \in U$ and $f \in A$,

$$(f(x_1), f(x_2)) \in V_0 \circ V_0 \subseteq V.$$

Thus $(E(x_1), E(x_2)) \in W(A, V)$ for all $x_1, x_2 \in U$, proving that $E$ is uniformly equicontinuous and hence continuous.
