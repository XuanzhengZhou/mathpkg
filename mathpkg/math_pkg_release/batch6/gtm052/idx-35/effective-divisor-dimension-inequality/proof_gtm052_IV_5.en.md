---
role: proof
locale: en
of_concept: effective-divisor-dimension-inequality
source_book: gtm052
source_chapter: "IV"
source_section: "§5"
---
We define a map of sets

$$\varphi: |D| \times |E| \rightarrow |D + E|$$

by sending $\langle D', E' \rangle$ to $D' + E'$ for any $D' \in |D|$ and $E' \in |E|$. The map $\varphi$ is finite-to-one, because a given effective divisor can be written in only finitely many ways as a sum of two other effective divisors. On the other hand, since $\varphi$ corresponds to the natural bilinear map of vector spaces

$$H^0(X, \mathcal{L}(D)) \times H^0(X, \mathcal{L}(E)) \rightarrow H^0(X, \mathcal{L}(D + E)),$$

we see that $\varphi$ is a morphism when we endow $|D|, |E|$ and $|D + E|$ with their structure of projective spaces. Therefore, since $\varphi$ is finite-to-one, the dimension of its image is exactly $\dim|D| + \dim|E|$, and from this the result follows.
