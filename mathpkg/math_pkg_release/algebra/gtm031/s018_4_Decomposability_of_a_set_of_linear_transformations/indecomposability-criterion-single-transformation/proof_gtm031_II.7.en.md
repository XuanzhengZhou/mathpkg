---
role: proof
locale: en
of_concept: indecomposability-criterion-single-transformation
source_book: gtm031
source_chapter: "II"
source_section: "7"
---

($\Rightarrow$) Suppose $A$ is indecomposable. If $f$ is a non-zero vector in $\mathfrak{R}$, then the cyclic subspace $\{f\}$ is an invariant subspace $\neq 0$. Let $\mu_f(\lambda)$ be the order of $f$ and suppose $\mu_f(\lambda) = \pi(\lambda)\nu(\lambda)$ where $\pi(\lambda)$ is irreducible, has positive degree, and leading coefficient $1$. Then $g = f\nu(A)$ has order $\pi(\lambda)$. Thus $\mathfrak{R}$ contains a vector whose order is a prime (irreducible polynomial).

Since $A$ is indecomposable, we must have $\mathfrak{R} = \{g\}$ where $\mu_g(\lambda) = \pi(\lambda)^k$ for some irreducible $\pi$ and $k \geq 1$. For if $\mathfrak{R}$ properly contained $\{g\}$, indecomposability would be contradicted. To see that $k > 1$ is possible: suppose $\mathfrak{R} = \mathfrak{R}_1 \oplus \mathfrak{R}_2$ is a proper decomposition with $\mathfrak{R}_i$ invariant. Let $\mu_i(\lambda)$ be the minimum polynomial of the transformation induced by $A$ in $\mathfrak{R}_i$. Since $x_i\pi(A)^k = 0$ for all $x_i \in \mathfrak{R}_i$, we have $\mu_i(\lambda) \mid \pi(\lambda)^k$, so $\mu_i(\lambda) = \pi(\lambda)^{k_i}$ with $k_i \leq k$. Now $x_i\pi(A)^{k_i} = 0$ for all $x_i \in \mathfrak{R}_i$, implying that if $\bar{k} = \max(k_1, k_2)$, then $\pi(A)^{\bar{k}} = 0$. Thus $\bar{k} = k$ and we may suppose $k_1 = k$. This means the minimum polynomial of $A$ in $\mathfrak{R}_1$ is $\pi(\lambda)^k$. Consequently there exists a vector $f_1$ in $\mathfrak{R}_1$ whose order is $\pi(\lambda)^k$. Then $\dim \{f_1\} = \deg \pi(\lambda)^k = \dim \mathfrak{R}$. Hence $\{f_1\} = \mathfrak{R}$ and since $\{f_1\} \subseteq \mathfrak{R}_1$, $\mathfrak{R}_1 = \mathfrak{R}$. Thus the decomposition $\mathfrak{R} = \mathfrak{R}_1 \oplus \mathfrak{R}_2$ is not proper, contradicting decomposability. Therefore $A$ is cyclic with minimum polynomial a power of a prime.

($\Leftarrow$) Conversely, suppose $\mathfrak{R} = \{g\}$ is cyclic with $\mu_g(\lambda) = \pi(\lambda)^k$ where $\pi$ is irreducible. Let $\mathfrak{S}$ be a subspace $\neq 0$ invariant under $A$. If $h \in \mathfrak{S}$ is non-zero, its order $\mu_h(\lambda)$ is a factor of $\pi(\lambda)^k$, so $\mu_h(\lambda) = \pi(\lambda)^j$ for some $j \leq k$. If $j = k$, then $\dim \{h\} = \deg \pi(\lambda)^k = \dim \mathfrak{R}$, so $\{h\} = \mathfrak{R}$ and $\mathfrak{S} = \mathfrak{R}$. It follows that any proper invariant subspace would have to consist of vectors of order $\pi(\lambda)^j$ with $j < k$, but such vectors cannot span the whole space. Hence no proper decomposition exists, and $A$ is indecomposable. $\square$
