---
role: proof
locale: en
of_concept: extension-of-homeomorphism-between-totally-disconnected-compact-sets
source_book: gtm047
source_chapter: "13"
source_section: "13"
---

**Proof.** (1) Let $A$ and $A'$ be $2$-cells containing $M$ and $M'$ respectively in their interiors. Let $N_1$ be a frame of $M$, lying in $\operatorname{Int} A$, and lying in a sufficiently small neighborhood of $M$ so that every component of $N_1$ has diameter $< 1$. (Theorem 6.) Then the sets $f(M \cap C)$, where $C$ is a component of $N_1$, are disjoint and compact. Let $L$ be a frame of $M'$, lying in $\operatorname{Int} A'$, with components $C'$ of sufficiently small diameter so that no $C'$ intersects two different sets $f(M \cap C)$. By repeated applications of Theorem 2 we get a frame $N'_1$ of $M'$, lying in $\operatorname{Int} A'$, such that each set $f(M \cap C)$ is the intersection of $M'$ and a component of $N'_1$. Now there is a homeomorphism $f_0: \mathbb{R}^2 - \operatorname{Int} A \leftrightarrow \mathbb{R}^2 - \operatorname{Int} A'$. Let $E_1 = \mathbb{R}^2 - \operatorname{Int} N_1$, $E'_1 = \mathbb{R}^2 - \operatorname{Int} N'_1$. By Theorem 1, $f_0$ can be extended so as to give a homeomorphism $f_1: E_1 \leftrightarrow E'_1$, such that if $D$ and $D'$ are components of $N_1$ and $N'_1$, with $f_1(\operatorname{Bd} D) = \operatorname{Bd} D'$, then $f(M \cap D) = M' \cap D'$.

(2) Suppose that we have given a frame $N_{2i-1}$ of $M$, a frame $N'_{2i-1}$ of $M'$, and a homeomorphism $f_{2i-1}: E_{2i-1} \leftrightarrow E'_{2i-1}$, where

$$E_{2i-1} = \mathbb{R}^2 - \operatorname{Int} N_{2i-1}, \quad E'_{2i-1} = \mathbb{R}^2 - \operatorname{Int} N'_{2i-1}.$$

The construction is then iterated: frames $N_{2i}$ and $N'_{2i}$ are chosen with smaller component diameters, and $f_{2i}: E_{2i} \leftrightarrow E'_{2i}$ is obtained, extending $f_{2i-1}$.

(d) Each $f_i$ is a homeomorphism $E_i \leftrightarrow E_i'$, where

$$E_i = \mathbb{R}^2 - \operatorname{Int} N_i, \quad E_i' = \mathbb{R}^2 - \operatorname{Int} N_i'.$$

(e) For each $i$, $f_{i+1}$ is an extension of $f_i$.

Now let

$$F = f \cup \bigcup_{i=1}^{\infty} f_i.$$

By (e), $F$ is a well-defined function. Since

$$\mathbb{R}^2 = M \cup \bigcup_{i=1}^{\infty} E_i = M' \cup \bigcup_{i=1}^{\infty} E_i',$$

$F$ is a bijection $\mathbb{R}^2 \leftrightarrow \mathbb{R}^2$. It remains to show that $F$ and $F^{-1}$ are continuous.

Given $P \in \mathbb{R}^2 - M$, $Q = F(P)$, we have $Q \in \mathbb{R}^2 - M'$. Given an open set $U$ containing $Q$, we may suppose that $U \subset \operatorname{Int} E_i'$ for some $i$. Since $f_i$ is a homeomorphism, some neighborhood of $P$ is mapped into $U$ by $F$.

If $P \in M$, then $Q = F(P) = f(P) \in M'$, and $Q$ has arbitrarily small neighborhoods which are components $D'$ of sets $N_i'$. It is now easy to check that $D' = F(D)$ for some component $D$ of $N_i$. Thus $F$ maps small neighborhoods of $P$ onto small neighborhoods of $Q$. Therefore $F$ is continuous. The continuity of $F^{-1}$ can be shown similarly. (Again, the situation is logically symmetric.)
