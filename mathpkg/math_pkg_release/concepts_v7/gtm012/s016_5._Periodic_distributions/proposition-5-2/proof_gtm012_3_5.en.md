---
role: proof
locale: en
of_concept: proposition-5-2
source_book: gtm012
source_chapter: "3"
source_section: "5"
---

# Proof of Difference Quotient Convergence to Derivative in $\mathcal{P}'$

**Proposition 5.2.** If $F \in \mathcal{P}'$, then

$$t^{-1}(T_{-t}F - F) \to DF \quad \text{in } \mathcal{P}'$$

as $t \to 0$.

*Proof.* Suppose $u \in \mathcal{P}$. By the definitions of translation (5) and the difference quotient,

$$
\begin{aligned}
t^{-1}(T_{-t}F - F)(u) &= t^{-1} T_{-t}F(u) - t^{-1} F(u) \\
&= t^{-1} F(T_t u) - t^{-1} F(u) \\
&= -F\bigl(t^{-1}[u - T_t u]\bigr).
\end{aligned}
$$

Now

$$t^{-1}[u - T_t u](x) = t^{-1}\bigl[u(x) - u(x - t)\bigr].$$

An argument like that proving Lemma 3.2 and Corollary 3.3 shows that the expression $t^{-1}[u - T_t u]$ converges to $Du$ in the sense of $\mathcal{P}$ as $t \to 0$. Since $F$ is continuous on $\mathcal{P}$, it follows that

$$F\bigl(t^{-1}[u - T_t u]\bigr) \to F(Du).$$

Therefore

$$t^{-1}(T_{-t}F - F)(u) = -F\bigl(t^{-1}[u - T_t u]\bigr) \to -F(Du) = DF(u).$$

Since this holds for every $u \in \mathcal{P}$, we have $t^{-1}(T_{-t}F - F) \to DF$ in $\mathcal{P}'$ as $t \to 0$. $\square$

As an illustration, for the Dirac $\delta$-distribution:

$$t^{-1}(T_{-t}\delta - \delta)(u) = t^{-1}[u(-t) - u(0)] \to -Du(0) = (D\delta)(u).$$
