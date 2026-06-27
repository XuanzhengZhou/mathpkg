---
role: proof
locale: en
of_concept: existence-of-inverse-bundle
source_book: gtm033
source_chapter: "3"
source_section: "3. The Classification of Vector Bundles"
---

# Proof of Existence of Inverse Bundle (Theorem 3.3)

Let $\xi$ be a $C^r$ $k$-plane bundle over an $n$-manifold $M$. By Theorem 3.1, the zero monomorphism (defined on the empty closed set) extends to a $C^r$ monomorphism

$$F: \xi \hookrightarrow M \times \mathbb{R}^{k+n}$$

over $1_M$. Concretely, Theorem 3.1 with $s = k + n$ and the empty closed set guarantees the existence of a global monomorphism into the trivial bundle of fiber dimension $k + n$, since $k + n \geqslant k + \dim M = k + n$ (the dimension condition holds with equality).

Now endow the trivial bundle $M \times \mathbb{R}^{k+n}$ with its standard Euclidean orthogonal structure (the usual inner product on each fiber $\{x\} \times \mathbb{R}^{k+n}$). Define $\eta$ to be the orthogonal complement subbundle of the image of $F$:

$$\eta = F(\xi)^\perp \subset M \times \mathbb{R}^{k+n}.$$

That is, for each $x \in M$, the fiber $\eta_x$ is the orthogonal complement of the $k$-dimensional subspace $F(\xi_x)$ in $\mathbb{R}^{k+n}$. Since $F$ is a $C^r$ monomorphism, $F(\xi)$ is a $C^r$ $k$-dimensional subbundle of $M \times \mathbb{R}^{k+n}$, and its orthogonal complement $\eta$ is a $C^r$ $(n+k - k) = n$-dimensional subbundle.

By construction, the fiberwise orthogonal decomposition

$$\mathbb{R}^{k+n} = F(\xi_x) \oplus \eta_x$$

holds for all $x \in M$. This gives an orthogonal splitting of the total bundle, hence a $C^r$ vector bundle isomorphism

$$\xi \oplus \eta \cong_r M \times \mathbb{R}^{k+n},$$

where the isomorphism sends $(v, w) \in \xi_x \oplus \eta_x$ to $F(v) + w \in \mathbb{R}^{k+n}$. Thus $\eta$ is the desired complementary $n$-plane bundle. $\square$
