---
role: proof
locale: en
of_concept: kappa-chain-condition-direct-system
source_book: gtm008
source_chapter: "22"
source_section: "The Completion of a Boolean Algebra"
---

Define $C_{\alpha}$ ($\alpha \leq \kappa$) and $C$ as follows:
\begin{enumerate}
\item[(i)] $C_0 = \{b \in B_0 \mid b > 0\}$.
\item[(ii)] $C_{\alpha+1} = \{b \in B_{\alpha+1} \mid \#_{\alpha}(b) \in C_{\alpha}\}$, where $\#_{\alpha}: B_{\alpha+1} \to B_{\alpha}$ is the sharp operator associated with the inclusion $B_{\alpha} \subseteq B_{\alpha+1}$.
\item[(iii)] $C_{\alpha} = \bigcup_{\beta < \alpha} C_{\beta}$ for every limit ordinal $\alpha$.
\item[(iv)] $C = C_{\kappa}$.
\end{enumerate}

Define $P_{\alpha} = \langle C_{\alpha}, \leq \rangle$. Then $\langle P_{\alpha} \mid \alpha < \kappa \rangle$ forms a limiting system of partial order structures. Applying Theorem 22.30 to this system yields that $B$ satisfies the $\kappa$-chain condition, and since the completion of a $\kappa$-c.c. Boolean algebra of size less than $\kappa$ is the algebra itself (under the given hypotheses), we obtain $\bar{B} = B$.
