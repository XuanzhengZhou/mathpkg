---
role: proof
locale: en
of_concept: serre-duality-for-projective-scheme
source_book: gtm052
source_chapter: "III"
source_section: "7"
---

(a) As in the proof of (7.1c), we can write any coherent sheaf $\mathcal{F}$ as a quotient of a sheaf $\mathcal{E} = \bigoplus_{i=1}^{N} \mathcal{O}_X(-q)$, with $q \gg 0$. Then $\operatorname{Ext}^i(\mathcal{E}, \omega_X^\circ) \cong \bigoplus H^i(X, \omega_X^\circ(q))$, which is $0$ for $i > 0$ and $q \gg 0$ by (5.2). Thus the functor $\operatorname{Ext}^i(\cdot, \omega_X^\circ)$ is coeffaceable. The maps $\theta^i$ are constructed inductively using the $\delta$-functor structure.

(i) $\Rightarrow$ (ii). If $X$ is Cohen--Macaulay and equidimensional of dimension $n$, then for any closed point $x \in X$, the local ring $\mathcal{O}_{X,x}$ has depth $n$. Embed $X$ in $\mathbf{P}^N_k$ and let $x$ be a closed point. Choose a system of parameters; by Cohen--Macaulayness it is a regular sequence. Standard cohomology vanishing arguments yield $H^i(X, \mathcal{F}(-q)) = 0$ for $i < n$ and $q \gg 0$ when $\mathcal{F}$ is locally free.

(ii) $\Rightarrow$ (iii). Since we have already seen that $(\operatorname{Ext}^i(\cdot, \omega_X^\circ))$ is a universal contravariant $\delta$-functor, to show that the $\theta^i$ are isomorphisms, it will be sufficient to show that the $\delta$-functor $(H^{n-i}(X, \cdot)^\vee)$ is universal also. For this it suffices by (1.3A) to show that $H^{n-i}(X, \cdot)^\vee$ is coeffaceable for $i > 0$. So given a coherent sheaf $\mathcal{F}$, write $\mathcal{F}$ as a quotient of $\mathcal{E} = \bigoplus \mathcal{O}(-q)$ with $q \gg 0$. Then $H^{n-i}(X, \mathcal{E})^\vee = 0$ for $i > 0$ by (ii), so the functor is coeffaceable.

(iii) $\Rightarrow$ (ii). If $\theta^i$ is an isomorphism, then for any $\mathcal{F}$ locally free, we have

$$H^i(X, \mathcal{F}(-q)) \cong \operatorname{Ext}^{n-i}(\mathcal{F}(-q), \omega_X^\circ)^\vee.$$

But this Ext is isomorphic to $H^{n-i}(X, \mathcal{F} \otimes \omega_X^\circ(q))$ by (6.3) and (6.7), so it is $0$ for $n-i > 0$ and sufficiently large $q$.

(ii) $\Rightarrow$ (i). Embed $X$ in $\mathbf{P}^N_k$. For each closed point $x \in X$, let $A = \mathcal{O}_{P,x}$ and consider the vanishing $H^i(X, \mathcal{F}(-q)) = 0$ for $i < n$ and $\mathcal{F}$ locally free. By local duality and (6.12A), this forces depth $\mathcal{O}_{X,x} \geq n$. Since $\dim X = n$, we must have equality for every closed point of $X$. This shows, using (II, 8.21Ab), that $X$ is Cohen--Macaulay and equidimensional.
