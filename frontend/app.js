/**
 * MatchPulse: Intelligent Resume-Job Matching & ATS Optimizer
 * Client-side Controller & UI State Engine
 */

// Application State
const state = {
    currentTab: "studio",
    matchData: null,
    taxonomy: null,
    samples: null,
    stagedFiles: {
        resume: null,
        job: null,
        batch: []
    },
    activeSkillFilter: "all"
};

// DOM References
const elements = {
    // Nav
    navTabs: document.querySelectorAll(".nav-tab"),
    tabPanels: document.querySelectorAll(".tab-panel"),
    navScorePill: document.getElementById("navScorePill"),
    navAnalytics: document.getElementById("navAnalytics"),
    navOptimizer: document.getElementById("navOptimizer"),

    // Studio Inputs
    resumeModeUpload: document.getElementById("resumeModeUpload"),
    resumeModePaste: document.getElementById("resumeModePaste"),
    resumeDropzone: document.getElementById("resumeDropzone"),
    resumeFileInput: document.getElementById("resumeFileInput"),
    resumeFilePill: document.getElementById("resumeFilePill"),
    resumeFileName: document.getElementById("resumeFileName"),
    btnRemoveResumeFile: document.getElementById("btnRemoveResumeFile"),
    resumePasteZone: document.getElementById("resumePasteZone"),
    resumeTextArea: document.getElementById("resumeTextArea"),
    resumeCharCount: document.getElementById("resumeCharCount"),
    btnClearResumeText: document.getElementById("btnClearResumeText"),

    jobModeUpload: document.getElementById("jobModeUpload"),
    jobModePaste: document.getElementById("jobModePaste"),
    jobDropzone: document.getElementById("jobDropzone"),
    jobFileInput: document.getElementById("jobFileInput"),
    jobFilePill: document.getElementById("jobFilePill"),
    jobFileName: document.getElementById("jobFileName"),
    btnRemoveJobFile: document.getElementById("btnRemoveJobFile"),
    jobPasteZone: document.getElementById("jobPasteZone"),
    jobTextArea: document.getElementById("jobTextArea"),
    jobCharCount: document.getElementById("jobCharCount"),
    btnClearJobText: document.getElementById("btnClearJobText"),
    jobTitleInput: document.getElementById("jobTitleInput"),

    btnRunMatch: document.getElementById("btnRunMatch"),

    // Presets
    samplePresetsContainer: document.getElementById("samplePresetsContainer"),

    // Analytics Hero
    radialProgressBar: document.getElementById("radialProgressBar"),
    heroScoreDisplay: document.getElementById("heroScoreDisplay"),
    heroTierPill: document.getElementById("heroTierPill"),
    heroCandidateMeta: document.getElementById("heroCandidateMeta"),
    heroVerdictHeadline: document.getElementById("heroVerdictHeadline"),
    heroVerdictText: document.getElementById("heroVerdictText"),
    metaExpYears: document.getElementById("metaExpYears"),
    metaSeniority: document.getElementById("metaSeniority"),
    metaEducation: document.getElementById("metaEducation"),
    metaSkillsFound: document.getElementById("metaSkillsFound"),

    // Dimensions
    scoreSkills: document.getElementById("scoreSkills"),
    fillSkills: document.getElementById("fillSkills"),
    detailSkills: document.getElementById("detailSkills"),
    scoreSemantic: document.getElementById("scoreSemantic"),
    fillSemantic: document.getElementById("fillSemantic"),
    scoreExp: document.getElementById("scoreExp"),
    fillExp: document.getElementById("fillExp"),
    detailExp: document.getElementById("detailExp"),
    scoreSeniority: document.getElementById("scoreSeniority"),
    fillSeniority: document.getElementById("fillSeniority"),
    detailSeniority: document.getElementById("detailSeniority"),
    scoreEdu: document.getElementById("scoreEdu"),
    fillEdu: document.getElementById("fillEdu"),
    detailEdu: document.getElementById("detailEdu"),

    // Skills Matrix
    skillsBadgeWall: document.getElementById("skillsBadgeWall"),
    countSkillsAll: document.getElementById("countSkillsAll"),
    countSkillsMatched: document.getElementById("countSkillsMatched"),
    countSkillsMissing: document.getElementById("countSkillsMissing"),
    countSkillsBonus: document.getElementById("countSkillsBonus"),
    filterSkillsAll: document.getElementById("filterSkillsAll"),
    filterSkillsMatched: document.getElementById("filterSkillsMatched"),
    filterSkillsMissing: document.getElementById("filterSkillsMissing"),
    filterSkillsBonus: document.getElementById("filterSkillsBonus"),
    domainBarsContainer: document.getElementById("domainBarsContainer"),

    // Optimizer
    atsChecklistItems: document.getElementById("atsChecklistItems"),
    bulletSuggestionsList: document.getElementById("bulletSuggestionsList"),
    recommendationsContainer: document.getElementById("recommendationsContainer"),

    // Batch Tab
    batchJobTitle: document.getElementById("batchJobTitle"),
    batchJobText: document.getElementById("batchJobText"),
    batchDropzone: document.getElementById("batchDropzone"),
    batchFilesInput: document.getElementById("batchFilesInput"),
    batchFileSummary: document.getElementById("batchFileSummary"),
    batchFileCountLabel: document.getElementById("batchFileCountLabel"),
    btnClearBatchFiles: document.getElementById("btnClearBatchFiles"),
    btnLoadBatchDefaultJob: document.getElementById("btnLoadBatchDefaultJob"),
    btnLoadSampleCohort: document.getElementById("btnLoadSampleCohort"),
    btnRunBatch: document.getElementById("btnRunBatch"),
    batchLeaderboardSection: document.getElementById("batchLeaderboardSection"),
    leaderboardTbody: document.getElementById("leaderboardTbody"),
    btnExportCSV: document.getElementById("btnExportCSV"),

    // Modal
    modalTaxonomy: document.getElementById("modalTaxonomy"),
    btnExploreTaxonomy: document.getElementById("btnExploreTaxonomy"),
    btnCloseTaxonomy: document.getElementById("btnCloseTaxonomy"),
    taxonomyModalBody: document.getElementById("taxonomyModalBody"),
    taxonomySearchInput: document.getElementById("taxonomySearchInput"),

    // Toasts
    toastContainer: document.getElementById("toastContainer")
};

// ================= INITIALIZATION =================
document.addEventListener("DOMContentLoaded", async () => {
    initDragonEmbers();
    setupTabNavigation();
    setupFileInputs();
    setupTextAreas();
    setupBatchHandlers();
    setupTaxonomyModal();
    await fetchSamplesAndTaxonomy();
});

function initDragonEmbers() {
    const container = document.getElementById("dragonParticles");
    if (!container) return;
    for (let i = 0; i < 18; i++) {
        const ember = document.createElement("span");
        ember.className = "ember";
        const left = Math.floor(Math.random() * 100);
        const dur = (6 + Math.random() * 8).toFixed(1);
        const delay = (Math.random() * 6).toFixed(1);
        const drift = Math.floor(-50 + Math.random() * 100);
        const size = Math.floor(2 + Math.random() * 4);
        const maxOp = (0.5 + Math.random() * 0.45).toFixed(2);

        ember.style.left = `${left}%`;
        ember.style.width = `${size}px`;
        ember.style.height = `${size}px`;
        ember.style.setProperty("--dur", `${dur}s`);
        ember.style.setProperty("--delay", `${delay}s`);
        ember.style.setProperty("--drift", `${drift}px`);
        ember.style.setProperty("--max-op", maxOp);
        container.appendChild(ember);
    }
}

// Toast System
function showToast(message, type = "info") {
    const toast = document.createElement("div");
    toast.className = `toast toast-${type}`;
    const icon = type === "success" ? "✅" : type === "error" ? "❌" : "ℹ️";
    toast.innerHTML = `<span>${icon}</span><span>${message}</span>`;
    elements.toastContainer.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = "0";
        toast.style.transform = "translateY(10px)";
        setTimeout(() => toast.remove(), 300);
    }, 3500);
}

// ================= TAB NAVIGATION =================
function setupTabNavigation() {
    elements.navTabs.forEach(tab => {
        tab.addEventListener("click", () => {
            if (tab.disabled) return;
            const target = tab.dataset.tab;
            switchTab(target);
        });
    });
}

function switchTab(tabId) {
    state.currentTab = tabId;
    elements.navTabs.forEach(tab => {
        tab.classList.toggle("active", tab.dataset.tab === tabId);
    });
    elements.tabPanels.forEach(panel => {
        panel.classList.toggle("active", panel.id === `tab${capitalize(tabId)}`);
    });
    window.scrollTo({ top: 0, behavior: "smooth" });
}

function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

// ================= FETCH METADATA =================
async function fetchSamplesAndTaxonomy() {
    try {
        const [sampleRes, taxRes] = await Promise.all([
            fetch("/api/samples"),
            fetch("/api/skills-taxonomy")
        ]);
        state.samples = await sampleRes.json();
        state.taxonomy = await taxRes.json();
        setupSamplePresetClicks();
        renderTaxonomyModal();
    } catch (e) {
        console.error("Failed to fetch initial samples/taxonomy", e);
    }
}

// ================= INPUT MODES & FILE HANDLING =================
function setupFileInputs() {
    // Mode switches (Upload vs Paste)
    setupModeToggle(elements.resumeModeUpload, elements.resumeModePaste, elements.resumeDropzone, elements.resumePasteZone);
    setupModeToggle(elements.jobModeUpload, elements.jobModePaste, elements.jobDropzone, elements.jobPasteZone);

    // Dropzone Resume
    setupDropzone(
        elements.resumeDropzone,
        elements.resumeFileInput,
        elements.resumeFilePill,
        elements.resumeFileName,
        file => { state.stagedFiles.resume = file; }
    );

    elements.btnRemoveResumeFile.addEventListener("click", (e) => {
        e.stopPropagation();
        state.stagedFiles.resume = null;
        elements.resumeFileInput.value = "";
        elements.resumeFilePill.style.display = "none";
        elements.resumeDropzone.querySelector(".dropzone-content").style.display = "block";
    });

    // Dropzone Job
    setupDropzone(
        elements.jobDropzone,
        elements.jobFileInput,
        elements.jobFilePill,
        elements.jobFileName,
        file => { state.stagedFiles.job = file; }
    );

    elements.btnRemoveJobFile.addEventListener("click", (e) => {
        e.stopPropagation();
        state.stagedFiles.job = null;
        elements.jobFileInput.value = "";
        elements.jobFilePill.style.display = "none";
        elements.jobDropzone.querySelector(".dropzone-content").style.display = "block";
    });

    // Run Match Action
    elements.btnRunMatch.addEventListener("click", runMatchAnalysis);
}

function setupModeToggle(btnUpload, btnPaste, zoneUpload, zonePaste) {
    btnUpload.addEventListener("click", () => {
        btnUpload.classList.add("active");
        btnPaste.classList.remove("active");
        zoneUpload.style.display = "flex";
        zonePaste.style.display = "none";
    });

    btnPaste.addEventListener("click", () => {
        btnPaste.classList.add("active");
        btnUpload.classList.remove("active");
        zonePaste.style.display = "flex";
        zoneUpload.style.display = "none";
    });
}

function setupDropzone(dropzone, input, pill, nameLabel, onSelect) {
    dropzone.addEventListener("click", () => input.click());

    input.addEventListener("change", (e) => {
        if (e.target.files && e.target.files[0]) {
            handleFile(e.target.files[0]);
        }
    });

    ["dragenter", "dragover"].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropzone.classList.add("dragover");
        });
    });

    ["dragleave", "drop"].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropzone.classList.remove("dragover");
        });
    });

    dropzone.addEventListener("drop", (e) => {
        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
            handleFile(e.dataTransfer.files[0]);
        }
    });

    function handleFile(file) {
        onSelect(file);
        nameLabel.textContent = `${file.name} (${formatBytes(file.size)})`;
        dropzone.querySelector(".dropzone-content").style.display = "none";
        pill.style.display = "flex";
        showToast(`Loaded: ${file.name}`, "info");
    }
}

function setupTextAreas() {
    elements.resumeTextArea.addEventListener("input", () => {
        elements.resumeCharCount.textContent = `${elements.resumeTextArea.value.length.toLocaleString()} characters`;
    });
    elements.btnClearResumeText.addEventListener("click", () => {
        elements.resumeTextArea.value = "";
        elements.resumeCharCount.textContent = "0 characters";
    });

    elements.jobTextArea.addEventListener("input", () => {
        elements.jobCharCount.textContent = `${elements.jobTextArea.value.length.toLocaleString()} characters`;
    });
    elements.btnClearJobText.addEventListener("click", () => {
        elements.jobTextArea.value = "";
        elements.jobCharCount.textContent = "0 characters";
    });
}

function formatBytes(bytes) {
    if (bytes === 0) return "0 B";
    const k = 1024;
    const sizes = ["B", "KB", "MB"];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + " " + sizes[i];
}

// ================= PRESET SAMPLES =================
function setupSamplePresetClicks() {
    const chips = elements.samplePresetsContainer.querySelectorAll(".sample-chip");
    chips.forEach(chip => {
        chip.addEventListener("click", () => {
            const pairType = chip.dataset.samplePair;
            loadSamplePair(pairType);
        });
    });
}

function loadSamplePair(type) {
    if (!state.samples) return;

    let resume, job;

    if (type === "fullstack") {
        resume = state.samples.resumes[0]; // Alex Morgan
        job = state.samples.jobs[0];       // CloudScale Senior Full-Stack
    } else if (type === "aiml") {
        resume = state.samples.resumes[1]; // Elena Rostova
        job = state.samples.jobs[1];       // DeepCognition AI
    } else if (type === "gap") {
        resume = state.samples.resumes[2]; // Marcus Vance
        job = state.samples.jobs[0];       // Senior Full-Stack
    }

    if (!resume || !job) return;

    // Switch both cards to Paste mode so user can see full text
    elements.resumeModePaste.click();
    elements.jobModePaste.click();

    elements.resumeTextArea.value = resume.text;
    elements.resumeCharCount.textContent = `${resume.text.length.toLocaleString()} characters`;
    state.stagedFiles.resume = null;

    elements.jobTextArea.value = job.text;
    elements.jobCharCount.textContent = `${job.text.length.toLocaleString()} characters`;
    elements.jobTitleInput.value = job.title;
    state.stagedFiles.job = null;

    showToast(`Loaded Preset: ${resume.name} ➔ ${job.title}`, "success");

    // Automatically trigger match
    runMatchAnalysis();
}

// ================= MATCH ENGINE EXECUTION =================
async function runMatchAnalysis() {
    const formData = new FormData();

    // Resume
    if (state.stagedFiles.resume) {
        formData.append("resume_file", state.stagedFiles.resume);
    } else if (elements.resumeTextArea.value.trim()) {
        formData.append("resume_text", elements.resumeTextArea.value.trim());
    } else {
        showToast("Please provide a resume file or paste resume text.", "error");
        elements.resumeDropzone.scrollIntoView({ behavior: "smooth" });
        return;
    }

    // Job
    if (state.stagedFiles.job) {
        formData.append("job_file", state.stagedFiles.job);
    } else if (elements.jobTextArea.value.trim()) {
        formData.append("job_text", elements.jobTextArea.value.trim());
    } else {
        showToast("Please provide a job description file or paste job requirements.", "error");
        elements.jobDropzone.scrollIntoView({ behavior: "smooth" });
        return;
    }

    if (elements.jobTitleInput.value.trim()) {
        formData.append("job_title", elements.jobTitleInput.value.trim());
    }

    // Button animation
    elements.btnRunMatch.disabled = true;
    elements.btnRunMatch.querySelector("span").textContent = "Analyzing NLP & Vector Semantics...";

    try {
        const response = await fetch("/api/match", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.detail || "Analysis request failed.");
        }

        const data = await response.json();
        state.matchData = data;

        // Render analytics & optimizer
        renderAnalytics(data);
        renderOptimizer(data);

        // Enable tabs
        elements.navAnalytics.disabled = false;
        elements.navOptimizer.disabled = false;
        elements.navScorePill.style.display = "inline-block";
        elements.navScorePill.textContent = `${data.match.overall_score}%`;

        // Switch to Analytics Tab
        switchTab("analytics");
        showToast(`Match complete! Overall Score: ${data.match.overall_score}%`, "success");

    } catch (err) {
        console.error(err);
        showToast(err.message, "error");
    } finally {
        elements.btnRunMatch.disabled = false;
        elements.btnRunMatch.querySelector("span").textContent = "Run Intelligent Match Analysis";
    }
}

// ================= RENDER ANALYTICS =================
function renderAnalytics(data) {
    const match = data.match;
    const score = match.overall_score;

    // 1. Radial Score Animation
    animateScoreDisplay(score);

    // Tier Pill & Color
    elements.heroTierPill.textContent = `${match.badge_icon} ${match.tier}`;
    elements.heroTierPill.className = `tier-pill ${match.tier_class}`;

    // Meta Header
    const candidateName = match.candidate_summary.name || "Candidate";
    const jobTitle = data.job.title || "Target Role";
    elements.heroCandidateMeta.textContent = `${candidateName} vs. ${jobTitle}`;
    elements.heroVerdictHeadline.textContent = match.tier;
    elements.heroVerdictText.textContent = match.verdict;

    // Meta Stat Badges
    elements.metaExpYears.textContent = `${match.candidate_summary.experience_years} yrs`;
    elements.metaSeniority.textContent = match.candidate_summary.seniority || "--";
    elements.metaEducation.textContent = match.candidate_summary.education || "--";
    elements.metaSkillsFound.textContent = match.candidate_summary.total_skills_count || "0";

    // 2. 5-Dimensional Breakdown
    const cats = match.category_scores;

    elements.scoreSkills.textContent = `${cats.skills.score}%`;
    elements.fillSkills.style.width = `${cats.skills.score}%`;
    elements.detailSkills.textContent = `${match.skills_analysis.matched_count} matched of ${match.skills_analysis.total_required} required`;

    elements.scoreSemantic.textContent = `${cats.semantic.score}%`;
    elements.fillSemantic.style.width = `${cats.semantic.score}%`;

    elements.scoreExp.textContent = `${cats.experience.score}%`;
    elements.fillExp.style.width = `${cats.experience.score}%`;
    elements.detailExp.textContent = cats.experience.details;

    elements.scoreSeniority.textContent = `${cats.seniority.score}%`;
    elements.fillSeniority.style.width = `${cats.seniority.score}%`;
    elements.detailSeniority.textContent = cats.seniority.details;

    elements.scoreEdu.textContent = `${cats.education.score}%`;
    elements.fillEdu.style.width = `${cats.education.score}%`;
    elements.detailEdu.textContent = cats.education.details;

    // 3. Skills Matrix
    renderSkillsMatrix(match.skills_analysis);

    // 4. Domain fulfillment
    renderDomainBars(match.skills_analysis.domain_breakdown);
}

function animateScoreDisplay(targetScore) {
    // Radial SVG circumference: 2 * PI * 68 = 427.26
    const circumference = 427.26;
    const offset = circumference - (targetScore / 100) * circumference;

    // Set stroke color based on tactical crimson tier
    let strokeColor = "#f00010";
    if (targetScore >= 88) strokeColor = "#f00010";
    else if (targetScore >= 74) strokeColor = "#ff3344";
    else if (targetScore >= 55) strokeColor = "#f59e0b";
    else strokeColor = "#a00010";

    elements.radialProgressBar.style.stroke = strokeColor;
    elements.radialProgressBar.style.strokeDashoffset = offset;

    // Numerical counter
    let current = 0;
    const duration = 1200;
    const start = performance.now();

    function step(timestamp) {
        const progress = Math.min((timestamp - start) / duration, 1);
        const easeOut = 1 - Math.pow(1 - progress, 3);
        const val = (targetScore * easeOut).toFixed(1);
        elements.heroScoreDisplay.textContent = val;
        if (progress < 1) {
            requestAnimationFrame(step);
        } else {
            elements.heroScoreDisplay.textContent = targetScore.toFixed(1);
        }
    }
    requestAnimationFrame(step);
}

// ================= SKILLS MATRIX =================
function renderSkillsMatrix(skillsAnalysis) {
    const matched = skillsAnalysis.matched_skills || [];
    const missing = skillsAnalysis.missing_skills || [];
    const bonus = skillsAnalysis.bonus_skills || [];

    elements.countSkillsAll.textContent = matched.length + missing.length + bonus.length;
    elements.countSkillsMatched.textContent = matched.length;
    elements.countSkillsMissing.textContent = missing.length;
    elements.countSkillsBonus.textContent = bonus.length;

    setupSkillFilterPills();
    updateSkillBadgeWall();

    function updateSkillBadgeWall() {
        elements.skillsBadgeWall.innerHTML = "";
        let list = [];

        if (state.activeSkillFilter === "all") {
            list = [
                ...matched.map(s => ({ ...s, tagType: "matched", icon: "✓" })),
                ...missing.map(s => ({ ...s, tagType: "missing", icon: "!" })),
                ...bonus.map(s => ({ ...s, tagType: "bonus", icon: "★" }))
            ];
        } else if (state.activeSkillFilter === "matched") {
            list = matched.map(s => ({ ...s, tagType: "matched", icon: "✓" }));
        } else if (state.activeSkillFilter === "missing") {
            list = missing.map(s => ({ ...s, tagType: "missing", icon: "!" }));
        } else if (state.activeSkillFilter === "bonus") {
            list = bonus.map(s => ({ ...s, tagType: "bonus", icon: "★" }));
        }

        if (list.length === 0) {
            elements.skillsBadgeWall.innerHTML = `<p class="dim-detail" style="padding: 1rem 0;">No skills found under this filter.</p>`;
            return;
        }

        list.forEach(skill => {
            const tag = document.createElement("div");
            tag.className = `skill-tag skill-tag-${skill.tagType}`;
            tag.innerHTML = `
                <span>${skill.icon}</span>
                <span>${skill.name}</span>
                <span class="skill-cat-label">${skill.category || "Skill"}</span>
            `;
            elements.skillsBadgeWall.appendChild(tag);
        });
    }

    function setupSkillFilterPills() {
        const filterBtns = [
            elements.filterSkillsAll,
            elements.filterSkillsMatched,
            elements.filterSkillsMissing,
            elements.filterSkillsBonus
        ];

        filterBtns.forEach(btn => {
            btn.onclick = () => {
                filterBtns.forEach(b => b.classList.remove("active"));
                btn.classList.add("active");
                state.activeSkillFilter = btn.dataset.filter;
                updateSkillBadgeWall();
            };
        });
    }
}

function renderDomainBars(domains) {
    elements.domainBarsContainer.innerHTML = "";
    if (!domains || domains.length === 0) {
        elements.domainBarsContainer.innerHTML = "<p class='dim-detail'>No technical domains identified.</p>";
        return;
    }

    domains.forEach(d => {
        const item = document.createElement("div");
        item.className = "domain-bar-item";
        item.innerHTML = `
            <div class="domain-bar-top">
                <span class="domain-bar-name">${d.domain}</span>
                <span class="domain-bar-pct">${d.matched}/${d.required} (${d.match_percentage}%)</span>
            </div>
            <div class="domain-track">
                <div class="domain-fill" style="width: ${d.match_percentage}%;"></div>
            </div>
        `;
        elements.domainBarsContainer.appendChild(item);
    });
}

// ================= ATS OPTIMIZER =================
function renderOptimizer(data) {
    const resume = data.resume;
    const match = data.match;

    // 1. Checklist
    elements.atsChecklistItems.innerHTML = "";
    const checks = [
        {
            title: "Standard Section Headers",
            status: resume.sections && resume.sections.experience && resume.sections.skills ? "pass" : "warn",
            desc: "Parsers look for standard headings: Summary, Skills, Experience, Education."
        },
        {
            title: "Optimal Resume Length",
            status: (resume.raw_text && resume.raw_text.split(" ").length >= 350) ? "pass" : "warn",
            desc: "Resume contains healthy density of technical accomplishments."
        },
        {
            title: "Direct Contact Information",
            status: resume.contact && resume.contact.email ? "pass" : "warn",
            desc: resume.contact && resume.contact.email ? `Found: ${resume.contact.email}` : "Missing email address."
        },
        {
            title: "Technical Skills Section",
            status: resume.skills && resume.skills.length >= 8 ? "pass" : "warn",
            desc: `${resume.skills ? resume.skills.length : 0} technical skills detected.`
        }
    ];

    checks.forEach(c => {
        const item = document.createElement("div");
        item.className = "check-item";
        const isPass = c.status === "pass";
        item.innerHTML = `
            <div class="check-icon-circle ${isPass ? 'check-pass' : 'check-warn'}">
                ${isPass ? '✓' : '!'}
            </div>
            <div class="check-item-content">
                <h5>${c.title}</h5>
                <p>${c.desc}</p>
            </div>
        `;
        elements.atsChecklistItems.appendChild(item);
    });

    // 2. Tailored Bullets
    elements.bulletSuggestionsList.innerHTML = "";
    const recs = match.recommendations || [];
    const bulletRec = recs.find(r => r.type === "tailored_bullets");

    if (bulletRec && bulletRec.bullets && bulletRec.bullets.length > 0) {
        bulletRec.bullets.forEach(b => {
            const card = document.createElement("div");
            card.className = "bullet-item-card";
            card.innerHTML = `
                <span class="bullet-target-skill">Targeting: ${b.skill}</span>
                <p class="bullet-text">"${b.suggested_bullet}"</p>
                <button class="bullet-copy-btn">
                    <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    <span>Copy Bullet</span>
                </button>
            `;
            const copyBtn = card.querySelector(".bullet-copy-btn");
            copyBtn.onclick = () => {
                navigator.clipboard.writeText(b.suggested_bullet);
                copyBtn.innerHTML = `<span>✓ Copied!</span>`;
                showToast(`Copied bullet for ${b.skill}!`, "success");
                setTimeout(() => {
                    copyBtn.innerHTML = `<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg><span>Copy Bullet</span>`;
                }, 2000);
            };
            elements.bulletSuggestionsList.appendChild(card);
        });
    } else {
        elements.bulletSuggestionsList.innerHTML = `
            <p class="dim-detail">No missing critical skills! Candidate covers all primary requirements.</p>
        `;
    }

    // 3. Actionable Recommendations Stream
    elements.recommendationsContainer.innerHTML = "";
    recs.forEach(r => {
        if (r.type === "tailored_bullets") return; // Handled above
        const card = document.createElement("div");
        card.className = "rec-card";
        const impactClass = r.impact === "High" ? "impact-high" : r.impact === "Medium" ? "impact-medium" : "impact-low";
        card.innerHTML = `
            <span class="rec-impact-badge ${impactClass}">${r.impact} Impact</span>
            <div class="rec-body">
                <h4>${r.title}</h4>
                <p>${r.description}</p>
                ${r.action ? `<span class="rec-action-callout">Recommended Step: ${r.action}</span>` : ''}
            </div>
        `;
        elements.recommendationsContainer.appendChild(card);
    });
}

// ================= BATCH APPLICANT RANKER =================
function setupBatchHandlers() {
    // Dropzone for multiple resumes
    elements.batchDropzone.addEventListener("click", () => elements.batchFilesInput.click());

    elements.batchFilesInput.addEventListener("change", (e) => {
        if (e.target.files) {
            state.stagedFiles.batch = Array.from(e.target.files);
            updateBatchSummary();
        }
    });

    elements.btnClearBatchFiles.addEventListener("click", () => {
        state.stagedFiles.batch = [];
        elements.batchFilesInput.value = "";
        updateBatchSummary();
    });

    // Load default CloudScale job
    elements.btnLoadBatchDefaultJob.addEventListener("click", () => {
        if (state.samples && state.samples.jobs[0]) {
            elements.batchJobTitle.value = state.samples.jobs[0].title;
            elements.batchJobText.value = state.samples.jobs[0].text;
            showToast("Loaded CloudScale Job for Batch Ranking", "info");
        }
    });

    // Load sample cohort (3 resumes)
    elements.btnLoadSampleCohort.addEventListener("click", () => {
        if (state.samples && state.samples.resumes) {
            // Create synthetic File objects from sample resumes
            const files = state.samples.resumes.map(r => {
                const blob = new Blob([r.text], { type: "text/plain" });
                return new File([blob], `${r.name.replace(/\s+/g, "_")}_resume.txt`, { type: "text/plain" });
            });
            state.stagedFiles.batch = files;
            updateBatchSummary();
            showToast("Staged 3 Sample Resumes (Alex, Elena, Marcus)", "success");
        }
    });

    // Run Batch
    elements.btnRunBatch.addEventListener("click", runBatchRanking);

    // Export CSV
    elements.btnExportCSV.addEventListener("click", exportLeaderboardCSV);
}

function updateBatchSummary() {
    const count = state.stagedFiles.batch.length;
    if (count > 0) {
        elements.batchFileSummary.style.display = "flex";
        elements.batchFileCountLabel.textContent = `${count} resume file(s) staged ready for analysis`;
    } else {
        elements.batchFileSummary.style.display = "none";
    }
}

async function runBatchRanking() {
    const jobText = elements.batchJobText.value.trim();
    if (!jobText) {
        showToast("Please provide or load a target Job Description for batch matching.", "error");
        elements.batchJobText.focus();
        return;
    }

    if (state.stagedFiles.batch.length === 0) {
        showToast("Please upload at least 2 resumes or click 'Load 3 Sample Resumes'.", "error");
        return;
    }

    const formData = new FormData();
    formData.append("job_text", jobText);
    formData.append("job_title", elements.batchJobTitle.value.trim() || "Target Role");

    state.stagedFiles.batch.forEach(file => {
        formData.append("resume_files", file);
    });

    elements.btnRunBatch.disabled = true;
    elements.btnRunBatch.querySelector("span").textContent = `Analyzing & Ranking ${state.stagedFiles.batch.length} Applicants...`;

    try {
        const response = await fetch("/api/batch-match", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.detail || "Batch ranking request failed.");
        }

        const data = await response.json();
        renderLeaderboard(data.leaderboard);
        elements.batchLeaderboardSection.style.display = "block";
        elements.batchLeaderboardSection.scrollIntoView({ behavior: "smooth" });
        showToast(`Successfully ranked ${data.leaderboard.length} candidates!`, "success");

    } catch (err) {
        console.error(err);
        showToast(err.message, "error");
    } finally {
        elements.btnRunBatch.disabled = false;
        elements.btnRunBatch.querySelector("span").textContent = "Analyze & Rank Candidate Cohort";
    }
}

function renderLeaderboard(candidates) {
    elements.leaderboardTbody.innerHTML = "";

    candidates.forEach((c, idx) => {
        const rank = idx + 1;
        const rankClass = rank === 1 ? "rank-1" : rank === 2 ? "rank-2" : rank === 3 ? "rank-3" : "";
        const tr = document.createElement("tr");

        tr.innerHTML = `
            <td>
                <div class="rank-badge ${rankClass}">${rank}</div>
            </td>
            <td>
                <div class="candidate-cell-name">${c.candidate_name || "Applicant"}</div>
                <div class="candidate-cell-file">${c.filename}</div>
            </td>
            <td>
                <span class="score-badge">${c.overall_score}%</span>
            </td>
            <td>
                <span class="tier-pill ${c.tier_class}" style="font-size: 0.76rem; padding: 0.25rem 0.65rem;">
                    ${c.badge_icon} ${c.tier}
                </span>
            </td>
            <td>
                <span>${c.experience_years} yrs</span>
            </td>
            <td>
                <span style="color: var(--emerald); font-weight: 600;">${c.matched_skills_count} skills</span>
            </td>
            <td>
                <span style="color: var(--amber); font-size: 0.8rem;">
                    ${c.missing_skills && c.missing_skills.length > 0 ? c.missing_skills.join(", ") : "None"}
                </span>
            </td>
        `;

        elements.leaderboardTbody.appendChild(tr);
    });
}

function exportLeaderboardCSV() {
    const rows = elements.leaderboardTbody.querySelectorAll("tr");
    if (rows.length === 0) return;

    let csv = "Rank,Candidate Name,File,Score,Tier,Experience Years,Matched Skills Count\n";

    rows.forEach(row => {
        const cols = row.querySelectorAll("td");
        const rank = cols[0].innerText.trim();
        const name = cols[1].querySelector(".candidate-cell-name").innerText.trim();
        const file = cols[1].querySelector(".candidate-cell-file").innerText.trim();
        const score = cols[2].innerText.trim();
        const tier = cols[3].innerText.trim().replace(/,/g, " ");
        const exp = cols[4].innerText.trim();
        const skills = cols[5].innerText.trim();

        csv += `"${rank}","${name}","${file}","${score}","${tier}","${exp}","${skills}"\n`;
    });

    const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `matchpulse_leaderboard_${new Date().toISOString().slice(0, 10)}.csv`;
    a.click();
    URL.revokeObjectURL(url);
    showToast("Downloaded leaderboard CSV!", "success");
}

// ================= MODAL: TAXONOMY EXPLORER =================
function setupTaxonomyModal() {
    elements.btnExploreTaxonomy.addEventListener("click", () => {
        elements.modalTaxonomy.style.display = "flex";
    });

    elements.btnCloseTaxonomy.addEventListener("click", () => {
        elements.modalTaxonomy.style.display = "none";
    });

    elements.modalTaxonomy.addEventListener("click", (e) => {
        if (e.target === elements.modalTaxonomy) {
            elements.modalTaxonomy.style.display = "none";
        }
    });

    elements.taxonomySearchInput.addEventListener("input", (e) => {
        filterTaxonomy(e.target.value.toLowerCase().trim());
    });
}

function renderTaxonomyModal() {
    if (!state.taxonomy) return;
    elements.taxonomyModalBody.innerHTML = "";

    for (const [category, skills] of Object.entries(state.taxonomy)) {
        const block = document.createElement("div");
        block.className = "tax-category-block";
        block.dataset.category = category.toLowerCase();

        block.innerHTML = `
            <h4>${category} (${skills.length})</h4>
            <div class="tax-skills-grid">
                ${skills.map(s => `<span class="tax-skill-pill">${s}</span>`).join("")}
            </div>
        `;
        elements.taxonomyModalBody.appendChild(block);
    }
}

function filterTaxonomy(query) {
    const blocks = elements.taxonomyModalBody.querySelectorAll(".tax-category-block");
    blocks.forEach(block => {
        const pills = block.querySelectorAll(".tax-skill-pill");
        let hasMatch = false;

        pills.forEach(pill => {
            const match = pill.textContent.toLowerCase().includes(query);
            pill.style.display = match ? "inline-block" : "none";
            if (match) hasMatch = true;
        });

        block.style.display = (hasMatch || query === "") ? "block" : "none";
    });
}
