import { useState } from "react";

export default function RouteForm({ onSubmit, loading }) {
  const [start, setStart] = useState("");
  const [finish, setFinish] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    onSubmit({
      start,
      finish,
    });
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-slate-800 p-6 rounded-2xl shadow-lg space-y-4"
    >
      <div>
        <label className="block mb-2">Start Location</label>

        <input
          type="text"
          placeholder="New York"
          value={start}
          onChange={(e) => setStart(e.target.value)}
          className="w-full p-3 rounded-xl bg-slate-700 outline-none"
          required
        />
      </div>

      <div>
        <label className="block mb-2">Destination</label>

        <input
          type="text"
          placeholder="Chicago"
          value={finish}
          onChange={(e) => setFinish(e.target.value)}
          className="w-full p-3 rounded-xl bg-slate-700 outline-none"
          required
        />
      </div>

      <button
        className="w-full bg-blue-600 hover:bg-blue-700 transition-all p-3 rounded-xl font-semibold"
      >
        {loading ? "Optimizing Route..." : "Optimize Route"}
      </button>
    </form>
  );
}