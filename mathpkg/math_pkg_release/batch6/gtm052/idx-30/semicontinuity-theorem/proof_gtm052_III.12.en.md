---
role: proof
locale: en
of_concept: semicontinuity-theorem
source_book: gtm052
source_chapter: "III"
source_section: "12"
---

The question is local on $Y$, so we may assume $Y = \operatorname{Spec} A$ is affine, with $A$ noetherian. Thus we can apply the earlier results of this section. By (9.4) we have

$$h^i(y, \mathcal{F}) = \dim_{k(y)} T^i(k(y)).$$

Let $L^\bullet$ be the complex of finitely generated free $A$-modules given by Lemma 12.3, and let $W^i = \operatorname{coker}(d^{i-1}: L^{i-1} \to L^i)$. As in the proof of Proposition 12.4, we have

$$T^i(k(y)) = \ker(W^i \otimes k(y) \to L^{i+1} \otimes k(y)).$$

Let $d^i \otimes k(y): W^i \otimes k(y) \to L^{i+1} \otimes k(y)$ be the induced map. Then

$$h^i(y, \mathcal{F}) = \dim \ker(d^i \otimes k(y)).$$

Now consider the linear map $d^i: W^i \to L^{i+1}$. For any $y \in Y$, the dimension of the kernel of $d^i \otimes k(y)$ is

$$\dim W^i \otimes k(y) - \operatorname{rank}(d^i \otimes k(y)).$$

The dimension $\dim W^i \otimes k(y)$ is an upper semicontinuous function of $y$ (Example 12.7.2), and the rank of $d^i \otimes k(y)$ is a lower semicontinuous function of $y$ (it is the largest $r$ such that the $r$-th exterior power of $d^i$ is nonzero at $y$). The difference of an upper semicontinuous function and a lower semicontinuous function is upper semicontinuous. Therefore $h^i(y, \mathcal{F})$ is upper semicontinuous.

More explicitly, we can characterize the set $\{y \in Y \mid h^i(y, \mathcal{F}) \geq n\}$. For $h^i(y, \mathcal{F}) \geq n$, we need $\dim \ker(d^i \otimes k(y)) \geq n$, which is equivalent to the condition that the map

$$\bigwedge^{r-n+1} W^i \to \bigwedge^{r-n+1} L^{i+1}$$

induced by $d^i$ vanishes at $y$, where $r = \dim W^i \otimes k(y)$. Since the vanishing locus of a map of coherent sheaves is closed, this set is closed, proving upper semicontinuity.
