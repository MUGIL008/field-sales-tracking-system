import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

function LogVisit() {
  const [outlets, setOutlets] = useState([]);
  const [selectedOutlet, setSelectedOutlet] = useState("");
  const [casesSold, setCasesSold] = useState("");
  const [notes, setNotes] = useState("");
  const [date, setDate] = useState(
    new Date().toISOString().split("T")[0]
  );

  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  useEffect(() => {
    if (!token) {
      navigate("/");
      return;
    }

    fetch("http://127.0.0.1:8000/outlets", {
      headers: {
        Authorization: "Bearer " + token
      }
    })
      .then((res) => res.json())
      .then((data) => setOutlets(data))
      .catch(() => alert("Error fetching outlets"));
  }, [navigate, token]);

  const handleSubmit = async () => {
    // Outlet validation
    if (!selectedOutlet) {
      alert("Please select an outlet");
      return;
    }

    // Cases Sold validation
    if (casesSold === "" || !/^\d+$/.test(casesSold)) {
      alert("Cases Sold must be 0 or a positive whole number");
      return;
    }

    // Date validation
    if (!date) {
      alert("Please select a date");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/visits", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + token
        },
        body: JSON.stringify({
          outlet_id: parseInt(selectedOutlet),
          cases_sold: parseInt(casesSold),
          notes: notes,
          date: date
        })
      });

      if (response.ok) {
        alert("Visit logged successfully!");
        navigate("/dashboard");
      } else {
        alert("Error logging visit");
      }
    } catch (error) {
      alert("Server error");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Log Visit</h2>

      <label>Select Outlet:</label><br />
      <select
        value={selectedOutlet}
        onChange={(e) => setSelectedOutlet(e.target.value)}
      >
        <option value="">-- Select Outlet --</option>
        {outlets.map((outlet) => (
          <option key={outlet.id} value={outlet.id}>
            {outlet.name}
          </option>
        ))}
      </select>
      <br /><br />

      <label>Cases Sold:</label><br />
      <input
        type="number"
        value={casesSold}
        min="0"
        step="1"
        onChange={(e) => {
          const value = e.target.value;

          // Allow only digits
          if (/^\d*$/.test(value)) {
            setCasesSold(value);
          }
        }}
      />
      <br /><br />

      <label>Date:</label><br />
      <input
        type="date"
        value={date}
        max={new Date().toISOString().split("T")[0]}
        onChange={(e) => setDate(e.target.value)}
      />
      <br /><br />

      <label>Notes:</label><br />
      <textarea
        value={notes}
        onChange={(e) => setNotes(e.target.value)}
      />
      <br /><br />

      <button onClick={handleSubmit}>Submit</button>
      <button
        onClick={() => navigate("/dashboard")}
        style={{ marginLeft: "10px" }}
      >
        Back
      </button>
    </div>
  );
}

export default LogVisit;