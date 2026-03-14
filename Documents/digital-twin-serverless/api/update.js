export default async function handler(req, res) {
  const fetch = (await import("node-fetch")).default;

  // Firebase Realtime Database URL
  const firebaseUrl = "https://digital-twin-demo-new-default-rtdb.firebaseio.com/sensor.json";

  // Simulated sensor data (replace with real sensor input or API)
  const sensorData = {
    temperature: Math.floor(Math.random() * 40),
    humidity: Math.floor(Math.random() * 100)
  };

  try {
    await fetch(firebaseUrl, {
      method: "PUT",
      body: JSON.stringify(sensorData),
      headers: { "Content-Type": "application/json" }
    });
    res.status(200).json({ message: "Sensor data pushed", data: sensorData });
  } catch (err) {
    res.status(500).json({ error: err.toString() });
  }
}
