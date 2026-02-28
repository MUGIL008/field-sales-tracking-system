import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function Dashboard() {
  const [totalVisits, setTotalVisits] = useState(0);
  const [totalCases, setTotalCases] = useState(0);
  const [topOutlets, setTopOutlets] = useState([]);

  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  useEffect(() => {
    if (!token) {
      navigate("/");
      return;
    }

    fetch("http://127.0.0.1:8000/dashboard", {
      headers: {
        Authorization: "Bearer " + token
      }
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Unauthorized");
        }
        return res.json();
      })
      .then((data) => {
        setTotalVisits(data.total_visits);
        setTotalCases(data.total_cases_sold);
        setTopOutlets(data.top_3_outlets);
      })
      .catch((err) => {
        console.error(err);
        localStorage.removeItem("token");
        navigate("/");
      });
  }, [navigate, token]);

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Dashboard</h2>

      <button onClick={logout}>Logout</button>

      <hr />

      <h3>Total Visits</h3>
      <p>{totalVisits}</p>

      <h3>Total Cases Sold</h3>
      <p>{totalCases}</p>

      <h3>Top 3 Outlets</h3>
      <ul>
        {topOutlets.map((outlet, index) => (
          <li key={index}>
            {outlet.outlet_name} - {outlet.total_cases}
          </li>
        ))}
      </ul>

      <hr />

      <button onClick={() => navigate("/log-visit")}>Log Visit</button>
      <button onClick={() => navigate("/visits")} style={{ marginLeft: "10px" }}>
        View Visits
      </button>
    </div>
  );
}

export default Dashboard;