---
role: proof
locale: en
of_concept: universal-property-of-tensor-product
source_book: gtm028
source_chapter: "I"
source_section: "14. Tensor products of rings"
---

Every element $\xi$ of $C$ has an expression of the form $\xi = \sum_i \varphi(a_i)\psi(b_i)$, where $a_i \in A$ and $b_i \in B$. We set

$$f(\xi) = \sum_i g(a_i)h(b_i).$$

Then $f$ is a transformation of $C$ into $R$ (perhaps not single-valued) which satisfies the following two conditions:
\begin{enumerate}
  \item[(a)] for any $\xi$ in $C$ the set $f(\xi)$ is non-empty;
  \item[(b)] if $u \in f(\xi)$ and $v \in f(\eta)$, then $u + v \in f(\xi + \eta)$ and $uv \in f(\xi\eta)$.
\end{enumerate}

It follows from Lemma 2 of I, §11, that $f$ can be asserted to be univalent (and hence a homomorphism), provided the set $f(0)$ contains only the zero of $R$. We shall show now that this last condition is indeed satisfied if $(C, \varphi, \psi)$ is a tensor product of $A$ and $B$, and this will prove the necessity of the condition since we have $f = \varphi^{-1}g$ on $A\varphi$ and $f = \psi^{-1}h$ on $B\psi$.

Let $0 = \sum_i \varphi(a_i)\psi(b_i)$ be an expression of the zero in $C$. We fix a basis $\{x_\alpha\}$ of the vector space $\sum k a_i$ (over $k$) and a basis $\{y_\beta\}$ of the vector space $\sum k b_i$, and we express the $a_i$ and the $b_i$ in terms of these basis elements:

$$a_i = \sum_\alpha c_{i\alpha} x_\alpha, \quad b_i = \sum_\beta d_{i\beta} y_\beta,$$

with $c_{i\alpha}, d_{i\beta} \in k$. Then

$$0 = \sum_i \varphi(a_i)\psi(b_i) = \sum_{\alpha,\beta} \left(\sum_i c_{i\alpha} d_{i\beta}\right) \varphi(x_\alpha)\psi(y_\beta).$$

By the definition of a tensor product, the products $\varphi(x_\alpha)\psi(y_\beta)$ are linearly independent over $k$. Therefore $\sum_i c_{i\alpha} d_{i\beta} = 0$ for all $\alpha, \beta$. Consequently,

$$f(0) = \sum_i g(a_i)h(b_i) = \sum_{\alpha,\beta} \left(\sum_i c_{i\alpha} d_{i\beta}\right) g(x_\alpha)h(y_\beta) = 0.$$

Thus $f(0) = \{0\}$, and $f$ is a well-defined homomorphism.

Conversely, if the condition is satisfied, then taking $R = C'$ for any tensor product $(C', \varphi', \psi')$ and setting $g = \varphi'$, $h = \psi'$, we obtain a homomorphism $f: C \to C'$ with $f\varphi = \varphi'$ and $f\psi = \psi'$. Since $C = [A\varphi, B\psi]$, $f$ is surjective. By symmetry we also get a homomorphism $f': C' \to C$, and the composition $f'f$ is the identity on the generators, hence on all of $C$. Thus $f$ is an isomorphism and $(C, \varphi, \psi)$ is a tensor product.
