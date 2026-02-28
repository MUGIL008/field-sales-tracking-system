import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Register() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  const navigate = useNavigate();

  const handleRegister = async () => {
    if (password !== confirmPassword) {
      alert("Passwords do not match!");
      return;
    }

    const response = await fetch("http://127.0.0.1:8000/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name: name,
        email: email,
        password: password
      })
    });

    if (response.ok) {
      alert("Registration successful! Please login.");
      navigate("/");
    } else {
      const data = await response.json();
      alert(data.detail || "Registration failed");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Register</h2>

      <input
        type="text"
        placeholder="Name"
        onChange={(e) => setName(e.target.value)}
      /><br /><br />

      <input
        type="email"
        placeholder="Email"
        onChange={(e) => setEmail(e.target.value)}
      /><br /><br />

      <input
        type={showPassword ? "text" : "password"}
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
      /><br /><br />

      <input
        type={showPassword ? "text" : "password"}
        placeholder="Confirm Password"
        onChange={(e) => setConfirmPassword(e.target.value)}
      /><br /><br />

      <label>
        <input
          type="checkbox"
          checked={showPassword}
          onChange={(e) => setShowPassword(e.target.checked)}
        />
        {" "}Show Password
      </label><br /><br />

      <button onClick={handleRegister}>Register</button>
      <button onClick={() => navigate("/")} style={{ marginLeft: "10px" }}>
        Back to Login
      </button>
    </div>
  );
}

export default Register;