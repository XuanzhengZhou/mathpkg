---
role: proof
locale: en
of_concept: twin-prime-nonstandard-equivalence
source_book: gtm037
source_chapter: "Part 4"
source_section: "Model Theory"
---

$(i) \Rightarrow (ii)$. Assume $(i)$. Let $f \in {}^\omega\omega$ be such that for each $i$, $f_i$ is a prime such that $f_i + 2$ is a prime, and $f_i + 2 < f_{i+1}$. Clearly $t[f]$ is an infinite prime such that $t[f] + 2$ is also a prime.

$(ii) \Rightarrow (i)$. Say $t[g]$ is an infinite prime such that $t[g] + 2$ is also a prime. We show that for any $m \in \omega$ there is a prime $p > m$ such that $p + 2$ is also a prime. Since $[g]$ is infinite, $I_0 = \{i : m < g_i\} \in F$. Since $[g]$ is a prime, $I_1 = \{i : g_i \text{ is prime}\} \in F$. Since $[g] + 2$ is a prime, $I_2 = \{i : g_i + 2 \text{ is prime}\} \in F$. Thus $I_0 \cap I_1 \cap I_2 \in F$. For any $i \in I_0 \cap I_1 \cap I_2$, $g_i$ is a prime $> m$ such that $g_i + 2$ is a prime.
