---
role: proof
locale: en
of_concept: unique-readability-of-sentences
source_book: gtm037
source_chapter: "8"
source_section: "8.1"
---

\begin{proof}
Let $\varphi = \langle \varphi_0, \ldots, \varphi_{m-1} \rangle$ be a sentence. We prove by induction on $m$ that $\varphi$ satisfies exactly one of (i)-(iii).

If $m = 1$, then $\varphi = \langle s \rangle$ for some $s \in P$, since the only expressions of length 1 that are sentences are atomic ones. Then (i) holds uniquely.

Now assume, inductively, that $m > 1$. Since $\varphi$ is a sentence, it must be formed by $\neg$ or $\rightarrow$ from shorter sentences.

\textbf{Case 1:} $\varphi = \neg \psi$ for some sentence $\psi$. Thus $\varphi_0 = n$, and $\psi = \langle \varphi_1, \ldots, \varphi_{m-1} \rangle$. If $\langle \varphi_0, \ldots, \varphi_i \rangle$ is a sentence, then it must be $\neg \theta$ for some sentence $\theta$, so $\langle \varphi_1, \ldots, \varphi_i \rangle$ would be a sentence, contradicting the induction hypothesis that $\psi$ is a sentence and no proper initial segment of $\psi$ is a sentence. Hence (ii) holds uniquely.

\textbf{Case 2:} $\varphi = \psi \rightarrow \chi$ for sentences $\psi$ and $\chi$. Then $\varphi_0 = c$, and there is a $j$ with $1 < j < m-1$ such that $\psi = \langle \varphi_1, \ldots, \varphi_j \rangle$ and $\chi = \langle \varphi_{j+1}, \ldots, \varphi_{m-1} \rangle$. Suppose that $\langle \varphi_0, \ldots, \varphi_i \rangle$ is a sentence. Then it must be $\theta \rightarrow \sigma$ for sentences $\theta, \sigma$; hence there is a $k$ with $1 < k < i$ such that $\theta = \langle \varphi_1, \ldots, \varphi_k \rangle$ and $\sigma = \langle \varphi_{k+1}, \ldots, \varphi_i \rangle$. Since $k, j < m-1$ and $\psi$ and $\theta$ are sentences, the induction hypothesis gives $k = j$. But then $\sigma$ is a proper initial segment of $\chi$, contradicting the induction hypothesis. Hence (iii) holds uniquely.

Part (iv) (uniqueness of decomposition for implication) is easily established using (iii).
\end{proof}
