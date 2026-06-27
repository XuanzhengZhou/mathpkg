---
role: proof
locale: en
of_concept: ordinal-space-disjoint-closed-accumulation
source_book: gtm027
source_chapter: "4"
source_section: "E. Problems (Ordinal Space Properties)"
---

# Proof: Accumulation Point of Disjoint Closed Sets in Ordinal Space

**Statement (b)**: If $A$ and $B$ are closed disjoint subsets of $\Omega_0 = [0, \Omega)$, then $\Omega$ is not an accumulation point of both $A$ and $B$.

**Proof**:

Recall that $\Omega$ denotes the first uncountable ordinal, and $\Omega_0 = [0, \Omega)$ consists of all countable ordinals with the order topology. The ordinal $\Omega$ serves as the "point at infinity" in the one-point compactification $\Omega' = [0, \Omega]$.

Suppose, for contradiction, that $\Omega$ is an accumulation point of both $A$ and $B$. Then every neighborhood of $\Omega$ in $\Omega'$ intersects both $A$ and $B$. Neighborhoods of $\Omega$ take the form $(\alpha, \Omega]$ for $\alpha < \Omega$.

Since $A$ and $B$ are disjoint, we may assume without loss of generality (perhaps after renaming) that there exist ordinals $\alpha_0 < \beta_0 < \alpha_1 < \beta_1 < \cdots$ such that $\alpha_n \in A$ and $\beta_n \in B$ for each $n$, and these ordinals increase without bound toward $\Omega$.

More formally, since $\Omega$ is an accumulation point of $A$, we can choose $a_0 \in A$ arbitrarily. Since $\Omega$ is also an accumulation point of $B$, choose $b_0 \in B$ with $b_0 > a_0$. Continue inductively: having chosen $a_n \in A$, pick $b_n \in B$ with $b_n > a_n$; having chosen $b_n \in B$, pick $a_{n+1} \in A$ with $a_{n+1} > b_n$. This yields sequences $\{a_n\}$ in $A$ and $\{b_n\}$ in $B$ with
$$a_0 < b_0 < a_1 < b_1 < a_2 < \cdots < \Omega.$$

Let $\xi = \sup_n a_n = \sup_n b_n$. Since each $a_n$ and $b_n$ is a countable ordinal, the supremum $\xi$ is also a countable ordinal (a countable supremum of countable ordinals is countable), so $\xi \in \Omega_0$.

But then $\xi$ is a limit point of both sequences. Since $A$ is closed, $a_n \to \xi$ in the order topology implies $\xi \in A$. Similarly, $b_n \to \xi$ implies $\xi \in B$. This contradicts the assumption that $A$ and $B$ are disjoint.

Therefore $\Omega$ cannot be an accumulation point of both $A$ and $B$.
