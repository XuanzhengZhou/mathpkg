---
role: proof
locale: en
of_concept: general-sentential-logic-functional-completeness
source_book: gtm037
source_chapter: "8. Sentential Logic"
source_section: "8.2 Elements of Logic"
---

Let $\mathcal{P}' = (K, 1, f, g)$, $\mathcal{P}'' = (K, 2, f, g)$, and let $\mathcal{P}''' = (\{n', c'\}, P, f', g')$ be a sentential logic. For $\varphi$ a sentence of $\mathcal{P}'$ and $\psi$ a sentence of $\mathcal{P}$, let $\varphi[\psi]$ be the sentence of $\mathcal{P}$ obtained from $\varphi$ by substituting $\psi$ for $\langle 0 \rangle$ throughout $\varphi$. If $h$ is a model of $\mathcal{P}$ and $\psi$ is a sentence of $\mathcal{P}$, then $h'_{\psi} = h^+ \psi$.

First we establish:

(1) If $\varphi$ is a sentence of $\mathcal{P}'$, $\psi$ a sentence of $\mathcal{P}$, and $h$ is a model of $\mathcal{P}$, then $h^+ \varphi[\psi] = h'_{\psi}{}^+ \varphi$.

This is proved by induction on $\varphi$. The same construction works for $\mathcal{P}''$. For $\varphi$ a sentence of $\mathcal{P}''$ and $\psi, \chi$ sentences of $\mathcal{P}$, let $\varphi[\psi, \chi]$ be the sentence of $\mathcal{P}$ obtained from $\varphi$ by substituting $\psi$ for $\langle 0 \rangle$ and $\chi$ for $\langle 1 \rangle$ throughout $\varphi$.

Now, by hypothesis there exists a sentence $\varphi_0$ of $\mathcal{P}'$ with $\mathcal{T}_{\varphi_0} = \mathit{neg}$, and a sentence $\varphi_1$ of $\mathcal{P}''$ with $\mathcal{T}_{\varphi_1} = \mathit{imp}$. Using these sentences and the substitution construction above, any truth function that is expressible using $\mathit{neg}$ and $\mathit{imp}$ in the standard sentential logic can be expressed in $\mathcal{P}$. Since $\{\mathit{neg}, \mathit{imp}\}$ is functionally complete (by a standard result), and $P$ is finite, it follows that $\mathcal{P}$ is functionally complete.
