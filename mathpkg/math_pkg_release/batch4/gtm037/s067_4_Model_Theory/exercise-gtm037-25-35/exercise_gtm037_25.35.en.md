---
role: exercise
locale: en
chapter: "25"
section: "Exercises"
exercise_number: 35
---
An occurrence of a symbol in $\varphi$ is positive if it is within the scope of an even number of negation symbols; otherwise it is negative. Now let $\mathcal{L}$ be a language with no operation symbols. Assume that $\varphi$ and $\psi$ are sentences in which $=$ does not occur, and that $\models \varphi \rightarrow \psi$, not $(\models \neg \varphi)$, and not $(\models \psi)$. Then there is a sentence $\chi$ in which $=$ does not occur such that $\models \varphi \rightarrow \chi$ and $\models \chi \rightarrow \psi$, and such that any relation symbol occurring positively (negatively) in $\chi$ also occurs positively (negatively) in both $\varphi$ and $\psi$.

**Hint:** Use the model existence theorem, as follows. For each sentence $\chi$ of $\mathcal{L}$ let
$$\Gamma_{\chi} = \{\vartheta : \vartheta \text{ is a sentence of } \mathcal{L}, \text{ and each relation symbol which occurs positively (negatively) in } \vartheta \text{ also occurs positively (negatively) in } \chi\}.$$
Also, let $\Gamma' = \{\vartheta : \vartheta \text{ is a sentence of } \mathcal{L}, \text{ and } = \text{ does not occur in } \vartheta\}$. Let $S$ be the collection of all $\Delta \subseteq \text{Sent}_{\mathcal{L}}$ such that there exist finite subsets $\Delta_0 \subseteq \Gamma_{\chi}$ and $\Delta_1 \subseteq \Gamma_{\neg \chi}$ with $\Delta = \Delta_0 \cup \Delta_1$ such that: (1) if $\chi \in \Delta$ and $=$ occurs in $\chi$, then $\chi$ is $c = c$ for some $c \in C$; (2) both $\Delta_0$ and $\Delta_1$ have models; (3) for all $\chi_0 \in \Gamma_{\chi} \cap \Gamma_{\neg \psi} \cap \Gamma'$ and $\chi_1 \in \Gamma_{\neg \chi} \cap \Gamma_{\neg \varphi} \cap \Gamma'$, if $\models \bigwedge \Delta_0 \rightarrow \chi_0$ and $\models \bigwedge \Delta_1 \rightarrow \chi_1$, then $\chi_0 \land \chi_1$ has a model.
