---
role: proof
locale: en
of_concept: lemma-10-34
source_book: gtm040
source_chapter: "10"
source_section: "34"
---

**Proof:** For a typical basic statement $x_0 = i \wedge x_1 = j \wedge x_2 = k$, we have, by Definition 10-23,

$$\Pr^h[x_0 = i \wedge x_1 = j \wedge x_2 = k

Take $p$ to be the statement $x_v \in E$, where $E$ is a Borel set of $S^*$. The claim is that $x_v \in E$ if and only if $x_v^h \in E$, and similarly for $h^{(1)}$ and $h^{(2)}$. For each $n$ we certainly have $x_n = x_n^h$. Hence $x_v = x_v^h$ when $v$ is finite. When $v$ is infinite, we have $x_v = x_v^h$ because $x_n = x_n^h$ for all $n$ and because $S^{h*}$ is isometric with a subset of $S^*$. Therefore

$$\Pr^h[x_v \in E] = c_1 \Pr^{h^{(1)}}[x_v \in E] + c_2 \Pr^{h^{(2)}}[x_v \in E]$$

or

$$\mu^h = c_1 \mu^{h^{(1)}} + c_2 \mu^{h^{(2)}}.$$
