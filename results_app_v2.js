document.addEventListener('DOMContentLoaded', () => {
    // Add timestamp to bypass browser cache
    const timestamp = new Date().getTime();
    fetch(`database/last_analysis.json?t=${timestamp}`)
        .then(response => response.json())
        .then(data => renderReport(data))
        .catch(err => {
            console.warn("Using fallback mock data...", err);
            renderReport(mockFallback);
        });
});

const mockFallback = {
    account: "@greef_agency_demo",
    niche: "Marketing / Infoprodutos",
    score: 8.7,
    kpis: {
        reach: "42.500",
        eng: "4.2%",
        followers: "+124",
        readiness: "92%"
    },
    insights: {
        strong: "Seus Reels de 'Bastidores' têm uma taxa de retenção 40% superior à média do nicho.",
        bottleneck: "As artes dos posts estáticos estão com excesso de texto."
    },
    plan: [
        { task: "Exemplo de tarefa de fallback.", priority: "Média" }
    ]
};

function renderReport(data) {
    document.getElementById('account-name').textContent = data.account;
    document.getElementById('nicho-tag').textContent = data.niche;
    document.getElementById('health-score').textContent = data.score;

    document.getElementById('reach-val').textContent = data.kpis.reach;
    document.getElementById('eng-val').textContent = data.kpis.eng;
    document.getElementById('foll-val').textContent = data.kpis.followers;
    document.getElementById('sale-val').textContent = data.kpis.readiness;

    document.getElementById('strong-point').textContent = data.insights.strong;
    document.getElementById('bottleneck').textContent = data.insights.bottleneck;

    const actionList = document.getElementById('action-list');
    actionList.innerHTML = data.plan.map(item => `
        <div class="checklist-item">
            <div class="check-box"></div>
            <div style="flex: 1;">
                <p style="font-weight: 600;">${item.task}</p>
                <span style="font-size: 0.7rem; color: ${item.priority === 'Crítica' ? '#ff4444' : 'var(--text-dim)'}; text-transform: uppercase;">Prioridade: ${item.priority}</span>
            </div>
        </div>
    `).join('');
}
