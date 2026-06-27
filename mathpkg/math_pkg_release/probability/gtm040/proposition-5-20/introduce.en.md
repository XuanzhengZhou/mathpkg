---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Let $P$ be the transition matrix of a Markov chain obtained from sums of independent random variables. If, for each pair of states $q$ and $r$, there is a state $s$ such that $q$ can be reached from $s$ or $s$ can be reached from

$q + a_1 + \cdots + a_m$ and $r, r + b_1, \ldots, r + b_1 + \cdots + b_n$ be respective paths of positive probability leading from $q$ to $s$ and from $r$ to $s$. Then

$$f_{q+a_1+\cdots+a_m} = f_s = f_{r+b_1+\cdots+b_n},$$

so that at least one of the equalities in the two chains

$$f_q = f_{q+a_1} = f_{q+a_1+a_2} = \cdots = f_{q+a_1+\cdots+a_m}$$

and

$$f_r = f_{r+b_1} = f_{r+b_1+b_2} = \cdots = f_{r+b_1+\cdots+b_n}$$

must be false, since otherwise $f_q = f_r$. Without loss of generality, let $f_{q+\cdots+a_k-1} \neq f_{q+\cdots+a_k}$ and let $a = a_k$. Then $p_a > 0$. Let $g_i = f_{i+a} - f_i$. Then $g$ is not identically 0. Further, $g$ is regular because

$$\sum_j P_{ij} g_j = \sum_j P_{ij}(f_{j+a} - f_j)$$

$$= \sum_j P_{ij} f_{j+a} - \sum_j P_{ij} f_j$$

$$= \sum_j P_{i+a,j+a} f_{j+a} - \sum_j P_{ij} f_j$$

$$= f_{i+a} - f_i$$

$$= g_i.$$

Suppose that for all $i$, $|f_i| \leq c$. Then $|g_i|$ is bounded by 2$c$. Since multiplying $g$ by $-1$ affects neither its regularity nor its boundedness, we may assume $b = \sup_i g_i$ is positive and finite. For any $i$ and any $m > 0$,
