---
role: proof
locale: en
of_concept: montel-space-k0d-properties
source_book: gtm003
source_chapter: "IV"
source_section: "Exercises, No. 37"
---

$E = K_0^d$ is the Montel space, which is the product of $d$ copies of $K$ endowed with the product topology (the topology of pointwise convergence). 

$B = [0,1]^d$ with the induced topology is completely regular as a subspace of the completely regular space $E$. By Tychonoff's theorem, $B$ is compact (as a product of compact intervals). To see that $B$ is not sequentially compact, note that a sequence $\{f_n\}$ in $B$ corresponds to a sequence of functions $f_n : d \to [0,1]$. Since $d$ is the cardinality of the continuum, one can construct a sequence with no convergent subsequence — for example, take $f_n$ to be the characteristic function of the $n$-th element in an enumeration of a countable subset of $d$, giving a sequence with no pointwise convergent subsequence.

$B_0$ consists of elements with at most countably many non-zero coordinates. $B_0$ is sequentially compact: given any sequence in $B_0$, a diagonal argument extracts a pointwise convergent subsequence (since the union of the supports is countable). However, $B_0$ is not compact because it is dense in $B$ (every element of $B$ can be approximated by elements of $B_0$ with finite support) but $B_0 \neq B$, as elements with continuum many non-zero coordinates exist in $B$ but not in $B_0$.

$B_0$, as a subspace of a complete uniform space, inherits a uniform structure. It is precompact because its completion is $B$ (which is compact). It is semi-complete because Cauchy sequences converge (the limit of a Cauchy sequence in $B_0$ has at most countably many non-zero coordinates). Yet $B_0$ is not complete since its completion $B$ is strictly larger.
