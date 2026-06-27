---
role: proof
locale: en
of_concept: fundamental-region-of-gamma0-p
source_book: gtm041
source_chapter: "4"
source_section: "4.3"
---

Let $R$ denote the set

$$R = R_\Gamma \cup \bigcup_{k=0}^{p-1} ST^k(R_\Gamma).$$

We prove two properties:

**(i)** If $\tau \in H$, there is a $V \in \Gamma_0(p)$ such that $V\tau \in R$.

**(ii)** If $\tau_1 \in R$, $\tau_2 \in R$ and $V\tau_1 = \tau_2$ for some $V \in \Gamma_0(p)$, then $\tau_1 = \tau_2$.

---

**Proof of (i).** Let $\tau \in H$. Since $R_\Gamma$ is a fundamental region of $\Gamma$, there exists $V \in \Gamma$ such that $V\tau \in R_\Gamma$. By Theorem 4.1, every $V \in \Gamma$ can be expressed as $V = PA_k$ where $P \in \Gamma_0(p)$ and $A_k = ST^k$ for $0 \leq k < p$, or $A_p = I$. Thus $PA_k\tau \in R_\Gamma$, which implies $A_k\tau \in P^{-1}(R_\Gamma)$. Since $P^{-1} \in \Gamma_0(p)$, the element $P^{-1}$ preserves the structure under consideration. Now $A_k\tau = ST^k\tau \in P^{-1}(R_\Gamma)$, so $T^k\tau \in S^{-1}P^{-1}(R_\Gamma) = SP^{-1}(R_\Gamma)$. Applying $P$ gives $PT^k\tau \in R_\Gamma$. Setting $V = PT^k$ (which lies in $\Gamma_0(p)$ because $T^k \in \Gamma_0(p)$), we obtain $V\tau \in R_\Gamma \subseteq R$. This establishes (i).

Alternatively, the standard argument proceeds as follows: given $\tau \in H$, choose $V \in \Gamma$ with $V\tau \in R_\Gamma$. By Theorem 4.1, write $V = PA_k$ with $P \in \Gamma_0(p)$. Then $PA_k\tau \in R_\Gamma$, so $P^{-1}\tau \in A_k^{-1}(R_\Gamma)$. Since $A_k = ST^k$, we have $A_k^{-1} = T^{-k}S$, so $P^{-1}\tau \in T^{-k}S(R_\Gamma)$. Equivalently, $T^kP^{-1}\tau \in S(R_\Gamma)$. Let $W = T^kP^{-1}$, then $W \in \Gamma_0(p)$ and $W\tau \in S(R_\Gamma) = ST^0(R_\Gamma) \subseteq R$.

---

**Proof of (ii).** Suppose $\tau_1 \in R$, $\tau_2 \in R$ and $V\tau_1 = \tau_2$ for some $V$ in $\Gamma_0(p)$. We prove that $\tau_1 = \tau_2$. There are three cases to consider:

**(a)** $\tau_1 \in R_\Gamma$, $\tau_2 \in R_\Gamma$. In this case $\tau_1 = \tau_2$ since $V \in \Gamma$ (as $\Gamma_0(p) \subseteq \Gamma$) and $R_\Gamma$ is a fundamental region of $\Gamma$.

**(b)** $\tau_1 \in R_\Gamma$, $\tau_2 \in ST^k(R_\Gamma)$. In this case, $\tau_2 = ST^k\tau_3$ where $\tau_3 \in R_\Gamma$. The equation

$$V\tau_1 = \tau_2$$

implies

$$V\tau_1 = ST^k\tau_3, \quad \tau_1 = V^{-1}ST^k\tau_3.$$

But $\tau_1 \in R_\Gamma$ and $\tau_3 \in R_\Gamma$, so $V^{-1}ST^k = I$, hence

$$V = ST^k = \begin{pmatrix} 0 & -1 \\ 1 & k \end{pmatrix}.$$

This contradicts the fact that $V \in \Gamma_0(p)$, since $ST^k \notin \Gamma_0(p)$ (its lower-left entry is $1$, which is not divisible by $p$). Therefore case (b) cannot occur.

**(c)** $\tau_1 \in ST^{k_1}(R_\Gamma)$, $\tau_2 \in ST^{k_2}(R_\Gamma)$. In this case

$$\tau_1 = ST^{k_1}\tau_1' \quad \text{and} \quad \tau_2 = ST^{k_2}\tau_2'$$

where $\tau_1'$ and $\tau_2'$ are in $R_\Gamma$. Since $V\tau_1 = \tau_2$, we have

$$VST^{k_1}\tau_1' = ST^{k_2}\tau_2'$$

so $VST^{k_1} = ST^{k_2}$, which gives

$$V = ST^{k_2}T^{-k_1}S = ST^{k_2-k_1}S.$$

Since $V \in \Gamma_0(p)$, this requires $k_2 \equiv k_1 \pmod{p}$. But both $k_1, k_2$ are in the interval $[0, p-1]$, so $k_2 = k_1$. Therefore

$$V = ST^0S = S^2 = I$$

and $\tau_1 = \tau_2$.

This completes the proof. $\square$
