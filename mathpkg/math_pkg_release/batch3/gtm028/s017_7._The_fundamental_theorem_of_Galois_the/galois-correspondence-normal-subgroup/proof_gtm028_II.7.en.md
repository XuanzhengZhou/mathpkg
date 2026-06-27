---
role: proof
locale: en
of_concept: galois-correspondence-normal-subgroup
source_book: gtm028
source_chapter: "II"
source_section: "§7. The fundamental theorem of Galois theory"
---

Let $H = G(K/L)$. If $\tau$ is any element of $G(K/k)$, then the fixed field of the subgroup $\tau H \tau^{-1}$ is $\tau(L)$. Hence, by the Fundamental Theorem, $\tau H \tau^{-1}$ is the subgroup corresponding to the field $\tau(L)$.

If $L$ is a normal extension of $k$, then $\tau(L) = L$ for all $\tau \in G(K/k)$, and consequently $\tau H \tau^{-1} = H$. Thus $H = G(K/L)$ is an invariant subgroup of $G(K/k)$.

Conversely, if $H$ is an invariant subgroup of $G(K/k)$, then $\tau H \tau^{-1} = H$ for all $\tau \in G(K/k)$. By the Fundamental Theorem, the corresponding fixed fields must coincide, i.e., $\tau(L) = L$. Hence every $k$-automorphism of $K$ sends $L$ into itself, and since $K/k$ is normal, it follows that $L$ is a normal extension of $k$.

Now assume that $L/k$ is normal. Then every $k$-automorphism $\tau$ of $K$ induces a $k$-automorphism of $L$, and the mapping $\tau \mapsto \tau|_L$ is a homomorphism of $G(K/k)$ into $G(L/k)$. The kernel of this homomorphism consists of those $k$-automorphisms of $K$ that leave every element of $L$ fixed, i.e., the subgroup $G(K/L) = H$. Moreover, since $K/k$ is normal, every $k$-automorphism of $L$ can be extended to a $k$-automorphism of $K$; thus the restriction mapping is surjective onto $G(L/k)$. It follows that $G(L/k) \cong G(K/k)/G(K/L)$.
