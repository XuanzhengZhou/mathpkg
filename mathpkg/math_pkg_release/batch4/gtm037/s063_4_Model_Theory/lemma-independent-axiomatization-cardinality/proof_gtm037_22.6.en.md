---
role: proof
locale: en
of_concept: lemma-countable-independent-axiomatization
source_book: gtm037
source_chapter: "22"
source_section: "6"
---

Write $\Gamma = \{\varphi_i : i \in \omega\}$. For each $i \in \omega$ let $\psi_i$ be the sentence $\bigwedge_{j < i} \varphi_j \rightarrow \varphi_i$, where by convention $\psi_0$ is $\varphi_0$. Let $\Delta = \{\psi_i : \text{not}(\models \psi_i)\}$. We claim that $\Delta$ independently axiomatizes $\Gamma$.

Obviously $\Gamma \models \psi_i$ for each $i$, and hence $\Gamma \models \chi$ for each $\chi \in \Delta$. By induction on $i$ it is clear that $\models \bigwedge_{j < i} \psi_j \rightarrow \varphi_i$ for each $i \in \omega$. Hence $\Delta \models \varphi_i$ for each $i \in \omega$. Hence $\Gamma = \{\psi : \Delta \models \psi\}$, i.e., $\Delta$ axiomatizes $\Gamma$.

It remains to show that $\Delta$ is independent. First note:

(1) If $\psi_i, \psi_j \in \Delta$ and $i \neq j$, then $\models \psi_i \lor \psi_j$.

In fact, suppose $i < j$. Clearly $\models \neg \psi_j \rightarrow \bigwedge_{k < j} \varphi_k$, and hence $\models \neg \psi_j \rightarrow \varphi_i$ and $\models \neg \psi_j \rightarrow \psi_i$. Thus (1) holds.

Now assume that $\chi \in \Delta$ and $\Delta \setminus \{\chi\} \models \chi$. Thus $\models \bigwedge \Theta \rightarrow \chi$ for some finite subset $\Theta$ of $\Delta \setminus \{\chi\}$. But for each $\theta \in \Theta$ we have $\models \theta \lor \chi$ by (1), so $\models \bigwedge \Theta \lor \chi$. Hence $\models \chi$, contradiction. Therefore $\Delta$ is independent.
