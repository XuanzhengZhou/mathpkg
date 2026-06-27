---
role: proof
locale: en
of_concept: function-injection-surjection-bijection-count
source_book: gtm095
source_chapter: "1"
source_section: "14"
---

# Proof of Counting Functions, Injections, Surjections, and Bijections

Let $A = A(n)$ and $B = B(m)$ be two sets consisting of $n$ and $m$ elements respectively.

## Function

A mapping $\mathbb{F} : A \to B$ is a *function* if to each $a \in A$ it assigns some $b \in B$. For each of the $n$ elements of $A$, there are $m$ possible choices in $B$, independently. Hence

$$N(\mathbb{F}) = m^n.$$

## Injection

A mapping $\mathbb{I} : A \to B$ is an *injection* if distinct elements of $A$ map to distinct elements of $B$ (requiring $n \leq m$). The first element of $A$ has $m$ choices, the second has $m-1$ choices, and so on. Thus

$$N(\mathbb{I}) = m(m-1) \cdots (m-n+1) = (m)_n,$$

where $(m)_n$ denotes the falling factorial.

## Bijection

A mapping $\mathbb{B} : A \to B$ is a *bijection* if it is both an injection and a surjection (requiring $n = m$). A bijection is simply a permutation of the $n$ elements, so

$$N(\mathbb{B}) = n!.$$

Alternatively, by the inclusion–exclusion principle,

$$N(\mathbb{B}) = \sum_{i=0}^{n} (-1)^i \binom{n}{i} (n-i)^n.$$

Note that this sum equals $n!$ (it counts the number of derangements for a related problem).

## Surjection

A mapping $\mathbb{S} : A \to B$ is a *surjection* (or onto function) if for every $b \in B$ there exists $a \in A$ such that $\mathbb{S}(a) = b$ (requiring $n \geq m$).

To count surjections, we use the inclusion–exclusion principle. Let $B = \{b_1, \ldots, b_m\}$. The total number of functions $A \to B$ is $m^n$. Let $C_i$ be the set of functions that do *not* take the value $b_i$ (i.e., $b_i$ is not in the image). Then the number of surjections is

$$N(\mathbb{S}) = N(\overline{C}_1 \cap \overline{C}_2 \cap \cdots \cap \overline{C}_m).$$

By inclusion–exclusion,

$$N(\mathbb{S}) = \sum_{i=0}^{m} (-1)^i \sum_{1 \leq j_1 < \cdots < j_i \leq m} N(C_{j_1} \cap \cdots \cap C_{j_i}).$$

If a function avoids $i$ specified elements of $B$, its values are restricted to the remaining $m-i$ elements. Hence

$$N(C_{j_1} \cap \cdots \cap C_{j_i}) = (m-i)^n.$$

There are $\binom{m}{i}$ ways to choose the $i$ avoided elements. Therefore

$$N(\mathbb{S}) = \sum_{i=0}^{m} (-1)^i \binom{m}{i} (m-i)^n.$$

$\square$
