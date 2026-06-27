---
role: proof
locale: en
of_concept: lemma-4-22
source_book: gtm040
source_chapter: "4"
source_section: "22"
---

Proof: The result is obvious if $i = j$. If $i \neq j$, consider returning to $i$ with and without first reaching $j$. By conclusion (3) of Lemma 4-19,

$$1 = \bar{H}_{ii} = i\bar{H}_{ij}H_{ji} + j\bar{H}_{ii}$$

Since $i\bar{H}_{ij} + j\bar{H}_{ii} \leq 1$, this equation is a contradiction unless $j\bar{H}_{ii} = 1$ or $H_{ji} = 1$. The first alternative is ruled out by Lemma 4-22. Thus $H_{ji} = 1$ and $i\bar{H}_{ij} = 1 - j\bar{H}_{ii}$. Next, since $i$ is recurrent, one may compute $H_{ij}$ by summing the probabilities of reaching $j$ for the first time after $n$ returns to $i$, where $n = 0, 1, 2, \ldots$. By conclusion (4) of Lemma 4-19,

$$H_{ij} = \sum_{n=0}^{\infty} (j\bar{H}_{ii})^n i\bar{H}_{ij} = (1 - j\bar{H}_{ii}) \sum_{n=0}^{\infty} (j\bar{H}_{ii})^n = 1.$$

The last equality holds, since $j\bar{H}_{ii} < 1$ by Lemma 4-22.

Proposition 4-24: All states in an equivalence class are of the same

Proposition 4-26: Recurrent classes are closed and maximal with respect to the partial ordering $R$.

Proof: It is sufficient to prove that a recurrent class $S'$ is closed, since closed classes are clearly maximal. Suppose the class can be left, say from a state $j \in S'$. If $k$ is a state outside $S'$ for which $P_{jk} > 0$, then it is not true that $R(k,j)$ because $j$ and $k$ do not communicate. Thus $\bar{H}_{jj} \leq 1 - P_{jk} < 1$, and $j$ is not recurrent.

Proposition 4-27: If a Markov chain is started in a recurrent class $S'$, then the chain is in every state of $S'$ infinitely often with probability one. In particular, if $i$ and $j$ are in $S'$, then $N_{ij} = +\infty$.

Proof: Suppose the chain is started in state $i$. Then, by conclusion (5) of Lemma 4-19, the probability of being in state $j$ at least $n$ times is $H_{ij}(\bar{H}_{jj})^{n-1} = 1$. By Proposition 2-6 the chain is in state $j$ infinitely often with probability one. Again by Proposition 2-6 it is in every state infinitely often with probability one.

Proposition 4-28: A Markov chain is in a finite subset of transient states only finitely often, with probability one.

Proof: If the chain were in a finite set $S'$ infinitely often with positive probability, it would be in one state $j$ of $S'$ infinitely often with positive probability. Such an occurrence would imply that $N_{ij}$ is infinite for some $i$, in contradiction to Corollary 4-21 if $j$ is transient.

We single out two kinds of Markov chains for special attention. We note that every absorbing state forms a one-element recurrent class, and conversely.

Definition 4-29: A Markov chain is said to be a recurrent chain if its states comprise a single equivalence class and if that class is

(2) If the process $P$ starts in a transient state, its behavior while in transient states is the same as the behavior of the transient chain $P'$ obtained from $P$ by making all recurrent states absorbing. If $P$ enters a recurrent state, then $P'$ becomes absorbed. And after $P$ has entered a recurrent state, its properties are those of a recurrent chain. Thus the properties of $P$ may be studied by considering the one transient chain $P'$ and the $r$ separate recurrent chains.

Because of these observations, we shall restrict our discussion in subsequent chapters to Markov chains which are either transient or recurrent.

The reader should notice that every chain whose states form only one equivalence class is either a transient chain or a recurrent chain. Shortly we shall examine the basic example, in which all pairs of states communicate, to determine when it is transient and when it is recurrent.

First we discuss some properties of maximal classes for a moment. Not every chain has maximal classes; a tree process, for example, consists of infinitely many transient classes of one state each. None of the classes is maximal. Even if a chain does have a maximal class, that class does not have to be closed. The process may have a positive probability of disappearing from some state in the maximal class.

Nor is it true that all closed classes are recurrent. An additional condition is needed.
