---
role: proof
locale: en
of_concept: completion-theorem
source_book: gtm036
source_chapter: "7"
source_section: "7.10"
---

According to Theorem 6.9 there is a topological isomorphism $S$ which maps $E$ into a product $\bigwedge \{E_t : t \in A\}$ of pseudo-metrizable linear spaces. Let $E_t^\wedge$ be a pseudo-metrizable completion of $E_t$ (constructed via the pseudo-metric method described below). Then $\bigwedge \{E_t^\wedge : t \in A\}$ is complete. The closure of $S[E]$ in this product is the required completion $E^\wedge$.

For a pseudo-metrizable linear topological space $E$ with invariant pseudo-metric $d$, the completion is constructed as follows. Let $E^\wedge$ be the set of all Cauchy sequences in $E$, with the equivalence that $\{x_n\}$ and $\{y_n\}$ are identified if $\lim d(x_n, y_n) = 0$. Define $d^\wedge(\{x_n\}, \{y_n\}) = \lim d(x_n, y_n)$. With the definitions $\{x_n\} + \{y_n\} = \{x_n + y_n\}$ and $a\{x_n\} = \{ax_n\}$, $E^\wedge$ is a linear topological space with invariant pseudo-metric $d^\wedge$. For an $x$ in $E$ let $T(x)$ be the sequence each of whose terms is $x$. Clearly $T$ preserves distance, and the problem reduces to showing that $E^\wedge$ is complete relative to $d^\wedge$. Observe that $T[E]$ is dense in $E^\wedge$, because $T(x_n)$ is near $\{x_n\}$ if $n$ is large. It follows that for each Cauchy sequence in $E^\wedge$ there is a Cauchy sequence in $T[E]$ so that the distance between the $n$-th term of the former and the $n$-th term of the latter converges to zero. Consequently $E^\wedge$ will be proved complete relative to $d^\wedge$ if it is shown that each Cauchy sequence in $T[E]$ converges to some member of $E^\wedge$. But if $\{T(x_n)\}$ is a Cauchy sequence, then $\{x_n\}$ is a Cauchy sequence and is therefore a member of $E^\wedge$, and $T(x_n)$ converges to $\{x_n\}$. Since $d^\wedge$ is an invariant pseudo-metric, $E^\wedge$ is complete by 7.1.
