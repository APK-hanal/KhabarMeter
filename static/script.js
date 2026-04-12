async function loadAndRender(url, chartId, containerId, statsPrefix) {
    const response = await fetch(url);
    const data = await response.json();

    let positive = 0, negative = 0, neutral = 0;
    for (let article of data) {
        const s = article.sentiment.toLowerCase();
        if (s === "positive") positive++;
        else if (s === "negative") negative++;
        else neutral++;
    }

    document.getElementById(statsPrefix + '-positive').textContent = positive;
    document.getElementById(statsPrefix + '-negative').textContent = negative;
    document.getElementById(statsPrefix + '-neutral').textContent = neutral;

    new Chart(document.getElementById(chartId), {
        type: "doughnut",
        data: {
            labels: ["Positive", "Negative", "Neutral"],
            datasets: [{
                data: [positive, negative, neutral],
                backgroundColor: ["#4e9e6e", "#b85450", "#5a6e8a"],
                borderColor: "#161616",
                borderWidth: 3
            }]
        },
        options: {
            responsive: true,
            cutout: '70%',
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: '#666',
                        font: { family: 'Inter', size: 11 },
                        padding: 16,
                        boxWidth: 10,
                        boxHeight: 10
                    }
                }
            }
        }
    });

    const container = document.getElementById(containerId);
    for (let article of data) {
        const sentiment = article.sentiment.toLowerCase();
        container.innerHTML += `
            <div class="article ${sentiment}">
                <a href="${article.link}" target="_blank">${article.header}</a>
                <div class="article-meta">
                    <span class="sentiment-badge ${sentiment}">${article.sentiment}</span>
                    <span class="confidence">${article.score}% confidence</span>
                </div>
            </div>
        `;
    }
}

loadAndRender('/results/economy', 'eco-chart', 'eco-articles', 'eco');
loadAndRender('/results/politics', 'pol-chart', 'pol-articles', 'pol');