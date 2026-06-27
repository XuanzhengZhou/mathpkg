---
role: proof
locale: en
of_concept: reznikoffs-theorem
source_book: gtm037
source_chapter: "22"
source_section: "9"
---

Let $C\varphi$ denote the set of all nonlogical constants occurring in $\varphi$. By Lemma 22.6 we may assume that our language has infinitely many nonlogical constants. Let $\Gamma$ be a theory. We define $\langle \Delta_i : i < \omega \rangle$ by recursion:

$$\Delta_n = \left\{ \varphi \in \Gamma : \text{not} \left( \bigcup_{i < n} \Delta_i \models \varphi \right) \text{ and } |C\varphi| = n \right\}.$$

Let $\Delta_\omega = \bigcup_{i < \omega} \Delta_i$. Then $\Delta_\omega$ axiomatizes $\Gamma$. This follows from the following obvious fact:

If $\varphi \in \Gamma$ and $|C\varphi| = n$, then $\bigcup_{i \leq n} \Delta_i \models \varphi$.

This fact also implies that

(1) If $\varphi \in \Delta_\omega$, $\chi \in \Gamma$, and $|C\chi| < |C\varphi|$, then $\text{not}(\models \chi \rightarrow \varphi)$.

Now to show that $\Gamma$ is independently axiomatizable, it suffices to show that $\Delta_\omega$ satisfies condition (i) of Lemma 22.8. Hence assume that $\varphi \in \Delta_\omega$, $m \in \omega \sim 1$, $\psi_i \in \Delta_\omega$ for $i < m$, $C\varphi \not\subseteq C \bigwedge_{i < m} \psi_i$, while $\models \bigwedge_{i < m} \psi_i \rightarrow \varphi$.

Let $n = |C\varphi|$. By the definition of $\Delta_n$, we have $\varphi \in \Delta_n$. For each $i < m$, let $n_i = |C\psi_i|$. If $n_i > n$ for some $i$, then by (1) we get a contradiction with the definition of $\Delta_{n_i}$. If $n_i \leq n$ for all $i$, then all nonlogical constants of $\bigwedge_{i < m} \psi_i$ are among those appearing in sentences with at most $n$ constants, which contradicts $C\varphi \not\subseteq C \bigwedge_{i < m} \psi_i$ and the fact that $\bigcup_{i < m} C\psi_i \models \varphi$.

Hence $\Delta_\omega$ satisfies the independence condition. Therefore $\Delta_\omega$ is an independent axiomatization of $\Gamma$.
