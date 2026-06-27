---
role: proof
locale: en
of_concept: parentheses-bijection-uniqueness
source_book: gtm053
source_chapter: "II"
source_section: "1.2"
---

Let the function $\varepsilon : \{1, \ldots, n\} \to \{0, \pm 1\}$ take the value $1$ on $\Pi^+$, $-1$ on $\Pi^-$, and $0$ everywhere else. We claim that for every $i \in \Pi^+$, for any parentheses bijection $c : \Pi^+ \to \Pi^-$, and for any $k$ with $1 \leqslant k \leqslant c(i) - i$, we have the relations

$$\sum_{j=1}^{c(i)} \varepsilon(j) = 0, \quad \sum_{j=1}^{c(i)-k} \varepsilon(j) > 0.$$

The lemma follows immediately from these relations, since we obtain the following recipe for determining $c$ from $\Pi^+$ and $\Pi^-$: $c(i)$ is the least $l > i$ for which $\sum_{j=i}^{l} \varepsilon(j) = 0$.

The first relation holds because the elements of $\Pi^+$ and $\Pi^-$ that appear in the interval $[i, c(i)]$ do so in pairs $(j, c(j))$, and $\varepsilon(j) + \varepsilon(c(j)) = 0$.

To prove the second relation, suppose that for some $i$ and $k$ we have $\sum_{j=i}^{c(i)-k} \varepsilon(j) \leqslant 0$. Since $\varepsilon(i) = 1$, it follows that $\sum_{j=i+1}^{c(i)-k} \varepsilon(j) < 0$. Hence, the number of elements of $\Pi^-$ in the interval $[i+1, c(i)-k]$ is strictly larger than the number of elements of $\Pi^+$ in the same interval. By the pigeonhole principle, at least one right parenthesis in this interval is paired with a left parenthesis to the left of $i$, contradicting the definition of a parentheses bijection. Thus the second relation holds, and the bijection is uniquely determined.
