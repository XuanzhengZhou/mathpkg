---
role: proof
locale: en
of_concept: partial-recursive-function-r.e.-graph
source_book: gtm037
source_chapter: "6"
source_section: "6.3"
---

$(i) \Rightarrow (ii)$. Assume $(i)$. For any $x, y \in \omega$ let

$$g(x, y) \simeq \mu z(|y - f x| = 0).$$

Clearly $g$ is partial recursive and $\operatorname{Dmn} g = \{(x, f x) : x \in \operatorname{Dmn} f\}$, so the graph of $f$ is r.e. (as the domain of a partial recursive function).

$(ii) \Rightarrow (i)$. Assume the graph of $f$ is r.e. By Theorem 6.13, there exists a recursive relation $S \subseteq {}^3 \omega$ such that

$$\{(x, f x) : x \in \operatorname{Dmn} f\} = \{(x, y) : \exists z \, S(x, y, z)\}.$$

Then $f(x) \simeq \mu y \, \exists z \, S(x, y, z)$, showing $f$ is partial recursive. $\square$
