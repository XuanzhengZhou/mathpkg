---
role: proof
locale: en
of_concept: valuation-of-defined-connectives
source_book: gtm037
source_chapter: "Chapter 8: Sentential Logic"
source_section: "2. Elements of Logic"
---
This is stated as an obvious proposition in the text. The proof follows directly from Definition 8.30 and the truth-table semantics of $\neg$ and $\rightarrow$:

For $\lor$: $f^+(\varphi \lor \psi) = f^+(\neg\varphi \to \psi) = 1$ iff $f^+(\neg\varphi)=0$ or $f^+\psi=1$, i.e., iff $f^+\varphi=1$ or $f^+\psi=1$.

For $\land$: $f^+(\varphi \land \psi) = f^+(\neg(\varphi \to \neg\psi)) = 1$ iff $f^+(\varphi \to \neg\psi)=0$, i.e., iff $f^+\varphi=1$ and $f^+(\neg\psi)=0$, i.e., iff $f^+\varphi=1$ and $f^+\psi=1$.

For $\leftrightarrow$: $f^+(\varphi \leftrightarrow \psi) = f^+((\varphi\to\psi) \land (\psi\to\varphi)) = 1$ iff both implications hold, i.e., iff $f^+\varphi = f^+\psi$.
