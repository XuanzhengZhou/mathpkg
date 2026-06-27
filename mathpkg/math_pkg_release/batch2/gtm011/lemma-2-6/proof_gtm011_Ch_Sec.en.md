---
role: proof
locale: en
of_concept: lemma-2-6
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Let $C$ be a component of $G$ and let $x_0 \in C$. Since $G$ is open there is an $\epsilon > 0$ with $B(x_0; \epsilon) \subset G$. By Lemma 2.6, $B(x_0; \epsilon) \cup C$ is connected and so it must be $C$. That is $B(x_0; \epsilon) \subset C$ and $C$ is, therefore, open.

To see that the number of components is countable let $S = \{a + ib : a$ and $b$ are rational and $a + bi \in G\}$. Then $S$ is countable and each component of $G$ contains a point of $S$, so that the number of components is countable.

Exercises

1. The purpose of this exercise is to show that a connected subset of $\mathbb{R}$ is an interval.
(a) Show that a set $A \subset \mathbb{R}$ is an interval iff for any two points $a$ and $b$ in $A$ with $a < b$, the interval $[a, b] \subset A$.
(b) Use part (a) to show that if a set $A \subset \mathbb{R}$ is connected then it is an interval.

2. Show that the sets $S$ and $T$ in the proof of Theorem 2.3 are open.

3. Which of the following subsets $X$ of $\mathbb{C}$ are connected; if $X$ is not connected, what are its components: (a) $X = \{z : |z|

\{x_n\} converges to $x$—in symbols $x = \lim x_n$ or $x_n \rightarrow x$—if for every $\epsilon > 0$ there is an integer $N$ such that $d(x, x_n) < \epsilon$ whenever $n \geq N$.

Alternately, $x = \lim x_n$ if $0 = \lim d(x, x_n)$.

If $X = \mathbb{C}$ then $z = \lim z_n$ means that for each $\epsilon > 0$ there is an $N$ such that $|z - z_n| < \epsilon$ when $n \geq N$.

Many concepts in the theory of metric spaces can be phrased in terms of sequences. The following is an example.
