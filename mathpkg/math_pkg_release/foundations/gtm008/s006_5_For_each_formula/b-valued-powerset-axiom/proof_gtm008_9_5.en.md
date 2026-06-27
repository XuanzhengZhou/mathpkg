---
role: proof
locale: en
of_concept: b-valued-powerset-axiom
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

Fix $a \in M$ with $a \in M_{\alpha+1}$. By Theorem 9.20, every definable $B$-valued subset of $a$ is defined over $M_{\alpha}$. By Theorem 9.22, there exists $\beta$ such that every element defined over $M_{\alpha}$ is equal (with value $1$) to some $b \in M_{\beta}$. Then one can collect all such $b$ into $c \in M$, and verify:
$$
\llbracket x \subseteq a \rrbracket = \llbracket x \subseteq a \rrbracket \llbracket b = x \cap a \rrbracket \leq \llbracket x = b \rrbracket = \llbracket x = b' \rrbracket \llbracket b' \in c \rrbracket \leq \llbracket x \in c \rrbracket,
$$
which completes the verification that the powerset axiom holds with value $1$.
