---
role: proof
locale: en
of_concept: morphisms-of-affine-varieties-correspond-to-algebra-homomorphisms
source_book: gtm052
source_chapter: "I"
source_section: "3"
---

First, suppose $\varphi: X \to Y$ is a morphism of affine varieties. Then for any regular function $f \in \mathcal{O}(Y)$, the composition $f \circ \varphi$ is a regular function on $X$ by definition of a morphism. This defines a map $h: \mathcal{O}(Y) \to \mathcal{O}(X)$ given by $h(f) = f \circ \varphi$. This is clearly a $k$-algebra homomorphism. By Theorem 3.2(a), $\mathcal{O}(Y) \cong A(Y)$ and $\mathcal{O}(X) \cong A(X)$, so we obtain a $k$-algebra homomorphism $h: A(Y) \to A(X)$.

Conversely, suppose we are given a $k$-algebra homomorphism $h: A(Y) \to A(X)$. Let $Y \subseteq \mathbf{A}^n$ with coordinates $x_1, \ldots, x_n$, so $A(Y) = k[x_1, \ldots, x_n]/I(Y)$. Let $\bar{x}_i$ be the image of $x_i$ in $A(Y)$. Define $a_i = h(\bar{x}_i) \in A(X)$. Since $A(X) \cong \mathcal{O}(X)$ by Theorem 3.2(a), each $a_i$ is a regular function on $X$. Then define a map $\psi: X \to \mathbf{A}^n$ by

$$\psi(P) = (a_1(P), \ldots, a_n(P)).$$

For any $f \in I(Y)$, we have $f(\bar{x}_1, \ldots, \bar{x}_n) = 0$ in $A(Y)$, hence $h(f(\bar{x}_1, \ldots, \bar{x}_n)) = f(a_1, \ldots, a_n) = 0$ in $A(X)$, which means $f(a_1(P), \ldots, a_n(P)) = 0$ for all $P \in X$. Thus $\psi(P) \in Y$ for all $P$, so $\psi$ defines a map $X \to Y$.

To complete the proof, we must show $\psi$ is a morphism. This follows from Lemma 3.6, since the coordinate functions $x_i \circ \psi = a_i$ are regular functions on $X$. Hence $\psi$ is a morphism, and the correspondence is established.
