"""
Comprehensive Skills and Domain Taxonomy for the Resume-Job Matching System.
Contains categorized technical and soft skills, synonyms/aliases, and normalization logic.
"""

# Categorized Skill Taxonomy
SKILL_TAXONOMY = {
    "Programming Languages": [
        "python", "javascript", "typescript", "java", "c++", "c#", "c", "go", "golang",
        "rust", "ruby", "php", "swift", "kotlin", "scala", "r", "dart", "shell", "bash",
        "powershell", "perl", "haskell", "elixir", "lua", "matlab", "sql", "html", "html5",
        "css", "css3", "sass", "scss", "less"
    ],
    "Frontend Frameworks & Libraries": [
        "react", "react.js", "reactjs", "vue", "vue.js", "vuejs", "angular", "angularjs",
        "next.js", "nextjs", "nuxt.js", "nuxtjs", "svelte", "sveltekit", "remix", "gatsby",
        "redux", "redux toolkit", "zustand", "mobx", "tailwind", "tailwindcss", "bootstrap",
        "material-ui", "mui", "chakra ui", "ant design", "shadcn", "jquery", "webpack",
        "vite", "turbopack", "babel", "rxjs", "three.js", "d3.js", "webgl"
    ],
    "Backend & APIs": [
        "node.js", "nodejs", "express", "express.js", "fastapi", "flask", "django",
        "spring", "spring boot", "asp.net", "asp.net core", ".net", ".net core",
        "ruby on rails", "rails", "laravel", "symfony", "nest.js", "nestjs", "koa",
        "graphql", "rest", "restful api", "rest api", "grpc", "soap", "websocket",
        "microservices", "serverless", "celery", "event-driven architecture"
    ],
    "Databases & Storage": [
        "postgresql", "postgres", "mysql", "mariadb", "sqlite", "mongodb", "redis",
        "cassandra", "dynamodb", "elasticsearch", "opensearch", "couchbase", "neo4j",
        "firebase", "supabase", "clickhouse", "snowflake", "bigquery", "redshift",
        "oracle", "microsoft sql server", "mssql", "prisma", "sqlalchemy", "hibernate",
        "mongoose", "typeorm"
    ],
    "Cloud & DevOps": [
        "aws", "amazon web services", "azure", "microsoft azure", "gcp", "google cloud",
        "docker", "kubernetes", "k8s", "terraform", "ansible", "jenkins", "gitlab ci",
        "github actions", "circleci", "helm", "prometheus", "grafana", "datadog",
        "linux", "nginx", "apache", "ci/cd", "continuous integration", "continuous deployment",
        "cloudformation", "pulumi", "vagrant", "argo cd", "istio", "vault"
    ],
    "AI, Machine Learning & Data": [
        "machine learning", "deep learning", "nlp", "natural language processing",
        "computer vision", "artificial intelligence", "ai", "llm", "large language models",
        "generative ai", "genai", "pytorch", "tensorflow", "keras", "scikit-learn",
        "pandas", "numpy", "scipy", "hugging face", "transformers", "langchain",
        "llamaindex", "rag", "vector database", "pinecone", "chroma", "weaviate", "qdrant",
        "opencv", "data analysis", "data science", "data engineering", "apache spark",
        "pyspark", "hadoop", "kafka", "airflow", "dbt", "tableau", "power bi"
    ],
    "Architecture, Testing & Quality": [
        "system design", "software architecture", "clean architecture", "design patterns",
        "unit testing", "integration testing", "e2e testing", "jest", "pytest", "cypress",
        "playwright", "selenium", "mocha", "chai", "tdd", "test-driven development",
        "bdd", "load testing", "postman", "swagger", "openapi"
    ],
    "Methodologies & Soft Skills": [
        "agile", "scrum", "kanban", "sprint planning", "jira", "confluence", "git",
        "github", "gitlab", "bitbucket", "code review", "mentoring", "leadership",
        "team management", "cross-functional collaboration", "problem solving",
        "critical thinking", "communication", "stakeholder management", "time management"
    ]
}

# Skill Synonyms / Aliases to canonical skill name
SKILL_ALIASES = {
    "reactjs": "React",
    "react.js": "React",
    "react": "React",
    "vuejs": "Vue.js",
    "vue.js": "Vue.js",
    "vue": "Vue.js",
    "angularjs": "Angular",
    "angular": "Angular",
    "nextjs": "Next.js",
    "next.js": "Next.js",
    "nuxtjs": "Nuxt.js",
    "nuxt.js": "Nuxt.js",
    "nodejs": "Node.js",
    "node.js": "Node.js",
    "node": "Node.js",
    "expressjs": "Express",
    "express.js": "Express",
    "express": "Express",
    "fastapi": "FastAPI",
    "flask": "Flask",
    "django": "Django",
    "spring boot": "Spring Boot",
    "springboot": "Spring Boot",
    "spring": "Spring Boot",
    "golang": "Go",
    "go": "Go",
    "k8s": "Kubernetes",
    "kubernetes": "Kubernetes",
    "docker": "Docker",
    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",
    "mongo": "MongoDB",
    "mongodb": "MongoDB",
    "amazon web services": "AWS",
    "aws": "AWS",
    "google cloud platform": "GCP",
    "google cloud": "GCP",
    "gcp": "GCP",
    "azure": "Azure",
    "microsoft azure": "Azure",
    "tailwind": "Tailwind CSS",
    "tailwindcss": "Tailwind CSS",
    "typescript": "TypeScript",
    "ts": "TypeScript",
    "javascript": "JavaScript",
    "js": "JavaScript",
    "python": "Python",
    "py": "Python",
    "ci/cd": "CI/CD",
    "continuous integration": "CI/CD",
    "continuous deployment": "CI/CD",
    "restful api": "REST APIs",
    "rest api": "REST APIs",
    "rest": "REST APIs",
    "graphql": "GraphQL",
    "grpc": "gRPC",
    "tensorflow": "TensorFlow",
    "pytorch": "PyTorch",
    "scikit-learn": "Scikit-Learn",
    "sklearn": "Scikit-Learn",
    "natural language processing": "NLP",
    "nlp": "NLP",
    "large language models": "LLMs",
    "llm": "LLMs",
    "llms": "LLMs",
    "genai": "Generative AI",
    "generative ai": "Generative AI",
    "microservices": "Microservices",
    "kafka": "Apache Kafka",
    "apache kafka": "Apache Kafka",
    "redis": "Redis",
    "elasticsearch": "Elasticsearch",
    "terraform": "Terraform",
    "git": "Git",
    "github": "GitHub",
    "gitlab": "GitLab",
    "jira": "Jira",
    "agile": "Agile",
    "scrum": "Scrum",
    "system design": "System Design",
    "pytest": "PyTest",
    "jest": "Jest",
    "cypress": "Cypress",
    "playwright": "Playwright"
}

# Seniority Levels with relative rank weights
SENIORITY_RANKS = {
    "intern": 1,
    "junior": 2,
    "associate": 2,
    "mid": 3,
    "intermediate": 3,
    "senior": 4,
    "lead": 5,
    "staff": 6,
    "principal": 7,
    "architect": 7,
    "director": 8,
    "head": 8,
    "vp": 9
}

# Education Levels with relative rank weights
EDUCATION_LEVELS = {
    "phd": 5,
    "doctorate": 5,
    "master": 4,
    "masters": 4,
    "msc": 4,
    "ms": 4,
    "mba": 4,
    "bachelor": 3,
    "bachelors": 3,
    "bsc": 3,
    "bs": 3,
    "btech": 3,
    "b.tech": 3,
    "b.e": 3,
    "associate": 2,
    "diploma": 2,
    "bootcamp": 2,
    "high school": 1
}

# Flattened list of all lookup terms sorted by length descending for greedy matching
ALL_SKILL_LOOKUPS = []
for category, skills in SKILL_TAXONOMY.items():
    for skill in skills:
        ALL_SKILL_LOOKUPS.append((skill.lower(), category))
for alias in SKILL_ALIASES.keys():
    ALL_SKILL_LOOKUPS.append((alias.lower(), "Synonym"))

# Sort by length descending to match multi-word skills like "spring boot" before "spring"
ALL_SKILL_LOOKUPS = sorted(list({term: cat for term, cat in ALL_SKILL_LOOKUPS}.items()), key=lambda x: len(x[0]), reverse=True)


def canonicalize_skill(skill: str) -> str:
    """Return the display-ready canonical name of a skill."""
    s_lower = skill.strip().lower()
    if s_lower in SKILL_ALIASES:
        return SKILL_ALIASES[s_lower]
    # Check if capitalized nicely in taxonomy
    for cat, skills in SKILL_TAXONOMY.items():
        for item in skills:
            if item.lower() == s_lower:
                return item.title() if len(item) > 3 else item.upper()
    return skill.title()


def get_skill_category(canonical_name: str) -> str:
    """Get the domain category for a canonical skill."""
    name_lower = canonical_name.lower()
    for cat, skills in SKILL_TAXONOMY.items():
        for s in skills:
            if s.lower() == name_lower or canonicalize_skill(s).lower() == name_lower:
                return cat
    return "Other Technical Skills"
