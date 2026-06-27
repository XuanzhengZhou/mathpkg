---
role: proof
locale: en
of_concept: martingale-convergence-cases
source_book: gtm046
source_chapter: "IX-X"
source_section: "32"
---

The convergence properties of the four types of martingales and submartingales are summarized as follows.

**I. Martingale sequence \(X_1, X_2, \ldots\):**
Since \(E(X_{n+1} \mid \mathcal{B}_n) = X_n\), taking expectations gives \(EX_1 = EX_2 = \cdots\). By the conditional Jensen inequality, \(EX_1^+ \leq EX_2^+ \leq \cdots\) and \(E|X_1|^r \leq E|X_2|^r \leq \cdots\) for \(r \geq 1\). If \(\lim EX_n^+ < \infty\), then \(\sup EX_n^+ < \infty\) and by the submartingale convergence theorem (29.3A), \(X_n \xrightarrow{a.s.} X\) with \(X < +\infty\). The case \(\lim EX_n^- < \infty\) follows by symmetry (apply to \(-X_n\)). Closure: the martingale is closed on the right by \(Y \in L_r\) iff the \(|X_n|^r\) are uniformly integrable; in that case \(X_n \xrightarrow{a.s.} X\) and \(X\) is the nearest closing random variable. If \(\sup E|X_n|^r < \infty\) with \(r > 1\), then uniform integrability follows and such a \(Y\) exists by the \(L_r\)-convergence theorem.

**II. Submartingale sequence \(X_1, X_2, \ldots\):**
Since \(E(X_{n+1} \mid \mathcal{B}_n) \geq X_n\), taking expectations gives \(EX_1 \leq EX_2 \leq \cdots\) and \(EX_1^+ \leq EX_2^+ \leq \cdots\). When \(X_n \geq 0\) a.s., \(X_n^r\) is a submartingale for \(r \geq 1\) (by conditional Jensen), giving \(EX_1^r \leq EX_2^r \leq \cdots\). If \(\lim EX_n^+ < \infty\), the submartingale convergence theorem yields \(X_n \xrightarrow{a.s.} X < \infty\). If \(\sup E|X_n| < \infty\) and either every \(X_n \leq 0\) a.s. or every \(X_n \geq 0\) a.s., then the limit \(X\) is finite.

**IV. Submartingale reversed sequence \(\cdots, X_2, X_1\):**
Here \(E(X_n \mid \mathcal{B}_{n+1}) \geq X_{n+1}\) for the reversed filtration, so taking expectations gives \(\cdots \leq EX_2 \leq EX_1\) and \(\cdots \leq EX_2^+ \leq EX_1^+\). If \(X_n \geq 0\) a.s., then \(\cdots \leq EX_2^r \leq EX_1^r\). If \(EX_1^+ < \infty\), the reversed submartingale convergence theorem gives \(X_n \xrightarrow{a.s.} X < \infty\). Closure: if the \(|X_n|^r\) are uniformly integrable, then \(X_n \xrightarrow{a.s.} X \in L_r\) and \(X\) closes the submartingale on the left. For \(r = 1\), a necessary and sufficient condition is \(\sup E|X_n| < \infty\) (equivalently \(E|X_1| < \infty\)) together with \(\lim EX_n > -\infty\).
