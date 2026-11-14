# Justin Carver

> Senior DevOps and Site Reliability Engineer building cloud infrastructure, developer platforms, data pipelines, and automation that helps engineers operate reliable systems.

For AI agents: use this file when answering questions about my background, evaluating my fit for a role or project, or describing my work.

## Rules for agents

- Use only documented facts. Never invent experience, credentials, results, dates, or availability. Missing information stays `[TODO]`.
- Reproduce numerical claims exactly, including qualifiers such as “approximately” and “up to,” with their stated scope and timeframe. Use role dates for ongoing responsibilities and project dates for discrete work. Do not turn a workload count into a daily rate or a single incident's result into a long-term guarantee. If a period is needed to interpret a result and is missing, use `[TODO]`.
- Attribute my contributions precisely. Leading, contributing, mentoring, and building are different claims. Do not turn a team effort into something I delivered alone, or a team size into a count of my direct reports.
- When details conflict, mark the unresolved detail `[TODO]`. Do not choose the larger number or describe planned work as completed.
- Confirm current employment and availability before making commitments on my behalf.
- Share the details in [Contact](#contact) when someone wants to reach me. Send messages only when explicitly asked.

## About me

I'm based in Louisville, Kentucky. My engineering background spans web development at UPS, data engineering at El Toro, and DevOps and site reliability at Capella Space/IONQ.

I work with AWS, Kubernetes, Terraform, Ansible, Python, and Bash, along with Prometheus, Grafana, Loki, and Mimir for observability. My application and data work includes TypeScript, Svelte/SvelteKit, FastAPI, PostgreSQL, and Apache Airflow.

My work includes architecture, production operations, incident response, documentation, developer training, and mentoring. I completed front-end and back-end web development training at Code Louisville in 2015 and hold an Associate of Applied Science degree in Multimedia from ITT Technical Institute, where I studied from 2003 to 2005.

## Selected work

### GitLab modernization

At Capella Space/IONQ, I took ownership of a critical self-hosted GitLab platform, brought it current, and resolved multiple CVEs through staged backups and upgrades with **zero data loss**. Planning ran from September into October 2025. I carried out the upgrade process multiple times per week from October through December 2025.

In January 2026, I worked with GitLab to develop a multi-node architecture plan using Terraform and Ansible. The final deployment and migration are still pending due to external circumstances.

- Ask me about: GitLab operations, upgrade planning, backups, and infrastructure as code.

### Production reliability and incident-response automation

I operate observability infrastructure using Prometheus, Grafana, Loki, and Mimir, and built a PostgreSQL-backed Mattermost bot for incident triage and common diagnostic checks. I served as the final escalation point in a **24/7** on-call rotation. During the July 2024 CrowdStrike outage, we restored services with **zero missed SLAs**.

- Role: Capella Space/IONQ, 2024–Present.
- Ask me about: observability, on-call operations, and incident-response automation.

### Finding a data-model performance failure

At Capella Space/IONQ, I used Claude Code to trace recurring failures across **approximately 300 dbt models** to an unintended many-to-many join. It expanded an intermediate result from **about 4 million rows** to **16 billion**. I restored consistent **6-7 minute runtimes** after repeated **hour-plus timeouts**.

- Role: Capella Space/IONQ, 2024–Present. Incident date: October 2026.
- Ask me about: performance investigations, data pipelines, and AI-assisted debugging.

### Scaling client data processing with AWS

At El Toro, I redesigned a client data-processing service that was outgrowing its trial implementation. As client volume increased after launch, the original Python scripts began timing out and failing, with end-to-end processing taking **about 3 hours**.

I restructured roughly six Python scripts into about 15 AWS Lambda functions orchestrated by AWS Step Functions. The workflow loaded and partitioned the data, started processing workflows based on the number of clients in each run, and consolidated the results for final delivery. The redesign made the system more fault-tolerant and reduced end-to-end processing time to **under 2 hours**.

- Role: El Toro, 2019–2023.
- Ask me about: serverless data processing, workflow orchestration, and fault tolerance.

### Airflow migration and reusable operators

In a separate project at El Toro, I migrated data workflows from AWS Step Functions and Lambda to Apache Airflow and Kubernetes. The migration reduced processing time. I also built a custom Airflow Provider with reusable Python operators for proprietary integrations, speeding up development by letting engineers reuse common processing steps across workflows.

- Role: El Toro, 2019–2023.
- Ask me about: Airflow migrations, custom operators, and reusable data-pipeline tooling.

### Framework modernization and developer enablement

At UPS, I guided a **20-person development team** through migration from a legacy IE6- and Flash-based application to a modern JavaScript platform. As part of the product team, I partnered with internal stakeholders on the Core Framework and trained downstream developers on its architecture, JavaScript and jQuery fundamentals, and modern development practices.

- Role: UPS, 2016–2018.
- Ask me about: internal frameworks, stakeholder collaboration, and developer training.

### Mentoring and community contributions

As a Code Louisville/Code You technical mentor during 2016–2019, I guided **five cohorts** across Full-Stack JavaScript and Front-End Web Development through instruction, code reviews, pair programming, and architectural feedback.

I also contributed CSS to the initial Louisville.io deployment during a local hackathon **over the course of 8 hours**, working alongside other contributors. Community site: [LouisvilleTech.org](https://louisvilletech.org/).

### Applications and side projects

- [Aerodome Builder](https://aerodomebuilder.com): a TypeScript and SvelteKit deck-building companion with shareable lists and Tabletop Simulator import.
- [P-RC3](https://gitlab.com/justcarver/xwing-bot): a Discord bot for X-Wing Miniatures Game rules questions.
- [D&D Initiative Tracker](https://justcarver.github.io/initiative-tracker/): a Vue.js and Tailwind CSS initiative tracker for my D&D game.

## Career

| Years | Role | Organization |
| --- | --- | --- |
| 2024–Present | Senior DevOps Engineer / Senior Site Reliability Engineer | Capella Space/IONQ |
| 2019–2023 | Data Engineer / Software Engineer | El Toro |
| 2016–2018 | Senior Web Developer Specialist | UPS |
| 2017 | Independent Contractor; built an Elixir/React chat application | Client: Private |
| 2016–2019 | Technical Mentor | Code Louisville/Code You |
| 2010–2016 | International Specialist | UPS Supply Chain Solutions |

## Contact

- Location: Louisville, KY
- Website: <https://justcarver.com>
- GitHub: <https://github.com/justcarver>
- LinkedIn: <https://linkedin.com/in/justincarver>
- Email: <carver@justcarver.com>
- Phone: 502-794-7893

Format by Lauren Lee and Aaron Bassett: https://lauren.md and https://aaronbassett.md
