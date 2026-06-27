---
role: proof
locale: en
of_concept: reflexivity-weak-compactness
source_book: gtm015
source_chapter: "IV"
source_section: "45"
---

# Proof of Reflexivity and Weak Compactness of the Unit Ball

Let $E$ be a normed space over $\mathbb{K}$ and let $E_0$ be the image of $E$ in $E''$ under the canonical embedding $x \mapsto x''$. Denote by $S = \{x \in E : \|x\| \leq 1\}$ the closed unit ball of $E$, and by $B = \{\varphi \in E'' : \|\varphi\| \leq 1\}$ the closed unit ball of $E''$. Let $T: E \to E''$ be the canonical embedding.

($\Rightarrow$) Suppose $E$ is a reflexive Banach space, i.e., $T(E) = E''$. Then $T(S) = B$. By Alaoglu's theorem (44.12), $B$ is weak* compact in $E''$. The mapping $T: (E, \sigma(E, E')) \to (E'', \sigma(E'', E'))$ is a homeomorphism onto its image (it is continuous for these topologies because for each $f \in E'$, $x \mapsto T(x)(f) = f(x)$ is $\sigma(E, E')$-continuous). Since $T(S) = B$ is weak* compact, $S$ is weakly compact.

($\Leftarrow$) Conversely, suppose $S$ is weakly compact. The canonical embedding $T: E \to E''$ maps $(E, \sigma(E, E'))$ continuously into $(E'', \sigma(E'', E'))$. By hypothesis, $S$ is weakly compact, therefore $T(S)$ is weak* compact and hence is weak* closed in $E''$. By Goldstine's theorem (45.3), the weak* closure of $T(S)$ is $B$. Thus $T(S)$ coincides with its weak* closure, so $T(S) = B$. Since $T$ is linear and $T(S) = B$, it follows that $T(E) = E''$, i.e., $E$ is reflexive. $\square$
