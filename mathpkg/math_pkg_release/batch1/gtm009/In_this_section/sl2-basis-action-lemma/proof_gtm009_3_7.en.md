---
role: proof
locale: en
of_concept: sl2-basis-action-lemma
source_book: gtm009
source_chapter: "3"
source_section: "7"
---

(a) Repeated application of Lemma 7.1 gives $h.(y^i.v_0) = (\lambda - 2i)y^i.v_0$, so $h.v_i = (\lambda - 2i)v_i$.

(b) By definition: $y.v_i = y.\left(\frac{1}{i!}y^i.v_0\right) = \frac{1}{i!}y^{i+1}.v_0 = (i+1)\frac{1}{(i+1)!}y^{i+1}.v_0 = (i+1)v_{i+1}$.

(c) We prove by induction on $i$. The case $i = 0$ is true since $x.v_0 = 0 = (\lambda - 0 + 1)v_{-1}$ (as $v_{-1} = 0$ by convention). For $i > 0$:

$$i x.v_i = x.y.v_{i-1} \quad \text{(by (b))}$$
$$= [x, y].v_{i-1} + y.x.v_{i-1}$$
$$= h.v_{i-1} + y.x.v_{i-1}$$
$$= (\lambda - 2(i-1))v_{i-1} + (\lambda - (i-1) + 1)y.v_{i-2} \quad \text{(by induction)}$$
$$= (\lambda - 2i + 2)v_{i-1} + (\lambda - i + 2)(i-1)v_{i-1}$$
$$= [\lambda - 2i + 2 + (\lambda - i + 2)(i-1)]v_{i-1}$$

Simplifying the coefficient:
$$\lambda - 2i + 2 + (\lambda - i + 2)(i-1) = \lambda - 2i + 2 + \lambda i - \lambda - i^2 + i + 2i - 2 = i(\lambda - i + 1).$$

Therefore $i x.v_i = i(\lambda - i + 1)v_{i-1}$, so $x.v_i = (\lambda - i + 1)v_{i-1}$.
