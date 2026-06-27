---
locale: en
of_concept: with-the-above-notations-let-u-ia-represent-the-morphism-u-x
role: proof
source_book: gtm020
source_chapter: 5. Local Coordinate Description of Fibre Bundles
source_section: '2'
---

For $z \in U_a \cap V_i \cap W_r$, we have $(z, w_{r,a}(z)x) = (h''_r)^{-1}vuh_a(z, x) = ((h''_r)^{-1}vh'_i)((h'_i)^{-1}uh_a)(z, x) = ((h''_r)^{-1}vh'_i)(z, u_{i,a}(z)x) = (z, v_{r,i}(z)u_{i,a}(z)x)$. This proves the desired result.

In (5.2), the $w_{r,a}: U_a \cap W_r \rightarrow \mathbf{L}(F^n, F^q)$ are determined by the relation $w_{r,a}(z) = v_{r,i}(z)u_{i,a}(z)$ for $z \in U_a \cap V_i \cap W_r$.

The result 3(2.5) is an immediate corollary of the analysis in (5.1) and (5.2).

6. Operations on Vector Bund

Proof. We carry out the proof for the case $p = q = 1$. Let $\xi$ and $\xi'$ be two vector bundles over $B$ with local coordinate charts $\{(U_a, h_a)\}$ and $\{(U_a, k_a)\}$ with transition functions $\{g_{a,b}\}$ and $\{f_{a,b}\}$ for $a, b \in A$. We define $F_B(\xi, \xi')$ to be a vector bundle with the (continuous) transition functions $\{F_B(g_{a,b}, f_{b,a})\}$ for $a, b \in A$.

If $u: \xi \rightarrow \eta$ and $u': \eta' \rightarrow \xi'$ are morphisms, they are represented by $\{u_{i,a}\}$ and $\{u'_{i,a}\}$, respectively, where $\{(V_i, h_i')\}$ and $\{(V_i, k_i')\}$ are atlases of $\eta$ and $\eta'$, respectively. Then the family of maps $F(u_{i,a}, u'_{i,a})$ defines a morphism $F_B(\xi, \xi') \rightarrow F_B(\eta, \eta')$, by (5.1), which is denoted $F_B(u, u')$. Since $F$ is a functor, it preserves the compatibility condition (C) of Proposition (5.1). Clearly, $F_B(1, 1) = 1$ by the remark following Proposition (5.1). With Proposition (5.2), we see that $F_B(vu, u'v') = F_B(v, v')F_B(u, u')$ by applying $F$ to the local morphisms representing $u, u', v$, and $v'$, where $v: \eta \rightarrow \zeta$ and $v': \zeta' \rightarrow \eta'$ are morphisms.

Finally, for a map $f: B_1 \rightarrow B$ we find that $F_{B_1}(f^*(\xi), f^*(\xi'))$ and $f^*(F_B(\xi, \xi'))$ are $B_1$-isomorphic. For this, observe that $\{

6.6 Example. If $\xi$ and $\eta$ are two vector bundles over $B$, the Whitney sum $\xi \oplus \eta$ is the prolongation to vector bundles of the direct sum functor. This follows from the fact that the fibre of $\xi \oplus \eta$ over a point of $B$ is the direct sum of the fibres of $\xi$ and of $\eta$. The usual properties of direct sums of vector spaces prolong to Whitney sums of vector bundles, by (6.3) and (6.4). There are the following isomorphisms, for example:

$$\xi \oplus \eta \cong \eta \oplus \xi \quad \text{and} \quad \xi \oplus (\eta \oplus \zeta) \cong (\xi \oplus \eta) \oplus \zeta$$

6.7 Example. The tensor product functor is continuous and, in view of (6.2), we may define the tensor product $\xi \otimes \eta$ of two vector bundles over $B$. If $u: \xi \oplus \eta \rightarrow \zeta$ is a bundle map that is bilinear on each fibre $b \in B$, then $u$ defines a vector bundle morphism $v: \xi \otimes \eta \rightarrow \zeta$ which is the usual factorization of bilinear maps through the tensor product on each fibre. Using (6.3) and (6.4), we have the following isomorphisms:

$$\xi \otimes \eta \cong \eta \otimes \xi \quad \xi \otimes (\eta \otimes \zeta) \cong (\xi \otimes \eta) \otimes \zeta$$
$$\xi \otimes \theta^1 \cong \xi \quad \text{and} \quad \xi \otimes (\eta \oplus \zeta) \cong (\xi \otimes \eta) \oplus (\xi \otimes \zeta)$$

where $\xi, \eta, \zeta$ are vector bundles over $B$ and $\theta^1$ is the trivial line bundle over $B$. This discussion holds for real and complex vector bundles.

6.8 Example. The
