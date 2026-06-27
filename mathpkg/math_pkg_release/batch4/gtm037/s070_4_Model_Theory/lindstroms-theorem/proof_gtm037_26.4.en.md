---
role: proof
locale: en
of_concept: lindstroms-theorem
source_book: gtm037
source_chapter: "26"
source_section: "4"
---

Assume the hypothesis, but suppose that $L \not\subseteq L_{\mathrm{fo}}$. By Lemma 26.23, with $\mathfrak{L}$ as in 26.22, there is an expansion $\mathcal{L}'$ of $\mathfrak{L}$ and an $L$-elementary class $K_0$ of $\mathcal{L}'$-structures such that $K_0 \upharpoonright \mathcal{L}$ satisfies (ii)--(iv) of 26.22. For each $n \in \omega \sim 1$, [one constructs a structure witnessing the separation of $L$ from $L_{\mathrm{fo}}$.]

There is an expansion $L'$ of $L$, still with only finitely many relation symbols and no operation symbols, and there is an $L$-$L'$-elementary class $\mathrm{Mod}_{L,L'} \psi$, such that the following conditions hold:

\begin{enumerate}
  \item[(1)] For any $\mathfrak{A} \in \mathrm{Mod}_{L',L'} \psi$, $\mathbf{P}^{2\mathfrak{A}}$ is finite and nonempty.
  \item[(2)] For every $n \in \omega \sim 1$ there is a countable $\mathfrak{A} \in \mathrm{Mod}_{L',L'} \psi$ such that $|\mathbf{P}^{2\mathfrak{A}}| = n$.
\end{enumerate}

By 26.19(v)(2) we may assume that $L'$ is a reduct of $\mathbf{L}_{\mathrm{un}}$. Let $L''$ be an expansion of $L'$ by adjoining a binary relation symbol $R$, with $L''$ still a reduct of $\mathbf{L}_{\mathrm{un}}$. Say the symbols of $L''$ are $S_0, \ldots, S_{m-1}, R, P$, of ranks $n_0, \ldots, n_{m-1}, 2, 1$ respectively. By 26.19(iv)(3) let $\chi$ be an $L$-$L''$-sentence such that

\begin{enumerate}
  \item[(3)] $\mathrm{Mod}_{L''',L} \chi = \{\mathfrak{A} \in \mathbf{S}_{L''}: \mathfrak{A} \upharpoonright L' \in \mathrm{Mod}_{L',L'} \psi\}$.
\end{enumerate}

Let $\bar{L}''$ be the reduct of $L''$ to $R$. We recall the following fact about $\bar{L}''$ which is a consequence of 16.52 and 15.32:

\begin{enumerate}
  \item[(4)] $g^{+*} \{\theta \in \mathrm{Sent}_{\bar{L}''}: \theta \text{ holds in all finite } \bar{L}''\text{-structures}\}$ is not r.e.
\end{enumerate}

The argument then proceeds by constructing a recursive translation that would contradict the non-r.e. property (4), thereby establishing $L \subseteq L_{\mathrm{fo}}$. Since $L_{\mathrm{fo}} \subseteq L$ by hypothesis, we obtain $L_{\mathrm{fo}} \equiv L$.

[The proof continues using effectivization: Now we show that $L \subseteq_{\mathrm{eff}} L_{\mathrm{fo}}^{\mathrm{eff}}$. Let $f$ be a recursive function with range $g^{+*} \mathrm{Sent}_{\mathcal{L}(\mathrm{un})}$. For any $x, y \in \omega$ set

$$k(x, y) = \mathrm{Un}_L(\mathrm{Int}_L(x, \mathrm{Trans}_{L(\mathrm{fo}, \mathrm{eff})}, L fy), \mathrm{Int}_L(\mathrm{Comp}_L x, \mathrm{Comp}_L \mathrm{Trans}_{L(\mathrm{fo}, \mathrm{eff})}, L fy)).$$

Thus $k$ is a recursive function, and if $(\mathcal{L}, \Gamma, \mathfrak{A}, \varphi, h) \in L$, $\psi \in \Gamma$, $\mathcal{L}$ is a reduct of $\mathcal{L}_{\mathrm{un}}$, $n \in \omega$, and $fn = g^{+} \chi$, then $k(h\psi, n) = h\theta$ for some $\theta \in \Gamma$ such that

$$\mathrm{Mod}_{\mathcal{L}, L} \theta = (\mathrm{Mod}_{\mathcal{L}, L} \psi \cap \mathrm{Mod}_{\mathcal{L}, L(\mathrm{fo}, \mathrm{eff})} \chi) \cup [(\mathbf{S}_{\mathcal{L}} \sim \mathrm{Mod}_{\mathcal{L}, L} \psi) \cap (\mathbf{S}_{\mathcal{L}} \sim \mathrm{Mod}_{\mathcal{L}, L(\mathrm{fo}, \mathrm{eff})} \chi)].$$

Thus

\begin{enumerate}
  \item[(8)] $\mathfrak{A} \models_{\mathcal{L}, L} \theta$ for all $\mathfrak{A} \in \mathbf{S}_{\mathcal{L}}$ iff $\mathrm{Mod}_{\mathcal{L}, L} \psi = \mathrm{Mod}_{\mathcal{L}, L(\mathrm{fo}, \mathrm{eff})} \chi$.
\end{enumerate}

Now by the assumption of the theorem and 26.25(iv), let $l$ be a recursive function [...].]
