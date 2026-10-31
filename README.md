# Aletheia Review

**Evidence-first scholarly review.**

![Aletheia Review v2: Harvard research context reports 100 percent GPT-5.5 preference among 132 decided pairs, with two undecided, and about 87 percent former-editor preference across 26 of 30 judgments. These are not accuracy, acceptance or Aletheia performance rates. Appendix C principles connect manuscript inputs to a six-section review.](assets/aletheia-review-overview-v2.png)

[Download the English LinkedIn infographic (v2)](assets/aletheia-review-overview-v2.png). This AI-generated poster separates the source study's preference results from Aletheia's workflow and summarizes Appendix C. Sources are [Supplement F.3 and Table S2](https://gking.harvard.edu/files/peerless-supp.pdf); these are not measured Aletheia results. [Original landscape overview](assets/aletheia-review-overview.png) remains available.

A reusable agent skill for constructive academic manuscript review: verify the literature, locate the real problem, and give the author a practical way to resolve it.

The name evokes *aletheia*, a Greek term associated with truth and disclosure. The package is **Aletheia Review**; the skill stays **Review**, with the identifier **`review`**. This is not a claim that the name is legally exclusive.

## A Research-Informed Reviewer You Can Reuse

Turn a carefully designed pre-submission review prompt into a persistent skill, rather than pasting a long prompt into every conversation. Improve the current paper with consequential criticism, relevant prior work and feasible revisions. This is an adviser, not an acceptance gatekeeper.

Gary King and Steven Worthington's October 22, 2026 [Harvard working paper](https://gking.harvard.edu/peerless/) and [supplement](https://gking.harvard.edu/files/peerless-supp.pdf) motivate this workflow:

| Evaluation | Reported result | What it means |
| --- | --- | --- |
| GPT-5.5 judging web-enabled AI reviews | 100% of decided comparisons: 132/132 | Table S2's tuned condition includes 134 pairs, two undecided. This is preference, not accuracy. |
| Three former journal editors | 26/30 judgments, about 87% | Each judged the same 10 blinded review pairs without the manuscripts. Not 30 independent papers or 87% of all editors. |

The tuned reviewer was Claude Opus 4.8 at maximum effort with web retrieval; GPT-5.5 was the judge. These results are **not Aletheia Review's measured performance**, an acceptance rate or proof that human reviewers are obsolete. The study did not measure improvements in subsequent revisions. See [source details and denominator caveats](skills/review/references/source-basis.md).

**Appendix C is the tuned AI reviewer prompt; Appendix B is the original rapidPeer guide.** Aletheia independently adapts C's constructive, retrieval-supported principles and six-section structure, adding privacy and method-specific checks. Similar instructions do not reproduce the experiment or transfer its results to another model.

Acknowledgment: the user-supplied Chinese excerpt credits [Austin Wang](https://www.facebook.com/wearytolove) with sharing the study and a Chinese rendering of its prompt. That is the reported discovery/translation route, not the evidence for the study's numbers.

## What It Does

- Reads the supplied manuscript and accessible supplements, including figures and tables when the host can inspect them.
- Searches relevant recent and foundational literature, close prior art, and rival explanations.
- Requires live verification of every external reference used in its report, with a DOI or original URL.
- Separates confirmed errors, plausible threats, reporting gaps, and unavailable evidence.
- Prioritizes manuscript-specific concerns with locations, consequences, feasible remedies, and resolution tests.
- Includes method-sensitive checks for quantitative, qualitative, mixed-methods, bioinformatics, multi-omics, computational, and evidence-synthesis work.
- Produces one author-facing report, not an editorial acceptance decision or a simulated three-reviewer panel.

This is an instruction-only skill, not an autonomous review service. It does not include a model, search subscription, API key, manuscript database, or MCP server. It uses the tools available in the host application.

## Optional Journal and Citation-Source Checks

The [optional module](skills/review/references/venue-source-check.md) activates for an explicit journal/source audit, a requested venue recommendation, or a concrete identity/integrity concern about an important citation. Ordinary manuscript review does not automatically scan every journal.

It compares journal name, ISSN, publisher and domain; checks material article updates; preserves dates, source disagreements and coverage gaps; and reuses matching venue checks without merging DOI-specific article status. Outcomes are **checked**, **risk signal**, **conflicting**, or **insufficient data**, with evidence and next steps. No uncalibrated confidence percentage or aggregate reputation score is used.

Unlisted is not predatory, indexed is not scientifically valid, and venue concerns do not automatically lower manuscript readiness or exclude a study. Relevant findings stay within the existing six report sections. The module is informed by [Florath's Aletheia-Probe paper](https://doi.org/10.48550/arXiv.2601.10431) and [official guidance](skills/review/references/source-basis.md#optional-venue-and-citation-source-module), but installs no third-party classifier or extra dependency.

Example: `$review Review this manuscript and check the identity and publication status of the important cited sources. Keep the six-section report; disclose uncertainty without numeric confidence scores.`

## Install in Codex

Ask Codex's skill installer:

```text
$skill-installer Install skills/review from https://github.com/Vincent4811/aletheia-reviewer.
```

Then invoke the installed skill:

```text
$review Review the attached manuscript and supplements. Verify relevant literature and return the six-section report in English.
```

Traditional Chinese is the default unless you request another language:

```text
$review 請審查附上的論文與補充資料，核對重要文獻，以繁體中文輸出正式審查意見。
```

Skill discovery and explicit invocation depend on the client. If a newly installed skill is missing, start a new session or restart the client. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Use in ChatGPT

This repository also includes a skills-only plugin manifest. Supported clients can package or install it as **Aletheia Review** and expose the bundled **Review** skill. After it is actually enabled, select **Review** from the `@` menu where supported.

Cloning this repository, attaching its ZIP to a chat, or installing it locally in Codex does **not** automatically install it in ChatGPT web, mobile, or another account. Local marketplace installation, workspace distribution, and availability vary by product and account. See [plugin packaging](https://developers.openai.com/plugins/build/plugins) and [installation testing](https://developers.openai.com/plugins/deploy/connect-chatgpt).

A textual `@Review` can be interpreted as an alias when these instructions are already loaded. That is not registration of a universal native mention. Do not assume a name typed in plain text has selected a skill.

## Report Structure

1. **Summary**: Research question, methods, claimed contribution, and material assessment limits.
2. **Strengths**: Specific, evidence-grounded strengths.
3. **Key Claims**: Prioritized central concerns, each with a manuscript location, evidence, significance, and feasible resolution.
4. **Specific Comments**: Useful secondary corrections with authentic locations.
5. **Literature and Data to Engage**: Verified references or datasets, linked to the relevant concern.
6. **Overall Assessment**: Ready to Submit, Minor Revisions, Major Revisions, or Rethink, with a short rationale. Incomplete central evidence may require a provisional or unassigned assessment.

Two or three high-value concerns are a prioritization target, not a quota. The skill must not invent defects to appear rigorous or inflate a local presentation issue into a fatal flaw.

## Privacy and Scientific Boundaries

Keep unpublished manuscripts, participant identifiers, distinctive confidential findings, and raw research data out of public repositories and external search queries. Review in the current environment does not authorize onward disclosure to another model, converter, or service. For confidential third-party peer review, establish permission and follow the applicable journal and institutional AI policy.

Do not assume an AI review verifies raw data, proves a causal mechanism, reproduces code, detects all image manipulation, or guarantees acceptance. When tools or source access are insufficient, the report must disclose that limitation rather than invent citations or completed analyses. Human authors remain responsible for scientific decisions.

## Package

```text
LICENSE
plugin.json
assets/aletheia-review-overview-v2.png
skills/review/
  SKILL.md
  agents/openai.yaml
  references/method-specific-checks.md
  references/source-basis.md
examples/review-requests.md
docs/validation.md
```

## Provenance and Validation

The workflow draws on the supplied Chinese prompt and King and Worthington's *AI Article Reviews Dominate Human Peer Reviews at Their Best: Evidence and Policy Choices*. On October 25, 2026, the primary paper and supplement were checked directly, including Appendices B/C, F.3 and Table S2. Appendix C's role, workflow and six-section format align with the Chinese text. This is an independent adaptation, not a certified literal translation or verbatim redistribution.

[Gary King](https://www.wcfia.harvard.edu/people/gary-king) is the Albert J. Weatherhead III University Professor at Harvard University; [Steven Worthington](https://www.iq.harvard.edu/people/steven-worthington-0) is Director of Data Science Services at Harvard's Institute for Quantitative Social Science. These links verify institutional roles, not endorsement of this project.

The original PDF is not redistributed. This is an independent implementation, not an official product of the paper's authors, Harvard, Nature, or OpenAI. See [source basis](skills/review/references/source-basis.md).

Metadata, reference paths, packaging, and disclosure checks have been tested. This is not a benchmark demonstrating review accuracy, superiority to human reviewers, or cross-client end-to-end performance. See [validation scope](docs/validation.md).

## Licensing

This project's original skill instructions, documentation and overview graphic are released under the [MIT License](LICENSE). Copyright (c) 2026 Vincent4811. Third-party papers and other external source material retain their own rights and are not relicensed by this repository.

If this workflow is useful, star the repository, try it on a manuscript you are authorized to process, and share grounded feedback through GitHub Issues. Check citations and substantive criticisms yourself before acting on an AI-generated review.
