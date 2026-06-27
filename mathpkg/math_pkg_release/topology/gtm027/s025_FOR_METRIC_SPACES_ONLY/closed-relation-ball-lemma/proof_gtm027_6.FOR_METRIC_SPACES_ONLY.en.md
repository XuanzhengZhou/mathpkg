---
role: proof
locale: en
of_concept: closed-relation-ball-lemma
source_book: gtm027
source_chapter: "6"
source_section: "FOR METRIC SPACES ONLY"
---

# Proof of the Closed Relation Ball Lemma

**Lemma.** Let $(X, d)$ and $(Y, \rho)$ be complete metric spaces and let $R$ be a closed subset of $X \times Y$. For each $x$ in $X$ and $y$ in $Y$, define $R[x] = \{y : (x, y) \in R\}$ and for a subset $A$ of $X$, $R[A] = \bigcup \{R[x] : x \in A\}$. Let $U_r[x] = \{u : d(x, u) < r\}$. Then for each $r > 0$ and $e > 0$, $R[U_r[x]]^{-} \subset R[U_{r+e}[x]]$.

**Proof.** The critical fact needed for the proof is: if $A$ is a subset of $X$ and $v \in R[A]^{-}$, then there is a set $B$ of arbitrarily small diameter such that $v \in R[B]^{-}$ and $A \cap B$ is not void. This is true because: if $r$ is arbitrary, if $V$ is a symmetric member of $\mathfrak{v}$ such that $R[U_r[x]]^{-} \supset V[y]$ for each member $(x, y)$ of $R$, if $v'$ is a point of $R[A]$ such that $v' \in V[v]$, and if $u$ is a point of $A$ such that $(u, v') \in R$, then $v \in V[v'] \subset R[U_r[u]]^{-}$, and the diameter of $U_r[u]$ is at most $2r$.

The lemma is now established as follows. Suppose that $v \in R[U_r[x]]^{-}$. It will be shown that $v \in R[U_{r+e}[x]]$, which will complete the proof. Let $A_0 = U_r[x]$, and select inductively, for each positive integer $n$, a subset $A_n$ of $X$ such that $v \in R[A_n]^{-}$, $A_n \cap A_{n-1}$ is not void, and the diameter of $A_n$ is less than $e2^{-n}$. Since $X$ is complete there is evidently a point $u$ such that each neighborhood $W$ of $u$ contains some $A_n$ (hence $v \in R[W]^{-}$). Clearly $d(x, u) < r + e$. For each neighborhood $W$ of $u$ and each neighborhood $Z$ of $v$ it is true that $R[W]$ intersects $Z$, and hence there is $(u', v')$ in $R$ with $u'$ in $W$ and $v'$ in $Z$; that is, $R \cap (W \times Z)$ is non-void. Since $R$ is closed, $(u, v) \in R$ and the proof is complete.
