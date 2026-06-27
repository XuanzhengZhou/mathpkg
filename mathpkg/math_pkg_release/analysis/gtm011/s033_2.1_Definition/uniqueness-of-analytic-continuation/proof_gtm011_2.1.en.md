---
role: proof
locale: en
of_concept: uniqueness-of-analytic-continuation
source_book: gtm011
source_chapter: "2"
source_section: "2.1"
---

Define the set
$$T = \{t \in [0, 1]: [f_t]_{\gamma(t)} = [g_t]_{\gamma(t)}\}.$$
We show $T$ is both open and closed in $[0, 1]$; since $T$ is non-empty ($0 \in T$), $T = [0, 1]$ and in particular $1 \in T$.

**$T$ is open.** Fix $t \in T$ and assume $t \neq 0, 1$ (if $t = 1$ the proof is complete; if $t = 0$ the same argument shows $[a, a + \delta) \subset T$). By the definition of analytic continuation, there is $\delta > 0$ such that for $|s - t| < \delta$, we have $\gamma(s) \in D_t \cap B_t$ and
$$[f_s]_{\gamma(s)} = [f_t]_{\gamma(s)}, \quad [g_s]_{\gamma(s)} = [g_t]_{\gamma(s)}.$$
Let $H$ be a connected subset of $D_t \cap B_t$ which contains $\gamma(s)$ and $\gamma(t)$. Since $[f_t]_{\gamma(t)} = [g_t]_{\gamma(t)}$, there is a neighborhood of $\gamma(t)$ where $f_t$ and $g_t$ agree. By the Identity Theorem, they agree on all of $H$, so $[f_t]_{\gamma(s)} = [g_t]_{\gamma(s)}$. Combining with the relations above gives $[f_s]_{\gamma(s)} = [g_s]_{\gamma(s)}$, so $s \in T$. Hence $(t - \delta, t + \delta) \cap [0, 1] \subset T$, proving $T$ is open.

**$T$ is closed.** Suppose $t_n \in T$ and $t_n \to t$. By continuity of $\gamma$, $\gamma(t_n) \to \gamma(t)$. Choose $\delta > 0$ as in the definition of analytic continuation. For large $n$ we have $|t_n - t| < \delta$, so $\gamma(t_n) \in D_t \cap B_t$ and $[f_{t_n}]_{\gamma(t_n)} = [f_t]_{\gamma(t_n)}$, $[g_{t_n}]_{\gamma(t_n)} = [g_t]_{\gamma(t_n)}$. Since $t_n \in T$, $[f_{t_n}]_{\gamma(t_n)} = [g_{t_n}]_{\gamma(t_n)}$, which implies $[f_t]_{\gamma(t_n)} = [g_t]_{\gamma(t_n)}$. Hence $f_t$ and $g_t$ agree on a neighborhood of $\gamma(t_n)$ for all large $n$, and by the Identity Theorem they agree on a neighborhood of $\gamma(t)$, giving $[f_t]_{\gamma(t)} = [g_t]_{\gamma(t)}$, i.e., $t \in T$. Thus $T$ is closed.

Since $[0,1]$ is connected and $T$ is non-empty, open, and closed, $T = [0,1]$. Therefore $1 \in T$, which means $[f_1]_b = [g_1]_b$.
