"""
Pre-packaged sample resumes and job descriptions for rapid testing and demonstrations.
"""

SAMPLE_JOBS = [
    {
        "id": "fullstack_sr",
        "title": "Senior Full-Stack Engineer (React, Python, AWS)",
        "company": "CloudScale Technologies",
        "text": """Job Title: Senior Full-Stack Engineer
Company: CloudScale Technologies
Location: Remote / Hybrid

About The Role:
We are seeking an experienced Senior Full-Stack Engineer with 5+ years of experience to lead development of our flagship analytics platform. You will design, build, and deploy high-performance web applications, scalable backend microservices, and robust cloud infrastructure.

Key Responsibilities:
- Architect and develop modern, responsive frontend web applications using React, TypeScript, Next.js, and Tailwind CSS.
- Build resilient, high-throughput REST APIs and asynchronous backend workflows using Python, FastAPI, and Node.js.
- Design relational and NoSQL database schemas using PostgreSQL and Redis for distributed caching.
- Deploy, monitor, and scale cloud infrastructure on AWS using Docker, Kubernetes, Terraform, and GitHub Actions for CI/CD.
- Implement comprehensive automated testing with PyTest, Jest, and Cypress to guarantee reliability.
- Collaborate with product designers and engineering teams in an Agile Scrum environment.

Required Qualifications & Skills:
- 5+ years of software engineering experience in full-stack web development.
- Strong proficiency in Python, JavaScript, and TypeScript.
- Deep hands-on experience with React, Next.js, and modern CSS frameworks (Tailwind).
- Proven expertise in FastAPI, Django, or Node.js/Express backend frameworks.
- Solid experience with relational databases (PostgreSQL) and caching layers (Redis).
- Practical experience with Docker, Kubernetes, and AWS cloud services (S3, ECS, Lambda).
- Experience setting up automated CI/CD pipelines (GitHub Actions, GitLab CI).
- Bachelor's degree in Computer Science, Software Engineering, or equivalent experience.
- Excellent communication, mentoring, and system design skills.
"""
    },
    {
        "id": "aiml_engineer",
        "title": "AI / Machine Learning Engineer (NLP & LLMs)",
        "company": "DeepCognition AI",
        "text": """Job Title: AI / Machine Learning Engineer
Company: DeepCognition AI
Location: San Francisco, CA / Remote

About The Role:
DeepCognition is looking for a passionate Machine Learning Engineer with 3+ years of experience to build next-generation Generative AI and NLP solutions. You will develop retrieval-augmented generation (RAG) pipelines, fine-tune open-weight models, and build high-performance vector search systems.

Key Responsibilities:
- Design, experiment, and deploy Machine Learning and NLP models using PyTorch, Hugging Face Transformers, and Scikit-Learn.
- Build production-ready RAG architectures with LangChain, LlamaIndex, and Vector Databases (Pinecone, Chroma, Qdrant).
- Deploy scalable model inference endpoints using Python, FastAPI, and Docker.
- Implement data processing pipelines using Pandas, NumPy, and Apache Spark.
- Conduct A/B testing and performance benchmarking on latency and accuracy metrics.

Requirements:
- 3+ years of hands-on Machine Learning, Deep Learning, or NLP experience.
- Proficiency in Python, PyTorch, Scikit-Learn, Pandas, and NumPy.
- Experience with LLM frameworks (LangChain, Hugging Face, Transformers) and RAG techniques.
- Familiarity with Vector Databases (Pinecone, Qdrant, Weaviate).
- Experience with containerization (Docker) and Cloud platforms (AWS or GCP).
- Master's or Bachelor's degree in Computer Science, Data Science, Mathematics, or related field.
"""
    },
    {
        "id": "devops_architect",
        "title": "Cloud DevOps & Platform Architect",
        "company": "Apex Infrastructure",
        "text": """Job Title: Cloud DevOps & Platform Architect
Company: Apex Infrastructure
Location: Remote

Overview:
Apex is looking for a Senior Cloud DevOps Specialist with 6+ years of experience in enterprise cloud migrations, Kubernetes cluster management, Infrastructure as Code (Terraform), and secure automated CI/CD workflows.

Key Responsibilities:
- Design multi-region cloud architectures on AWS and Azure using Terraform and Ansible.
- Manage enterprise Kubernetes clusters (EKS/AKS), service meshes (Istio), and Helm charts.
- Build automated, secure CI/CD pipelines with GitHub Actions, Jenkins, and Argo CD.
- Implement enterprise observability with Prometheus, Grafana, and Datadog.
- Drive security compliance, secrets management (HashiCorp Vault), and zero-trust networking.

Qualifications:
- 6+ years in DevOps, SRE, or Cloud Infrastructure engineering.
- Deep expertise with Kubernetes, Docker, Helm, and Linux administration.
- Advanced Infrastructure as Code (IaC) skills with Terraform.
- Strong scripting skills in Python, Bash, and Shell.
- In-depth knowledge of AWS and Azure cloud platforms.
- Proven experience with CI/CD automation and GitOps.
"""
    }
]

SAMPLE_RESUMES = [
    {
        "id": "alex_morgan",
        "name": "Alex Morgan",
        "target": "fullstack_sr",
        "title": "Senior Full-Stack Engineer",
        "text": """Alex Morgan
Email: alex.morgan.dev@email.com | Phone: (555) 382-9102
LinkedIn: linkedin.com/in/alexmorgan-dev | GitHub: github.com/alexm-code
Location: Austin, TX

PROFESSIONAL SUMMARY:
Senior Full-Stack Software Engineer with 6+ years of experience architecting and shipping mission-critical web applications. Expert in React, TypeScript, Python, FastAPI, and AWS. Proven track record reducing API latency by 45% and leading cross-functional teams to deliver enterprise SaaS platforms serving 500,000+ monthly active users.

TECHNICAL SKILLS:
- Languages: Python, TypeScript, JavaScript, SQL, HTML5, CSS3, Bash
- Frontend: React, Next.js, Redux Toolkit, Tailwind CSS, Material-UI, Vite
- Backend: FastAPI, Node.js, Express, Django, REST APIs, GraphQL, Microservices
- Databases: PostgreSQL, Redis, MongoDB, SQLAlchemy, Prisma
- Cloud & DevOps: AWS (EC2, S3, ECS, Lambda), Docker, Kubernetes, GitHub Actions, CI/CD, Terraform
- Testing & Quality: PyTest, Jest, Cypress, TDD, Agile, Scrum, Git

PROFESSIONAL EXPERIENCE:
Senior Software Engineer | FinTech Wave Corp | 2021 - Present
- Led end-to-end development of customer-facing dashboard using React, Next.js, TypeScript, and Tailwind CSS.
- Architected asynchronous RESTful microservices in Python using FastAPI and PostgreSQL, serving 12M daily requests.
- Integrated Redis caching layer, decreasing database query loads by 40% and response times from 350ms to 45ms.
- Containerized microservices using Docker and orchestrated deployments on AWS ECS with Terraform.
- Built automated CI/CD release pipelines with GitHub Actions, improving deployment frequency from weekly to daily.
- Mentored 4 junior developers and conducted weekly peer code reviews adhering to Clean Code standards.

Full-Stack Developer | Nexus Interactive | 2018 - 2021
- Developed interactive web portals with React, Node.js, and Express for Fortune 500 enterprise clients.
- Designed database schemas in PostgreSQL and optimized complex SQL queries for 30% faster analytics exports.
- Implemented unit and integration test suites using Jest and PyTest, achieving 88% overall test coverage.
- Participated in two-week Agile Scrum sprints, daily standups, and bi-weekly sprint planning sessions.

EDUCATION:
Bachelor of Science in Computer Science | University of Texas at Austin | Graduated 2018
"""
    },
    {
        "id": "elena_rostova",
        "name": "Elena Rostova",
        "target": "aiml_engineer",
        "title": "Machine Learning & NLP Specialist",
        "text": """Elena Rostova
Email: elena.rostova.ai@gmail.com | Phone: (415) 782-4411
LinkedIn: linkedin.com/in/elena-rostova | GitHub: github.com/erostova-ai
Location: San Francisco, CA

PROFESSIONAL SUMMARY:
Machine Learning Engineer with 4 years of experience specializing in Natural Language Processing (NLP), Deep Learning, and Generative AI. Skilled in PyTorch, Hugging Face Transformers, RAG architectures, and scalable model deployment with FastAPI and Docker.

TECHNICAL SKILLS:
- Core AI / ML: Machine Learning, Deep Learning, NLP, LLMs, Generative AI, PyTorch, TensorFlow, Scikit-Learn
- LLM & Vector Tools: Hugging Face, Transformers, LangChain, LlamaIndex, Pinecone, Chroma, Vector Databases
- Data Engineering: Python, Pandas, NumPy, Scipy, Apache Spark, SQL
- Engineering & Cloud: FastAPI, Docker, Git, AWS, REST APIs, Linux

WORK EXPERIENCE:
Machine Learning Engineer | Semantic AI Labs | 2022 - Present
- Built enterprise Retrieval-Augmented Generation (RAG) system with LangChain, PyTorch, and Pinecone vector database.
- Fine-tuned transformer models for multi-class legal document classification, boosting F1 score by 14% over baseline.
- Deployed low-latency model inference APIs using Python, FastAPI, and Docker on AWS cloud infrastructure.
- Designed automated data processing pipelines with Pandas, NumPy, and Scikit-Learn processing 200GB+ text daily.

Junior Data Scientist | DataCorp Solutions | 2020 - 2022
- Built predictive analytics models using Scikit-Learn and Pandas for customer churn prediction (ROC-AUC: 0.89).
- Conducted exploratory data analysis and feature engineering on structured tabular and unstructured text datasets.
- Created automated reporting scripts and collaborated with engineering teams to deploy models via REST APIs.

EDUCATION:
Master of Science in Data Science | Stanford University | 2020
Bachelor of Science in Mathematics | UC Berkeley | 2018
"""
    },
    {
        "id": "marcus_vance",
        "name": "Marcus Vance",
        "target": "fullstack_sr",
        "title": "Junior Web Developer (Gap Demo)",
        "text": """Marcus Vance
Email: marcus.vance@example.com | Phone: (555) 123-4567
LinkedIn: linkedin.com/in/marcusvance

PROFESSIONAL SUMMARY:
Junior Web Developer with 1.5 years of experience building simple client websites using HTML, CSS, JavaScript, and basic PHP. Seeking to transition into software engineering roles.

SKILLS:
HTML5, CSS3, JavaScript, jQuery, WordPress, PHP, Bootstrap, MySQL, Git

EXPERIENCE:
Junior Web Designer | Local Web Studio | 2023 - Present
- Created responsive websites for small businesses using HTML, CSS, and WordPress.
- Assisted with maintenance of MySQL databases and PHP scripts.
- Implemented responsive mobile layouts with Bootstrap.

EDUCATION:
Associate Degree in Web Design | Austin Community College | 2023
"""
    }
]
