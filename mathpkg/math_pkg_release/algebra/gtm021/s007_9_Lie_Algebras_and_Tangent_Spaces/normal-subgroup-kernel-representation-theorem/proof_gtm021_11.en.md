---
role: proof
locale: en
of_concept: normal-subgroup-kernel-representation-theorem
source_book: gtm021
source_chapter: "11"
source_section: "Construction of Certain Representations"
---
By Theorem 11.2, construct $\varphi: G \to \operatorname{GL}(V)$ and a line $L \subset V$ whose stabilizer in $G$ (resp. $\mathfrak{g}$) is $N$ (resp. $\mathfrak{n}$). Since $N$ acts on $L$ by scalar multiplication, there is an associated character $\chi_0 \in \mathbf{X}(N)$.

Consider the sum in $V$ of all nonzero subspaces $V_\chi = \{v \in V \mid n \cdot v = \chi(n)v \text{ for all } n \in N\}$ for $\chi \in \mathbf{X}(N)$. By Lemma 11.4 (linear independence of distinct characters), this sum is direct, so only finitely many $\chi$ appear, and it includes $L$.

Since $N$ is normal in $G$, the calculation
$$n \cdot (x \cdot v) = x \cdot ((x^{-1}nx) \cdot v) = x \cdot (\chi(x^{-1}nx) v) = \chi(x^{-1}nx) (x \cdot v)$$
shows that $\varphi(G)$ permutes the various $V_\chi$: $x$ maps $V_\chi$ into $V_{x \cdot \chi}$, where $(x \cdot \chi)(n) = \chi(x^{-1}nx)$. Thus we may assume $V$ itself is the sum of the $V_\chi$, with $N$ acting by scalars on each.

Now let $W$ be the subspace of $\operatorname{End} V$ consisting of those endomorphisms that preserve each $V_\chi$. Define $\psi: G \to \operatorname{GL}(W)$ by $\psi(x)(T) = \varphi(x) T \varphi(x)^{-1}$. Then $x \in \operatorname{Ker} \psi$ iff $\varphi(x)$ commutes with every $T \in W$, which forces $\varphi(x)$ to act as a scalar on each $V_\chi$, and by analyzing the action on the original line $L$, one finds $\varphi(x)|_L = \operatorname{id}_L$, hence $x \in N$. Thus $\operatorname{Ker} \psi = N$.

The statement about the differential follows by differentiating: $\operatorname{Ker} d\psi = \mathfrak{n}$.
