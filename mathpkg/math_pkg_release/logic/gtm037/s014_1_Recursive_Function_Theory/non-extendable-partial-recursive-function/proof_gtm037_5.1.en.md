---
role: proof
locale: en
of_concept: non-extendable-partial-recursive-function
source_book: gtm037
source_chapter: "5. Recursive Functions"
source_section: "5.1 Recursive Function Theory"
---

The rule for computing $f$ is as follows. For a given $x \in \omega$, determine whether or not $x$ is the Gödel number of a Turing machine. If it is not, set $fx = 0$. If it is, test in succession whether or not $(x, x, 0) \in T_1$, $(x, x, 1) \in T_1$, $(x, x, 2) \in T_1$, etc. The first time we find a $u$ such that $(x, x, u) \in T_1$, set $fx = Vu + 1$. If we never find such a $u$, the computation never ends. Clearly $f$ is intuitively a calculable partial function, and it has the following property: for any $x \in \omega$,

$$fx = 0 \quad \text{if } x \text{ is not the Gödel number of a Turing machine,}$$
$$fx = V\mu u((x, x, u) \in T_1) + 1 \quad \text{if } x \text{ is the Gödel number of a Turing machine and there is such a } u,$$
$$fx \text{ is undefined, otherwise.}$$

It is routine to show that $f$ is partial recursive. We can define $f$ by:

$$fx \simeq [V\mu u(\chi_{T_1}(x, x, u) = 1 \text{ or } \chi_{T_1}x = 0) + 1] \cdot \chi_{T_1}x,$$

so $f$ is partial recursive.

Now $f$ cannot be extended to a general recursive function. For, suppose $f \subseteq h$ with $h$ general recursive. By the proof of 3.3, this would contradict the unsolvability of the halting problem.
