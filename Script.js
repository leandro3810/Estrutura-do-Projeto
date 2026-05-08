// Dictionary to translate Open-Meteo WMO Codes
const weatherCodes = {
    0: "Clear sky",
    1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Depositing rime fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow fall", 73: "Moderate snow fall", 75: "Heavy snow fall",
    95: "Thunderstorm"
};

async function getWeather() {
    const city = document.getElementById('cityInput').value;
    const resultDiv = document.getElementById('weatherResult');
    
    // Step 1: Geocoding (Convert City Name to Coordinates)
    try {
        const geoUrl = `https://geocoding-api.open-meteo.com/v1/search?name=${city}&count=1&language=en&format=json`;
        const geoRes = await fetch(geoUrl);
        const geoData = await geoRes.json();

        if (!geoData.results) {
            alert("City not found!");
            return;
        }

        const { latitude, longitude, name } = geoData.results[0];

        // Step 2: Fetch Weather Data
        const weatherUrl = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true&hourly=relativehumidity_2m`;
        const weatherRes = await fetch(weatherUrl);
        const weatherData = await weatherRes.json();

        // Update UI
        document.getElementById('cityName').innerText = name;
        document.getElementById('temperature').innerText = Math.round(weatherData.current_weather.temperature);
        document.getElementById('description').innerText = weatherCodes[weatherData.current_weather.weathercode] || "Cloudy";
        document.getElementById('windSpeed').innerText = `${weatherData.current_weather.windspeed} km/h`;
        
        // Open-Meteo returns humidity in the hourly array
        const humidity = weatherData.hourly.relativehumidity_2m[0];
        document.getElementById('humidity').innerText = `${humidity}%`;

    } catch (error) {
        console.error("Error fetching weather:", error);
        alert("Failed to fetch data.");
    }
}

// Initial call
getWeather();
