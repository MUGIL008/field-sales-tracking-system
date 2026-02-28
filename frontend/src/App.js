import { Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import LogVisit from "./pages/LogVisit";
import Visits from "./pages/Visits";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/log-visit" element={<LogVisit />} />
      <Route path="/visits" element={<Visits />} />
    </Routes>
  );
}

export default App;