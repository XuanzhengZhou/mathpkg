---
role: proof
locale: en
of_concept: craigs-interpolation-theorem
source_book: gtm037
source_chapter: "22"
source_section: "1"
---

Clearly we may assume that the underlying language $\mathcal{L}$ is countable (i.e., that $|\text{Fmla}_{\mathcal{L}}| = \aleph_0$). We shall use the model existence theorem (Corollary 18.12). To this end, let $\mathcal{L}'$ be an expansion of $\mathcal{L}$ rich by $C$. Now for each sentence $\chi$ of $\mathcal{L}$ let

$$\Gamma_{\chi} = \{ \theta : \theta \text{ is a sentence of } \mathcal{L}' \text{, and the nonlogical constants of } \mathcal{L} \text{ which occur in } \theta \text{ also occur in } \chi \}.$$

Let $S$ be the collection of all $\Delta \subseteq \text{Sent}_{\mathcal{L}'}$ for which there exist finite subsets $\Theta_0 \subseteq \Gamma_\varphi$ and $\Theta_1 \subseteq \Gamma_\psi$ such that $\Delta = \Theta_0 \cup \Theta_1$ and for all $\chi_0, \chi_1 \in \Gamma_\varphi \cap \Gamma_\psi$, if $\models \bigwedge \Theta_0 \rightarrow \chi_0$ and $\models \bigwedge \Theta_1 \rightarrow \chi_1$, then $\chi_0 \wedge \chi_1$ has a model.

We now verify that $S$ satisfies conditions (C1)-(C9) of the model existence theorem (18.4).

(C1): If $\theta, \neg \theta \in \Delta$ for some $\theta$, then we derive a contradiction. The cases where both are in $\Theta_0$ or both in $\Theta_1$ are handled by the definition of $S$. If $\theta \in \Theta_0$ and $\neg \theta \in \Theta_1$, then both $\theta$ and $\neg \theta$ belong to $\Gamma_\varphi \cap \Gamma_\psi$, and our assumption on $\Theta_0, \Theta_1$ implies that $\theta \wedge \neg \theta$ has a model, contradiction.

(C2), (C3): These conditions are obvious from the definition.

(C4): Suppose that $\theta_0 \vee \theta_1 \in \Delta$; without loss of generality $\theta_0 \vee \theta_1 \in \Theta_0$. Let $\Theta'_0 = \Theta_0 \cup \{\theta_0\}$ and $\Theta''_0 = \Theta_0 \cup \{\theta_1\}$. If both $\Theta'_0 \cup \Theta_1$ and $\Theta''_0 \cup \Theta_1$ were not in $S$, we obtain sentences $\chi'_0, \chi'_1, \chi''_0, \chi''_1 \in \Gamma_\varphi \cap \Gamma_\psi$ with $\models \bigwedge \Theta'_0 \rightarrow \chi'_0$, etc., leading to contradictions. Hence one of these sets belongs to $S$.

(C5)-(C8): Verified similarly, using the finite character of the construction.

(C9): Let $\tau$ be a primitive term and $\mathbf{c} \in C$ not occurring in $\tau$ or in $\bigwedge \Theta_0 \wedge \bigwedge \Theta_1$. Let $\Theta'_0 = \Theta_0 \cup \{ \mathbf{c} = \tau \}$. Suppose $\chi_0, \chi_1 \in \Gamma_\varphi \cap \Gamma_\psi$ and $\models \bigwedge \Theta'_0 \rightarrow \chi_0, \models \bigwedge \Theta_1 \rightarrow \chi_1$. Then $\models \bigwedge \Theta_0 \rightarrow (\mathbf{c} = \tau \rightarrow \chi_0)$ and hence $\models \bigwedge \Theta_0 \rightarrow (\exists \alpha (\alpha = \tau) \rightarrow \exists \alpha \chi'_0)$ and $\models \bigwedge \Theta_1 \rightarrow \forall \alpha \chi'_1$, where $\alpha$ is a new variable and $\chi'_0, \chi'_1$ are obtained from $\chi_0, \chi_1$ by replacing $\mathbf{c}$ by $\alpha$. Since $\models \exists \alpha (\alpha = \tau)$, it follows that $\models \bigwedge \Theta_0 \rightarrow \exists \alpha \chi'_0$. Hence $\exists \alpha \chi'_0 \wedge \forall \alpha \chi'_1$ has a model, which yields a model of $\chi_0 \wedge \chi_1$.

Thus (C1)-(C9) of 18.4 are checked. Now our assumption that $\models \varphi \rightarrow \psi$ implies that $\{\varphi, \neg \psi\}$ does not have a model. Hence by the model existence theorem (18.12), $\{\varphi, \neg \psi\} \notin S$. This means there exist finite $\Theta_0 \subseteq \Gamma_\varphi$, $\Theta_1 \subseteq \Gamma_{\neg \psi}$, and sentences $\chi_0, \chi_1 \in \Gamma_\varphi \cap \Gamma_{\neg \psi} = \Gamma_\varphi \cap \Gamma_\psi$ such that $\models \bigwedge \Theta_0 \rightarrow \chi_0$, $\models \bigwedge \Theta_1 \rightarrow \chi_1$, and $\chi_0 \wedge \chi_1$ has no model. Then $\chi = \chi_0$ is the desired interpolant.
