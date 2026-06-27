---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Let $A$ be a matrix with index sets $K$ and $M$, and let $B$ be a matrix with index sets $M$ and

argument that an arbitrary entry of $A$ equals the corresponding entry of $B$. With this understanding, we see that the proof of the additive properties of matrices is reduced to a trivial repetition of the properties of real numbers. Propositions about multiplication, however, when looked at entry-by-entry involve a new idea.

Let $A$ be a matrix with index sets $M$ and $N$ and let $m$ and $n$ be fixed elements of $M$ and $N$, respectively. The $m$th row of $A$ is defined to be the restriction of the function $A$ to the domain of pairs $(m, s)$, where $s$ runs through the set $N$. Similarly the $n$th column of $A$ is defined to be the restriction of the function $A$ to the domain of pairs $(t, n)$, where $t$ runs through the elements of the set $M$. We note that the $m$th row of a matrix is a row vector and that the $n$th column is a column vector. With these conventions matrices can be thought of as sets of rows or as sets of columns, and addition of matrices is simply addition of corresponding rows or columns of the matrices involved. Furthermore, the $k$-$n$th entry in the matrix product of $A$ and $B$ is the product of the $k$th row of $A$ by the $n$th column of $B$ and is of the form $\sum_{m \in M} \pi_m f_m$, where $\pi$ is a row vector and $f$ is a column vector. That is, propositions about matrix multiplication, when proved entry-by-entry, may sometimes be proved by considering only the product of a row vector and a column vector.

Because of the correspondence of row vectors to rows and column vectors to columns, we shall agree to call the domain of a row vector or a column vector the elements of a single index set.

Connected with any definition of multiplication are five properties which may or may not be valid for the structure being considered. All five of the properties do hold for the real numbers, and we state them in this context:

(1) Existence and uniqueness of a multiplicative identity. The real number 1 satisfies $c1 = 1c = c$ for every $c$.

(2) Commutativity: $

The validity of the third property, that of distributivity, is the content of the next proposition.
