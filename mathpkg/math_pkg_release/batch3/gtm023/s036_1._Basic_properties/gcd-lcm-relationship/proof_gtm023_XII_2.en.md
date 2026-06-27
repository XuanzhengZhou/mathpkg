---
role: proof
locale: en
of_concept: gcd-lcm-relationship
source_book: gtm023
source_chapter: "XII"
source_section: "2"
---

From the GCD linear combination, $f = \sum_i f_i g_i = \sum_i f h_i g_i$, so $1 = \sum_i h_i g_i$, showing $h_1$ and $h_2$ are relatively prime. The polynomial $f h_1 h_2$ is clearly a common multiple of $f_1$ and $f_2$. Let $g$ be any common multiple: $g = f_1 p_1 = f_2 p_2$. Then $f p_1 = g_1 f_1 p_1 + g_2 f_2 p_1 = g_1 g + g_2 f_2 p_1 = f_2(g_1 p_2 + g_2 p_1) = f h_2(g_1 p_2 + g_2 p_1)$. Hence $p_1 = h_2(g_1 p_2 + g_2 p_1)$, so $g = f_1 p_1 = f h_1 h_2(g_1 p_2 + g_2 p_1)$, meaning $g$ is a multiple of $f h_1 h_2$.
