import React, { useEffect, useState } from "react";

const timeZones = [
  { label: "UTC", zone: "UTC" },
  { label: "New York", zone: "America/New_York" },
  { label: "London", zone: "Europe/London" },
  { label: "Tokyo", zone: "Asia/Tokyo" },
  { label: "São Paulo", zone: "America/Sao_Paulo" },
];

function getTimeInZone(zone) {
  return new Date().toLocaleTimeString("en-US", {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: false,
    timeZone: zone,
  });
}

export default function DigitalClock() {
  const [times, setTimes] = useState(
    timeZones.map((tz) => ({ ...tz, time: getTimeInZone(tz.zone) }))
  );

  useEffect(() => {
    const interval = setInterval(() => {
      setTimes(timeZones.map((tz) => ({ ...tz, time: getTimeInZone(tz.zone) })));
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h2>Digital Clock - Multi Time Zones</h2>
      <table>
        <thead>
          <tr>
            <th>Location</th>
            <th>Current Time</th>
          </tr>
        </thead>
        <tbody>
          {times.map((tz) => (
            <tr key={tz.zone}>
              <td>{tz.label}</td>
              <td>{tz.time}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
