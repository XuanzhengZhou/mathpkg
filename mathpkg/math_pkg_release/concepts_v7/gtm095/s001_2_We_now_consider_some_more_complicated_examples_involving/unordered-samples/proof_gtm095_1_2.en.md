---
role: proof
locale: en
of_concept: unordered-samples
source_book: gtm095
source_chapter: "1"
source_section: "2"
---

# Proof of Unordered Samples with Replacement

We prove by induction on $n$ that the number of unordered samples of size $n$ drawn with replacement from an urn containing $M$ distinguishable balls is

$$N(M,n) = C_{M+n-1}^n.$$

**Base case.** For $n = 1$, an unordered sample of size 1 is just a single ball, so $N(M,1) = M$. The formula gives $C_{M+1-1}^1 = C_M^1 = M$, which agrees.

**Inductive step.** Suppose that $N(k,n) = C_{k+n-1}^n$ holds for all $k \leq M$. We show that the formula continues to hold when $n$ is replaced by $n+1$.

For the unordered samples $[a_1, \ldots, a_{n+1}]$ that we are considering, we may suppose that the elements are arranged in nondecreasing order:

$$a_1 \leq a_2 \leq \cdots \leq a_{n+1}.$$

It is clear that the number of unordered samples of size $n+1$ with $a_1 = 1$ is $N(M,n)$, the number with $a_1 = 2$ is $N(M-1,n)$, etc. Consequently

$$N(M,n+1) = N(M,n) + N(M-1,n) + \cdots + N(1,n).$$

Applying the induction hypothesis to each term:

$$N(M,n+1) = C_{M+n-1}^n + C_{M-1+n-1}^n + \cdots + C_n^n.$$

Now we rewrite each term using the easily verified property of binomial coefficients

$$C_k^{l-1} + C_k^l = C_{k+1}^l,$$

which is Pascal's identity. Observe that $C_k^l = C_{k+1}^{l+1} - C_k^{l+1}$. Applying this rewriting to each summand:

$$C_{M+n-1}^n = C_{M+n}^{n+1} - C_{M+n-1}^{n+1},$$
$$C_{M-1+n-1}^n = C_{M-1+n}^{n+1} - C_{M-1+n-1}^{n+1},$$
$$\vdots$$
$$C_{n+1}^n = C_{n+2}^{n+1} - C_{n+1}^{n+1},$$

and finally $C_n^n = 1$. The sum telescopes:

$$N(M,n+1) = (C_{M+n}^{n+1} - C_{M+n-1}^{n+1}) + (C_{M-1+n}^{n+1} - C_{M-1+n-1}^{n+1}) + \cdots + (C_{n+2}^{n+1} - C_{n+1}^{n+1}) + C_n^n = C_{M+n}^{n+1}.$$

Thus the formula holds for $n+1$. By induction, $N(M,n) = C_{M+n-1}^n$ for all $n \geq 1$. $\square$
