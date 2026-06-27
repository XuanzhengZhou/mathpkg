---
role: proof
locale: en
of_concept: lemma-independent-extension-cardinal
source_book: gtm037
source_chapter: "22"
source_section: "7"
---

Assume the hypothesis. Then $\Delta \models \varphi$ for each $\varphi \in \Gamma$, so $\Delta$ axiomatizes $\{\varphi : \Gamma \models \varphi\}$. Obviously $\Delta$ is still independent in the $\mathcal{L}$-sense. By induction on the cardinal, it suffices to show that $\{\varphi \in \text{Sent}_{\mathcal{L}} : \Gamma \models \varphi\}$ is independently axiomatizable. Thus, returning to the original statement, we may assume that every nonlogical constant of $\mathcal{L}$ occurs in some sentence of $\Gamma$.

By Lemma 22.6 we may assume that $\mathcal{L}$ has infinitely many nonlogical constants. Let a well-ordering of $\Gamma$ be fixed. Let $m = |\text{Fmla}_{\mathcal{L}}|$, which is the cardinality of the set $C$ of all nonlogical constants of $\mathcal{L}$ and also the cardinality of $\Gamma$. Choose an enumeration $c : m \rightarrow C$.

Define a sequence $\langle \varphi_{\alpha} : \alpha < m \rangle$ of sentences of $\Gamma$ by: for $\beta < m$, let $d$ be the first nonlogical constant in the list $c_0, c_1, \ldots$ not in $\bigcup_{\alpha < \beta} C\varphi_{\alpha}$, and let $\varphi_{\beta}$ be the first member of $\Gamma$ in which $d$ occurs.

Next define a sequence $\langle \Delta_{\alpha} : \alpha < m \rangle$ of subsets of $\Gamma$:

$$\Delta_0 = \{\psi \in \Gamma : \text{not}(\models \psi) \text{ and } C\psi \cap C\varphi_0 \neq \emptyset\}.$$

By induction one shows that $\bigcup_{\alpha < m} \{\varphi : \Delta_{\alpha} \models \varphi\} = \{\varphi : \Gamma \models \varphi\}$. Define sets $T_{\alpha}$ as the sets of nonlogical constants occurring in the sentences of $\Delta_{\alpha}$. For any $\psi \in \Gamma$, the set $\{\beta : C\psi \cap T_{\beta} \neq \emptyset\}$ is finite.

Define for each $\beta < m$:

$$\psi_\beta = \bigwedge \{\varphi_\alpha : \alpha < \beta \text{ and } C\varphi_\beta \cap T_\alpha \neq \emptyset\} \rightarrow \varphi_\beta$$

and for $\chi \in \Gamma \setminus \{\varphi_\alpha : \alpha < m\}$:

$$\chi' = \bigwedge \{\varphi_\alpha : \alpha < m \text{ and } C\chi \cap T_\alpha \neq \emptyset\} \rightarrow \chi.$$

Let $\Theta = \{\psi_\beta : \beta < m\}$ and $\Omega = \{\chi' : \chi \in \Gamma \setminus \{\varphi_\alpha : \alpha < m\}\}$. Then $\Omega \cup \Theta$ axiomatizes $\{\varphi : \Gamma \models \varphi\}$ and satisfies the conditions of the lemma.
