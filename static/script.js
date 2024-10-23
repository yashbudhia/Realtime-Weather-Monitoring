async function loadWeatherData() {
    const response = await fetch('/api/summaries');
    const data = await response.json();

    const weatherSummaryDiv = document.getElementById('weather-summary');
    if (data && data.length > 0) {
        const summaries = data.map(item => `
            <div>
                <h3>${item.city}</h3>
                <p>Temperature: ${item.temperature}°C</p>
                <p>Condition: ${item.condition}</p>
            </div>
        `).join('');
        weatherSummaryDiv.innerHTML = summaries;
    } else {
        weatherSummaryDiv.innerHTML = '<p>No weather data available.</p>';
    }
}

loadWeatherData();
