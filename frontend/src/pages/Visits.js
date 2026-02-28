import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function Visits() {
  const [visits, setVisits] = useState([]);
  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  useEffect(() => {
    if (!token) {
      navigate("/");
      return;
    }

    fetch("http://127.0.0.1:8000/visits", {
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
        setVisits(data);
      })
      .catch((err) => {
        console.error(err);
        localStorage.removeItem("token");
        navigate("/");
      });
  }, [navigate, token]);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Visits List</h2>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Date</th>
            <th>Outlet</th>
            <th>Cases Sold</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody>
          {visits.map((visit, index) => (
            <tr key={index}>
              <td>{visit.date}</td>
              <td>{visit.outlet_name}</td>
              <td>{visit.cases_sold}</td>
              <td>{visit.notes}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <br />

      <button onClick={() => navigate("/dashboard")}>
        Back to Dashboard
      </button>
    </div>
  );
}

export default Visits;