---
role: proof
locale: en
of_concept: basis-equivalence
source_book: gtm028
source_chapter: "I"
source_section: "21"
---

We give a cyclic proof.

**(a) $\implies$ (c):** We have to prove that $X$ is free. Assume the contrary to be true. There exists then an element $x$ in $X$ such that $x \in s(X - x)$. Since we have $X - x \subset s(X - x)$ (by $(S_3)$), it follows that $X \subset s(X - x)$, and therefore
$$V = s(X) \subset s(s(X - x)) \quad \text{(by $(S_1)$)} = s(X - x) \quad \text{(by $(S_4)$)}.$$
Thus $X - x$ is a system of generators, in contradiction with the hypothesis that no proper subset of $X$ is a system of generators.

**(c) $\implies$ (b):** We know that $X$ is free. For every $x \in V$, $x \notin X$, we have $x \in s(X)$ since $X$ generates $V$. Hence $X \cup \{x\}$ is not free, for $x$ belongs to the span of $X$. Thus $X$ is a maximal free subset: it is free, and adjoining any element of $V$ not already in $X$ destroys freeness.

**(b) $\implies$ (a):** Since $X$ is free, we first show that $X$ generates $V$. If $s(X) \neq V$, then there exists $y \in V$ with $y \notin s(X)$. By the remark preceding the theorem, $X \cup \{y\}$ would then be free, contradicting the maximality of $X$. Therefore $s(X) = V$, so $X$ is a system of generators. To see that $X$ is minimal, note that for any $x \in X$, since $X$ is free we have $x \notin s(X - x)$. Hence $X - x$ does not generate $V$, as it fails to span $x$. Thus no proper subset generates $V$.
