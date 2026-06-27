---
role: proof
locale: en
of_concept: first-entrance-decomposition
source_book: gtm095
source_chapter: "1"
source_section: "12"
---

# Proof of the First Entrance Decomposition Formula

## Theorem (First Entrance Decomposition)

Let $\xi = (\xi_0, \xi_1, \ldots, \xi_n)$ be a homogeneous Markov chain with transition matrix $\|p_{ij}\|$. Define the first entrance probabilities

$$
f_{ij}^{(k)} = \mathrm{P}\{\xi_k = j, \xi_l \neq j \text{ for } 1 \leq l \leq k-1 \mid \xi_0 = i\}, \qquad k \geq 1,
$$

where $f_{ii}^{(k)}$ is the probability of first return to state $i$ at time $k$ (for $i=j$) and $f_{ij}^{(k)}$ (for $i \neq j$) is the probability of first arrival at state $j$ at time $k$. Then for all $n \geq 1$,

$$
p_{ij}^{(n)} = \sum_{k=1}^{n} f_{ij}^{(k)} \, p_{jj}^{(n-k)}, \tag{*}
$$

where $p_{jj}^{(0)} = 1$ and $p_{ij}^{(n)} = \mathrm{P}\{\xi_n = j \mid \xi_0 = i\}$.

## Intuitive Meaning

The intuitive meaning of formula $(*)$ is clear: to go from state $i$ to state $j$ in $n$ steps, it is necessary to reach state $j$ for the first time in $k$ steps ($1 \leq k \leq n$) and then to go from state $j$ to state $j$ in the remaining $n-k$ steps.

## Proof

Fix the target state $j$ and define the first hitting time

$$
\tau = \min\{\,1 \leq k \leq n : \xi_k = j\,\},
$$

with the convention that $\tau = n+1$ if the set $\{1 \leq k \leq n : \xi_k = j\}$ is empty. Then by definition,

$$
f_{ij}^{(k)} = \mathrm{P}\{\tau = k \mid \xi_0 = i\}.
$$

Now decompose the $n$-step transition probability according to the value of the first hitting time:

$$
\begin{aligned}
p_{ij}^{(n)} &= \mathrm{P}\{\xi_n = j \mid \xi_0 = i\} \\[4pt]
&= \sum_{k=1}^{n} \mathrm{P}\{\xi_n = j, \tau = k \mid \xi_0 = i\} \\[4pt]
&= \sum_{k=1}^{n} \mathrm{P}\{\xi_{\tau+(n-k)} = j, \tau = k \mid \xi_0 = i\}.
\end{aligned}
$$

On the event $\{\tau = k\}$, we have $\xi_\tau = \xi_k = j$ and $\tau + (n-k) = n$, so $\xi_{\tau+(n-k)} = \xi_n$. Using the definition of conditional probability,

$$
\begin{aligned}
\mathrm{P}\{\xi_{\tau+(n-k)} = j, \tau = k \mid \xi_0 = i\}
&= \mathrm{P}\{\xi_{\tau+(n-k)} = j \mid \tau = k, \xi_0 = i\} \cdot \mathrm{P}\{\tau = k \mid \xi_0 = i\} \\[4pt]
&= \mathrm{P}\{\xi_{\tau+(n-k)} = j \mid \xi_\tau = j, \tau = k, \xi_0 = i\} \cdot f_{ij}^{(k)}.
\end{aligned}
$$

Now apply the strong Markov property at the stopping time $\tau$. Since on the event $\{\tau = k\}$ we know that $\xi_\tau = j$, the process restarts from state $j$ at time $\tau$, and therefore

$$
\mathrm{P}\{\xi_{\tau+(n-k)} = j \mid \xi_\tau = j, \tau = k, \xi_0 = i\}
= \mathrm{P}\{\xi_{n-k} = j \mid \xi_0 = j\}
= p_{jj}^{(n-k)}.
$$

Substituting this back, we obtain

$$
\begin{aligned}
p_{ij}^{(n)} &= \sum_{k=1}^{n} p_{jj}^{(n-k)} \cdot f_{ij}^{(k)} \\[4pt]
&= \sum_{k=1}^{n} f_{ij}^{(k)} \, p_{jj}^{(n-k)},
\end{aligned}
$$

which completes the proof of $(*)$.
