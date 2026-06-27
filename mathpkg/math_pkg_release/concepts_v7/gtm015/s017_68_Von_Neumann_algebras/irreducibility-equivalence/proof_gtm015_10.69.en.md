---
role: proof
locale: en
of_concept: irreducibility-equivalence
source_book: gtm015
source_chapter: "10"
source_section: "69"
---

# Proof of Irreducibility equivalence between group and algebra representations

Proof. The following conditions on $T \in \mathcal{L}(H)$ are equivalent: $T$ commutes with $\varphi(u) = \Phi(T_u)$ for all $u$; $T$ commutes with $\varphi(u) + \lambda I = \Phi(T_u + \lambda I)$ for all $u$ and $\lambda$ (recall that $\Phi$ is unital); $T_u + \lambda I \in \Phi^{-1}(\{T\}')$ for all $u$ and $\lambda$. Since the set $\{T_u + \lambda I : u \in L^1(G), \lambda \in \mathbb{C}\}$ is dense in $\mathcal{A}$ by the definition of $\mathcal{A}$ (69.24), and $\Phi$ is continuous (being a $*$-representation), the inverse image $\Phi^{-1}(\{T\}')$ is closed in $\mathcal{A}$. Therefore $T$ commutes with all $\varphi(u)$ iff $T$ commutes with all $\Phi(A)$ for $A \in \mathcal{A}$. This establishes

$$\{\varphi(u) : u \in L^1(G)\}' = \{\Phi(A) : A \in \mathcal{A}\}'.$$

In particular, $\varphi$ is irreducible iff $\Phi$ is irreducible, since irreducibility of a $*$-representation is characterized by its commutant being $\{\lambda I : \lambda \in \mathbb{C}\}$ (67.2).
