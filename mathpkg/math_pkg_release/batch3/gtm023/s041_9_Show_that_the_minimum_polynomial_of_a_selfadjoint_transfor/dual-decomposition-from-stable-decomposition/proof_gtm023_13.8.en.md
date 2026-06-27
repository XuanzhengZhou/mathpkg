---
role: proof
locale: en
of_concept: dual-decomposition-from-stable-decomposition
source_book: gtm023
source_chapter: "13"
source_section: "13.8"
---
First consider the case $r = 2$. Suppose $E = F_1 \oplus F_2$ with $F_1, F_2$ stable under $\varphi$. Define $F_1^* = F_2^\perp$ and $F_2^* = F_1^\perp$. By the previous proposition, $F_1^*$ and $F_2^*$ are stable under $\varphi^*$. From sec. 2.30, we have $E^* = F_1^* \oplus F_2^*$, and the pairs $F_1, F_1^*$ and $F_2, F_2^*$ are dual. One checks directly that $\varphi$ and $\varphi^*$ induce dual mappings in each pair.

For $r > 2$, define
$$F_i^* = \left( \sum_{j \neq i} F_j \right)^\perp.$$
By the same argument applied repeatedly, each $F_i^*$ is stable under $\varphi^*$, the sum is direct, and $E^* = \bigoplus_i F_i^*$. The duality and dual mapping properties follow by applying the $r=2$ case to the decomposition $E = F_i \oplus (\sum_{j \neq i} F_j)$.
