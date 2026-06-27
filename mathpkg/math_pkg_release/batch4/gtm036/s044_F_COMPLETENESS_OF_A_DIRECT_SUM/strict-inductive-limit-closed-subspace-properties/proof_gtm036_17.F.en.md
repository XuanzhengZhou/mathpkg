---
role: proof
locale: en
of_concept: strict-inductive-limit-closed-subspace-properties
source_book: gtm036
source_chapter: "17"
source_section: "F"
---

**(i) Relativization and closedness.** Fix $n$ and let $U_n$ be a convex circled $\mathcal{T}_n$-neighborhood of $0$ in $E_n$. Using 13E(b), construct a sequence $\{U_{n+m} : m = 0, 1, \dots\}$ of $\mathcal{T}_{n+m}$-neighborhoods of $0$ such that $E_{n+m} \cap U_{n+m+1} = U_{n+m}$ for each $m$. Set $U = \bigcup \{U_{n+m} : m = 0, 1, \dots\}$. Then $U$ is a convex circled $\mathcal{T}$-neighborhood of $0$ in $E$ with $E_n \cap U = U_n$. This shows that $\mathcal{T}_n$ is the relativization of $\mathcal{T}$ to $E_n$. Since $E_n$ is closed in $E_{n+1}$, the relativization property implies $E_n$ is $\mathcal{T}$-closed in $E$.

**(ii) Hausdorff property.** Assume each $E_n$ is Hausdorff. Given $x \neq y$ in $E$, choose $n$ large enough so that $x, y \in E_n$. Since $E_n$ is Hausdorff under $\mathcal{T}_n$, there exist disjoint $\mathcal{T}_n$-neighborhoods separating $x$ and $y$. By property (i), $\mathcal{T}_n$ is the relativization of $\mathcal{T}$, so $x$ and $y$ can be separated by $\mathcal{T}$-neighborhoods. Hence $E$ is Hausdorff. A direct construction using 13E(c) provides an alternative argument.

**(iii) Bounded subsets.** Let $B \subseteq E$ be $\mathcal{T}$-bounded. Suppose $B$ is not contained in any $E_n$. Then there exist $x_k \in B$ and strictly increasing indices $n_k$ such that $x_k \in E_{n_k} \setminus E_{n_k - 1}$. Using 13E(c) and the construction in (i), one can produce a $\mathcal{T}$-neighborhood $U$ of $0$ that fails to absorb the sequence $\{x_k\}$, contradicting the boundedness of $B$. Hence $B$ must be contained in some $E_n$.
