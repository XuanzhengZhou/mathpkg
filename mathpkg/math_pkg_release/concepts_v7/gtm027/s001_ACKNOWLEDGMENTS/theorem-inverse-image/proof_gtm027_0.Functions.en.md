---
role: proof
locale: en
of_concept: theorem-inverse-image
source_book: gtm027
source_chapter: "0"
source_section: "Functions"
---

# Proof of Theorem 7: Inverse Images of Unions, Intersections, and Complements

Parts (a)--(d) are straightforward verifications from the definitions. Only part (e) will be proved in detail; the other parts follow by similar reasoning.

**Proof of (e).** A point $x$ is a member of $f^{-1}\left[\bigcap\{X_c : c \in C\}\right]$ if and only if $f(x)$ belongs to this intersection, which is the case iff $f(x) \in X_c$ for each $c$ in $C$. But the latter condition is equivalent to $x \in f^{-1}[X_c]$ for each $c$ in $C$; that is, $x \in \bigcap\{f^{-1}[X_c] : c \in C\}$. Hence

$$
f^{-1}\left[\bigcap\{X_c : c \in C\}\right] = \bigcap\{f^{-1}[X_c] : c \in C\}.
$$

**Proof of (a).** $x \in f^{-1}[A \sim B]$ iff $f(x) \in A \sim B$, i.e., $f(x) \in A$ and $f(x) \notin B$. This is equivalent to $x \in f^{-1}[A]$ and $x \notin f^{-1}[B]$, i.e., $x \in f^{-1}[A] \sim f^{-1}[B]$.

**Proof of (b) and (c).** $x \in f^{-1}[A \cup B]$ iff $f(x) \in A \cup B$, i.e., $f(x) \in A$ or $f(x) \in B$, which is equivalent to $x \in f^{-1}[A] \cup f^{-1}[B]$. Similarly for intersection with "and" replacing "or".

**Proof of (d).** $x \in f^{-1}\left[\bigcup\{X_c : c \in C\}\right]$ iff $f(x) \in \bigcup\{X_c : c \in C\}$, which means there exists some $c_0 \in C$ with $f(x) \in X_{c_0}$. This is equivalent to $x \in f^{-1}[X_{c_0}]$ for some $c_0$, i.e., $x \in \bigcup\{f^{-1}[X_c] : c \in C\}$.

The theorem is often summarized as: the inverse of a function preserves relative complements, unions, and intersections. The validity of these formulae does not depend upon the sets being subsets of the range of the function.
