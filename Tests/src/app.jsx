import React, { useState } from "react";
import WeatherDisplay from "./components/WeatherDisplay";

const API_KEY = "YOUR_OPENWEATHERMAP_API_KEY";

export default function App() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);

  const fetchWeather = async (e) => {
    e.preventDefault();
    setWeather(null);
    try {
      const response = await fetch(
        `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(
          city
        )}&appid=${API_KEY}&units=metric`
      );
      if (!response.ok) {
        throw new Error("City not found");
      }
      const data = await response.json();
      setWeather(data);
    } catch (error) {
      setWeather({ error: error.message });
    }
  };

  return (
    <div>
      <h1>Weather Dashboard</h1>
      <form onSubmit={fetchWeather}>
        <input
          type="text"
          value={city}
          placeholder="Enter city"
          onChange={(e) => setCity(e.target.value)}
        />
        <button type="submit">Get Weather</button>
      </form>
      <WeatherDisplay weather={weather} />
    </div>
  );
}
