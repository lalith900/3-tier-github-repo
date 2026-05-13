import React, { useEffect, useState } from "react";

function App() {

  const [backendMessage, setBackendMessage] = useState("");
  const [healthStatus, setHealthStatus] = useState("");
  const [dbStatus, setDbStatus] = useState("");
  const [redisStatus, setRedisStatus] = useState("");

  useEffect(() => {

    fetch("/api/")
      .then((response) => response.json())
      .then((data) => {
        setBackendMessage(data.message);
      });

    fetch("/api/health")
      .then((response) => response.json())
      .then((data) => {
        setHealthStatus(data.status);
      });

    fetch("/api/db-check")
      .then((response) => response.json())
      .then((data) => {
        setDbStatus(data.database);
      });

    fetch("/api/redis-check")
      .then((response) => response.json())
      .then((data) => {
        setRedisStatus(data.redis);
      });

  }, []);

  return (
    <div style={{ padding: "30px" }}>
      <h1>Three Tier Application</h1>

      <h2>Backend Status</h2>
      <p>{backendMessage}</p>

      <h2>Health Status</h2>
      <p>{healthStatus}</p>

      <h2>Database Status</h2>
      <p>{dbStatus}</p>

      <h2>Redis Status</h2>
      <p>{redisStatus}</p>
    </div>
  );
}

export default App;
