---
role: proof
locale: en
of_concept: robinsons-joint-consistency-theorem
source_book: gtm037
source_chapter: "22"
source_section: "2"
---

Assume that $\Gamma_1 \cup \Gamma_2$ is inconsistent. Then there exist finite subsets $\Delta_1 \subseteq \Gamma_1$ and $\Delta_2 \subseteq \Gamma_2$ such that $\Delta_1 \cup \Delta_2$ has no model; and we may assume that $\Delta_1 \neq \emptyset \neq \Delta_2$. Thus we have

$$\models \bigwedge \Delta_1 \rightarrow \bigvee \{\neg \varphi : \varphi \in \Delta_2\},$$

and hence by Craig's Interpolation Theorem there is a $\chi \in \text{Sent } \mathcal{L}_0$ such that

$$\models \bigwedge \Delta_1 \rightarrow \chi \text{ and } \models \chi \rightarrow \bigvee \{\neg \varphi : \varphi \in \Delta_2\}.$$

Hence $\chi \in \Gamma_1$ (since $\Delta_1 \subseteq \Gamma_1$ and $\Gamma_0 \subseteq \Gamma_1$, and the nonlogical constants of $\chi$ are in $\mathcal{L}_0$), and $\models \bigwedge \Delta_2 \rightarrow \neg \chi$, so $\neg \chi \in \Gamma_2$. But then by the completeness of $\Gamma_0$, we have $\chi, \neg \chi \in \Gamma_0$, contradicting the consistency of $\Gamma_0$.

Note that if $\Gamma_0$ is complete, then condition (iv) in 22.2 follows from (iii). Craig's theorem can also be derived from Robinson's theorem: assume $\models \varphi \rightarrow \psi$. Let $\mathcal{L}_0, \mathcal{L}_1, \mathcal{L}_2$ be the languages with nonlogical constants those occurring in both $\varphi$ and $\psi$, in $\varphi$, and in $\psi$ respectively. Let $\Gamma = \{\theta \in \text{Sent } \mathcal{L}_0 : \models \varphi \rightarrow \theta\}$. Then $\Gamma \cup \{\neg \psi\}$ does not have a model, and applying Robinson's theorem yields the interpolant.
