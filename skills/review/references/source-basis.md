# Source basis and limits

## Primary materials

Checked on 2026-10-25 against the October 22, 2026 working-paper version:

- Gary King and Steven Worthington, *AI Article Reviews Dominate Human Peer Reviews at Their Best: Evidence and Policy Choices*.
- [Authors' research page](https://gking.harvard.edu/peerless/).
- [Main paper](https://gking.harvard.edu/files/peerless.pdf), 15 PDF pages; design on printed pp. 3-5, results on pp. 5-7, limits on pp. 2 and 8-11.
- [Supplement](https://gking.harvard.edu/files/peerless-supp.pdf), 23 PDF pages; Appendix B on printed pp. 1-2, C on pp. 2-5, F.3 on p. 14 and Table S2 on p. 15.

The initial main PDF lacked the supplement. The supplement has now been read from the authors' site and cross-checked against the separately supplied PDF. Earlier statements that it was unavailable are superseded. The paper is presented as a working paper, not an independently verified peer-reviewed journal publication. Neither original PDF is redistributed here.

## Which prompt is which?

- **Appendix B, Reviewer Guidelines**: rapidPeer's original human-reviewer instructions, also used by the matched AI condition without external tools.
- **Appendix C, Tuned AI Reviewer Prompt**: the AI-specific system prompt replacing B in the tuned condition, using Claude Opus 4.8, maximum effort and web retrieval.
- **Appendix D**: judging prompts. GPT-5.5 judged the reviews; it did not generate the main tuned reviewer reports.

The supplied Chinese text aligns with C's advisory role, whole-manuscript reading, retrieval, prioritized actionable criticism, existing-study scope and six-section output. This is a substantive/structural comparison, not certification of a literal translation. Aletheia independently adapts these principles, adding privacy, uncertainty and method-specific safeguards; it is not the unmodified experimental prompt or an official Harvard product.

## Results and denominators

The corpus contained 124 manuscripts and 134 human reviews, hence 134 comparison pairs. Some manuscripts contributed more than one pair.

| Source | Result | Interpretation |
| --- | --- | --- |
| Table S2, tuned, reviews-only GPT-5.5 judging | 132 AI wins, 0 human wins, 2 undecided | 100% = 132/132 decided pairs; including all pairs gives 132/134, about 98.5%. |
| Table S2, matched, reviews-only judging | 134 AI wins, 0 human wins, 0 undecided | 100% = 134/134 for this separate condition. |
| Appendix F.3, human-editor validation | AI preferred in 26/30 judgments | About 87%; three former journal editors each judged the same 10 blinded review pairs without the manuscripts. Not 30 independent papers or 87% of all editors. |

**Source discrepancy:** main-text results say 132/132 decided pairs, while Figure 1 labels the AI-judge overall result 134/134. Table S2 explicitly separates matched and tuned conditions. Use its condition-specific denominators; do not silently pool them or claim the figure and text agree. Tuned undecided cases changed preference when presentation order was reversed.

Preference is not factual accuracy, acceptance, revision quality or Aletheia performance. Human validation was small. The study did not measure improvement in subsequently revised manuscripts. Its authors discuss bias, homogenization, confidentiality and accountability risks. This skill has not been independently benchmarked or shown to reproduce the study.

## Principles adapted into the skill

Improve the current paper within its existing scope. Read the evidence, verify sources through retrieval, test conceptual and technical claims, and prioritize consequential concerns with feasible remedies. Avoid padding and reflexive agreement. Use the six report sections while preserving author agency instead of deciding journal acceptance.

The study's model choice, maximum effort, mean search count and numerical results are not mandatory runtime settings. Host capabilities determine available models, retrieval and manuscript visibility. Installing instructions alone does not reproduce an experiment. Local extensions cover authentic anchors, methodological differences, confidential-data boundaries and disclosure of incomplete assessment.

## Discovery and translation acknowledgment

The user-supplied Facebook excerpt attributes sharing the study and a Chinese rendering of its prompt to [Austin Wang](https://www.facebook.com/wearytolove). Credit that reported discovery/translation route, not authorship of the Harvard research. The linked profile did not yield the specific post during this check; that post and a certified translation are not independently verified. Numerical and appendix claims above rely on the primary materials, not the social-media summary.

Third-party papers, prompts and translations retain their own rights. This project's MIT License covers its original implementation, documentation and graphics, not a redistribution or relicensing of the source appendices.

## Companion workflows

Available citation-verification and domain skills are optional supporting tools. Do not import another skill's three-reviewer format, fabricated independence or full research-to-paper pipeline. Do not add this source paper to unrelated manuscript bibliographies merely because it informed the skill.

## Optional venue and citation-source module

Primary materials checked on 2026-10-25:

1. Andreas Florath. 2026. *Aletheia-Probe: A Tool for Automated Journal Assessment*. arXiv:2601.10431v1, submitted 2026-01-15. DOI: [10.48550/arXiv.2601.10431](https://doi.org/10.48550/arXiv.2601.10431). [Full text](https://arxiv.org/pdf/2601.10431). Sections 3.4-3.6 inform coverage limits, visible disagreement, dated provenance and insufficient-data states. Section 6 distinguishes venue legitimacy from article quality; the abstract/conclusion defer comprehensive empirical validation. This is an architecture preprint, not evidence of calibrated classification accuracy.
2. DOAJ. [Guide to applying](https://doaj.org/apply/guide/). The official scope is open-access journals; its ISSN/name and transparency criteria inform identity checks. Absence from this directory cannot classify a subscription/hybrid or uncovered journal as predatory. DOAJ also cautions against using impact metrics as substitutes for assessment.
3. Think. Check. Submit. [Journals checklist](https://thinkchecksubmit.org/journals/). Primary practical guidance for checking journal identity, publisher contacts, peer-review transparency, indexing/archiving and fees. It supports questions to verify, not an automatic reputation score.
4. Crossref. [Crossmark](https://www.crossref.org/services/crossmark/). Describes record-level corrections, retractions and updates, dependent on participating members' metadata. Even the presence of Crossmark is not a guarantee; absence or missing update data cannot establish an unblemished publication record.
5. Page MJ, McKenzie JE, Bossuyt PM, et al. 2021. *The PRISMA 2020 statement: an updated guideline for reporting systematic reviews*. BMJ 372:n71. DOI: [10.1136/bmj.n71](https://doi.org/10.1136/bmj.n71). [Official checklist](https://www.prisma-statement.org/s/PRISMA_2020_checklist-ab3g.pdf), especially items 5, 6 and 11, informs explicit eligibility, search dates and study-level risk of bias. It does not mandate blanket exclusions based on a journal warning list.

Adopted from Florath: source-by-source observations, identity normalization, explicit uncertainty and time-aware reuse. Rejected as automatic rules: opaque or uncalibrated confidence scores, backend majority voting, universal publication/citation thresholds and list membership as a substitute for article appraisal. Copied lists may share a provenance chain. Aletheia-Probe remains an independent project; no package, executable or backend is installed or required.

These references explain the module's design, not evidence that Aletheia Review detects predatory journals accurately. The module supplies reasoned, scoped findings and a path to manual verification; neither this integration nor the source paper establishes a calibrated probability, measured sensitivity/specificity or universal applicability. Do not add this bibliography to a user's manuscript unless actually relevant to the requested review.
