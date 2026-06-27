---
role: proof
locale: en
of_concept: proposition-1-36
source_book: gtm040
source_chapter: "1"
source_section: "36"
---

**Proof:** The assertions follow from the observations that
$$\{x \mid \sup f_n(x) > c\} = \bigcup_{n=1}^{\infty} \{x \mid f_n(x) > c\},$$
$$\{x \mid \inf f_n(x) < c\} = \bigcup_{n=1}^{\infty} \{x \mid f_n(x) < c\},$$
$$\limsup_n f_n(x) = \inf_n \sup_n f_m(x)$$
and
$$\liminf_n f_n(x) = \sup_n \inf_n f_m(x).$$

The supremum of finitely many functions is their pointwise maximum. Therefore the maximum and minimum of finitely many measurable

We shall give three examples of measurable functions.

(1) Let $F$ be the family of sets on the real line which are either finite unions of open and closed intervals or complements of such sets. Then $F$ is a field of sets. Let $G$ be the smallest Borel field containing $F$. All continuous real-valued functions are measurable with respect to the Borel field $G$.

(2) Let $X$ be a space for which $B$ is the family of all subsets of $X$. Then every function $f$ defined on $X$ is measurable.

(3) Let $X$ be the union of a sequence of disjoint sets $\{A_n\}$, and let $B$ be the family of all sets which are unions of sets in the sequence. Then a function $f$ is measurable if and only if its restriction to the domain $A_n$ is a constant function for each $n$. In particular, if $B = \{X, \emptyset\}$, then the measurable functions are the constant functions.

Let $A$ be any subset of $X$. The characteristic function of $A$, denoted $\chi_A(x)$, is defined by

$$\chi_A(x) = \begin{cases} 1 & \text{if } x \in A \\ 0 & \text{otherwise.} \end{cases}$$

A function that takes on only a finite number of values is called a simple function. It may be represented, uniquely, in the form

$$s = \sum_{n=1}^{N} c_n \chi_A_n$$

where the $c_n$ are the distinct values the function takes on and the sets $A_n$ are disjoint. The simple function is measurable if and only if all of the sets $A_1, A_2, \ldots, A_N$ are measurable.
