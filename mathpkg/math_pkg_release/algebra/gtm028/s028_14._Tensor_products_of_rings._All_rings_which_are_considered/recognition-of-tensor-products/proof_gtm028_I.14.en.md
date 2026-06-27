---
role: proof
locale: en
of_concept: recognition-of-tensor-products
source_book: gtm028
source_chapter: "I"
source_section: "14. Tensor products of rings"
---

Let $f: C \to C'$ be a homomorphism such that $f\varphi = \varphi'$ and $f\psi = \psi'$, where $(C', \varphi', \psi')$ is a tensor product. Since $(C', \varphi', \psi')$ is a tensor product, by Theorem 34 there exists a homomorphism $g: C' \to C$ such that $g\varphi' = \varphi$ and $g\psi' = \psi$. Then $gf$ is a homomorphism of $C$ into itself which is the identity on $A\varphi$ and $B\psi$. Since $C = [A\varphi, B\psi]$, it follows that $gf$ is the identity on $C$. Similarly, $fg$ is the identity on $C'$. Hence $f$ is an isomorphism.

Now to show that $(C, \varphi, \psi)$ is a tensor product: given any two $k$-homomorphisms $g_0: A \to R$ and $h_0: B \to R$, since $(C', \varphi', \psi')$ is a tensor product, there exists a homomorphism $f_0: C' \to R$ with $f_0\varphi' = g_0$ and $f_0\psi' = h_0$. Then $f_0 \circ f: C \to R$ satisfies $(f_0 \circ f)\varphi = f_0\varphi' = g_0$ and $(f_0 \circ f)\psi = f_0\psi' = h_0$. By Theorem 34, $(C, \varphi, \psi)$ is a tensor product.
